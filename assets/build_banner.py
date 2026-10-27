"""Professional profile banner (Stefano Theofanous, 2026-10-27: "the svg thing i want max professional").
Hierarchy from the library: Storytelling with Data p.87 (every element adds cognitive load) and p.31
(size, color and position set the visual hierarchy); Designing Interfaces p.229 (the most important
content stands out the most). One accent color, used once. Palette law: white on black, no grey text.
Fonts: Cinzel and Inter (SIL OFL 1.1), subset to the characters used, embedded as WOFF."""
import base64, sys
cin, inter, out = sys.argv[1:4]
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
W, H = 1280, 400
X = 132          # text column
CX, CY = 1072, 200  # Chi Rho center
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Stefano Theofanous, Platform and Systems Engineer, Goroshi LLC.">
<defs><style>
@font-face {{ font-family: "Cinzel"; font-weight: 400 900; src: url(data:font/woff;base64,{b64(cin)}) format("woff"); }}
@font-face {{ font-family: "Inter"; font-weight: 100 900; src: url(data:font/woff;base64,{b64(inter)}) format("woff"); }}
.co {{ font-family: "Inter", sans-serif; font-weight: 600; font-size: 15px; letter-spacing: 5px; fill: #f4f4f5; }}
.nm {{ font-family: "Cinzel", Georgia, serif; font-weight: 600; font-size: 58px; letter-spacing: 3px; fill: #f4f4f5; }}
.tt {{ font-family: "Inter", sans-serif; font-weight: 500; font-size: 26px; fill: #f4f4f5; }}
.fx {{ font-family: "Inter", sans-serif; font-weight: 400; font-size: 17px; fill: #f4f4f5; }}
.ao {{ font-family: "Cinzel", Georgia, serif; font-weight: 600; font-size: 26px; fill: #f4f4f5; }}
</style></defs>
<rect width="{W}" height="{H}" fill="#0a0a0b"/>
<rect x="20.5" y="20.5" width="{W-41}" height="{H-41}" fill="none" stroke="#26262b"/>
<rect x="{X-28}" y="118" width="4" height="176" fill="#d42a32"/>
<text class="co" x="{X}" y="138">GOROSHI LLC</text>
<text class="nm" x="{X-4}" y="212">STEFANO THEOFANOUS</text>
<text class="tt" x="{X}" y="254">Platform &amp; Systems Engineer</text>
<text class="fx" x="{X}" y="290">Rust · AI agent infrastructure · Financial systems · GPU compute</text>
<g fill="none" stroke="#d42a32" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
<path d="M{CX} {CY-52} V{CY+52}"/><path d="M{CX} {CY-52} H{CX+12} A16 16 0 0 1 {CX+12} {CY-20} H{CX}"/>
<path d="M{CX-24} {CY-6} L{CX+24} {CY+42}"/><path d="M{CX+24} {CY-6} L{CX-24} {CY+42}"/></g>
<text class="ao" x="{CX-66}" y="{CY+27}" text-anchor="middle">Α</text>
<text class="ao" x="{CX+66}" y="{CY+27}" text-anchor="middle">Ω</text>
</svg>
'''
open(out, "w").write(svg)
print(out, len(svg), "bytes")
