"""Rewrite nfc.html body copy in the homepage's register.

Also fixes a real inconsistency: the page said "Price on Review" for every
product while the homepage and the Product schema both quote ₹999 / ₹899 /
₹499. A buyer who sees a price on one page and a wall on the next assumes the
price went up. Only the menu stands keep "price on request", because no price
for them exists anywhere else on the site to be consistent with.
"""
import io
import sys

SWAPS = [
    # --- Hero -------------------------------------------------------------
    ("Zero Apps Required · Works with iPhone &amp; Android · Pre-Programmed &amp; Ready",
     "Works on every iPhone and Android · No app to install · Arrives programmed"),

    ("Smart Contactless Products for Your Business<span class=\"text-amber-700\">.</span>",
     "Hardware your customers tap<span class=\"text-amber-700\">.</span>"),

    ("Hand over a custom NFC card, place a review standee on your billing counter, or carry a smart keychain on your keys. "
     "Customers simply tap with their smartphone to view your contact profile, website, or 5-star Google review page in seconds.",
     "A card you hand over, a stand on your billing counter, a tag on your keys. "
     "The customer touches their phone to it and your review page, contact details or menu opens — "
     "no app, no QR scanner, no typing."),

    ("<span>Order Custom Hardware</span>", "<span>Order hardware</span>"),
    ("<span>See Product Lineup</span>", "<span>See the range</span>"),

    # --- How it works -----------------------------------------------------
    ("How It Works in 3 Seconds", "How does tapping an NFC card actually work?"),
    ("No cameras, no QR scanners, and no apps required to install.",
     "Three seconds, start to finish. Nothing to download and nothing to aim a camera at."),

    ("1. Tap Any Phone", "Tap"),
    ("Hold the card or touch the counter plaque to the top of any iPhone or the back of any Android phone.",
     "The customer holds their phone near the card or stand — the top edge on an iPhone, "
     "the back on an Android. They do not need to unlock it first."),

    ("2. Instant Launch", "A banner appears"),
    ("A native browser banner appears instantly. One tap opens your profile, Google Review page, or digital catalog.",
     "The phone recognises the chip on its own and shows a notification. "
     "One tap on that opens whatever you programmed it to — your review page, your menu, your contact card."),

    ("3. 5-Star Reviews &amp; Leads", "Done"),
    ("Clients submit Google reviews on the spot or save your phone and WhatsApp details with zero manual typing errors.",
     "They leave the review while they are still standing at your counter, or save your number "
     "without mistyping a digit. The moment you had their attention is the moment you used it."),

    # --- Products intro ---------------------------------------------------
    ("Contactless Products Ready to Order", "What NFC hardware can you order?"),
    ("Real physical hardware your customers tap with their phones. Custom printed with your logo and pre-programmed to your links.",
     "Printed with your logo, programmed to your links, tested before it ships. "
     "Shipped from Mumbai anywhere in India."),

    # --- Product 1: business cards ----------------------------------------
    ("NFC Premium Customized Business Cards", "NFC business card"),
    ("Tap any smartphone against the card to share your digital profile, contact details, portfolio, and social links instantly. No typing needed.",
     "Matte PVC card printed with your logo. Touch it to any phone and your contact details, "
     "portfolio and links land on their screen — no one has to type a thing."),
    ("Compatible with iPhone &amp; Android", "Works on every iPhone and Android"),
    ("Custom printed with your branding &amp; QR", "Printed with your branding, QR on the back"),
    ("Update your links anytime without reprinting", "Change the links later without reprinting"),

    # --- Product 2: standee -----------------------------------------------
    ("Google Review NFC Tap Standee", "Google review standee"),
    ("Clear acrylic counter stand placed at billing counters or tables. Customers tap with their phone and land directly on your 5-star Google review box.",
     "Acrylic stand for the billing counter. A customer paying their bill taps it and your "
     "five-star review box opens with the stars already selected."),
    ("Prompts reviews before the customer leaves", "Catches the review before they walk out"),
    ("Strengthens local Google Maps presence", "Steady real reviews lift your Maps ranking"),
    ("Pre-programmed to your official review link", "Programmed to your own review link"),

    # --- Product 3: keychain ----------------------------------------------
    ("Smart NFC Keychains &amp; Key Fobs", "NFC keychain"),
    ("Compact, durable tap tag attached right to your everyday keys. Perfect for fast profile sharing, Instagram/WhatsApp exchange, or contactless access.",
     "A small waterproof tag for your keys or bag. Useful when you are networking and "
     "nobody wants to type a URL off a screen."),
    ("Water-resistant, high-durability build", "Waterproof epoxy resin shell"),
    ("Metal keyring included for daily carry", "Metal keyring included"),
    ("Works on any NFC-enabled smartphone", "Works on any NFC phone"),

    # --- Product 4: menu stands -------------------------------------------
    ("Digital Menu Table Stands", "Digital menu stand"),
    ("Compact table stickers or plaques for dining tables. Diners tap to view digital menus, daily specials, and connect to Wi-Fi without printed paper menus.",
     "A small plaque or sticker for each table. Diners tap to open the menu and the day's "
     "specials, which you can change from your phone without reprinting anything."),
    ("Wipe-clean acrylic or wood finish", "Wipe-clean acrylic or wood"),
    ("Bulk packs for 10 to 50+ tables", "Bulk packs for 10 to 50 tables"),
    ("Pairs with SiteMaker digital food menus", "Works with a SiteMaker menu page"),

    # --- FAQ --------------------------------------------------------------
    ("Everything You Need to Know", "Questions people ask about NFC hardware."),
    ("Common questions about NFC compatibility, order customization, and delivery across India.",
     "Compatibility, customisation and delivery, answered properly."),

    ("Each card, stand, or keychain contains an integrated rewritable NFC microchip. When an iPhone or Android phone is tapped against it, "
     "the phone's built-in sensor instantly launches your digital card, Google review page, or website. No batteries or charging are required.",
     "Each one holds a small rewritable NFC chip. The phone's own sensor powers it on contact and "
     "opens whatever link it is programmed to — your review page, contact card or menu. "
     "There is no battery in it and nothing to charge, so it keeps working for years."),

    ("No. Modern iPhones (iPhone XS and newer) and all NFC-enabled Android devices have native tap detection built in. "
     "Tapping immediately displays a notification on the phone's screen with zero apps required.",
     "No. Every iPhone from the XS onward and essentially every Android sold in the last several years "
     "reads these natively. The notification appears on its own. For the rare old phone that cannot, "
     "the printed QR code on the back does the same job."),

    ("Customers often forget to leave reviews once they leave your store or clinic. Placing an acrylic tap standee on your counter "
     "allows customers to tap their phone while billing and open your 5-star review box in two seconds.",
     "Because almost nobody leaves a review once they are out of the door — they meant to, and then "
     "the day happened. Asking while they are still at the counter, with a two-second action instead "
     "of a search, is the entire difference. More real reviews is also what moves a Google Business "
     "Profile up the Maps results."),

    ("Yes. FlowCraft NFC products connect to dynamic destinations, meaning you can update your phone number, social media links, catalog, "
     "or review URL anytime without needing to replace the physical hardware.",
     "Yes. The chip points at a link you control rather than at the destination directly, so you can "
     "change your number, your menu or your review URL whenever you like and the same physical card "
     "keeps working. Changing a printed card would mean reprinting it."),

    ("Yes. We program, test, and ship custom NFC cards, review standees, and keychains directly from Mumbai to anywhere in India via tracked courier services.",
     "Yes, anywhere in India by tracked courier, sent from Mumbai. Everything is programmed and then "
     "tested on both an iPhone and an Android before it goes in the box."),

    # --- Closing CTA ------------------------------------------------------
    ("Order Custom Branded NFC Hardware", "Order your hardware"),
    ("Send your brand logo, Google Maps review link, or custom design. We program, test, and ship your hardware directly across India.",
     "Send me your logo and the link you want it to open. I program it, test it on both platforms, "
     "and ship it to you."),

    # --- Prices (were hidden behind "Price on Review") ---------------------
    ("Price on Review", "PRICE_PLACEHOLDER"),
]

PRICES = ["₹899", "₹999", "₹499", "Price on request"]

s = io.open("nfc.html", encoding="utf-8").read()
before = s

missed = []
for old, new in SWAPS:
    if old not in s:
        missed.append(old[:60])
        continue
    s = s.replace(old, new)

# Fill the four price slots in document order
for price in PRICES:
    s = s.replace("PRICE_PLACEHOLDER", price, 1)

if missed:
    print("NOT FOUND (%d):" % len(missed))
    for m in missed:
        print("   ", m)

if s == before:
    sys.exit("nothing changed")
io.open("nfc.html", "w", encoding="utf-8", newline="\n").write(s)
print("nfc.html rewritten")
