# FlowCraft — open work, SEO and GEO

Written 5 November 2026. Everything here is **not done**, and most of it is
waiting on a decision only you can make. The site itself is in a publishable
state: all 7 pages verified, 5 of 6 content pages score 100/100 on the SAGE
audit, about scores 94 with no flagged issues.

---

## Where you stand

Competitor scores, all measured with `audit-sage.mjs` on 5 Nov 2026:

| Competitor | URL | Overall | SEO | GEO | AEO |
|---|---|---|---|---|---|
| **FlowCraft** (5 pages) | flowcraftstudio.netlify.app | **100** | 100 | 100 | 100 |
| Digiigrow | digiigrow.com | 96 | 100 | 100 | 70 |
| SmartReviewer AI | smartreviewer.in | 96 | 93 | 100 | 100 |
| Accountune (`/marg-erp-alternative`) | accountune.com | 96 | 93 | 100 | 100 |
| TapQR | tapqr.in | 94 | 93 | 85 | 100 |
| Web Bird | webbird.in | 93 | 85 | 100 | 100 |
| AppShakti | appshakti.com | 90* | 100 | ~100* | 50 |
| Sysmic | sysmic.in | 88 | 93 | 85 | 100 |
| Webzo | webzo.in | 87 | 85 | 100 | 100 |
| TNXN | tnxn.agency | 85 | 85 | 100 | 50 |
| Vyapar | vyaparapp.in | 84 | 68 | 100 | 100 |
| Petpooja | petpooja.com | 84 | 100 | 80 | 50 |
| Technobizzar | technobizzar.com | 81 | 85 | 85 | 80 |
| ReviewKing | reviewking.in | 67 | 93 | 55 | 80 |
| RatingFlow | ratingflow.in | 63 | 85 | 55 | 80 |
| DigitalRankPro | digitalrankpros.in | 58 | 93 | 50 | 30 |
| Dukaan | mydukaan.io | 55 | 85 | 55 | 30 |

\* AppShakti's reported GEO 85 was a tool bug, not a real finding — see
"Known tool bug" below. Its true GEO is ~100, which makes it the strongest
self-serve competitor, not one with an exploitable hole.

**The verdict:** your technical score is maxed out. That is no longer an
advantage — 8 of 16 competitors already ship `llms.txt` and FAQPage schema.
The gap is **page count and query coverage**. You have 6 pages. Web Bird has
18. Every page below is an entry point you currently don't have.

---

## 1. Decisions only you can make

Nothing below can be written until these are answered.

### Pricing page — what goes public?
Nobody in the Navi Mumbai agency set publishes a full price table. It is your
clearest differentiator and it is not on a page anywhere.

- [ ] Which prices can be published? SiteMaker ₹5,999 and reviews ₹2,999 are
      already public. What about the custom site, each billing product, and the
      ranking work — fixed, "from ₹X", or quote-only?
- [ ] Is there a retainer price for ranking work, or is it always quoted?

### Location page — which areas do you claim?
Competitors name them as crawlable text. Yours exists only in JSON-LD.

- [ ] Confirm the list: Vashi, Nerul, Belapur, Kharghar, Airoli, Panvel, Ulwe,
      Taloja? Add or remove.
- [ ] Do you want Mumbai proper as well, or Navi Mumbai only?

### Case studies — who can be named?
You currently have zero third-party proof in markup: no `Review`, no
`AggregateRating`, no client list.

- [ ] B&B Hotel Derby is already on the site. Can it be a full case study?
- [ ] Two or three more clients who would agree to be named.
- [ ] Any of them willing to give a quotable sentence? That becomes `Review`
      schema, which nothing else in the set has.

### Billing software pages — what does the software actually do?
I will not write feature claims against named competitors without this. Getting
it wrong is a factual and legal exposure, not a copywriting problem.

- [ ] Pharmacy: does it handle drug licence on invoice, Schedule H/H1, the
      narcotics register, batch-expiry? Marg owns those; say honestly which you
      have and which you don't.
- [ ] GST: which returns does it file or prepare — GSTR-1, 3B, both?
- [ ] Restaurant: does it do KOT printing, table management, Swiggy/Zomato
      sync today, or is that the roadmap?
- [ ] Gym and transport: same question — what is built vs planned?
- [ ] For each: is it sold once or licensed yearly, and at what price?

---

## 2. Pages to build, in priority order

Each is a real asset. Slugs are chosen in final form on purpose — see
"Before the domain moves".

| # | Page | Why | Blocked on |
|---|---|---|---|
| 1 | `/website-design-navi-mumbai.html` | The money page. Zauca (₹3,800), Webzo (₹4,999) and IT Planet (₹6,999, Vashi office) own this query with keyword-in-URL. Your ₹5,999 is competitive and unfindable. | Locality list |
| 2 | `/pricing.html` | `OfferCatalog` with one `Offer` per line. Nobody in the agency set has one. | Price decisions |
| 3 | `/pharmacy-billing-software.html` | `accountune.com/marg-erp-alternative` scores 96 on one page with 66 statistics. You are not in this race at all. | Feature answers |
| 4 | `/gst-billing-software.html` | Vyapar ranks here with **no H1 at all** — a technical hole you can take. | Feature answers |
| 5 | `/restaurant-billing-software.html` | Petpooja scores 84 with AEO 50: no question headings, no definition block. | Feature answers |
| 6 | `/gym-management-software.html` | No strong incumbent found. | Feature answers |
| 7 | `/transport-billing-software.html` | No strong incumbent found. | Feature answers |
| 8 | `/seo-services-navi-mumbai.html` | Your ranking work is one homepage section. Web Bird monetises six separate SEO pages. | Price decisions |
| 9 | `/case-studies/` | Plus `Review` + `AggregateRating` on index. | Client permission |
| 10 | `/no-review-gating.html` | Uncontested. ReviewKing promises "Rank #1 on Google Maps Automatically"; RatingFlow leads on "no fake reviews" — neither explains Google's actual policy. You already hold the honest position. | Nothing — can be written now |

