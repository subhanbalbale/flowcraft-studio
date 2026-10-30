"""Stop cards nesting inside cards.

Three patterns created the nesting:
  1. icon tiles that carried their own border on top of a tinted background
  2. white sub-panels sitting inside an already-white glass panel
  3. image wells with both a tint and a border inside a product card
In every case the parent card already supplies the surface, so the inner one
is a second edge the eye has to parse for nothing.
"""
import io
import re
import sys

PAGES = ("index.html", "sitemaker.html", "nfc.html", "about.html",
         "leadsflowpro.html", "starscanner.html")

# 1. Icon tiles keep their tint, lose the border.
ICON_TILE = re.compile(
    r'(class="w-\d+ h-\d+ rounded-(?:lg|xl|2xl)[^"]*?)\s*border border-\w+-\d00(/\d+)?'
)

# 2 & 3. Inner surfaces inside a glass panel lose the white fill and the border.
INNER_WHITE = [
    ('p-5 rounded-2xl bg-white/70 border border-slate-200/80',
     'p-5 rounded-2xl bg-slate-50/60'),
    ('p-4 rounded-xl bg-white/90 border border-slate-200/80',
     'p-4 rounded-xl bg-slate-50/60'),
    ('p-6 rounded-2xl bg-white/90 border border-slate-200/80',
     'p-6 rounded-2xl bg-slate-50/60'),
    ('text-center p-6 rounded-2xl bg-white/80 border border-slate-200/80',
     'text-center p-6 rounded-2xl bg-slate-50/60'),
    ('p-3 rounded-xl bg-white/80 border border-slate-200/80',
     'p-3 rounded-xl bg-slate-50/60'),
    ('w-full h-44 rounded-2xl overflow-hidden bg-slate-100 border border-slate-200/80',
     'w-full h-44 rounded-2xl overflow-hidden bg-slate-50/70'),
    ('w-full h-44 rounded-2xl overflow-hidden bg-slate-50 border border-slate-200/80',
     'w-full h-44 rounded-2xl overflow-hidden bg-slate-50/70'),
]

total = 0
for name in PAGES:
    s = io.open(name, encoding="utf-8").read()
    before = s

    s, n_icon = ICON_TILE.subn(r"\1", s)

    n_inner = 0
    for old, new in INNER_WHITE:
        n_inner += s.count(old)
        s = s.replace(old, new)

    if s != before:
        io.open(name, "w", encoding="utf-8", newline="\n").write(s)
        total += n_icon + n_inner
        print("%-20s %2d icon tiles, %2d inner surfaces" % (name, n_icon, n_inner))

if not total:
    sys.exit("nothing changed")
print("flattened %d nested surfaces" % total)
