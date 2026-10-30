"""Generate FAQPage JSON-LD from the questions actually rendered on the page.

Reading the markup rather than hand-writing the schema guarantees the two can
never drift apart, which is the thing Google checks.
"""
import html
import io
import json
import re

DETAIL = re.compile(
    r'<details class="faq[^"]*">\s*<summary[^>]*>\s*<span>(.*?)</span>.*?'
    r'<p class="[^"]*">(.*?)</p>\s*</details>',
    re.S,
)

for name in ("sitemaker.html",):
    s = io.open(name, encoding="utf-8").read()
    if '"FAQPage"' in s:
        print(name, "already has FAQPage"); continue

    qas = []
    for q, a in DETAIL.findall(s):
        clean = lambda t: html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t))).strip()
        qas.append({
            "@type": "Question",
            "name": clean(q),
            "acceptedAnswer": {"@type": "Answer", "text": clean(a)},
        })

    assert qas, "%s: no FAQ entries found" % name
    block = "  <script type=\"application/ld+json\">\n  " + json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qas},
        indent=2, ensure_ascii=False,
    ).replace("\n", "\n  ") + "\n  </script>\n\n"

    s = s.replace('  <script type="application/ld+json">', block + '  <script type="application/ld+json">', 1)
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(b)
    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print("%-20s FAQPage with %d questions" % (name, len(qas)))
