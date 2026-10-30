"""One-off: lift sub-AA text colours onto their 600/700 steps."""
import io

# Each 500/600 tint sits below 4.5:1 on white; the next step clears it.
SWAPS = [
    ("text-amber-600", "text-amber-700"),
    ("text-sky-600", "text-sky-700"),
    ("text-emerald-600", "text-emerald-700"),
    ("text-pink-600", "text-pink-700"),
    ("text-rose-600", "text-rose-700"),
    ("text-slate-400\">", "text-slate-500\">"),
    ("bg-amber-500", "bg-amber-600"),
    ("text-[10px]", "text-[11px]"),
]

for name in ("about.html", "nfc.html", "sitemaker.html",
             "leadsflowpro.html", "starscanner.html"):
    s = io.open(name, encoding="utf-8").read()
    before = s
    for old, new in SWAPS:
        s = s.replace(old, new)
    if s != before:
        io.open(name, "w", encoding="utf-8", newline="\n").write(s)
        print(name, "contrast lifted")
