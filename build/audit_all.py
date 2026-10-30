"""Collect the numbers the report quotes, from the files themselves."""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
PAGES = ["index.html", "sitemaker.html", "nfc.html", "about.html",
         "leadsflowpro.html", "starscanner.html"]

links = set()
rows = []
for p in PAGES:
    s = io.open(p, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    desc = re.search(r'name="description" content="(.*?)"', s, re.S).group(1)
    canon = re.search(r'rel="canonical" href="(.*?)"', s)
    schema = []
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        d = json.loads(b)
        items = d.get("@graph", [d]) if isinstance(d, dict) else d
        schema += [i.get("@type") for i in items]
    for m in re.finditer(r'href="([^"#:]+\.html)', s):
        links.add((p, m.group(1)))
    rows.append({
        "page": p,
        "bytes": os.path.getsize(p),
        "title_len": len(title),
        "desc_len": len(desc),
        "canonical": bool(canon),
        "h1": len(re.findall(r"<h1\b", s)),
        "schema": schema,
        "og": len(re.findall(r'property="og:', s)),
        "imgs": len(re.findall(r"<img\b", s)),
    })

print("%-20s %7s %6s %6s %5s %4s %4s %s" %
      ("page", "bytes", "title", "desc", "canon", "h1", "og", "schema"))
for r in rows:
    print("%-20s %7d %6d %6d %5s %4d %4d %s" %
          (r["page"], r["bytes"], r["title_len"], r["desc_len"],
           r["canonical"], r["h1"], r["og"], ",".join(filter(None, r["schema"]))))

missing = sorted({t for _, t in links if not os.path.exists(t)})
print("\nbroken internal links:", missing or "none")
print("internal link edges:", len(links))
