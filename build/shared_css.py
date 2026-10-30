"""One-off: give every page the same display weight, type roles and browser surfaces."""
import io
import re
import sys

SHARED = """
    /* === Shared type roles (kept identical on every page) === */
    .card-title {
      font-weight: 600;
      letter-spacing: -0.014em;
      line-height: 1.25;
    }
    .lede {
      max-width: 62ch;
      text-wrap: pretty;
    }
    .label-eyebrow {
      font-weight: 600;
      font-size: 0.6875rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }

    /* === Shared browser surfaces === */
    ::selection {
      background: rgba(236, 72, 153, 0.18);
      color: #0f172a;
    }
    html {
      scrollbar-color: #cbd5e1 transparent;
      caret-color: #ec4899;
    }
    ::-webkit-scrollbar { width: 11px; height: 11px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border: 3px solid #faf8fa;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    :focus-visible {
      outline: 2px solid #ec4899;
      outline-offset: 3px;
      border-radius: 6px;
    }
    a { text-underline-offset: 0.22em; }
    .skip-link {
      position: absolute;
      left: 50%;
      top: 0.5rem;
      transform: translate(-50%, -200%);
      z-index: 100;
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      background: #0f172a;
      color: #fff;
      font-size: 0.75rem;
      font-weight: 600;
      transition: transform 0.2s ease;
    }
    .skip-link:focus-visible { transform: translate(-50%, 0); }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>"""

TITLE_RE = re.compile(
    r"(\.title-display \{\s*\n\s*)font-weight: \d+;(\s*\n\s*)letter-spacing: [-\d.]+em;"
)

for name in ("sitemaker.html", "nfc.html", "about.html",
             "leadsflowpro.html", "starscanner.html"):
    src = io.open(name, encoding="utf-8").read()
    before = src

    # One display weight everywhere
    src = TITLE_RE.sub(
        r"\1font-weight: 500;\2letter-spacing: -0.03em;", src, count=1
    )

    # Shared roles + browser surfaces, appended to the page's first <style>
    if ".label-eyebrow" not in src:
        src = src.replace("  </style>", SHARED, 1)

    # Heading weights: 700 -> 600 so large type reads crisp, not heavy
    src = re.sub(r'(<h[123][^>]*class="[^"]*?)\bfont-bold\b', r"\1font-semibold", src)

    # Skip link right after <body ...>
    if 'class="skip-link"' not in src:
        src = re.sub(
            r"(<body[^>]*>\n)",
            r'\1\n  <a href="#main" class="skip-link">Skip to content</a>\n',
            src,
            count=1,
        )

    if src == before:
        sys.exit(f"{name}: nothing changed")
    io.open(name, "w", encoding="utf-8", newline="\n").write(src)
    print(f"{name}: styled")
