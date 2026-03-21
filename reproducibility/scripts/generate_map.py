"""
Generate the Architectural Map of the Factor Skyline as a high-resolution PNG.
Large text version for publication readability.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

# ── Colour palette ──────────────────────────────────────────────────
C_PRIM   = '#1B3A5C'
C_P1     = '#2D6A4F';  C_P1_LT = '#D8F3DC'
C_P2     = '#B8860B';  C_P2_LT = '#FFF3CD'
C_P3     = '#6A0DAD';  C_P3_LT = '#E8D5F5'
C_P4     = '#A41034';  C_P4_LT = '#F8D7DA'
C_DEP    = '#4A4A4A';  C_DEP_LT = '#E9ECEF'
C_WHITE  = '#FFFFFF';  C_BLACK = '#1A1A1A'; C_BG = '#FAFAFA'

# Larger canvas, same coordinate system = bigger rendered text
fig, ax = plt.subplots(figsize=(34, 48))
fig.patch.set_facecolor(C_BG)
ax.set_xlim(0, 17)
ax.set_ylim(0, 24)
ax.set_aspect('equal')
ax.axis('off')

# ── Helper functions ────────────────────────────────────────────────
def rbox(x, y, w, h, fc, ec, lw=1.5, rad=0.12):
    ax.add_patch(FancyBboxPatch((x,y), w, h, boxstyle=f"round,pad={rad}",
                 facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2))

def sbox(x, y, w, h, fc, ec, lw=1.5):
    ax.add_patch(FancyBboxPatch((x,y), w, h, boxstyle="square,pad=0.04",
                 facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2))

def T(x, y, s, sz=8, wt='normal', c=C_BLACK, ha='center', va='center'):
    ax.text(x, y, s, fontsize=sz, fontweight=wt, color=c, ha=ha, va=va,
            fontfamily='sans-serif', zorder=5)

def arr(x1,y1,x2,y2, c=C_BLACK, lw=1.8, ls='-'):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle='->', color=c, lw=lw, linestyle=ls), zorder=3)

CX = 8.5
PW = 14.0
PX = CX - PW/2

# ═══════════════════════════════════════════════════════════════════
# TITLE
# ═══════════════════════════════════════════════════════════════════
T(CX, 23.55, 'Architectural Map of the Factor Skyline', sz=16, wt='bold', c=C_PRIM)

# ── PRIMITIVE BANNER ───────────────────────────────────────────────
bw, bh = 13, 0.7
bx = CX - bw/2
by = 22.45
rbox(bx, by, bw, bh, C_PRIM, C_PRIM, lw=0)
T(CX, by+bh/2, 'THE SINGLE PRIMITIVE:   lpf(n)  →  width · height · activation · coverage · escape',
  sz=10, wt='bold', c=C_WHITE)

# ═══════════════════════════════════════════════════════════════════
# PART I
# ═══════════════════════════════════════════════════════════════════
p1t = 21.5; p1h = 4.5
rbox(PX, p1t-p1h, PW, p1h, C_P1_LT, C_P1, lw=2.5, rad=0.18)
T(CX, p1t-0.3, 'PART I:  THE FACTOR SKYLINE ARCHITECTURE', sz=11, wt='bold', c=C_P1)

cw, ch = 3.6, 1.25
r1 = p1t - 1.85

# Ch 1
c1x = PX + 0.9
rbox(c1x, r1, cw, ch, C_WHITE, C_P1)
T(c1x+cw/2, r1+ch-0.2, 'Ch 1: Primitives & Coords', sz=8, wt='bold', c=C_P1)
T(c1x+cw/2, r1+0.55, 'Width, height, FS-x / y\nActivation, coverage, escape', sz=7, c=C_BLACK)
T(c1x+cw/2, r1+0.15, 'Thms I.1 – I.3', sz=7, wt='bold', c=C_P1)

# Ch 2
c2x = c1x + cw + 0.7
rbox(c2x, r1, cw, ch, C_WHITE, C_P1)
T(c2x+cw/2, r1+ch-0.2, 'Ch 2: Templates & Epochs', sz=8, wt='bold', c=C_P1)
T(c2x+cw/2, r1+0.55, 'Primorial periodicity\nEpoch structure', sz=7, c=C_BLACK)
T(c2x+cw/2, r1+0.15, 'Thms I.4 – I.6', sz=7, wt='bold', c=C_P1)

# Ch 3
c3x = c2x + cw + 0.7
rbox(c3x, r1, cw, ch, C_WHITE, C_P1)
T(c3x+cw/2, r1+ch-0.2, 'Ch 3: Protection & Persistence', sz=8, wt='bold', c=C_P1)
T(c3x+cw/2, r1+0.55, 'Coverage protection, C_H > 1\nPersistence, FS-x footprints', sz=7, c=C_BLACK)
T(c3x+cw/2, r1+0.15, 'Thms I.7 – I.11', sz=7, wt='bold', c=C_P1)

arr(c1x+cw, r1+ch/2, c2x, r1+ch/2, c=C_P1)
arr(c2x+cw, r1+ch/2, c3x, r1+ch/2, c=C_P1)

# Row 2
r2 = r1 - 1.55
c4x = CX - cw - 0.35
c5x = CX + 0.35

rbox(c4x, r2, cw, ch, C_WHITE, C_P1)
T(c4x+cw/2, r2+ch-0.2, 'Ch 4: Geometric PNT & Dickman', sz=8, wt='bold', c=C_P1)
T(c4x+cw/2, r2+0.55, 'π(N) ~ N · D(√N)\nDickman ρ, smooth–rough duality', sz=7, c=C_BLACK)
T(c4x+cw/2, r2+0.15, 'Thms I.12 – I.15', sz=7, wt='bold', c=C_P1)

rbox(c5x, r2, cw, ch, C_WHITE, C_P1)
T(c5x+cw/2, r2+ch-0.2, 'Ch 5: Möbius, Divisors, θ ~ x', sz=8, wt='bold', c=C_P1)
T(c5x+cw/2, r2+0.55, 'μ, τ, σ, Erdős–Kac\nConservation law θ(x) ~ x', sz=7, c=C_BLACK)
T(c5x+cw/2, r2+0.15, 'Thms I.16 – I.22', sz=7, wt='bold', c=C_P1)

arr(c1x+cw/2, r1, c4x+cw/2, r2+ch, c=C_P1)
arr(c2x+cw/2, r1, c4x+cw*0.7, r2+ch, c=C_P1)
arr(c3x+cw/2, r1, c5x+cw/2, r2+ch, c=C_P1)

# ── DEP I→II ──────────────────────────────────────────────────────
dw, dh = 11.0, 0.9
d1y = p1t - p1h - 1.0
sbox(CX-dw/2, d1y, dw, dh, C_DEP_LT, C_DEP, lw=1.8)
T(CX, d1y+dh/2+0.18, 'Cross-Part Dependencies   I → II', sz=8, wt='bold', c=C_DEP)
T(CX, d1y+dh/2-0.18,
  'Thm I.2 (CRT) → all Part II   ·   Thm I.7 (Survival) → Ch 6, 11   ·   Thm I.10 (Persistence) → Ch 11, 12   ·   Thm I.21 → Ch 9, 10',
  sz=6, c=C_DEP)
arr(CX, p1t-p1h, CX, d1y+dh, c=C_DEP, lw=2)

# ═══════════════════════════════════════════════════════════════════
# PART II
# ═══════════════════════════════════════════════════════════════════
p2t = d1y - 0.3; p2h = 4.1
rbox(PX, p2t-p2h, PW, p2h, C_P2_LT, C_P2, lw=2.5, rad=0.18)
T(CX, p2t-0.3, 'PART II:  CORRELATIONS & RANDOMNESS', sz=11, wt='bold', c=C_P2)
arr(CX, d1y, CX, p2t, c=C_DEP, lw=2)

cw6 = 5.8; cw7 = 4.5
c6x = PX + 0.8; c7x = PX + PW - 0.8 - cw7
r3 = p2t - 2.0

rbox(c6x, r3, cw6, 1.45, C_WHITE, C_P2)
T(c6x+cw6/2, r3+1.2, 'Ch 6: Correlation Theory', sz=8, wt='bold', c=C_P2)
T(c6x+cw6/2, r3+0.65, 'Master decomposition (shared / independent)\nEscape (HL) · Parity (Chowla) · Branching\nSpectral (GUE repulsion) · Four-level hierarchy', sz=6.5, c=C_BLACK)
T(c6x+cw6/2, r3+0.15, 'Thms II.1 – II.8', sz=7, wt='bold', c=C_P2)

rbox(c7x, r3, cw7, 1.45, C_WHITE, C_P2)
T(c7x+cw7/2, r3+1.2, 'Ch 7: Randomness', sz=8, wt='bold', c=C_P2)
T(c7x+cw7/2, r3+0.65, 'Sub-Poisson escape\n73 / 27 template–stochastic split\nω / μ mixing dichotomy', sz=6.5, c=C_BLACK)
T(c7x+cw7/2, r3+0.15, 'Thms II.9 – II.12', sz=7, wt='bold', c=C_P2)

c8w = 8.0; c8x = CX - c8w/2
r4 = r3 - 1.55
rbox(c8x, r4, c8w, 1.05, C_WHITE, C_P2)
T(CX, r4+0.8, 'Ch 8: Unified Statistical Architecture', sz=8, wt='bold', c=C_P2)
T(CX, r4+0.38, 'Entropy budget  (68.5% template  /  31.5% stochastic)    ·    "All randomness = CRT independence"', sz=6.5, c=C_BLACK)
T(CX, r4+0.1, 'Thms II.13 – II.14', sz=7, wt='bold', c=C_P2)

arr(c6x+cw6/2, r3, CX-1.2, r4+1.05, c=C_P2)
arr(c7x+cw7/2, r3, CX+1.2, r4+1.05, c=C_P2)

# ── DEP II→III ────────────────────────────────────────────────────
d2y = p2t - p2h - 1.0
sbox(CX-dw/2, d2y, dw, dh, C_DEP_LT, C_DEP, lw=1.8)
T(CX, d2y+dh/2+0.18, 'Cross-Part Dependencies   II → III', sz=8, wt='bold', c=C_DEP)
T(CX, d2y+dh/2-0.18,
  'Thm II.5 (ω non-mixing) → Ch 10   ·   Thm II.12 (dichotomy) → Ch 10   ·   Thm II.13 (Entropy) → Ch 9, 12   ·   Thm II.14 → Ch 11, 13',
  sz=6, c=C_DEP)
arr(CX, p2t-p2h, CX, d2y+dh, c=C_DEP, lw=2, ls='dashed')

# ═══════════════════════════════════════════════════════════════════
# PART III
# ═══════════════════════════════════════════════════════════════════
p3t = d2y - 0.3; p3h = 4.4
rbox(PX, p3t-p3h, PW, p3h, C_P3_LT, C_P3, lw=2.5, rad=0.18)
T(CX, p3t-0.3, 'PART III:  INFORMATION, DYNAMICS & UNIVERSALITY', sz=11, wt='bold', c=C_P3)
arr(CX, d2y, CX, p3t, c=C_DEP, lw=2, ls='dashed')

cw9 = 3.9
r5 = p3t - 2.05
c9x = PX + 0.6; c10x = CX - cw9/2; c11x = PX + PW - 0.6 - cw9

rbox(c9x, r5, cw9, 1.45, C_WHITE, C_P3)
T(c9x+cw9/2, r5+1.2, 'Ch 9: Entropy', sz=8, wt='bold', c=C_P3)
T(c9x+cw9/2, r5+0.6, 'Template: 0 bits\nEscape: 0.26 bits / int\nParity barrier = info gap', sz=6.5, c=C_BLACK)
T(c9x+cw9/2, r5+0.12, 'Thms III.1 – III.5', sz=7, wt='bold', c=C_P3)

rbox(c10x, r5, cw9, 1.45, C_WHITE, C_P3)
T(c10x+cw9/2, r5+1.2, 'Ch 10: Ergodic Theory', sz=8, wt='bold', c=C_P3)
T(c10x+cw9/2, r5+0.6, 'Rigid template\nMixing escape, GUE spectral\nQuasi-ergodic skyline', sz=6.5, c=C_BLACK)
T(c10x+cw9/2, r5+0.12, 'Thms III.6 – III.10', sz=7, wt='bold', c=C_P3)

rbox(c11x, r5, cw9, 1.45, C_WHITE, C_P3)
T(c11x+cw9/2, r5+1.2, 'Ch 11: Universality', sz=8, wt='bold', c=C_P3)
T(c11x+cw9/2, r5+0.6, '(A1)–(A4) axioms, 3 classes\n12 universal structures\nRenorm. flow D(p)', sz=6.5, c=C_BLACK)
T(c11x+cw9/2, r5+0.12, 'Thms III.11 – III.17', sz=7, wt='bold', c=C_P3)

# Triple correspondence
tcw = 7.0; tcx = CX - tcw/2; tcy = r5 - 1.5
rbox(tcx, tcy, tcw, 1.05, '#F3E8FF', C_P3, lw=2.0)
T(CX, tcy+0.8, 'TRIPLE CORRESPONDENCE   (Theorem III.17)', sz=8, wt='bold', c=C_P3)
T(CX, tcy+0.35, '0 entropy = rigid     ·     + entropy = ergodic     ·     max entropy = GUE', sz=7, c=C_P3)
T(CX, tcy+0.1, 'D(p) governs all three', sz=7, wt='bold', c=C_P3)

arr(c9x+cw9/2, r5, tcx+1.2, tcy+1.05, c=C_P3)
arr(c10x+cw9/2, r5, CX, tcy+1.05, c=C_P3)
arr(c11x+cw9/2, r5, tcx+tcw-1.2, tcy+1.05, c=C_P3)

# ── DEP III→IV ────────────────────────────────────────────────────
d3y = p3t - p3h - 1.0
sbox(CX-dw/2, d3y, dw, dh, C_DEP_LT, C_DEP, lw=1.8)
T(CX, d3y+dh/2+0.18, 'Cross-Part Dependencies   III → IV', sz=8, wt='bold', c=C_DEP)
T(CX, d3y+dh/2-0.18,
  'Thm III.5 (Parity = info gap) → Ch 13   ·   Thm III.14 (Universality) → Ch 13   ·   Thm III.16 (Renorm.) → Ch 12   ·   Thm III.17 → Ch 14',
  sz=6, c=C_DEP)
arr(CX, p3t-p3h, CX, d3y+dh, c=C_DEP, lw=2, ls='dotted')

# ═══════════════════════════════════════════════════════════════════
# PART IV
# ═══════════════════════════════════════════════════════════════════
p4t = d3y - 0.3; p4h = 3.9
rbox(PX, p4t-p4h, PW, p4h, C_P4_LT, C_P4, lw=2.5, rad=0.18)
T(CX, p4t-0.3, 'PART IV:  META-STRUCTURE & META-MATHEMATICS', sz=11, wt='bold', c=C_P4)
arr(CX, d3y, CX, p4t, c=C_DEP, lw=2, ls='dotted')

cw12 = 5.5
r6 = p4t - 1.85
c12x = PX + 0.9; c13x = PX + PW - 0.9 - cw12

rbox(c12x, r6, cw12, 1.35, C_WHITE, C_P4)
T(c12x+cw12/2, r6+1.1, 'Ch 12: Meta-Structure', sz=8, wt='bold', c=C_P4)
T(c12x+cw12/2, r6+0.55, 'lpf = sole primitive\n3 meta-axioms (M1–M3)\n3 dualities · Renormalization · Self-reference', sz=6.5, c=C_BLACK)
T(c12x+cw12/2, r6+0.12, 'Thms IV.1 – IV.5', sz=7, wt='bold', c=C_P4)

rbox(c13x, r6, cw12, 1.35, C_WHITE, C_P4)
T(c13x+cw12/2, r6+1.1, 'Ch 13: Meta-Mathematics', sz=8, wt='bold', c=C_P4)
T(c13x+cw12/2, r6+0.55, 'K = O(log N),   H ≥ 0.26 N\nPseudo-random (K ≪ H)\nBarrier ≠ Gödel  ·  T_FS first-order', sz=6.5, c=C_BLACK)
T(c13x+cw12/2, r6+0.12, 'Thms IV.6 – IV.11', sz=7, wt='bold', c=C_P4)

c14w = 8.5; c14x = CX - c14w/2
r7 = r6 - 1.55
rbox(c14x, r7, c14w, 1.1, C_WHITE, C_P4)
T(CX, r7+0.85, 'Ch 14: Unified Meta-Architecture', sz=8, wt='bold', c=C_P4)
T(CX, r7+0.5, 'Meta-correspondence (IV.12):   structure  ↔  logic at every level', sz=7, c=C_BLACK)
T(CX, r7+0.18, 'The boundary (IV.13):   ≡ 0.26 bits/int   ≡  escape hardness   ≡  Σ₁⁰ vs Π₂⁰   ≡  universal in (A1)–(A4)',
  sz=6.5, wt='bold', c=C_P4)

arr(c12x+cw12/2, r6, CX-1.5, r7+1.1, c=C_P4)
arr(c13x+cw12/2, r6, CX+1.5, r7+1.1, c=C_P4)

# ═══════════════════════════════════════════════════════════════════
# LEGEND
# ═══════════════════════════════════════════════════════════════════
ly = 0.2
sbox(PX+0.2, ly, PW-0.4, 1.35, C_WHITE, C_BLACK, lw=1.2)
T(PX+0.8, ly+1.1, 'LEGEND', sz=9, wt='bold', c=C_BLACK, ha='left')

# Arrow samples
lax = PX + 0.8
arr(lax, ly+0.82, lax+1.5, ly+0.82, c=C_BLACK, lw=2)
T(lax+1.7, ly+0.82, 'Structural dependence   (Part I → II)', sz=7, ha='left')

arr(lax, ly+0.52, lax+1.5, ly+0.52, c=C_BLACK, lw=1.5, ls='dashed')
T(lax+1.7, ly+0.52, 'Statistical dependence   (Part II → III)', sz=7, ha='left')

arr(lax, ly+0.22, lax+1.5, ly+0.22, c=C_BLACK, lw=1.5, ls='dotted')
T(lax+1.7, ly+0.22, 'Foundational dependence   (Part III → IV)', sz=7, ha='left')

# Colour key
for i, (c, lb) in enumerate([
    (C_P1, 'Part I: Architecture'), (C_P2, 'Part II: Statistics'),
    (C_P3, 'Part III: Foundations'), (C_P4, 'Part IV: Meta-theory'),
    (C_DEP_LT, 'Cross-part deps')
]):
    bxl = PX + 9.5 + (i % 3) * 2.0
    byl = ly + 0.9 - (i // 3) * 0.45
    rbox(bxl, byl-0.1, 0.3, 0.2, c, C_BLACK, lw=0.8, rad=0.03)
    T(bxl+0.45, byl, lb, sz=6.5, ha='left')

# Bottom summary
T(CX, ly-0.2, '66 theorems   ·   12 definitions   ·   2 corollaries   ·   20 verification tables   ·   14 chapters   ·   4 parts',
  sz=8, c=C_DEP, wt='bold')

plt.tight_layout(pad=0.5)
plt.savefig('FS_architectural_map.png', dpi=200, bbox_inches='tight', facecolor=C_BG)
print('Saved: FS_architectural_map.png')
