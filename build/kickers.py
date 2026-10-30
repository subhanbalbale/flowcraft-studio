"""One-off: delete kicker/eyebrow labels that sit directly above a heading.

The heading already carries the section; the label above it is decoration that
pushes the real title down and adds a second thing to read.
"""
import io
import re
import sys

# A kicker is an uppercase label whose very next element is a heading.
KICKER = re.compile(
    r'[ \t]*<span class="[^"]*uppercase[^"]*">[^<]{3,60}</span>\s*\n(?=\s*<h[1-6])'
)

for name in ("index.html", "about.html", "nfc.html", "sitemaker.html",
             "leadsflowpro.html", "starscanner.html"):
    s = io.open(name, encoding="utf-8").read()
    found = KICKER.findall(s)
    if not found:
        print("%-20s no kickers" % name)
        continue
    s = KICKER.sub("", s)
    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print("%-20s removed %d kicker(s)" % (name, len(found)))
