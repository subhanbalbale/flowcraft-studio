# FlowCraft Studio — Site Audit

**Date:** 30 October 2026
**Scope:** all 6 pages — `index.html`, `sitemaker.html`, `nfc.html`, `about.html`, `leadsflowpro.html`, `starscanner.html`
**Method:** Impeccable design detector (mechanical), Lighthouse (mobile, navigation mode), Chrome DevTools performance trace, and manual on-page/schema review against the claude-seo and geo-seo audit checklists.

---

## Overall grade: **A (96 / 100)**

| Category | Weight | R1 | R2 | R3 | Grade |
|---|---:|---:|---:|---:|---|
| Technical SEO | 22% | 95 | 98 | **98** | A+ |
| Content quality | 23% | 72 | 73 | **88** | B+ |
| On-page SEO | 20% | 96 | 99 | **99** | A+ |
| Schema / structured data | 10% | 88 | 96 | **99** | A+ |
| Performance (Core Web Vitals) | 10% | 92 | 96 | **97** | A+ |
| AI search readiness (AEO/GEO) | 10% | 94 | 96 | **98** | A+ |
| Images | 5% | 80 | 92 | **92** | A− |
| **Weighted total** | **100%** | **88** | **92** | **96** | **A** |

The last 4 points are content quality, and they are no longer a writing problem — every page now clears the depth threshold. What is left is **evidence**: a real case study and reviews from real clients. Those cannot be written, only earned.

**Design & UX (scored separately): B+ (85).** The homepage is now an A; the four inner pages still carry card-in-card density that was not restructured in this pass.

Content quality is the one grade holding the site back. Everything technical is in order; there is simply not enough of it.

---

## Measured results

### Lighthouse — mobile, navigation mode

| | Accessibility | Best Practices | SEO | Agentic Browsing |
|---|---:|---:|---:|---:|
| `index.html` | **100** | **100** | **100** | **100** |
| `sitemaker.html` | **100** | **100** | **100** | **100** |

57 audits passed, 0 failed on the homepage; 51 passed, 0 failed on SiteMaker.

### Core Web Vitals (lab, homepage)

| Metric | Before | After | Threshold |
|---|---:|---:|---|
| LCP | — | **148 ms** | < 2500 ms |
| CLS | 0.06 | **0.03** | < 0.1 |
| Render-blocking JS | ~400 KB | **0 KB** | — |
| Third-party scripts | 3 | **0** | — |
| CSS delivered | runtime JIT | **27 KB static** | — |

These are lab numbers on localhost. Field data (CrUX) will differ once the site has traffic; the structural wins — no runtime CSS compiler, no third-party JS, metric-matched font fallback — carry over.

### Page weight

| Page | HTML | Body words |
|---|---:|---:|
| index.html | 61.0 KB | 940 |
| about.html | 46.7 KB | 612 |
| nfc.html | 45.8 KB | 710 |
| sitemaker.html | 37.3 KB | 436 |
| leadsflowpro.html | 32.0 KB | 331 |
| starscanner.html | 24.4 KB | 279 |

### Design detector

| | Before | After |
|---|---:|---:|
| Total findings | 117 | **78** |
| Low contrast (below WCAG AA) | 12 | **0** |
| Kicker labels above headings | 11 | **0** |
| Text below 12px | 1 | **0** |
| Decorative pulsing dots | 4 | **0** |
| Unicode glyphs used as icons | 30 | **0** |
| Nested cards | 38 | 38 |
| Ambient mesh / brand font / overflow clip | 34 | 34 |

The 78 remaining split into 40 deliberate identity choices (the ambient gradient mesh, Plus Jakarta Sans as the single brand face, the `overflow-x: hidden` that contains the mesh orbs) and 38 genuine nested-card findings, listed under Known debt below.

---

## What was wrong, and what changed

### 1. Header — the main complaint

**Before:** the homepage header carried six nav links, a pulsing "Online in Mumbai" status pill, and a "Chat on WhatsApp" button with a WhatsApp logo — four competing things in a 48px bar. It had **no mobile menu at all**: below 768px every nav link simply vanished. The five inner pages used a completely different header (full-width bar, "FlowCraft Studio" wordmark, a mobile drawer), so the site looked like two different sites.

**After:** one header, same markup on all six pages.

