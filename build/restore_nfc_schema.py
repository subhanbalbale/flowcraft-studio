"""Restore the Product / LocalBusiness / BreadcrumbList nodes.

The FAQ resync replaced a combined @graph script wholesale because the graph
happened to contain the FAQPage node. Rebuild the graph from the pre-edit
backup, then drop in the current (rewritten) FAQ so visible text and markup
still agree.
"""
import io
import json
import re

cur = io.open("nfc.html", encoding="utf-8").read()
old = io.open("build/backup-pre-cleanup/nfc.html", encoding="utf-8").read()

blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', cur, re.S)
faq = next(json.loads(b) for b in blocks if '"FAQPage"' in b)

graph = json.loads(
    re.search(r'<script type="application/ld\+json">(.*?)</script>', old, re.S).group(1)
)["@graph"]

# Swap the stale FAQPage in the restored graph for the current one
graph = [faq["mainEntity"] and {"@type": "FAQPage", "mainEntity": faq["mainEntity"]}
         if n.get("@type") == "FAQPage" else n for n in graph]

assert [n["@type"] for n in graph] == ["Product", "LocalBusiness", "FAQPage", "BreadcrumbList"], \
    [n["@type"] for n in graph]

block = '  <script type="application/ld+json">\n  ' + json.dumps(
    {"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False
).replace("\n", "\n  ") + "\n  </script>"

# Replace the standalone FAQPage script with the full graph
cur = re.sub(
    r'\s*<script type="application/ld\+json">\s*\{\s*"@context"[^<]*?"@type":\s*"FAQPage".*?</script>',
    "\n" + block, cur, count=1, flags=re.S,
)

types = []
for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', cur, re.S):
    d = json.loads(b)
    types += [x.get("@type") for x in (d.get("@graph", [d]))]

io.open("nfc.html", "w", encoding="utf-8", newline="\n").write(cur)
print("restored:", types)
