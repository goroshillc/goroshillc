"""LinkedIn profile background for Stefano Theofanous (2026-10-27: "a perfect banner for my linked in").
1584x396, LinkedIn's personal background size. The round profile photo covers the lower-left corner on
desktop and phone, so every element sits right of x=520. Same language as the GitHub banner.
Usage: python3.14 linkedin.py ASSETS_DIR OUT_DIR"""
import sys

import gmark
from typeset import path_d

A, OUT = sys.argv[1:3]
INTER = {w: f"{A}/Inter-{w}.ttf" for w in (400, 500, 600)}
CINZEL = f"{A}/Cinzel-600.ttf"
gmark.CINZEL = CINZEL
W, H, X = 1584, 396, 560
defs, body = gmark.monogram(1400, 198, 104, uid="li")
word = path_d(CINZEL, "GOROSHI LLC", 64, X - 2, 178, tracking=10)
tag = path_d(INTER[500], "Platform & Systems Engineering", 30, X, 228)
fx = path_d(INTER[400], "Rust · AI agent infrastructure · Financial systems · GPU compute", 19, X, 270)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Goroshi LLC. Platform and Systems Engineering.">
<defs>{defs}
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#07070d"/><stop offset=".55" stop-color="#0c0d2b"/><stop offset="1" stop-color="#14123f"/></linearGradient>
<linearGradient id="rule" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d7b8ff"/><stop offset="1" stop-color="#BC43D3"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<g filter="url(#blur)">
<ellipse cx="1180" cy="120" rx="320" ry="130" fill="#181A56" opacity=".95"/>
<ellipse cx="1380" cy="300" rx="260" ry="150" fill="#46439F" opacity=".7"/>
<ellipse cx="860" cy="330" rx="260" ry="100" fill="#8877B6" opacity=".4"/>
<ellipse cx="1540" cy="60" rx="140" ry="80" fill="#BC43D3" opacity=".3"/>
</g>
<path d="M600 376 C 780 330, 930 400, 1090 356 S 1220 330, 1260 344" fill="none" stroke="#ffffff" stroke-opacity=".45" stroke-width="1.4"/>
<path d="M640 30 C 800 76, 960 18, 1100 52 S 1220 70, 1250 50" fill="none" stroke="#ffffff" stroke-opacity=".35" stroke-width="1.1"/>
<rect x="{X - 30}" y="118" width="4" height="164" rx="2" fill="url(#rule)"/>
<path fill="#f5f4ff" d="{word}"/>
<path fill="#f5f4ff" d="{tag}"/>
<path fill="#d9d6ff" d="{fx}"/>
{body}
</svg>
'''
open(f"{OUT}/linkedin-banner.svg", "w").write(svg)
print("ok")
