"""Goroshi LLC profile banner v3 (Stefano Theofanous, 2026-10-27).
His direction: the animation was clean; the Chi Rho must match the Alpha and Omega; fit GitHub dark and
light seamlessly; colorway midnight blue, black and a little purple (Jerry Garcia "Butterfly Trap Line
Swirls" purple and "Urban Cat Ghost" berry ties; Solo Leveling). Hierarchy from the library: Storytelling
with Data p.87 and p.31, Designing Interfaces p.229. Fonts: Cinzel and Inter (SIL OFL 1.1), subset.
Usage: build_banner3.py CINZEL.woff INTER.woff OUT_DARK.svg OUT_LIGHT.svg"""
import base64, sys
cin, inter, out_dark, out_light = sys.argv[1:5]
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
W, H, X = 1280, 400, 112
EX, EY = 1056, 200          # emblem center
CAP = 34                    # cap height the Chi Rho is drawn to (Cinzel 48px caps)
SW = 5.4                    # stroke matched to Cinzel 600 stems at 48px

def chi_rho(cx, cy, color):
    # Chi spans the capital height exactly (cap top to baseline of the Alpha and Omega beside it);
    # the Rho stem rises above it with a full bowl and drops a little below, as in the classic monogram.
    c = CAP / 2
    top, bot = cy - c - 16, cy + c + 4
    r = 10.5
    return (f'<g fill="none" stroke="{color}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{cx} {top} V{bot}"/>'
            f'<path d="M{cx} {top} H{cx + 4} A{r} {r} 0 0 1 {cx + 4} {top + 2 * r} H{cx}"/>'
            f'<path d="M{cx - c} {cy - c} L{cx + c} {cy + c}"/><path d="M{cx + c} {cy - c} L{cx - c} {cy + c}"/></g>')

def svg(mode):
    dark = mode == "dark"
    ink = "#f5f4ff" if dark else "#11123a"
    sub = "#d9d6ff" if dark else "#2a2870"
    bg = ('<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#07070d"/>'
          '<stop offset=".55" stop-color="#0c0d2b"/><stop offset="1" stop-color="#14123f"/></linearGradient>') if dark else \
         ('<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/>'
          '<stop offset="1" stop-color="#f3f1ff"/></linearGradient>')
    silk = [("#181A56", .95 if dark else .16), ("#46439F", .70 if dark else .18), ("#8877B6", .45 if dark else .20), ("#BC43D3", .30 if dark else .12)]
    line = "#ffffff" if dark else "#46439F"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Stefano Theofanous, Platform and Systems Engineer, Goroshi LLC.">
