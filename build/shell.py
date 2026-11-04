"""Write the shared page shell into every page.

The head links, sticky header, footer and behaviour script are identical on all
seven pages, so they live here once and get stamped between markers:

    <!-- shell:header --><!-- /shell:header -->

Pages that also carry <!-- pixelfield:NAME --> markers get their dissolve bands
regenerated in the same pass.

    python build/shell.py
"""
import io
import re
import sys

import pixelfield

PAGES = ["index.html", "about.html", "sitemaker.html", "reviews.html",
         "leadsflowpro.html", "starscanner.html", "404.html"]

# label, href on index, href everywhere else, pages that mark it active
NAV = [
    ("Apps",          "#build",       "index.html#build",  ("sitemaker.html",
                                                            "leadsflowpro.html",
                                                            "starscanner.html")),
    ("Smart Reviews", "reviews.html", "reviews.html",      ("reviews.html",)),
    ("Ranking",       "#ranking",     "index.html#ranking", ()),
    ("About",         "about.html",   "about.html",        ("about.html",)),
]

WA = ("https://wa.me/919372407018?text=Hi%20Subhan%2C%20I%20want%20to%20start"
      "%20a%20project%20with%20FlowCraft.")

ARROW = ('<svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.25" stroke-linecap="square" aria-hidden="true">'
         '<path d="M7 17 17 7"/><path d="M8 7h9v9"/></svg>')

HEAD = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">

  <!-- Tailwind plus the FlowCraft design system, compiled ahead of time -->
  <link rel="stylesheet" href="assets/css/tailwind.css">

  <!-- Gate the scroll-reveal start state on JS actually running, so a parse
       error or a blocked script can never leave a page blank. -->
  <script>document.documentElement.classList.add('js')</script>
"""


def nav_links(page, mobile):
    out = []
    for label, on_index, elsewhere, active_on in NAV:
        href = on_index if page == "index.html" else elsewhere
        current = ' aria-current="page"' if page in active_on else ""
        if mobile:
            cls = "px-3 py-3 text-sm font-semibold text-mint hover:bg-mint/10"
            out.append(f'        <a href="{href}" class="{cls}"{current}>{label}</a>')
        else:
            out.append(f'        <a href="{href}"{current}>{label}</a>')
    return "\n".join(out)


def header(page):
    WA_ = WA
    return f"""
  <a href="#main" class="skip-link">Skip to content</a>

  <header class="sticky top-0 z-50 bg-ground/90 backdrop-blur-sm">
    <div class="max-w-[1320px] mx-auto px-5 sm:px-8 py-3 flex items-center justify-between gap-4">

      <a href="index.html" aria-label="FlowCraft Studio, home"
         class="flex items-center gap-2 bg-mint text-navy pl-2 pr-3.5 py-1.5 shrink-0">
        <span class="w-6 h-6 bg-ground flex items-center justify-center p-1">
          <svg viewBox="0 0 512 512" class="w-full h-full" fill="none" aria-hidden="true">
            <path d="M 245 150 C 215 150, 185 170, 185 210 V 360" fill="none" stroke="#ddf5ec" stroke-width="46" stroke-linecap="square"/>
            <path d="M 140 235 H 275 C 335 235, 365 260, 365 300 C 365 342, 325 365, 275 365 C 230 365, 205 340, 205 305" fill="none" stroke="#ddf5ec" stroke-width="46" stroke-linecap="square"/>
            <rect x="382" y="322" width="56" height="56" fill="#fa7d13"/>
          </svg>
        </span>
        <span class="font-bold text-[14px] tracking-tight">FlowCraft</span>
      </a>

      <nav aria-label="Main" class="nav-pill hidden md:flex">
{nav_links(page, False)}
      </nav>

      <div class="flex items-center gap-2">
        <a href="{WA_}" target="_blank" rel="noopener noreferrer"
           class="hidden sm:inline-flex items-center gap-1.5 text-[13px] font-semibold text-mint hover:text-flame transition-colors">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.87 9.87 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2z"/></svg>
          <span>WhatsApp</span>
        </a>

        <button id="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu"
                class="md:hidden w-10 h-10 bg-flame text-navy flex items-center justify-center">
          <span class="sr-only">Menu</span>
          <svg id="nav-open-icon" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="square" aria-hidden="true"><line x1="4" y1="8" x2="20" y2="8"/><line x1="4" y1="16" x2="20" y2="16"/></svg>
          <svg id="nav-close-icon" class="w-5 h-5 hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="square" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
    </div>

    <div id="nav-menu" hidden class="md:hidden border-t border-mint/25 bg-ground">
      <div class="max-w-[1320px] mx-auto px-5 py-3 grid gap-1">
{nav_links(page, True)}
        <a href="{WA_}" target="_blank" rel="noopener noreferrer"
           class="btn mt-2 w-full">Message on WhatsApp</a>
      </div>
    </div>
  </header>