### Informational pages (the SmartReviewer play)
SmartReviewer scores 96 and owns the review-advice funnel with exactly five
posts, each an exact query slug. These are the queries it has **not** taken:

- [ ] `/how-much-does-a-website-cost-in-navi-mumbai.html`
- [ ] `/do-i-need-a-website-if-i-have-instagram.html`
- [ ] `/how-to-get-more-google-reviews-for-a-restaurant-in-india.html`
- [ ] `/is-review-gating-against-google-policy.html`
- [ ] `/how-to-rank-on-google-maps-in-navi-mumbai.html`

Each wants `FAQPage` + `HowTo` schema and 40–50 word answers under question
H2s. None of them is blocked on a decision.

### Also missing
- [ ] Standalone `/contact.html` (currently a section, no URL of its own)
- [ ] Terms, privacy and refund pages — matters for a paid self-serve product
      and as a trust signal. SmartReviewer has all three.

---

## 3. Quick wins not yet done

- [ ] **`HowTo` schema.** Nobody in the agency or builder buckets has one; only
      TapQR does. It is the format AI assistants quote near-verbatim. Two
      candidates: "How to get a website for your shop in Navi Mumbai" on the
      location page, "How to get more Google reviews without gating" on
      reviews.html.
- [ ] **Statistical density.** Index detects 39 numbers. TNXN has 50,
      Accountune 66. Princeton's GEO research ranks this the #1 factor. Use real
      ones: turnaround in days, page weight in KB, load time in ms, 60
      templates, 20 trades, measured review lift with its window.
- [ ] **`sameAs` corroboration.** Instagram and mysitemaker.in are in. Still
      needed: Google Business Profile URL, LinkedIn, GitHub, IndiaMART listing.
      Your entity currently only exists on your own domain. Every agency
      competitor has a GBP. **This is also the highest-value preparation for the
      domain move** — send me the URLs and it is a five-minute job.
- [ ] **Query language in H2s.** Your section headings are brand-voice ("The
      studio", "Business software"). Competitors use the query verbatim in H1s.
      I deliberately did not change your hero — you chose impact over keywords
      and I am not undoing that silently — but the H2s and section ledes could
      carry the trade and city terms without touching the design.

---

## 4. Before the domain moves

Every competitor that ranks does it on an exact-match keyword slug on its own
domain. When you move off `flowcraftstudio.netlify.app`:

- [ ] Choose every slug above in its **final** form before building, not at
      migration time.
- [ ] 301 redirect 1:1. Do not restructure during the move — that is where this
      kind of work usually gets thrown away.
- [ ] Update `canonical`, `og:url`, `sitemap.xml`, `robots.txt` sitemap line,
      `llms.txt`, and every `@id` in the JSON-LD graph (they are absolute URLs).
- [ ] Re-verify the Google Search Console property and resubmit the sitemap.

---

## 5. Known tool bug in `sage-audit`

Two regexes in `~/.claude/skills/sage-audit/audit-sage.mjs` are unbounded and
produce false results. **I have not patched this — it is your global tooling,
not this project.**

- **Line 568**, `blocksSearch`:
  `/User-agent:\s*(?:OAI-SearchBot|PerplexityBot|Claude-SearchBot)[\s\S]*?Disallow:\s*\//i`
  The `[\s\S]*?` spans unlimited text and `Disallow:\s*\/` has no end-of-line
  anchor, so any later `Disallow: /api/` satisfies it. **Any site that names an
  AI agent and then disallows a subpath is falsely reported as blocking AI
  crawlers.** This is what produced the wrong AppShakti finding.
- **Line 571**, `blocksTraining`: same pattern for GPTBot / ClaudeBot /
  Google-Extended. This one fails the other way — SAGE treats controlled
  training access as a positive, so a false positive here can **inflate** a
  score.

Fix is to anchor the match to the agent's own rule group. Ask me and I'll patch
both and re-run the affected audits.

---

## 6. Other open items from this session

- [ ] **StarScanner name conflict.** `C:\Users\subby\Documents\Star Scanner`
      contains an npm package named `smart-review-system` whose README is
      titled "StarScan — More Google reviews from the customers already at your
      counter". That is the review product, not a site scanner. The site sells
      StarScanner as an unreleased site-audit tool. Nothing on the site is
      wrong today, but two products share a name. Settle it before launch.
- [ ] **SiteMaker screenshot shows the Diwali offer.** `assets/showcase/sitemaker-app.webp`
      was captured while mysitemaker.in was running the ₹4,999 Diwali promo. The
      card crop deliberately stops above the price so it cannot contradict the
      ₹5,999 in the copy, but the offer pill is still visible. A reminder is
      scheduled for 16 Nov to re-shoot it.
- [ ] **Is ₹5,999 still the standing price?** Confirm, so the copy and the
      `Offer` schema stay truthful once the promo ends.
- [ ] **Nothing in this session has been committed.** The working tree holds the
      whole redesign.
