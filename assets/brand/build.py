"""Build the Goroshi LLC brand set for the public GitHub profile (Stefano Theofanous, 2026-10-27).

Outputs (dark and light variants, picked by GitHub's color scheme):
  banner-dark.svg / banner-light.svg   animated banner, all text outlined
  stack-dark.svg  / stack-light.svg    curated stack ribbons with Simple Icons (CC0) brand marks
  logo.svg + logo-1024.png (rendered separately)  avatar mark

Colorway (his ties: Jerry Garcia "Butterfly Trap Line Swirls" purple, "Urban Cat Ghost" berry):
near-black #121122, midnight #181A56, indigo #46439F, violet #8877B6, electric purple #BC43D3.
Hierarchy and clutter rules from the library: Storytelling with Data pp.31, 87; Designing Interfaces p.229.
Usage: python3.14 build.py ASSETS_DIR SIMPLE_ICONS_DIR OUT_DIR
"""
import json
import os
import re
import sys

import mark as M
from typeset import cap_height, path_d, width

A, SI, OUT = sys.argv[1:4]
INTER = {w: f"{A}/Inter-{w}.ttf" for w in (400, 500, 600)}
CINZEL = f"{A}/Cinzel-600.ttf"
DIDOT = f"{A}/GFSDidot.ttf"

PAL = {
    "dark": dict(ink="#f5f4ff", sub="#d9d6ff", accent="#cbb8ff", line="#ffffff", edge="#23234d",
                 bg=("#07070d", "#0c0d2b", "#14123f"), silk=(.95, .70, .45, .30), aura=(.55, .22),
                 pill="#13143a", pill_edge="#2b2a66", head="#cbb8ff"),
    "light": dict(ink="#11123a", sub="#2a2870", accent="#46439F", line="#46439F", edge="#e3e0ff",
                  bg=("#ffffff", "#fbfaff", "#f3f1ff"), silk=(.16, .18, .20, .12), aura=(.30, .12),
                  pill="#ffffff", pill_edge="#d9d4ff", head="#46439F"),
}
SILK = ("#181A56", "#46439F", "#8877B6", "#BC43D3")


def banner(mode):
    p = PAL[mode]
    W, H, X = 1280, 400, 112
    name = path_d(CINZEL, "STEFANO THEOFANOUS", 58, X - 3, 212, tracking=3)
    co = path_d(INTER[600], "GOROSHI LLC", 15, X, 138, tracking=5)
    tt = path_d(INTER[500], "Platform & Systems Engineer", 26, X, 254)
    fx = path_d(INTER[400], "Rust · AI agent infrastructure · Financial systems · GPU compute", 17, X, 290)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Stefano Theofanous, Platform and Systems Engineer, Goroshi LLC.">
