"""Build the Goroshi LLC brand set for the public GitHub profile (Stefano Theofanous, 2026-10-27).

Outputs (dark and light variants, picked by GitHub's color scheme):
  banner-dark.svg / banner-light.svg   animated banner, all text outlined
  stack-dark.svg  / stack-light.svg    curated stack ribbons with Simple Icons (CC0) brand marks

Colorway: midnight blue and Solo Leveling purple; no pink or magenta (Stefano 2026-10-27).
Hierarchy and clutter rules from the library: Storytelling with Data pp.31, 87; Designing Interfaces p.229.
Usage: python3.14 build.py ASSETS_DIR SIMPLE_ICONS_DIR OUT_DIR
"""
import json
import os
import re
import sys

import gmark
import mark as M
from typeset import cap_height, path_d, width

A, SI, OUT = sys.argv[1:4]
INTER = {w: f"{A}/Geist-{w}.ttf" for w in (400, 500, 600)}  # Geist (SIL OFL 1.1)
CINZEL = f"{A}/Geist-600.ttf"  # display face: Geist 600 (Cinzel retired 2026-10-27)
DIDOT = f"{A}/GFSDidot.ttf"

PAL = {
    "dark": dict(ink="#F7F4FF", sub="#DDD6FF", accent="#B9A8FF", edge="#251E60",
                 bg=("#05060F", "#0D0B33", "#1A1252"), silk=(.95, .75, .55, .40), aura=(.55, .22),
                 pill="#120F40", pill_edge="#2E267A", head="#B9A8FF", rule=("#B9A8FF", "#6A35FF")),
    "light": dict(ink="#140E40", sub="#2E2380", accent="#5A35E0", edge="#E2DCFF",
                  bg=("#FFFFFF", "#F7F8FF", "#F1EEFF"), silk=(.14, .16, .16, .12), aura=(.28, .12),
                  pill="#FFFFFF", pill_edge="#DAD2FF", head="#4A2FC4", rule=("#3A1F9E", "#6A35FF")),
}
# Midnight base, Shadow Monarch purple accents at 252-258 deg hue; never past 270 deg (pink starts ~290).
SILK = ("#130F4A", "#3A1F9E", "#4E2BC8", "#6A35FF")


def banner(mode):
    p = PAL[mode]
    W, H, X = 1280, 400, 112
    name = path_d(f"{A}/Geist-600.ttf", "Stefano Theofanous", 62, X - 3, 212, tracking=-1.2)
    co = path_d(INTER[500], "GOROSHI LLC", 14, X, 138, tracking=4.5)
    tt = path_d(INTER[500], "Founder and Rust Systems Engineer", 26, X, 254)
    fx = path_d(INTER[400], "Multi-model AI agent platform, cent-exact bookkeeping, Rust GPU kernels", 17, X, 290)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Stefano Theofanous, Founder and Rust Systems Engineer, Goroshi LLC. Multi-model AI agent platform, cent-exact bookkeeping, Rust GPU kernels.">
