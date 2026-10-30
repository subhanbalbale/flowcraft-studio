"""Give the inner pages their own Twitter Card tags and a visible updated date.

X falls back to Open Graph when these are absent, so this is a completeness fix
rather than a repair, but explicit tags stop the card being guessed.
"""
import io
import re
import sys

for name in ("sitemaker.html", "nfc.html", "about.html",
             "leadsflowpro.html", "starscanner.html"):
    s = io.open(name, encoding="utf-8").read()
    before = s

    if 'name="twitter:' not in s:
        def grab(prop):
            m = re.search(r'<meta property="og:%s" content="(.*?)">' % prop, s, re.S)
            return m.group(1) if m else ""

        card = (
            '\n  <!-- Twitter / X Cards -->\n'
            '  <meta name="twitter:card" content="summary_large_image">\n'
            '  <meta name="twitter:title" content="%s">\n'
            '  <meta name="twitter:description" content="%s">\n'
            '  <meta name="twitter:image" content="%s">\n'
            '  <meta name="twitter:image:alt" content="%s">\n'
            % (grab("title"), grab("description"), grab("image"), grab("image:alt"))
        )
        # Sits right after the Open Graph block it mirrors
        s = re.sub(
            r'(<meta property="og:image:alt" content="[^"]*">\n)',
            lambda m: m.group(1) + card, s, count=1,
        )

    s = s.replace(
        "&copy; 2026 FlowCraft \u2022 Subhan Balbale. All rights reserved.",
        '&copy; 2026 FlowCraft \u2022 Subhan Balbale. '
        '<span class="text-slate-400">Updated <time datetime="2026-10-30">30 October 2026</time>.</span>',
    )

    if s == before:
        sys.exit("%s: nothing changed" % name)
    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print("%-20s twitter card + updated line" % name)