"""


FOOTER = """
  <footer class="bg-ground pt-14 sm:pt-20 pb-10">
    <div class="max-w-[1320px] mx-auto px-5 sm:px-8">

      <a href="index.html" class="d2 text-mint inline-block mb-10 sm:mb-14">Flowcraft</a>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-x-8 gap-y-10">

        <div class="col-span-2 md:col-span-1">
          <p class="body-s text-aqua max-w-xs">
            Independent software engineering studio run by Subhan Balbale.
            Based in Navi Mumbai, Maharashtra. Online service, reachable across
            India on WhatsApp.
          </p>
        </div>

        <div class="body-s tnum">
          <h2 class="serif serif-md text-mint mb-3">Contact</h2>
          <p><a href="tel:+919372407018" class="text-aqua hover:text-mint">+91 93724 07018</a></p>
          <p class="mt-1"><a href="mailto:subhanilyasbalbale@gmail.com" class="text-aqua hover:text-mint">subhanilyasbalbale@gmail.com</a></p>
        </div>

        <nav aria-label="Products" class="body-s">
          <h2 class="serif serif-md text-mint mb-3">Products</h2>
          <ul class="space-y-1.5 text-aqua">
            <li><a href="https://mysitemaker.in" target="_blank" rel="noopener noreferrer" class="hover:text-mint inline-flex items-center gap-1"><span>SiteMaker WebApp</span><svg class="w-3 h-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="square" aria-hidden="true"><path d="M7 17 17 7"/><path d="M8 7h9v9"/></svg></a></li>
            <li><a href="sitemaker.html" class="hover:text-mint">SiteMaker overview</a></li>
            <li><a href="reviews.html" class="hover:text-mint">Smart Review System</a></li>
            <li><a href="leadsflowpro.html" class="hover:text-mint">LeadsFlowPro</a></li>
            <li><a href="starscanner.html" class="hover:text-mint">StarScanner</a></li>
          </ul>
        </nav>

        <nav aria-label="Studio" class="body-s">
          <h2 class="serif serif-md text-mint mb-3">Studio</h2>
          <ul class="space-y-1.5 text-aqua">
            <li><a href="about.html" class="hover:text-mint">About Subhan</a></li>
            <li><a href="index.html#faq" class="hover:text-mint">FAQ</a></li>
            <li><a href="%s" target="_blank" rel="noopener noreferrer" class="hover:text-mint">WhatsApp</a></li>
            <li><a href="https://www.instagram.com/_flowcraft.studio/" target="_blank" rel="noopener noreferrer" class="hover:text-mint">Instagram</a></li>
          </ul>
        </nav>

      </div>

      <hr class="rule mt-12 mb-6">
      <p class="body-s text-aqua">
        &copy; 2026 FlowCraft Studio by Subhan Balbale. Updated
        <time datetime="2026-10-31">31 October 2026</time>.
      </p>
    </div>
  </footer>
