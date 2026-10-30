"""Rewrite about.html body copy in the homepage's register.

Two factual corrections go in alongside the tone change:

  * LeadsFlowPro was described here as a scraper that "extracts verified phone
    numbers" and exports "Excel & CSV". Its own product page says plainly that
    it does not send anything on its own and is not a CRM, and no export
    feature is claimed there. The two pages have to describe one product.
  * SiteMaker was "under 10 minutes" here and "24 hours" everywhere else.
"""
import io
import sys

SWAPS = [
    # --- Hero -------------------------------------------------------------
    ("Subhan Balbale is a software engineer and the founder of FlowCraft Studio in Mumbai, India. "
     "He engineers high-performance web applications, automated lead generation software, "
     "and custom tap-to-connect NFC hardware for businesses.",
     "I build websites, lead-generation software and tap-to-connect NFC hardware for local "
     "businesses, out of Mumbai. FlowCraft is me — there is no team behind this page, which "
     "is the point of it."),

    ("Born Feb 2, 2006 (20 Years Old)", "20 years old"),
    ("Shipped 3+ Production Systems", "Three products in production"),
    ("Available Worldwide &amp; Local", "Mumbai, working anywhere in India"),

    # --- Mission ----------------------------------------------------------
    ("Who is Subhan Balbale and what is FlowCraft's mission?",
     "Why does FlowCraft exist?"),
    ("FlowCraft Studio is an independent software and hardware engineering studio founded by Subhan Balbale "
     "that values real business growth, clean code, and personal client relationships over corporate agency complexity.",
     "Because a shop owner in Mumbai can pay ₹30,000 for a website that takes two months, loads "
     "slowly, and never rings their phone. I kept meeting people in that position and could not "
     "explain to them why it had to cost that much, so I started building the other version."),

    ("&quot;Software should solve tangible business problems and bring real revenue.&quot;",
     "&quot;If it doesn't bring you customers, it's decoration.&quot;"),
    ("Too many agencies build complex, bloated websites that take months to complete and never bring in customers. "
     "My approach is simple: understand what brings sales to your business, build it with lightning speed, "
     "and give you modern tools that you actually enjoy using.",
     "A website is not the goal — a phone call is. So I start from the thing that actually brings "
     "you work, build only what serves it, and ship it in days. You get something you can edit "
     "yourself afterwards, and you own all of it."),

    ("3-to-7 day turnaround", "Three to seven days"),
    ("Direct communication with the builder", "You talk to the person writing the code"),
    ("Zero agency markups", "One price, no retainer"),

    # --- Capabilities -----------------------------------------------------
    ("Intelligent Automations", "Automation"),
    ("I build custom artificial intelligence systems that automate repetitive work: extracting leads from Google Maps, "
     "answering customer inquiries 24/7 on WhatsApp, and generating personalized marketing campaigns.",
     "The boring, repeated parts of running a small business are the parts software is actually "
     "good at. Pulling prospects off Google Maps, handling the same five WhatsApp questions at "
     "eleven at night, putting a campaign together from a list you already have."),

    ("Zero-Bloat Websites", "Websites that load"),
    ("Every website and web app I write is engineered for ultra-fast loading speeds on mobile devices. "
     "No heavy, broken WordPress plugins—clean, modern code that ranks higher on Google and converts visitors into paying customers.",
     "Your customer is on a phone, on mobile data, standing outside your shop. If the page takes "
     "four seconds they have already gone back to Maps. I write plain, modern code with no plugin "
     "stack behind it, because that is what makes a page open instantly."),

    ("Contactless Hardware", "Hardware"),
    ("I bridge the gap between physical retail counters and digital sales. By programming custom NFC chips into acrylic counter stands "
     "and business cards, your customers can tap their phone and leave 5-star Google reviews in 2 seconds.",
     "Software stops at the screen, and a lot of business still happens at a counter. I program "
     "NFC chips into acrylic stands and printed cards so the customer standing in front of you "
     "can leave a review before they have put their wallet away."),

    # --- Products ---------------------------------------------------------
    ("What software applications and digital products does Subhan build?",
     "What has FlowCraft actually shipped?"),
    ("Test these live web applications directly in your browser.",
     "Two are live and you can open them right now. The third is still being built."),

    ("Google Maps B2B Lead Generator", "Finds local businesses with no website"),
    ("An automated lead discovery tool built specifically for sales teams and business owners. It searches Google Maps for any industry in any city, "
     "extracts verified phone numbers, addresses, and website status, and exports ready-to-contact lead lists in seconds.",
     "Give it a pin code and a trade and it reads the public Google Maps listings for that area, "
     "then filters to the businesses with no website of their own. Those owners are already being "
     "found on Maps with nowhere to send anyone. You work down the list and open each WhatsApp "
     "thread yourself — it sends nothing on its own."),
    ("Google Maps Scraper", "Reads public Maps listings"),
    ("WhatsApp Outreach", "One-tap WhatsApp threads"),
    ("Excel &amp; CSV Export", "Call pipeline with notes"),

    ("Instant Mobile Website Creator", "A real website for ₹5,999, once"),
    ("A fast, simple website builder designed for local businesses, shops, and freelancers. It lets anyone enter their business details, menu, "
     "and photos to launch a polished, mobile-friendly website with instant WhatsApp ordering in under 10 minutes.",
     "Sixty finished designs across twenty trades, so your site starts finished rather than blank. "
     "It fills itself from your Google Maps listing — your photos, hours and reviews — and puts a "
     "WhatsApp button on every page. Live in 24 hours, one payment, no monthly bill."),
    ("Zero-Code Setup", "Nothing to configure"),
    ("Instant Mobile Previews", "Preview before you pay"),
    ("1-Tap WhatsApp Ordering", "One-tap WhatsApp enquiries"),

    # --- Stack ------------------------------------------------------------
    ("What tech stack, languages, and engineering systems do I use daily?",
     "What do you actually build with?"),
    ("Carefully selected technologies that prioritize real-world speed, reliability, and security.",
     "Boring, well-understood tools. Nothing here is chosen to look impressive on a page."),

    # --- Contact ----------------------------------------------------------
    ("How can you get in touch or start a project directly?",
     "How do you get hold of me?"),
    ("Whether you need a custom website, an AI lead generation system, or smart NFC business cards for your company, "
     "reach out directly to me. No middle managers.",
     "WhatsApp is fastest and I answer it myself, at most hours. Tell me what your business does "
     "and what you want people to do when they find you — that is enough to start. If I think you "
     "do not need what you are asking for, I will say so."),

    ("Chat On WhatsApp", "Message me on WhatsApp"),
    ("Send An Email", "Send an email"),
]

s = io.open("about.html", encoding="utf-8").read()
before = s
missed = []
for old, new in SWAPS:
    if old not in s:
        missed.append(old[:70])
        continue
    s = s.replace(old, new)

if missed:
    print("NOT FOUND (%d):" % len(missed))
    for m in missed:
        print("   ", m)

if s == before:
    sys.exit("nothing changed")
io.open("about.html", "w", encoding="utf-8", newline="\n").write(s)
print("about.html rewritten")
