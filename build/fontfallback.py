"""One-off: metric-matched fallback so the webfont swap stops shifting layout.

Measured in the browser at 100px: Plus Jakarta Sans is 106.66% the width of
Arial, with ascent 104 and descent 22 against Arial's 91 and 21. Overrides are
expressed against the size-adjusted em.
"""
import io
import sys

FACE = """    /* Metric-matched fallback: holds the exact space the webfont will take,
       so swapping it in causes no layout shift. */
    @font-face {
      font-family: 'Jakarta Fallback';
      src: local('Arial'), local('Helvetica'), local('Liberation Sans');
      size-adjust: 106.66%;
      ascent-override: 97.5%;
      descent-override: 20.6%;
      line-gap-override: 0%;
    }

"""

for name in ("index.html", "sitemaker.html", "nfc.html", "about.html",
             "leadsflowpro.html", "starscanner.html"):
    s = io.open(name, encoding="utf-8").read()
    before = s
    if "Jakarta Fallback" not in s:
        s = s.replace("    :root {", FACE + "    :root {", 1)
    s = s.replace(
        "font-family: 'Plus Jakarta Sans', sans-serif;",
        "font-family: 'Plus Jakarta Sans', 'Jakarta Fallback', sans-serif;",
    )
    if s == before:
        sys.exit("%s: nothing changed" % name)
    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print(name, "fallback added")