<defs>
<style>
@font-face {{ font-family: "Cinzel"; font-weight: 400 900; src: url(data:font/woff;base64,{b64(cin)}) format("woff"); }}
@font-face {{ font-family: "Inter"; font-weight: 100 900; src: url(data:font/woff;base64,{b64(inter)}) format("woff"); }}
.co {{ font-family: "Inter", sans-serif; font-weight: 600; font-size: 15px; letter-spacing: 5px; fill: {sub}; }}
.nm {{ font-family: "Cinzel", Georgia, serif; font-weight: 600; font-size: 58px; letter-spacing: 3px; fill: {ink}; }}
.tt {{ font-family: "Inter", sans-serif; font-weight: 500; font-size: 26px; fill: {ink}; }}
.fx {{ font-family: "Inter", sans-serif; font-weight: 400; font-size: 17px; fill: {sub}; }}
.ao {{ font-family: "Cinzel", Georgia, serif; font-weight: 600; font-size: 48px; fill: {ink}; }}
.s1 {{ animation: drift1 28s ease-in-out infinite alternate; transform-origin: 900px 160px; }}
.s2 {{ animation: drift2 34s ease-in-out infinite alternate; transform-origin: 1100px 260px; }}
.s3 {{ animation: drift3 40s ease-in-out infinite alternate; transform-origin: 700px 300px; }}
@keyframes drift1 {{ to {{ transform: translate(-120px, 40px) rotate(18deg) scale(1.15); }} }}
@keyframes drift2 {{ to {{ transform: translate(80px, -50px) rotate(-14deg) scale(.9); }} }}
@keyframes drift3 {{ to {{ transform: translate(140px, -30px) rotate(10deg) scale(1.1); }} }}
.ln {{ stroke-dasharray: 1600; stroke-dashoffset: 1600; animation: draw 14s ease-in-out infinite; }}
.ln2 {{ animation-delay: 4s; }}
@keyframes draw {{ 0% {{ stroke-dashoffset: 1600; opacity: 0; }} 15% {{ opacity: .55; }} 55% {{ stroke-dashoffset: 0; opacity: .55; }} 85%,100% {{ stroke-dashoffset: 0; opacity: 0; }} }}
.aura {{ animation: breathe 7s ease-in-out infinite; transform-origin: {EX}px {EY}px; }}
@keyframes breathe {{ 0%,100% {{ opacity: .55; transform: scale(.94); }} 50% {{ opacity: 1; transform: scale(1.06); }} }}
@media (prefers-reduced-motion: reduce) {{ .s1, .s2, .s3, .aura {{ animation: none; }} .ln {{ animation: none; stroke-dashoffset: 0; opacity: .4; }} }}
</style>
{bg}
<radialGradient id="au"><stop offset="0" stop-color="#8877B6" stop-opacity="{.55 if dark else .30}"/><stop offset=".55" stop-color="#46439F" stop-opacity="{.22 if dark else .12}"/><stop offset="1" stop-color="#46439F" stop-opacity="0"/></radialGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
<clipPath id="card"><rect width="{W}" height="{H}" rx="20"/></clipPath>
<linearGradient id="cr" gradientUnits="userSpaceOnUse" x1="0" y1="{EY-60}" x2="0" y2="{EY+40}"><stop offset="0" stop-color="{"#ffffff" if dark else "#11123a"}"/><stop offset="1" stop-color="{"#cbb8ff" if dark else "#3b2f9a"}"/></linearGradient>
<linearGradient id="rule" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{"#d7b8ff" if dark else "#6b3fd1"}"/><stop offset="1" stop-color="{"#BC43D3" if dark else "#46439F"}"/></linearGradient>
</defs>
<g clip-path="url(#card)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<g filter="url(#blur)">
<ellipse class="s1" cx="900" cy="150" rx="260" ry="120" fill="{silk[0][0]}" opacity="{silk[0][1]}"/>
<ellipse class="s2" cx="1120" cy="270" rx="220" ry="140" fill="{silk[1][0]}" opacity="{silk[1][1]}"/>
<ellipse class="s3" cx="720" cy="320" rx="200" ry="90" fill="{silk[2][0]}" opacity="{silk[2][1]}"/>
<ellipse class="s2" cx="1210" cy="90" rx="120" ry="70" fill="{silk[3][0]}" opacity="{silk[3][1]}"/>
</g>
<path class="ln" d="M640 360 C 760 250, 860 380, 980 260 S 1180 120, 1300 210" fill="none" stroke="{line}" stroke-width="1.4"/>
<path class="ln ln2" d="M560 40 C 700 120, 820 20, 930 110 S 1120 260, 1290 160" fill="none" stroke="{line}" stroke-width="1.1"/>
<circle class="aura" cx="{EX}" cy="{EY}" r="130" fill="url(#au)"/>
</g>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="20" fill="none" stroke="{"#23234d" if dark else "#e3e0ff"}"/>
<rect x="{X-28}" y="118" width="4" height="176" rx="2" fill="url(#rule)"/>
<text class="co" x="{X}" y="138">GOROSHI LLC</text>
<text class="nm" x="{X-4}" y="212">STEFANO THEOFANOUS</text>
<text class="tt" x="{X}" y="254">Platform &amp; Systems Engineer</text>
<text class="fx" x="{X}" y="290">Rust · AI agent infrastructure · Financial systems · GPU compute</text>
<text class="ao" x="{EX-70}" y="{EY+CAP/2}" text-anchor="middle">Α</text>
{chi_rho(EX, EY, "url(#cr)")}
<text class="ao" x="{EX+70}" y="{EY+CAP/2}" text-anchor="middle">Ω</text>
</svg>
'''
for mode, out in (("dark", out_dark), ("light", out_light)):
    open(out, "w").write(svg(mode))
    print(out, len(svg(mode)), "bytes")