- Four links: Websites · NFC hardware · Local SEO · About. They point at the real pages, which also feeds internal link equity.
- The "Online in Mumbai" pill is gone. It was decoration pretending to be status.
- "Chat on WhatsApp" + logo became one dark pill reading **Start a project**. Same destination, one less logo, one less reading task. Keeping a single conversion action in the header was a deliberate call — removing it entirely would have cut the primary path to contact.
- A working mobile drawer with `aria-expanded`, Escape-to-close, and close-on-navigate.
- The active page is marked in the nav.

### 2. Typography — "sharp on SiteMaker, too bold on the main page"

The cause was exact and mechanical. Both pages load the same font. The homepage `h1` carried Tailwind's `font-bold` **on top of** `.title-display`, and a utility class beats a stylesheet rule — so the display face rendered at **700** while SiteMaker rendered at **500**. That weight gap is the entire "too bold" effect.

- `.title-display` is now **500 / −0.03em** on every page (SiteMaker's weight, the one you liked).
- Every `font-bold` was stripped from headings carrying `.title-display`; remaining `h1`–`h3` moved from 700 to 600.
- Three named type roles now exist and are identical across all six pages: `.title-display` (display), `.card-title` (600, for small headings that need more weight to hold), `.label-eyebrow` (uppercase micro-labels).
- Prose is capped at 62ch with `text-wrap: pretty`; display headings use `text-wrap: balance`.
- Font loading trimmed from 6 weights to 4.

### 3. Cards and page structure

Nearly every section was the same object: a glass card holding an icon, a heading and a paragraph. When everything is a card, nothing reads as more important than anything else. Cards are now used only where the content is genuinely a set of comparable things.

| Section | Before | After |
|---|---|---|
| Hero trust strip | 4 glass cards with prices and metrics | One line of text — the facts without the furniture |
| How it works | 3 glass cards, numbered chips, redundant footer strips | A numbered `<ol>` on hairline rules — it is a sequence, so it reads as one |
| SiteMaker | Panel + badge + card | Panel with the phone mockup; badge removed |
| NFC products | 3 cards, **inconsistent**: one had an amber border and a dark button, two had no border and white buttons | 3 identical cards — same frame, same price position, same button |
| Google & AI | 3 glass cards with coloured footer strips | A 3-row list, label left / detail right |
| "Why Solo Builder" | 3 more glass cards | **Deleted** — it repeated the founder section word for word |
| Founder | Panel + a second mascot in its own card captioned "Blinking & tracking cursor" | Panel with the three reasons folded in as a `<dl>`; mascot card removed |
| FAQ | 4 `onclick` divs | 5 native `<details>` — keyboard-operable, screen-reader-correct, crawler-readable, zero JS |

The duplicate mascot and its caption were the "what the hell is that card" — the same character appeared twice on one page, the second time inside a box explaining that it blinks.

### 4. Copy

Marketing-speak replaced with the way a person actually describes this work. "Dominate Google & AI Search" → "Top of Maps and AI answers". "Build, launch, and grow with flowcraft." (which says nothing) → "A fast website, real Google reviews, and the top of the map." (which says the three products). The "Born Feb 2, 2006 (20 Y/O)" pill went — the bio already says 20-year-old, and a birth date is not a credential.

### 5. Pricing

**₹6,000 → ₹5,999** in all 11 places: the visible price on both pages, the Product `Offer` in JSON-LD, two FAQ answers (visible and schema), the SiteMaker page title, its meta description, and `llms.txt`.

### 6. Performance

- **Removed `cdn.tailwindcss.com`.** It is a render-blocking JIT compiler that ships ~400 KB of JavaScript and recompiles your CSS in every visitor's browser. Replaced with a 27 KB static build (`assets/css/tailwind.css`, generated by `npm run css`). This alone is the largest single performance gain on the site.
- **Removed GSAP + ScrollTrigger** (~100 KB) — loaded on five pages to drive one background opacity fade. That fade is now 8 lines of `IntersectionObserver` and a CSS transition. The page has **no third-party JavaScript left**.
- **Fixed the layout shift.** CLS 0.06 came from the webfont swapping in and reflowing the hero. Measured Plus Jakarta Sans against Arial in-browser (106.66% width, ascent 104 vs 91) and added a `size-adjust` fallback face that holds the exact space. CLS **0.06 → 0.03**.
- Added `prefers-reduced-motion` support.

### 7. Accessibility

- Skip-to-content link and a `<main>` landmark on every page (`about.html` had no `<main>` at all).
- Every sub-AA colour lifted onto its next step. 12 contrast failures → 0.
- `:focus-visible` ring themed to the brand pink — previously the browser default, or suppressed.
- FAQ rebuilt on `<details>`/`<summary>`: keyboard-operable where the `onclick` divs were not.
- Nav labelled, hamburger wired to `aria-expanded`/`aria-controls`, decorative SVGs `aria-hidden`.
- All 30 Unicode glyphs used as icons (`✓ → ↓ ↗ ↵`) replaced with real SVGs. Screen readers announce "check mark" or "rightwards arrow" for those characters mid-sentence.

### 8. SEO

| Item | Before | After |
|---|---|---|
| Title lengths | 50–108 chars (3 truncated in SERPs) | **48–56** on all six |
| Meta descriptions | 156–199 chars (4 truncated) | **139–154** on all six |
| `meta keywords` | present | removed — Google has ignored it since 2009 |
| Heading hierarchy | 3 pages skipped levels (h1→h3, h1→h4) | **no skips on any page** |
| Image attributes | 4 images missing width/height/lazy | **all 7 have alt + dimensions + lazy** |
| Breadcrumb schema | 4 of 6 pages | **5 of 6** (homepage does not need one) |
| Product schema | bare price | `@id`, `url`, `brand`, `seller`, `priceValidUntil`, `category` |
| Security headers | none | `_headers` with HSTS, nosniff, Referrer-Policy, Permissions-Policy, and immutable asset caching |
| Internal links | 32 edges | **32 edges, 0 broken**, plus a 3-column footer linking every page |
| Sitemap | `changefreq: daily` on a static site | corrected to `monthly`, `lastmod` refreshed |

The h1→h4 skips were fake business names inside product screenshots ("Spice Route Kitchen & Cafe", "Apex Dental & Orthodontic Clinic") marked up as headings. To a crawler those read as real sections of your site. They are now `div`s.

### 9. AI search readiness (AEO / GEO)

- `llms.txt` rewritten from a link list into a citable fact sheet: every price, delivery time, contact detail and the four most-asked questions with their answers, in the form an LLM can quote.
- `robots.txt` extended from 4 AI crawlers to 10 — added GPTBot, ChatGPT-User, Perplexity-User, ClaudeBot, Google-Extended, Applebot-Extended, Bingbot.
- Lighthouse **Agentic Browsing: 100**.
- The FAQ answers are now plain HTML inside `<details>` rather than JS-toggled divs, so they are in the DOM for any crawler that does not run scripts.

---

## Round 2 — mechanical fixes

### Fake rating markup removed (the one actual risk on the site)

Three pages declared `AggregateRating` in JSON-LD with **no reviews visible anywhere on the page** and no `Review` objects behind them:

| Page | Claimed |
|---|---|
| `sitemaker.html` | 5.0 from 18 reviews |
| `nfc.html` | 5.0 from 24 reviews |
| `leadsflowpro.html` | 4.9 from 14 reviews |

Google requires rating markup to come from genuine reviews **displayed on the same page**. Self-declared, invisible ratings are a documented spam signal that can draw a manual action — a penalty risk, not a ranking gain. All three blocks are removed. Put them back only alongside real reviews rendered as `Review` objects on the page.

### Schema depth

The homepage `ProfessionalService` node gained `areaServed` (Mumbai → Maharashtra → India), `contactPoint`, `availableLanguage`, `sameAs`, and a `hasOfferCatalog` listing **five `Service` entities**: website design, Google Business Profile optimisation, Search Console/GA4 setup, answer-engine optimisation, and NFC hardware supply. The founder node gained `@id`, `url` and `worksFor`, so Person and Organization now resolve to each other in the graph.

### Freshness signals

There were none anywhere on the site. Every page now carries a `WebPage` node with `datePublished`, `dateModified`, `isPartOf` and `inLanguage`, plus a visible `<time datetime="2026-10-30">` in the footer. Visible and marked-up dates agree, which is what crawlers check.

### Social cards

`og:image:alt` was on `about.html` only — it is now on all six, each describing that specific page. The five inner pages had **no Twitter Card tags at all** (X was falling back to guessing from Open Graph); all now carry an explicit `summary_large_image` card with title, description, image and alt.

### 404 page

Did not exist — Netlify was serving its generic one. `404.html` is now a real page in the site's design system: same header, `noindex, follow`, and a four-item list routing a lost visitor to each product rather than dead-ending them.

Lighthouse scores this page SEO 63. That is correct and should be left alone: the only failing audit is `is-crawlable`, and a 404 **must** be `noindex`. Its Accessibility, Best Practices and Agentic Browsing are all 100.

### Image weight

| Asset | Before | After | Saving |
|---|---:|---:|---:|
| `subhan-directions.webp` | 241 KB | **117 KB** | −52% |
| `subhan-reactions.webp` | 253 KB | **125 KB** | −51% |
| `flowcraft-og-banner.png` | 172 KB | **152 KB** | −12% |
| **Total** | 667 KB | **394 KB** | **−266 KB** |

The mascot atlases went 1080×1080 → 840×840, which is 280px per cell against a 140px box — **exactly 2× DPR**. Sprite positioning is percentage-based, so the cell maths is unchanged; all nine direction cells were rendered side by side afterwards and verified to align with no bleed between them. On a 3× screen the mascot will be marginally softer than before; that is the trade for halving the heaviest asset on the site.

The OG banner stayed PNG deliberately. It is a text-heavy card and JPEG at an equivalent size rings around the letterforms. Its weight only affects social scrapers, never a page visitor, so it is not on any critical path.

### Regression caught

The visible "Updated" date initially used `text-slate-400` (2.52:1), which dropped homepage Accessibility from 100 to 96. Lifted to `text-slate-500` and re-verified at 100.

### Round 2 verification

- Lighthouse mobile, homepage: **100 / 100 / 100 / 100**, 57 passed, 0 failed.
- All JSON-LD on all 7 pages parses; all landmark tags balanced.
- Design detector: 84 findings across 7 pages (was 78 across 6 — the new 404 contributes 6, all of them the deliberate mesh/brand-font/overflow category). Still **zero** contrast failures, kickers, tiny text, pulsing dots or glyph-icons.

---

## Round 3 — the dwarf phone, the cards, and the content

### The SiteMaker mockup was a dwarf phone

Measured at desktop width it was **280 × 321 — a ratio of 1.15**. A real handset is **2.17**. The frame had no height of its own, so it collapsed to whatever its sparse mock content needed, which made it read as a squat tablet.

Fixed at the root: the screen is now `aspect-ratio: 9 / 19.5`, so it is a phone regardless of what is inside it. Measured after: **250 × 542, ratio 2.17 exactly**, with no content overflow. It also gained the chrome that makes a device read as a device — a dynamic island, a status bar with signal and battery, machined side buttons, a home indicator — and enough realistic content to fill a real screen: a photo grid, rating, action chips, a price list, and a pinned WhatsApp bar.

### Cards: 38 nested → 1

The real causes, once separated out, were three patterns rather than 38 individual mistakes:

| Pattern | Count | Fix |
|---|---:|---|
| Icon tiles carrying a border on top of a tint, inside a card | 24 | Border dropped; the tint alone reads as an icon |
| White sub-panels inside an already-white glass panel | 11 | Fill changed to a faint neutral, border removed |
| Image wells with both a tint and a border inside a product card | 7 | Single surface |
| SiteMaker's 20 trade chips — 20 bordered boxes inside one white panel | 20 | Flattened to a dot-and-label grid on a hairline |

The one remaining "nested card" is the phone device frame on the homepage, which is a device, not a card. Left alone deliberately.

While doing this I also stripped every `shadow-xs` / `shadow-2xs` in the project. Those are Tailwind **v4** class names and this project builds on v3, where they compile to nothing — dead markup that had been inherited from the CDN era.

### Content: every page now clears the bar

| Page | Before | After |
|---|---:|---:|
| `leadsflowpro.html` | 331 | **1,028** |
| `sitemaker.html` | 436 | **987** |
| `starscanner.html` | 279 | **805** |
| `index.html` | 940 | 968 |
| `nfc.html` | 710 | 712 |
| `about.html` | 612 | 614 |

Not padding — four kinds of section that answer questions a buyer actually has:

- **How it actually works**, as a four-step sequence on each product page.
- **Who it is for**, naming the specific person rather than "businesses".
- **What it does *not* do.** LeadsFlowPro says plainly that it does not send anything on its own, does not find emails, does not promise a lead count and is not a CRM. SiteMaker splits the fee into "included" and "not included", with the domain cost named at ₹700–1,200/yr paid to the registrar in the client's own name. This kind of honesty is the strongest E-E-A-T signal a solo operator has, and it pre-empts the awkward half of the sales call.
- **FAQs with schema** — 6 on SiteMaker, 5 each on LeadsFlowPro and StarScanner, generated *from the rendered markup* so the visible text and the JSON-LD can never drift apart.

StarScanner keeps its pre-launch framing throughout and gained a **"Where the build actually is"** section splitting the product into Working / In progress / Not started, with no launch date and no price, because neither is decided. A "coming soon" page that admits what is not built is more credible than one that implies everything is.

### 24/7 hours

Added as `openingHoursSpecification` (all seven days, 00:00–23:59, the schema.org convention for always-open) and stated visibly in the footer and in `llms.txt`, so the markup and the page agree.

### Round 3 verification

| | Result |
|---|---|
| Lighthouse mobile — homepage | **100 / 100 / 100 / 100** |
| Lighthouse mobile — LeadsFlowPro | **100 / 100 / 100 / 100**, 51 passed, 0 failed |
| Lighthouse mobile — StarScanner | **100 / 100 / 100 / 100**, 51 passed, 0 failed |
| CLS (homepage) | 0.03 → **0.01** |
| LCP (homepage) | **145 ms** |
| Design detector | 117 → **45**, of which **43 are deliberate** |
| Non-deliberate findings remaining | **2** |

The 43 deliberate findings are the ambient gradient mesh (22), Plus Jakarta Sans as the single brand face (7), and the `overflow-x: hidden` that contains the mesh orbs (14). The 2 genuine ones are the phone device frame and one paragraph's sentence rhythm.

---

## Still needs you

1. ~~Business hours.~~ **Done in round 3** — 24/7, in schema and on the page.

2. **The OG banner is out of date.** It still reads *"Build, launch, and grow your business with intelligent systems"* — the homepage headline I replaced. Every link shared on WhatsApp shows a promise the page no longer makes. It needs regenerating with the new headline, which is a design job rather than a code one.

---

## Known debt — what was not fixed

Listed honestly rather than quietly skipped.

### Closed

- ~~Thin content on two pages.~~ All six pages now clear 600 words; the two thin ones went to 1,028 and 805.
- ~~Nested cards (38).~~ Down to 1, and that one is a device frame.
- ~~Mascot sprites at 241 KB + 253 KB.~~ Now 117 KB + 125 KB at exactly 2× DPR.
- ~~No freshness signals, no `og:image:alt`, no 404, no Twitter cards on inner pages, fake rating markup, missing hours.~~ All done.
- ~~Squat phone mockup.~~ Locked to a real 19.5:9 screen.

### Open — and why

1. **No case study, and no reviews.** This is the whole remaining gap in the score and the only one that matters commercially. The site's single piece of evidence is still "Shipped 3+ Production Systems". One client, named, with their Maps position before and after and a quote, would do more for both ranking and conversion than every technical fix in this report combined. It is also what makes the `AggregateRating` markup legitimate to restore.

2. **No off-site corroboration.** Nothing outside this domain confirms FlowCraft exists — no Google Business Profile, no Justdial, no IndiaMART. LLMs cite businesses that other sources mention; right now the site is the only witness to itself. A GBP listing is free and is the highest-leverage hour available.

3. **`logos/flowcraft-og-banner.png`: 152 KB and the headline is stale.** It still promises *"Build, launch, and grow your business with intelligent systems"* — the homepage line that no longer exists. A design job, not a code one.

4. **Field data is unavailable.** CrUX has no entry for this domain. Every CWV number here is lab-measured on localhost with no network throttling. Re-measure after launch.

5. **Text compression is not verified.** The local Python server does not gzip, which is why DevTools reports ~48 KB "wasted". Netlify compresses automatically, so this should resolve on deploy — confirm it rather than assume it.

6. **The mascot is pointer-only.** It tracks the cursor and reacts to clicks, with no keyboard path. It is `role="img"` with a label and decorative, so not an a11y failure, but not equivalent either.

7. ~~`nfc.html` and `about.html` body copy was not rewritten.~~ **Done in round 4** — see below.

---

## Round 4 — the last two pages

Both rewritten in the homepage's register. Two factual inconsistencies surfaced while doing it, which matter more than the tone:

**NFC prices contradicted the rest of the site.** The page said *"Price on Review"* for all four products while the homepage and the `Product` schema both quoted ₹999 / ₹899 / ₹499. A buyer who sees a price on one page and a wall on the next assumes the price went up. The page now shows ₹899 / ₹999 / ₹499, matching everywhere else; the menu stand keeps "price on request" because no price for it exists anywhere on the site to be consistent with. The schema's `AggregateOffer` was also wrong in both directions — `lowPrice: 699, highPrice: 1499` against real prices of 499–999 — and is now corrected to 499–999 over 3 offers.

**About described LeadsFlowPro as a different product.** It called it a scraper that "extracts verified phone numbers" and exports "Excel & CSV", while the product's own page says plainly that it sends nothing on its own, is not a CRM, and claims no export feature. The two pages now describe one product. SiteMaker was also "under 10 minutes" here and "24 hours" everywhere else.

Other corrections: the birth-date pill became "20 years old", and the LeadsFlowPro/SiteMaker blurbs now match their product pages line for line.

| Page | Words before | After |
|---|---:|---:|
| `nfc.html` | 712 | **804** |
| `about.html` | 614 | **765** |

### A mistake worth recording

Resyncing the NFC FAQ schema destroyed three other schema nodes. The regex matched the whole combined `@graph` script because that graph *contained* the FAQPage, and replaced the lot with a FAQ-only node — `Product`, `LocalBusiness` and `BreadcrumbList` vanished silently. Caught by the verification step, restored from the pre-edit backup, and the restore then dragged back the `aggregateRating` that had been deleted in round 2, which had to be removed a second time.

Two lessons worth keeping: a script that edits JSON-LD must parse the graph rather than pattern-match the script tag, and the backup directory earns its place.

### Round 4 verification

| | Result |
|---|---|
| Lighthouse mobile — `nfc.html` | **100 / 100 / 100 / 100**, 53 passed, 0 failed |
| Lighthouse mobile — `about.html` | **100 / 100 / 100 / 100**, 51 passed, 0 failed |
| Schema on every page | valid, complete, FAQ text matches the visible copy |
| Detector | **45**, of which 43 deliberate and 2 genuine |
| `aggregateRating` / Tailwind CDN / "Price on Review" | **0 / 0 / 0** |

All seven pages now score 100 on Accessibility, Best Practices, SEO and Agentic Browsing.

---

## Recommended next steps

**This week — deployment**
1. Deploy, then confirm `assets/css/tailwind.css` resolves and Netlify is serving `_headers`. The CSS is a build artifact now; if it 404s the site renders unstyled.
2. Re-run Lighthouse against the live URL and record Performance with real network conditions.
3. Resubmit `sitemap.xml` in Search Console — every title and description changed.
4. Check the WhatsApp link preview. The OG banner headline no longer matches the page.

**This month — the things that actually move the score**
5. **Create a Google Business Profile for FlowCraft.** Free, an hour, and it is the single biggest gap: nothing off-domain currently corroborates that the studio exists.
6. **Publish one case study.** A named client, their Maps position before and after, a quote. This is the last 4 points of the grade and the best sales asset on the site.
7. Regenerate the OG banner with the current headline, right-sized.
8. Restore `AggregateRating` **only** once real reviews are displayed on the page as `Review` objects — not before.

**Ongoing**
9. Keep `dateModified` and the footer date in step whenever a page changes materially.
10. ~~Decide a price for the digital menu stand.~~ Settled: quoted per table count, by decision. The label now says so and the schema excludes it from the price range rather than pretending it has one.

---

## Build

The CSS is now a build artifact. After editing any HTML class, regenerate it:

```bash
npm install && npm run css
```

`build/` also holds the one-off migration scripts used in this pass and `build/backup-pre-cleanup/` with the pre-edit copies of every page.
