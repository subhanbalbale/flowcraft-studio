"""One-off: replace unicode glyphs standing in for icons with real SVG icons."""
import io
import re

CHECK = ('<svg class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" viewBox="0 0 24 24" '
         'fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" '
         'aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>')
ARROW = ('<svg class="w-4 h-4 shrink-0" viewBox="0 0 24 24" fill="none" '
         'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
         'aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')
DOWN = ('<svg class="w-4 h-4 shrink-0" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        'aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>')

for name in ("nfc.html", "sitemaker.html", "starscanner.html", "leadsflowpro.html"):
    s = io.open(name, encoding="utf-8").read()
    before = s

    # Bare "✓ " opening a list item
    s = re.sub(r'(<li class="flex items-center gap-2">)✓\s*', r"\1" + CHECK + " ", s)
    # Standalone ✓ in a styled span
    s = re.sub(r'<span class="text-rose-600 font-bold">✓</span>',
               CHECK.replace("text-emerald-600", "text-rose-600"), s)
    # Trailing arrows inside link labels
    s = re.sub(r'(<span>[^<]+?)\s*→</span>', r"\1</span>" + ARROW, s)
    s = re.sub(r'(<span>[^<]+?)\s*↓</span>', r"\1</span>" + DOWN, s)
    s = re.sub(r'\n(\s*)([A-Z][^<\n]+?)\s*→\n', lambda m: "\n%s%s\n" % (m.group(1), m.group(2)), s)
    s = s.replace(" ↗", "").replace("↵", "")

    if s != before:
        io.open(name, "w", encoding="utf-8", newline="\n").write(s)
        print(name, "glyphs replaced")