<title>Stefano Theofanous · Platform &amp; Systems Engineer · Goroshi LLC</title>
<defs>
<style>
.s1 {{ animation: d1 28s ease-in-out infinite alternate; transform-origin: 900px 160px; }}
.s2 {{ animation: d2 34s ease-in-out infinite alternate; transform-origin: 1100px 260px; }}
.s3 {{ animation: d3 40s ease-in-out infinite alternate; transform-origin: 700px 300px; }}
@keyframes d1 {{ to {{ transform: translate(-120px, 40px) rotate(18deg) scale(1.15); }} }}
@keyframes d2 {{ to {{ transform: translate(80px, -50px) rotate(-14deg) scale(.9); }} }}
@keyframes d3 {{ to {{ transform: translate(140px, -30px) rotate(10deg) scale(1.1); }} }}
.ln {{ stroke-dasharray: 1600; stroke-dashoffset: 1600; animation: draw 14s ease-in-out infinite; }}
.ln2 {{ animation-delay: 4s; }}
@keyframes draw {{ 0% {{ stroke-dashoffset: 1600; opacity: 0; }} 15% {{ opacity: .55; }} 55% {{ stroke-dashoffset: 0; opacity: .55; }} 85%, 100% {{ stroke-dashoffset: 0; opacity: 0; }} }}
.aura {{ animation: breathe 7s ease-in-out infinite; transform-origin: 1080px 206px; }}
@keyframes breathe {{ 0%, 100% {{ opacity: .55; transform: scale(.94); }} 50% {{ opacity: 1; transform: scale(1.06); }} }}
@media (prefers-reduced-motion: reduce) {{ .s1, .s2, .s3, .aura {{ animation: none; }} .ln {{ animation: none; stroke-dashoffset: 0; opacity: .4; }} }}
</style>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{p["bg"][0]}"/><stop offset=".55" stop-color="{p["bg"][1]}"/><stop offset="1" stop-color="{p["bg"][2]}"/></linearGradient>
<radialGradient id="au"><stop offset="0" stop-color="#8877B6" stop-opacity="{p["aura"][0]}"/><stop offset=".55" stop-color="#46439F" stop-opacity="{p["aura"][1]}"/><stop offset="1" stop-color="#46439F" stop-opacity="0"/></radialGradient>
<linearGradient id="cr" gradientUnits="userSpaceOnUse" x1="0" y1="150" x2="0" y2="230"><stop offset="0" stop-color="{p["ink"]}"/><stop offset="1" stop-color="{p["accent"]}"/></linearGradient>
<linearGradient id="rule" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{"#d7b8ff" if mode == "dark" else "#6b3fd1"}"/><stop offset="1" stop-color="{"#BC43D3" if mode == "dark" else "#46439F"}"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
<clipPath id="card"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>
<g clip-path="url(#card)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<g filter="url(#blur)">
<ellipse class="s1" cx="900" cy="150" rx="260" ry="120" fill="{SILK[0]}" opacity="{p["silk"][0]}"/>
<ellipse class="s2" cx="1120" cy="270" rx="220" ry="140" fill="{SILK[1]}" opacity="{p["silk"][1]}"/>
<ellipse class="s3" cx="720" cy="320" rx="200" ry="90" fill="{SILK[2]}" opacity="{p["silk"][2]}"/>
<ellipse class="s2" cx="1210" cy="90" rx="120" ry="70" fill="{SILK[3]}" opacity="{p["silk"][3]}"/>
</g>
<path class="ln" d="M520 372 C 680 322, 820 398, 960 352 S 1170 318, 1300 338" fill="none" stroke="{p["line"]}" stroke-width="1.4"/>
<path class="ln ln2" d="M560 44 C 700 92, 840 30, 960 66 S 1150 96, 1290 50" fill="none" stroke="{p["line"]}" stroke-width="1.1"/>
<circle class="aura" cx="1080" cy="206" r="150" fill="url(#au)"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="{p["edge"]}"/>
<rect x="{X - 28}" y="118" width="4" height="176" rx="2" fill="url(#rule)"/>
<path fill="{p["sub"]}" d="{co}"/>
<path fill="{p["ink"]}" d="{name}"/>
<path fill="{p["ink"]}" d="{tt}"/>
<path fill="{p["sub"]}" d="{fx}"/>
{chi_rho_banner(p)}
</svg>
'''


def chi_rho_banner(p):
    """The Chi Rho inside the same fine gradient ring as the G logo, so banner and logo read as one
    family (Stefano 2026-10-27: "make sure it actually fits"). Centered on the text block."""
    cx, cy, R = 1080, 206, 74
    ring_w = 2.6
    cap, sw = 58, 4.2
    paths, top, bottom = M.chi_rho(cx, 0, cap, sw)
    dy = cy - (top + bottom) / 2
    strokes = "".join(f'<path d="{d}"/>' for d in paths)
    return (f'<linearGradient id="crb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{p["ink"]}"/>'
            f'<stop offset=".55" stop-color="{p["accent"]}"/><stop offset="1" stop-color="{"#BC43D3" if p["ink"] == "#f5f4ff" else "#46439F"}"/></linearGradient>'
            f'<linearGradient id="crs" gradientUnits="userSpaceOnUse" x1="0" y1="{top + dy:.0f}" x2="0" y2="{bottom + dy:.0f}">'
            f'<stop offset="0" stop-color="{p["ink"]}"/><stop offset="1" stop-color="{p["accent"]}"/></linearGradient>'
            f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="url(#crb)" stroke-width="{ring_w}"/>'
            f'<g transform="translate(0 {dy:.2f})" fill="none" stroke="url(#crs)" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{strokes}</g>')


# Curated stack: what an employer or client scans for. Security posture and the reading list stay
# private (Stefano 2026-10-27: "cant people copy me"). (label, simple-icons slug or None)
STACK = [
    ("Languages", [("Rust", "rust"), ("TypeScript", "typescript"), ("Python", "python"), ("Go", "go"),
                   ("Swift", "swift"), ("C", "c"), ("SQL", "postgresql"), ("Lean 4", None), ("WebAssembly", "webassembly")]),
    ("Systems and services", [("Tokio", "rust"), ("Axum", "rust"), ("Leptos", "leptos"), ("Apache Arrow", "apachearrow"),
                              ("DataFusion", "rust"), ("redb", "rust"), ("PostgreSQL", "postgresql"), ("SQLite", "sqlite"), ("DuckDB", "duckdb")]),
    ("AI engineering", [("Claude Code", "claude"), ("Codex", None), ("Gemini", "googlegemini"), ("Cursor", "cursor"),
                        ("GitHub Copilot", "githubcopilot"), ("Model Context Protocol", "modelcontextprotocol"),
                        ("Ollama", "ollama"), ("Hugging Face", "huggingface"), ("ONNX Runtime", "onnx")]),
    ("Compute and infrastructure", [("CUDA", "nvidia"), ("Metal", "apple"), ("Arch Linux", "archlinux"), ("macOS", "apple"),
                                    ("Docker", "docker"), ("Kubernetes", "kubernetes"), ("Cloudflare", "cloudflare"),
                                    ("Tailscale", "tailscale"), ("GitHub Actions", "githubactions")]),
    ("Workflow", [("Git", "git"), ("Neovim", "neovim"), ("WezTerm", "wezterm"), ("Ghostty", "ghostty"),
                  ("Nushell", "nushell"), ("Bun", "bun"), ("Tailwind CSS", "tailwindcss"), ("uv", "uv"), ("Ruff", "ruff")]),
]


def lum(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4  # noqa: E731
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)


def icon(slug, x, y, size, mode, data):
    if slug is None:
        c = PAL[mode]["accent"]
        return f'<rect x="{x + size * .2:.2f}" y="{y + size * .2:.2f}" width="{size * .6:.2f}" height="{size * .6:.2f}" rx="{size * .14:.2f}" fill="none" stroke="{c}" stroke-width="1.6" transform="rotate(45 {x + size / 2:.2f} {y + size / 2:.2f})"/>'
    svg = open(f"{SI}/icons/{slug}.svg").read()
    d = re.search(r' d="([^"]+)"', svg).group(1)
    hexc = data[slug]
    L = lum(hexc)
    if mode == "dark" and L < .08:
        fill = "#f5f4ff"           # near-black brand marks (Apple, GitHub, Rust) turn to ink on dark
    elif mode == "light" and L > .72:
        fill = "#11123a"           # near-white or pale marks turn to ink on light
    else:
        fill = f"#{hexc}"
    s = size / 24
    return f'<path fill="{fill}" transform="translate({x:.2f} {y:.2f}) scale({s:.4f})" d="{d}"/>'


def stack(mode):
    p = PAL[mode]
    data = {i.get("slug") or "": i["hex"] for i in json.load(open(f"{SI}/data/simple-icons.json"))}
    W, PADX, ROWH, PILLH, GAPX, GAPY, ICON, FS = 880, 0, 0, 36, 10, 10, 18, 14.5
    out, y = [], 4
    for head, items in STACK:
        out.append(f'<path fill="{p["head"]}" d="{path_d(INTER[600], head.upper(), 11.5, 2, y + 13, tracking=2.4)}"/>')
        y += 26
        x = 0
        for label, slug in items:
            tw = width(INTER[500], label, FS)
            pw = 14 + ICON + 9 + tw + 16
            if x + pw > W:
                x, y = 0, y + PILLH + GAPY
            out.append(f'<rect x="{x + .5:.2f}" y="{y + .5:.2f}" width="{pw - 1:.2f}" height="{PILLH - 1}" rx="{(PILLH - 1) / 2}" fill="{p["pill"]}" stroke="{p["pill_edge"]}"/>')
            out.append(icon(slug, x + 14, y + (PILLH - ICON) / 2, ICON, mode, data))
            base = y + PILLH / 2 + FS * cap_height(INTER[500]) / 2
            out.append(f'<path fill="{p["ink"]}" d="{path_d(INTER[500], label, FS, x + 14 + ICON + 9, base)}"/>')
            x += pw + GAPX
        y += PILLH + 26
    H = y - 18
    labels = "; ".join(f"{h}: " + ", ".join(l for l, _ in it) for h, it in STACK)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}" role="img" aria-label="Stack. {labels}.">'
            f'<title>Stack. {labels}.</title>' + "".join(out) + "</svg>\n")


os.makedirs(OUT, exist_ok=True)
for mode in ("dark", "light"):
    open(f"{OUT}/banner-{mode}.svg", "w").write(banner(mode))
    open(f"{OUT}/stack-{mode}.svg", "w").write(stack(mode))
for f in sorted(os.listdir(OUT)):
    print(f, os.path.getsize(f"{OUT}/{f}"))