<title>Stefano Theofanous · Founder and Rust Systems Engineer · Goroshi LLC</title>
<defs>
<style>
.s1 {{ animation: d1 22s ease-in-out infinite alternate; transform-origin: 900px 160px; }}
.s2 {{ animation: d2 26s ease-in-out infinite alternate; transform-origin: 1100px 260px; }}
.s3 {{ animation: d3 18s ease-in-out infinite alternate; transform-origin: 700px 300px; }}
.sweep {{ animation: sweep 16s ease-in-out infinite; }}
@keyframes sweep {{ 0% {{ transform: translateX(-700px); opacity: 0; }} 30% {{ opacity: .55; }} 70% {{ opacity: .55; }} 100% {{ transform: translateX(1500px); opacity: 0; }} }}
@keyframes d1 {{ to {{ transform: translate(-260px, 70px) rotate(22deg) scale(1.3); }} }}
@keyframes d2 {{ to {{ transform: translate(160px, -90px) rotate(-18deg) scale(.8); }} }}
@keyframes d3 {{ to {{ transform: translate(300px, -60px) rotate(14deg) scale(1.25); }} }}
.aura {{ animation: breathe 7s ease-in-out infinite; transform-origin: 1080px 206px; }}
@keyframes breathe {{ 0%, 100% {{ opacity: .45; transform: scale(.9); }} 50% {{ opacity: 1; transform: scale(1.1); }} }}
@media (prefers-reduced-motion: reduce) {{ .s1, .s2, .s3, .aura, .sweep {{ animation: none; }} .sweep {{ opacity: 0; }} }}
</style>
<linearGradient id="sw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B9A8FF" stop-opacity="0"/><stop offset=".5" stop-color="#B9A8FF" stop-opacity="{.10 if mode == "dark" else .16}"/><stop offset="1" stop-color="#B9A8FF" stop-opacity="0"/></linearGradient>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{p["bg"][0]}"/><stop offset=".55" stop-color="{p["bg"][1]}"/><stop offset="1" stop-color="{p["bg"][2]}"/></linearGradient>
<radialGradient id="au"><stop offset="0" stop-color="#6A35FF" stop-opacity="{p["aura"][0]}"/><stop offset=".55" stop-color="#3A1F9E" stop-opacity="{p["aura"][1]}"/><stop offset="1" stop-color="#3A1F9E" stop-opacity="0"/></radialGradient>
<linearGradient id="rule" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p["rule"][0]}"/><stop offset="1" stop-color="{p["rule"][1]}"/></linearGradient>
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
<rect class="sweep" x="0" y="0" width="420" height="{H}" fill="url(#sw)" transform="skewX(-18)"/>
<circle class="aura" cx="1080" cy="206" r="150" fill="url(#au)"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="{p["edge"]}"/>
<rect x="{X - 28}" y="118" width="4" height="176" rx="2" fill="url(#rule)"/>
<path fill="{p["sub"]}" d="{co}"/>
<path fill="{p["ink"]}" d="{name}"/>
<path fill="{p["ink"]}" d="{tt}"/>
<path fill="{p["sub"]}" d="{fx}"/>
{goroshi_g_banner(p, mode)}
</svg>
'''


def goroshi_g_banner(p, mode):
    """The bare Goroshi G (no ring, no disc), centered on the text block, lit by the violet aura."""
    gmark.CINZEL = CINZEL
    size = 132
    x0, y0, x1, y1 = gmark.ink_box(CINZEL, "G", size)
    top, bot = ("#F7F4FF", "#B9A8FF") if mode == "dark" else ("#24186B", "#6A35FF")
    return (f'<defs><linearGradient id="gb" gradientUnits="userSpaceOnUse" x1="0" y1="{206 - (y1 - y0) / 2:.0f}" '
            f'x2="0" y2="{206 + (y1 - y0) / 2:.0f}"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bot}"/>'
            f'</linearGradient></defs><path fill="url(#gb)" d="{gmark.g_path(1080, 206, size)}"/>')


# Curated stack: what an employer or client scans for. Security posture and the reading list stay
# private (Stefano 2026-10-27: "cant people copy me"). (label, simple-icons slug or None)
STACK = [
    ("Languages", [("Rust", "rust"), ("Python", "python"), ("TypeScript", "typescript"), ("JavaScript", "javascript"),
                   ("Go", "go"), ("Lua", "lua"), ("Shell", "gnubash"), ("Java", "openjdk"), ("C", "c"), ("C++", "cplusplus"),
                   ("C#", "dotnet"), ("Swift", "swift"), ("SQL", "postgresql"), ("HTML", "html5"), ("CSS", "css"),
                   ("PowerShell", None), ("Ruby", "ruby"), ("Nushell", "nushell"), ("Lean 4", None), ("WebAssembly", "webassembly")]),
    ("Systems and services", [("Tokio", "rust"), ("Axum", "rust"), ("Tower", "rust"), ("Serde", "rust"), ("Leptos", "leptos"),
                              ("Apache Arrow", "apachearrow"), ("DataFusion", "rust"), ("redb", "rust"), ("PostgreSQL", "postgresql"),
                              ("SQLite", "sqlite"), ("DuckDB", "duckdb")]),
    ("AI engineering", [("Claude Code", "claude"), ("Codex", None), ("Muse", None), ("Antigravity", None), ("Gemini", "googlegemini"),
                        ("Cursor", "cursor"), ("GitHub Copilot", "githubcopilot"), ("OpenCode", "opencode"), ("Kimi", "kimi"),
                        ("DeepSeek", "deepseek"), ("Qwen", "qwen"), ("Grok", None), ("Model Context Protocol", "modelcontextprotocol"),
                        ("Ollama", "ollama"), ("Hugging Face", "huggingface"), ("ONNX Runtime", "onnx"), ("whisper.cpp", None)]),
    ("Compute and infrastructure", [("CUDA", "nvidia"), ("Metal", "apple"), ("Arch Linux", "archlinux"), ("Hyprland", "hyprland"),
                                    ("macOS", "apple"), ("Docker", "docker"), ("Kubernetes", "kubernetes"), ("Ansible", "ansible"),
                                    ("Cloudflare", "cloudflare"), ("Tailscale", "tailscale"), ("Syncthing", "syncthing"),
                                    ("GitHub Actions", "githubactions")]),
    ("Workflow", [("Git", "git"), ("GitHub", "github"), ("Neovim", "neovim"), ("Helix", "helix"), ("Zed", "zedindustries"),
                  ("WezTerm", "wezterm"), ("Ghostty", "ghostty"), ("Starship", "starship"), ("Bun", "bun"),
                  ("Tailwind CSS", "tailwindcss"), ("Biome", "biome"), ("uv", "uv"), ("Ruff", "ruff")]),
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
    out.append(f'<path fill="{p["head"]}" d="{path_d(INTER[600], "STACK", 11.5, 2, y + 13, tracking=2.4)}"/>')
    y += 44
    for head, items in STACK:
        out.append(f'<path fill="{p["sub"]}" d="{path_d(INTER[500], head, 13, 2, y + 13)}"/>')
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