""" % WA


SCRIPT = r"""
  <script>
    /* ------------------------------------------------------------------
       Scroll reveal. One observer at threshold 0.15, a 1200ms masked
       slide-up, no stagger. The extra top check catches blocks taller than
       0.15 of the viewport can ever cover, which would never fire.
       ------------------------------------------------------------------ */
    (function setupReveal() {
      var els = [].slice.call(document.querySelectorAll('[data-reveal]'));
      if (!els.length) return;

      function show(el, instant) {
        if (instant) el.classList.add('no-anim');
        el.classList.add('is-in');
      }

      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches ||
          !('IntersectionObserver' in window)) {
        els.forEach(function (el) { show(el, true); });
        return;
      }

      // threshold 0 with a small bottom inset: an element reveals as soon as
      // it genuinely enters the viewport, whichever way you are scrolling.
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          show(e.target);
          io.unobserve(e.target);
        });
      }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });

      // A reload can restore a scroll position mid-page. Anything already
      // scrolled past is shown straight away rather than left blank until the
      // visitor scrolls back down over it again.
      var restored = (window.scrollY || window.pageYOffset) > 0;
      els.forEach(function (el) {
        if (restored && el.getBoundingClientRect().bottom < 0) {
          show(el, true);
        } else {
          io.observe(el);
        }
      });

      // Safety net. A suspended or throttled page can withhold observer
      // callbacks indefinitely, and content that never reveals is content the
      // visitor never reads. After load, show anything already on screen.
      window.addEventListener('load', function () {
        setTimeout(function () {
          els.forEach(function (el) {
            if (el.classList.contains('is-in')) return;
            var r = el.getBoundingClientRect();
            if (r.top < window.innerHeight && r.bottom > 0) {
              show(el);
              io.unobserve(el);
            }
          });
        }, 400);
      });
    })();

    /* ------------------------------------------------------------------
       Background parallax at speed 0.2, the figure the reference uses.
       Layers are inset past their section on both sides, so the translate
       never exposes an edge.
       ------------------------------------------------------------------ */
    (function setupParallax() {
      var layers = document.querySelectorAll('[data-parallax]');
      if (!layers.length) return;
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

      var queued = false;
      var geom = [];

      /* Geometry is measured once per layout, not once per frame. Reading
         getBoundingClientRect inside the scroll frame interleaves reads with
         the transform writes below it, which is how a parallax ends up
         forcing a synchronous layout on every single frame. Only scrollY
         changes while scrolling, so that is the only thing worth reading. */
      function measure() {
        var y = window.pageYOffset;
        geom = [];
        for (var i = 0; i < layers.length; i++) {
          var r = layers[i].getBoundingClientRect();
          geom.push({
            top: r.top + y - (layers[i]._shift || 0),
            height: r.height,
            speed: parseFloat(layers[i].getAttribute('data-parallax')) || 0.2
          });
        }
      }

      function frame() {
        queued = false;
        var y = window.pageYOffset;
        var vh = window.innerHeight;
        for (var i = 0; i < layers.length; i++) {
          var g = geom[i];
          if (!g) continue;
          var p = (vh - (g.top - y)) / (vh + g.height);
          var shift = (p - 0.5) * g.speed * g.height;
          layers[i]._shift = shift;
          layers[i].style.transform =
            'translate3d(0,' + shift.toFixed(2) + 'px,0)';
        }
      }

      function onScroll() {
        if (queued) return;
        queued = true;
        requestAnimationFrame(frame);
      }

      function onResize() { measure(); onScroll(); }

      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onResize, { passive: true });
      window.addEventListener('load', onResize);
      measure();
      frame();
    })();

    /* ------------------------------------------------------------------
       Mobile navigation drawer
       ------------------------------------------------------------------ */
    (function setupNav() {
      var btn = document.getElementById('nav-toggle');
      var menu = document.getElementById('nav-menu');
      if (!btn || !menu) return;

      var openIcon = document.getElementById('nav-open-icon');
      var closeIcon = document.getElementById('nav-close-icon');

      function setOpen(open) {
        menu.hidden = !open;
        btn.setAttribute('aria-expanded', String(open));
        openIcon.classList.toggle('hidden', open);
        closeIcon.classList.toggle('hidden', !open);
      }

      btn.addEventListener('click', function () { setOpen(menu.hidden); });
      menu.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () { setOpen(false); });
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && !menu.hidden) { setOpen(false); btn.focus(); }
      });
    })();

    /* ------------------------------------------------------------------
       Mascot: pointer tracking across a 3x3 sprite sheet, click to boop.
       Only present on pages that render #hero-mascot.
       ------------------------------------------------------------------ */
    (function setupMascot() {
      var box = document.getElementById('hero-mascot');
      if (!box) return;

      var DIR = {
        'up-left': '0% 0%',     'up': '50% 0%',      'up-right': '100% 0%',
        'left': '0% 50%',       'center': '50% 50%', 'right': '100% 50%',
        'down-left': '0% 100%', 'down': '50% 100%',  'down-right': '100% 100%'
      };
      var CLOCKWISE = ['right', 'down-right', 'down', 'down-left',
                       'left', 'up-left', 'up', 'up-right'];
      var REACTIONS = ['0% 0%', '50% 0%', '100% 0%',
                       '0% 50%', '50% 50%', '100% 50%',
                       '0% 100%', '50% 100%', '100% 100%'];
      var SECTOR = (Math.PI * 2) / 8;
      var DEAD_ZONE = 55; // px

      var isBooped = false, boopTimer = null, reactionIdx = 0;

      window.addEventListener('pointermove', function (e) {
        if (isBooped) return;
        var rect = box.getBoundingClientRect();
        var dx = e.clientX - (rect.left + rect.width / 2);
        var dy = e.clientY - (rect.top + rect.height / 2);
        var dir = 'center';
        if (Math.hypot(dx, dy) >= DEAD_ZONE) {
          var angle = Math.atan2(dy, dx);
          if (angle < 0) angle += Math.PI * 2;
          dir = CLOCKWISE[Math.round(angle / SECTOR) % 8];
        }
        box.style.backgroundImage = "url('assets/mascot/subhan-directions.webp')";
        box.style.backgroundPosition = DIR[dir];
      }, { passive: true });

      box.addEventListener('click', function () {
        isBooped = true;
        clearTimeout(boopTimer);
        reactionIdx = (reactionIdx + 1) % REACTIONS.length;
        box.style.backgroundImage = "url('assets/mascot/subhan-reactions.webp')";
        box.style.backgroundPosition = REACTIONS[reactionIdx];
        box.classList.remove('boop-animation');
        void box.offsetWidth; // reflow
        box.classList.add('boop-animation');
        boopTimer = setTimeout(function () {
          isBooped = false;
          box.style.backgroundImage = "url('assets/mascot/subhan-directions.webp')";
          box.classList.remove('boop-animation');
        }, 550);
      });
    })();
  </script>
"""


def stamp(src, name, markup, page):
    pattern = re.compile(r"(<!-- shell:%s -->).*?(<!-- /shell:%s -->)" % (name, name), re.S)
    if not pattern.search(src):
        raise SystemExit("%s: missing shell:%s markers" % (page, name))
    return pattern.sub(lambda m: m.group(1) + markup + m.group(2), src)


def main():
    for page in PAGES:
        src = io.open(page, encoding="utf-8").read()
        src = stamp(src, "head", HEAD, page)
        src = stamp(src, "header", header(page), page)
        src = stamp(src, "footer", FOOTER, page)
        src = stamp(src, "script", SCRIPT, page)
        io.open(page, "w", encoding="utf-8", newline="\n").write(src)
        bands = pixelfield.main(page, required=False)
        print("%-20s shell stamped%s" % (page, (", %s" % bands) if bands else ""))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
