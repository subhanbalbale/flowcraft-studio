"""One-off: demote headings that live inside product mockups.

Fake business names and price numbers inside a screenshot are not sections of
the page; as headings they skip levels and pollute the document outline.
"""
import io
import re
import sys

DEMOTE = {
    "sitemaker.html": [
        ("h3", "Spice Route Kitchen"),
        ("h4", "Why Business Owners Choose It"),
        ("h3", "\u20b95,999"),
    ],
    "leadsflowpro.html": [
        ("h4", "Apex Dental"),
        ("h4", "Royal Glow Unisex Salon"),
        ("h4", "Urban Fit Cross Training Gym"),
    ],
    "starscanner.html": [
        ("h3", "Full-Stack Digital Diagnostics"),
    ],
}

for name, items in DEMOTE.items():
    s = io.open(name, encoding="utf-8").read()
    for tag, needle in items:
        pat = re.compile(
            r"<%s(\s[^>]*)?>(\s*%s.*?)</%s>" % (tag, re.escape(needle), tag), re.S
        )
        m = pat.search(s)
        if not m:
            sys.exit("%s: %s %r not found" % (name, tag, needle))
        s = pat.sub(lambda mm: "<div%s>%s</div>" % (mm.group(1) or "", mm.group(2)), s, count=1)
    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print(name, "headings demoted")
