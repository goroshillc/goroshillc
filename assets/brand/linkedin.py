"""LinkedIn profile background for Stefano Theofanous (2026-10-27: "a perfect banner for my linked in").
1584x396, LinkedIn's personal background size. The round profile photo covers the lower-left corner on
desktop and phone, so every element sits right of x=520. Same language as the GitHub banner.
Usage: python3.14 linkedin.py ASSETS_DIR OUT_DIR"""
import sys

import gmark
from typeset import path_d

A, OUT = sys.argv[1:3]
INTER = {w: f"{A}/Geist-{w}.ttf" for w in (400, 500, 600)}  # Geist (SIL OFL 1.1)
CINZEL = f"{A}/Geist-600.ttf"  # display face: Geist 600 (Cinzel retired 2026-10-27)
gmark.CINZEL = CINZEL
W, H, X = 1584, 396, 560
gx0, gy0, gx1, gy1 = gmark.ink_box(CINZEL, "G", 150)
defs = (f'<linearGradient id="gli" gradientUnits="userSpaceOnUse" x1="0" y1="{198 - (gy1 - gy0) / 2:.0f}" x2="0" y2="{198 + (gy1 - gy0) / 2:.0f}">'
        f'<stop offset="0" stop-color="#F7F4FF"/><stop offset="1" stop-color="#B9A8FF"/></linearGradient>'
        f'<radialGradient id="ali" cx="1400" cy="198" r="210" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6A35FF" stop-opacity=".55"/>'
        f'<stop offset=".55" stop-color="#3A1F9E" stop-opacity=".22"/><stop offset="1" stop-color="#3A1F9E" stop-opacity="0"/></radialGradient>')
body = f'<circle cx="1400" cy="198" r="210" fill="url(#ali)"/><path fill="url(#gli)" d="{gmark.g_path(1400, 198, 150)}"/>'
word = path_d(CINZEL, "GOROSHI", 66, X - 2, 178, tracking=8)
tag = path_d(INTER[500], "Production Systems in Rust", 30, X, 228)
fx = path_d(INTER[400], "AI agent platform, cent-exact finance, GPU kernels at 294 GB/s", 19, X, 270)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Goroshi LLC. Production systems in Rust: AI agent platform, cent-exact finance, GPU kernels at 294 GB/s.">
<defs>{defs}
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#05060F"/><stop offset=".55" stop-color="#0D0B33"/><stop offset="1" stop-color="#1A1252"/></linearGradient>
<linearGradient id="rule" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B9A8FF"/><stop offset="1" stop-color="#6A35FF"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<g filter="url(#blur)">
<ellipse cx="1180" cy="120" rx="320" ry="130" fill="#130F4A" opacity=".95"/>
<ellipse cx="1380" cy="300" rx="260" ry="150" fill="#3A1F9E" opacity=".75"/>
<ellipse cx="860" cy="330" rx="260" ry="100" fill="#4E2BC8" opacity=".45"/>
<ellipse cx="1540" cy="60" rx="140" ry="80" fill="#6A35FF" opacity=".4"/>
</g>
<rect x="{X - 30}" y="118" width="4" height="164" rx="2" fill="url(#rule)"/>
<path fill="#F7F4FF" d="{word}"/>
<path fill="#F7F4FF" d="{tag}"/>
<path fill="#DDD6FF" d="{fx}"/>
{body}
</svg>
'''
open(f"{OUT}/linkedin-banner.svg", "w").write(svg)
print("ok")
