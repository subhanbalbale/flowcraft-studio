"""Remove AggregateRating markup that no visible review backs.

Google requires rating markup to come from genuine reviews that are shown on
the same page. These three blocks had no Review objects, no testimonials and
no visible stars, which makes them a manual-action risk rather than a ranking
gain. Put them back only alongside real, displayed reviews.
"""
import io
import json
import re
import sys

BLOCK = re.compile(
    r",?\s*\"aggregateRating\"\s*:\s*\{[^{}]*\}", re.S
)

for name in ("sitemaker.html", "nfc.html", "leadsflowpro.html"):
    s = io.open(name, encoding="utf-8").read()
    if '"aggregateRating"' not in s:
        sys.exit("%s: no aggregateRating found" % name)
    s = BLOCK.sub("", s)
    if '"aggregateRating"' in s:
        sys.exit("%s: aggregateRating survived the edit" % name)

    # The JSON-LD must still parse after the splice
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(b)

    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print(name, "aggregateRating removed, JSON-LD still valid")
