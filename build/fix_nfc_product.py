"""Align the NFC Product node with the prices the page actually shows.

The restored node carried an AggregateOffer of 699-1499 and an AggregateRating
with no visible reviews behind it. The page lists 499, 899 and 999, so the
range was wrong in both directions, and the rating is the same policy risk
that was removed from the other pages.
"""
import io
import json
import re

s = io.open("nfc.html", encoding="utf-8").read()
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
raw = next(b for b in blocks if '"@graph"' in b)
doc = json.loads(raw)

for node in doc["@graph"]:
    if node.get("@type") != "Product":
        continue
    node.pop("aggregateRating", None)          # no reviews shown on the page
    node["name"] = "Smart NFC hardware — cards, review standees and keychains"
    offers = node["offers"]
    offers["lowPrice"] = "499"                  # keychain, the cheapest listed
    offers["highPrice"] = "999"                 # review standee, the dearest listed
    offers["price"] = "499"
    offers["offerCount"] = "3"                  # the three with a published price

for node in doc["@graph"]:
    node.pop("aggregateRating", None)

new = json.dumps(doc, indent=2, ensure_ascii=False).replace("\n", "\n  ")
s = s.replace(raw, "\n  " + new + "\n  ", 1)

for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
    json.loads(b)

io.open("nfc.html", "w", encoding="utf-8", newline="\n").write(s)
print("Product node aligned; aggregateRating removed:", "aggregateRating" not in s)
