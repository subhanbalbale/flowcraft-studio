"""Generate the pixel dissolve bands that sit under the hero and above the footer.

The squares are written straight into index.html between <!-- pixelfield:NAME -->
markers, so the page pays no runtime JS or image request for them. Runs merge
horizontally and each colour collapses into one <path>, which keeps the inlined
markup small enough to gzip well.

Re-run after changing the grid, the palette or the dissolve shape:
    python build/pixelfield.py
"""
import io
import math
import random
import re

BLUE = "#0350c4"
FLAME = "#fa7d13"

# cols, rows, seed, horizon (0 = top), band depth, flame share
BANDS = {
    "hero":   (104, 26, 20260103, 0.40, 0.88, 0.020),
    "footer": (104, 11, 20260104, 0.40, 0.70, 0.016),
}


def grid(cols, rows, seed, horizon, depth, flame_rate):
    """1 = blue, 2 = flame, 0 = empty. Density ramps downward past an
    undulating horizon so the dissolve never reads as a straight line."""
    rnd = random.Random(seed)
    cells = [[0] * cols for _ in range(rows)]
    for x in range(cols):
        u = x / cols
        h = horizon + 0.17 * math.sin(u * 2.4 * math.pi + 0.7) \
                    + 0.07 * math.sin(u * 5.1 * math.pi + 2.1)
        for y in range(rows):
            t = (y / (rows - 1) - h) / depth + 0.5
            t = min(1.0, max(0.0, t))
            if rnd.random() < t ** 1.6:
                cells[y][x] = 2 if rnd.random() < flame_rate else 1
    return cells


def paths(cells):
    """Merge each row's runs of one colour into a single rect subpath."""
    out = {1: [], 2: []}
    for y, row in enumerate(cells):
        x = 0
        while x < len(row):
            c = row[x]
            if not c:
                x += 1
                continue
            n = 1
            while x + n < len(row) and row[x + n] == c:
                n += 1
            out[c].append("M%d %dh%dv1h-%dz" % (x, y, n, n))
            x += n
    return out


def svg(name, cols, rows, cells):
    d = paths(cells)
    return (
        '<svg class="dissolve" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
        'preserveAspectRatio="none" shape-rendering="crispEdges" aria-hidden="true" '
        'focusable="false"><path fill="%s" d="%s"/><path fill="%s" d="%s"/></svg>'
        % (cols, rows, BLUE, "".join(d[1]), FLAME, "".join(d[2]))
    )


def main(page="index.html", required=True):
    """Fill whichever pixelfield markers the page carries. Returns the names
    filled, so the caller can report them."""
    s = io.open(page, encoding="utf-8").read()
    done = []
    for name, (cols, rows, seed, horizon, depth, flame) in BANDS.items():
        pattern = re.compile(
            r"(<!-- pixelfield:%s -->).*?(<!-- /pixelfield:%s -->)" % (name, name),
            re.S)
        if not pattern.search(s):
            if required:
                raise SystemExit("no pixelfield:%s markers in %s" % (name, page))
            continue
        markup = svg(name, cols, rows,
                     grid(cols, rows, seed, horizon, depth, flame))
        s = pattern.sub(lambda m: m.group(1) + markup + m.group(2), s)
        done.append(name)
    if done:
        io.open(page, "w", encoding="utf-8", newline="\n").write(s)
    return ", ".join(done)


if __name__ == "__main__":
    print(main())
