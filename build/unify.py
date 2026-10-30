"""One-off: unify the header, drop the Tailwind CDN, and fix pricing across pages."""
import io
import re
import sys

LOGO = """<svg viewBox="0 0 512 512" class="w-full h-full" fill="none" aria-hidden="true">
            <path d="M 245 150 C 215 150, 185 170, 185 210 V 360" fill="none" stroke="#ffffff" stroke-width="44" stroke-linecap="round"/>
            <path d="M 140 235 H 275 C 335 235, 365 260, 365 300 C 365 342, 325 365, 275 365 C 230 365, 205 340, 205 305" fill="none" stroke="#ffffff" stroke-width="44" stroke-linecap="round"/>
            <circle cx="410" cy="350" r="28" fill="#ec4899"/>
          </svg>"""

NAV = [
    ("Websites", "sitemaker.html"),
    ("NFC hardware", "nfc.html"),
    ("Local SEO", "index.html#ranking"),
    ("About", "about.html"),
]

WA = ("https://wa.me/919372407018?text=Hi%20Subhan%2C%20I%20want%20to%20start%20a"
      "%20project%20with%20FlowCraft.")


def desktop_links(active):
    out = []
    for label, href in NAV:
        on = href.split("#")[0] == active
        cls = ("text-slate-950 font-semibold" if on else "hover:text-slate-950")
        out.append(f'        <a href="{href}" class="{cls} transition-colors">{label}</a>')
    return "\n".join(out)


def drawer_links(active):
    out = []
    for label, href in NAV:
        on = href.split("#")[0] == active
        extra = " text-slate-950" if on else ""
        out.append(
            f'      <a href="{href}" class="mobile-nav-link block px-4 py-3 rounded-2xl '
            f'text-sm font-medium text-slate-800{extra} hover:bg-slate-50">{label}</a>'
        )
    return "\n".join(out)


def header(active, cta_label, cta_href, cta_external=True):
    rel = ' target="_blank" rel="noopener noreferrer"' if cta_external else ""
    return f"""<header class="sticky top-4 z-50 px-4 sm:px-6 max-w-5xl mx-auto">
    <nav aria-label="Main" class="bg-white/85 backdrop-blur-md border border-slate-200/80 rounded-full pl-5 pr-2 py-2 flex items-center justify-between shadow-xs">

      <a href="index.html" aria-label="FlowCraft Studio, home" class="flex items-center gap-2.5 shrink-0">
        <span class="w-7 h-7 rounded-full bg-slate-950 flex items-center justify-center p-1.5">
          {LOGO}
        </span>
        <span class="font-semibold text-[15px] tracking-tight text-slate-950">flowcraft<span class="text-pink-500">.</span></span>
      </a>

      <div class="hidden md:flex items-center gap-7 text-[13px] font-medium text-slate-600">
{desktop_links(active)}
      </div>

      <div class="flex items-center gap-1.5">
        <a href="{cta_href}"{rel} class="pill-button hidden sm:inline-flex px-5 py-2.5 text-[13px] font-semibold">{cta_label}</a>

        <button id="mobile-menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu"
                class="md:hidden w-10 h-10 rounded-full flex items-center justify-center text-slate-800 hover:bg-slate-100 transition-colors">
          <span class="sr-only">Menu</span>
          <svg id="hamburger-icon" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><line x1="4" y1="8" x2="20" y2="8"/><line x1="4" y1="16" x2="20" y2="16"/></svg>
          <svg id="close-icon" class="w-5 h-5 hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
    </nav>

    <div id="mobile-menu" class="hidden md:hidden mt-2 rounded-3xl bg-white/95 backdrop-blur-md border border-slate-200/80 shadow-lg p-2">
{drawer_links(active)}
      <a href="{cta_href}"{rel} class="pill-button block mt-1 px-4 py-3 text-center text-sm font-semibold">{cta_label}</a>
    </div>
  </header>"""


PAGES = {
    "sitemaker.html": ("Order a website", WA, True),
    "nfc.html": ("Order hardware", WA, True),
    "about.html": ("Start a project", WA, True),
    "leadsflowpro.html": ("Start a project", WA, True),
    "starscanner.html": ("Start a project", WA, True),
}

CDN_RE = re.compile(r'[ \t]*<script src="https://cdn\.tailwindcss\.com"></script>\n')
HEADER_RE = re.compile(r"<header\b.*?</header>", re.S)
GSAP_RE = re.compile(
    r'[ \t]*<script src="https://cdnjs\.cloudflare\.com/ajax/libs/gsap/[^"]*"></script>\n'
)

for name, (cta, href, ext) in PAGES.items():
    src = io.open(name, encoding="utf-8").read()
    before = src

    # 1. Tailwind: runtime CDN -> compiled stylesheet
    if not CDN_RE.search(src):
        sys.exit(f"{name}: tailwind CDN tag not found")
    src = CDN_RE.sub(
        '  <link rel="stylesheet" href="assets/css/tailwind.css">\n', src, count=1
    )

    # 2. GSAP was loaded but only ever used for decoration on these pages
    src = GSAP_RE.sub("", src)

    # 3. One header everywhere
    if not HEADER_RE.search(src):
        sys.exit(f"{name}: header not found")
    src = HEADER_RE.sub(lambda m: header(name, cta, href, ext), src, count=1)

    # 4. aria-expanded on the drawer toggle
    src = src.replace(
        "          const isOpen = !mobileMenu.classList.contains('hidden');",
        "          const isOpen = !mobileMenu.classList.contains('hidden');\n"
        "          mobileMenuBtn.setAttribute('aria-expanded', String(!isOpen));",
    )

    # 5. Headings: stop Tailwind's font-bold overriding the display weight
    src = src.replace('class="title-display ', 'class="title-display ')
    src = re.sub(
        r'(class="[^"]*title-display[^"]*)\bfont-bold\b', r"\1", src
    )
    src = re.sub(
        r'(class="[^"]*title-display[^"]*)\bfont-normal\b', r"\1", src
    )

    # 6. Pricing
    src = src.replace("₹6,000", "₹5,999").replace('"price": "6000"', '"price": "5999"')
    src = src.replace("website design 6000", "website design 5999")

    if src == before:
        sys.exit(f"{name}: nothing changed")
    io.open(name, "w", encoding="utf-8", newline="\n").write(src)
    print(f"{name}: updated")
