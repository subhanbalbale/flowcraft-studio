import collections
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
data = json.load(open("build/detect.json", encoding="utf-8"))
counts = collections.Counter(
    (os.path.basename(x["file"]), x["antipattern"], x.get("snippet", "")[:46])
    for x in data
)
print("total findings:", len(data))
for (f, a, s), n in sorted(counts.items()):
    print("%3dx %-20s %-30s %s" % (n, f, a, s))
