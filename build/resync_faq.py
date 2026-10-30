"""Regenerate a page's FAQPage JSON-LD from the questions it actually renders.

Run this after editing any FAQ copy. The visible answer and the marked-up
answer have to say the same thing: Google treats a mismatch as misleading
structured data, and it is exactly the kind of drift nobody notices by eye.
"""
import html
import io
import json
import re
import sys

DETAIL = re.compile(
    r"<details[^>]*>\s*<summary[^>]*>\s*<span>(.*?)</span>.*?<p[^>]*>(.*?)</p>\s*</details>",
    re.S,
)
FAQ_NODE = re.compile(
    r'\s*<script type="application/ld\+json">\s*\{[^<]*?"@type":\s*"FAQPage".*?</script>',
    re.S,
)


def clean(t):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t))).strip()


for name in sys.argv[1:]:
    s = io.open(name, encoding="utf-8").read()

    qas = [
        {"@type": "Question", "name": clean(q),
         "acceptedAnswer": {"@type": "Answer", "text": clean(a)}}
        for q, a in DETAIL.findall(s)
    ]
    if not qas:
        sys.exit("%s: no <details> FAQ entries found" % name)

    block = '  <script type="application/ld+json">\n  ' + json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qas},
        indent=2, ensure_ascii=False,
    ).replace("\n", "\n  ") + "\n  </script>"

    if FAQ_NODE.search(s):
        s = FAQ_NODE.sub("\n" + block, s, count=1)
        action = "replaced"
    else:
        s = s.replace('  <script type="application/ld+json">',
                      block + "\n\n  " + '<script type="application/ld+json">', 1)
        action = "added"

    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(b)

    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print("%-20s FAQPage %s, %d questions in sync" % (name, action, len(qas)))
