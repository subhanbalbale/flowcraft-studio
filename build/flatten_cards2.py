"""Second flattening pass: catch the variants the exact-string pass missed.

Also strips shadow-xs / shadow-2xs, which are Tailwind v4 class names. This
project builds with v3, where they generate nothing at all — dead markup that
only made these elements read as cards to a scanner.
"""
import io
import re

PAGES = ("index.html", "sitemaker.html", "nfc.html", "about.html",
         "leadsflowpro.html", "starscanner.html")

RULES = [
    # white sub-surfaces inside an already-white panel
    (re.compile(r'bg-white/\d0 border border-slate-200/\d0'), 'bg-slate-50/60'),
    (re.compile(r'bg-slate-100 border border-slate-200/\d0'), 'bg-slate-50/70'),
    (re.compile(r'bg-slate-50 border border-slate-200/\d0'), 'bg-slate-50/70'),
    (re.compile(r'bg-rose-50/60 (p-\d+ rounded-2xl) border border-\w+-\d00/?\d*'), r'bg-rose-50/60 \1'),
    # v4-only shadow names: they compile to nothing here
    (re.compile(r'\s+shadow-2xs\b'), ''),
    (re.compile(r'\s+shadow-xs\b(?!["\s]*$)'), ''),
]

for name in PAGES:
    s = io.open(name, encoding="utf-8").read()
    before = s
    for pat, rep in RULES:
        s = pat.sub(rep, s)
    if s != before:
        io.open(name, "w", encoding="utf-8", newline="\n").write(s)
        print("%-20s flattened" % name)
