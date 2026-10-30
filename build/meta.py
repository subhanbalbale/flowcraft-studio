"""One-off: bring every page's title and description inside SERP truncation limits."""
import io
import re
import sys

META = {
    "sitemaker.html": (
        "SiteMaker — Websites for Indian Businesses, \u20b95,999",
        "Ready-made websites for Indian small businesses. Pick a design built for your "
        "trade, auto-fill from Google Maps, pay \u20b95,999 once. Live in 24 hours.",
    ),
    "nfc.html": (
        "Smart NFC Cards &amp; Google Review Standees | FlowCraft",
        "Custom NFC business cards, tap-to-review Google standees and smart keychains. "
        "Works on every iPhone and Android with no app. Shipped across India.",
    ),
    "leadsflowpro.html": (
        "LeadsFlowPro — Google Maps Lead Finder | FlowCraft",
        "Find local businesses on Google Maps that have no website, sort them into a "
        "calling pipeline and reach them on WhatsApp from one dashboard.",
    ),
    "starscanner.html": (
        "StarScanner — Website SEO &amp; Security Scanner (Soon)",
        "Scan a local business website for broken links, missing security headers, Core "
        "Web Vitals problems and search visibility gaps. Coming soon from FlowCraft.",
    ),
    "about.html": (
        "About Subhan Balbale — Founder, FlowCraft Studio",
        "Subhan Balbale is an independent full-stack engineer and hardware builder in "
        "Mumbai, and the maker of SiteMaker, LeadsFlowPro and FlowCraft NFC hardware.",
    ),
}

for name, (title, desc) in META.items():
    s = io.open(name, encoding="utf-8").read()
    before = s
    s = re.sub(r"<title>.*?</title>", "<title>%s</title>" % title, s, count=1, flags=re.S)
    s = re.sub(
        r'(<meta name="description" content=").*?(">)',
        lambda m: m.group(1) + desc + m.group(2),
        s, count=1, flags=re.S,
    )
    # Keep the social cards in step with the page itself
    s = re.sub(
        r'(<meta property="og:title" content=").*?(">)',
        lambda m: m.group(1) + title + m.group(2), s, count=1, flags=re.S,
    )
    s = re.sub(
        r'(<meta property="og:description" content=").*?(">)',
        lambda m: m.group(1) + desc + m.group(2), s, count=1, flags=re.S,
    )
    s = re.sub(
        r'(<meta name="twitter:title" content=").*?(">)',
        lambda m: m.group(1) + title + m.group(2), s, count=1, flags=re.S,
    )
    s = re.sub(
        r'(<meta name="twitter:description" content=").*?(">)',
        lambda m: m.group(1) + desc + m.group(2), s, count=1, flags=re.S,
    )
    # Drop the keywords meta: Google has ignored it since 2009
    s = re.sub(r'[ \t]*<meta name="keywords"[^>]*>\n', "", s)
    if s == before:
        sys.exit("%s: nothing changed" % name)
    io.open(name, "w", encoding="utf-8", newline="\n").write(s)
    print(name, "meta updated")
