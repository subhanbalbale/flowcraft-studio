"""Add dateModified/datePublished and og:image:alt.

Freshness signals were absent site-wide; og:image:alt was on about.html only.
"""
import io
import json
import re
import sys

MODIFIED = "2026-10-30"
PUBLISHED = "2026-10-16"   # first commit of the site's assets

ALT = {
    "index.html": "FlowCraft Studio — fast websites, NFC review hardware and "
                  "Google Maps ranking for local businesses in Mumbai",
    "sitemaker.html": "SiteMaker by FlowCraft Studio — a ready-made business "
                      "website for \u20b95,999 once",
    "nfc.html": "FlowCraft Smart NFC range — Google review standee, business "
                "card and keychain",
    "leadsflowpro.html": "LeadsFlowPro by FlowCraft Studio — Google Maps lead "
                         "finder dashboard",
    "starscanner.html": "StarScanner by FlowCraft Studio — website SEO and "
                        "security scanner",
}

WEBPAGE = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "@id": "%(url)s#webpage",
    "url": "%(url)s",
    "name": "%(name)s",
    "isPartOf": { "@id": "https://flowcraft-studio.netlify.app/#website" },
    "about": { "@id": "https://flowcraft-studio.netlify.app/#organization" },
    "datePublished": "%(published)s",
    "dateModified": "%(modified)s",
    "inLanguage": "en-IN"
  }
  </script>

"""

URLS = {
    "index.html": "https://flowcraft-studio.netlify.app/",
    "sitemaker.html": "https://flowcraft-studio.netlify.app/sitemaker.html",
    "nfc.html": "https://flowcraft-studio.netlify.app/nfc.html",
    "about.html": "https://flowcraft-studio.netlify.app/about.html",
    "leadsflowpro.html": "https://flowcraft-studio.netlify.app/leadsflowpro.html",
    "starscanner.html": "https://flowcraft-studio.netlify.app/starscanner.html",
}

for name, url in URLS.items():
    s = io.open(name, encoding="utf-8").read()
    before = s

    # og:image:alt right after the og:image tag, where one is missing
    if "og:image:alt" not in s and name in ALT:
        s = re.sub(
            r'(<meta property="og:image" content="[^"]*">\n)',
            lambda m: m.group(1) + '  <meta property="og:image:alt" content="%s">\n' % ALT[name],
            s, count=1,
        )
        # Twitter reads its own alt attribute
        s = re.sub(
            r'(<meta name="twitter:image" content="[^"]*">\n)',
            lambda m: m.group(1) + '  <meta name="twitter:image:alt" content="%s">\n' % ALT[name],
            s, count=1,
        )

    # A WebPage node carries the freshness dates and ties the page to the graph
    if '"WebPage"' not in s:
        title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        block = WEBPAGE % {
            "url": url,
            "name": title.replace("&amp;", "&").replace('"', "'"),
            "published": PUBLISHED,
            "modified": MODIFIED,
        }
        s = s.replace('  <script type="application/ld+json">', block + '  <script type="application/ld+json">', 1)

    # A visible last-updated line is the signal users and crawlers both read
    s = s.replace(
        "&copy; 2026 FlowCraft Studio by Subhan Balbale.",
        '&copy; 2026 FlowCraft Studio by Subhan Balbale. '
        '<span class="text-slate-400">Updated <time datetime="%s">30 October 2026</time>.</span>'
        % MODIFIED,
    )

    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(b)

    if s == before:
        sys.exit("%s: nothing changed" % name)
    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print("%-20s dates + og:image:alt" % name)
