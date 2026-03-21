# Architectural Map of the Factor Skyline

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║   THE SINGLE PRIMITIVE:  lpf(n)  ──→  width, height, activation, coverage, escape║
║                                                                                  ║
╚══════════════════════════════════════════╤═══════════════════════════════════════╝
                                           │
          ┌────────────────────────────────┴────────────────────────────────┐
          │                    PART I: ARCHITECTURE                         │
          │                                                                 │
          │  ┌──────────┐    ┌──────────────┐    ┌───────────────────────┐  │
          │  │  Ch 1     │───▷│   Ch 2        │───▷│   Ch 3               │  │
          │  │ Primitives│    │ Templates &   │    │ Coverage protection  │  │
          │  │ & coords  │    │ epochs        │    │ Template persistence │  │
          │  │           │    │               │    │ FS-x footprints      │  │
          │  │ I.1─I.3   │    │ I.4─I.6       │    │ I.7─I.11             │  │
          │  └─────┬─────┘    └───────┬───────┘    └───────────┬──────────┘  │
          │        │                  │                        │             │
          │        │         ┌────────┴────────┐     ┌────────┴──────────┐  │
          │        └────────▷│   Ch 4           │    │   Ch 5             │  │
          │                  │ Geometric PNT    │    │ Möbius, divisors,  │  │
          │                  │ Dickman smooth   │    │ conservation law   │  │
          │                  │ Smooth-rough     │    │ Template invariants│  │
          │                  │ I.12─I.15        │    │ I.16─I.22          │  │
          │                  └─────────────────┘    └────────────────────┘  │
          └────────────────────────────┬───────────────────────────────────┘
                                       │
               ╔═══════════════════════╧════════════════════════╗
               ║  KEY DEPENDENCIES FLOWING DOWN:                ║
               ║  Thm I.2 (CRT independence) ──→ ALL of Part II║
               ║  Thm I.7 (Survival factor)  ──→ Ch 6, Ch 11   ║
               ║  Thm I.10 (Persistence)     ──→ Ch 11, Ch 12  ║
               ║  Thm I.21 (Conservation)    ──→ Ch 9, Ch 10   ║
               ╚═══════════════════════╤════════════════════════╝
                                       │
          ┌────────────────────────────┴────────────────────────────────┐
          │               PART II: CORRELATIONS & RANDOMNESS            │
          │                                                             │
          │  ┌──────────────────────────────┐   ┌────────────────────┐  │
          │  │  Ch 6: Correlation Theory     │   │  Ch 7: Randomness  │  │
          │  │                               │   │                    │  │
          │  │  6.1 Master decomposition     │   │  7.1 Sub-Poisson   │  │
          │  │      (shared/independent)     │   │  7.2 73/27 split   │  │
          │  │  6.2 Escape (HL constants)    │   │  7.3 Three-level   │  │
          │  │  6.3 Parity (Chowla)          │   │      hierarchy     │  │
          │  │  6.4 Branching (divisor corr) │   │  7.4 ω/μ dichotomy │  │
          │  │  6.5 Spectral (GUE repulsion) │   │                    │  │
          │  │  6.6 Four-level hierarchy     │   │  II.9─II.12        │  │
          │  │                               │   │                    │  │
          │  │  II.1─II.8                    │   │                    │  │
          │  └──────────────┬────────────────┘   └─────────┬──────────┘  │
          │                 │                              │             │
          │                 └──────────┬───────────────────┘             │
          │                            │                                │
          │                 ┌──────────┴──────────────────────────────┐  │
          │                 │  Ch 8: Unified Statistical Architecture  │  │
          │                 │                                          │  │
          │                 │  8.1 Entropy budget (68.5/31.5 split)   │  │
          │                 │  8.2 Unified randomness principle        │  │
          │                 │      "All randomness = CRT independence" │  │
          │                 │                                          │  │
          │                 │  II.13─II.14                             │  │
          │                 └─────────────────────────────────────────┘  │
          └────────────────────────────┬────────────────────────────────┘
                                       │
               ╔═══════════════════════╧════════════════════════╗
               ║  KEY DEPENDENCIES FLOWING DOWN:                ║
               ║  Thm II.5  (ω non-mixing)  ──→ Ch 10          ║
               ║  Thm II.12 (ω/μ dichotomy) ──→ Ch 10          ║
               ║  Thm II.13 (Entropy budget) ──→ Ch 9, Ch 12   ║
               ║  Thm II.14 (Randomness)     ──→ Ch 11, Ch 13  ║
               ╚═══════════════════════╤════════════════════════╝
                                       │
          ┌────────────────────────────┴────────────────────────────────┐
          │          PART III: INFORMATION, DYNAMICS & UNIVERSALITY      │
          │                                                             │
          │  ┌───────────────┐  ┌───────────────┐  ┌────────────────┐  │
          │  │ Ch 9: Entropy  │  │Ch 10: Ergodic │  │Ch 11: Universal│  │
          │  │                │  │               │  │                │  │
          │  │ Template: 0    │  │ Template:     │  │ Axioms (A1-A4) │  │
          │  │ Escape: 0.26   │  │   rigid       │  │ 3 classes      │  │
          │  │ Spectral: max  │  │ Escape:       │  │ 12 structures  │  │
          │  │ Parity barrier │  │   mixing      │  │ GUE from       │  │
          │  │ = info gap     │  │ Spectral:     │  │   incommens.   │  │
          │  │                │  │   GUE-ergodic │  │ Renorm. flow   │  │
          │  │ III.1─III.5    │  │ Quasi-ergodic │  │ Universal      │  │
          │  │                │  │               │  │   parity barr. │  │
          │  │                │  │ III.6─III.10  │  │ III.11─III.17  │  │
          │  └───────┬────────┘  └───────┬───────┘  └───────┬────────┘  │
          │          │                   │                  │           │
          │          └───────────────────┼──────────────────┘           │
          │                              │                             │
          │                   ┌──────────┴──────────────┐              │
          │                   │  TRIPLE CORRESPONDENCE   │              │
          │                   │  (Theorem III.17)        │              │
          │                   │                          │              │
          │                   │  0 entropy = rigid       │              │
          │                   │  + entropy = ergodic     │              │
          │                   │  max entropy = GUE       │              │
          │                   │                          │              │
          │                   │  D(p) governs all three  │              │
          │                   └─────────────────────────┘              │
          └────────────────────────────┬────────────────────────────────┘
                                       │
               ╔═══════════════════════╧════════════════════════╗
               ║  KEY DEPENDENCIES FLOWING DOWN:                ║
               ║  Thm III.5  (Parity = info gap) ──→ Ch 13     ║
               ║  Thm III.14 (Universality crit.) ──→ Ch 13    ║
               ║  Thm III.16 (Renormalization)    ──→ Ch 12    ║
               ║  Thm III.17 (Triple corresp.)    ──→ Ch 14    ║
               ╚═══════════════════════╤════════════════════════╝
                                       │
          ┌────────────────────────────┴────────────────────────────────┐
          │            PART IV: META-STRUCTURE & META-MATHEMATICS        │
          │                                                             │
          │  ┌─────────────────────┐         ┌────────────────────────┐ │
          │  │ Ch 12: Meta-Structure│         │ Ch 13: Meta-Mathematics│ │
          │  │                     │         │                        │ │
          │  │ lpf = sole primitive│         │ K(S_N) = O(log N)     │ │
          │  │ 3 meta-axioms (M1-3)│         │ H(esc|templ) ≥ 0.26N │ │
          │  │ 4-level emergence   │         │ Pseudo-random (K ≪ H) │ │
          │  │ 3 dualities         │         │ Barrier ≠ Gödel       │ │
          │  │ Renormalization     │         │ T_FS = first-order    │ │
          │  │ Self-reference      │         │ Comput. hierarchy     │ │
          │  │                     │         │                        │ │
          │  │ IV.1─IV.5           │         │ IV.6─IV.11             │ │
          │  └──────────┬──────────┘         └───────────┬────────────┘ │
          │             │                                │              │
          │             └────────────┬───────────────────┘              │
          │                          │                                  │
          │               ┌──────────┴──────────────────────────┐      │
          │               │  Ch 14: Unified Meta-Architecture    │      │
          │               │                                      │      │
          │               │  Meta-correspondence (IV.12):        │      │
          │               │    structure ←→ logic at every level │      │
          │               │                                      │      │
          │               │  The boundary (IV.13):               │      │
          │               │    ≡ 0.26 bits/int (information)     │      │
          │               │    ≡ escape hardness (computation)   │      │
          │               │    ≡ Σ₁⁰ vs Π₂⁰ gap (logic)        │      │
          │               │    ≡ universal in all (A1-A4) (meta) │      │
          │               └─────────────────────────────────────┘      │
          └────────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════
LEGEND
═══════════════════════════════════════════════════════════════════════════

  ───▷    Structural dependence (definitions, constructions)
           Ch 1 → Ch 2 → Ch 3: each chapter builds on the previous

  ═══╤═══ Cross-part dependence (theorems referenced across parts)
           Listed explicitly in the dependency boxes between parts

  ┌─────┐
  │     │  Chapter (with theorem range)
  └─────┘

  ╔═════╗
  ║     ║  Key cross-part dependency summary
  ╚═════╝

  ARROW TYPES IN CROSS-PART BOXES:
    ──→  All arrows from Part I are STRUCTURAL (definitions, CRT)
    ──→  Arrows from Part II are STATISTICAL (correlations, entropy)
    ──→  Arrows from Part III are FOUNDATIONAL (information, dynamics)

═══════════════════════════════════════════════════════════════════════════
GLOBAL FLOW
═══════════════════════════════════════════════════════════════════════════

  lpf(n)
    │
    ▼
  Coverage architecture  ─── CRT independence (Thm I.2) ───┐
    │                                                        │
    ▼                                                        ▼
  D(p) = ∏(1−1/q)  ◄──── the single governing quantity ────▷ ALL statistics
    │                                                        │
    ├──▷ PNT: π(N) ∼ N·D(√N)                               │
    ├──▷ Conservation: θ(x) ∼ x                             │
    ├──▷ Template persistence: N_H grows                     │
    ├──▷ Coverage protection: C_H > 1                        │
    │                                                        │
    ▼                                                        ▼
  Renormalization: D(p_{k+1}) = D(p_k)·(1−1/p_{k+1})      Entropy budget
    │                                                     (68.5% template
    ▼                                                      31.5% stochastic
  D → 0: corridor collapse                                0.26 bits = barrier)
    │
    ▼
  The parity barrier: architecture determines OPEN positions
                      but not ESCAPE occupancy (~0.26 bits/int)
    │
    ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  PROVED (below barrier)  │  OPEN (above barrier)            │
  │  Template persistence    │  Twin prime conjecture            │
  │  Coverage protection     │  Goldbach conjecture              │
  │  Geometric PNT           │  Riemann Hypothesis               │
  │  Erdős–Kac, Möbius       │  Cramér conjecture                │
  │  Conservation law         │  Chowla conjecture                │
  │  12 universal structures  │  k-tuple conjecture               │
  └─────────────────────────────────────────────────────────────┘
```
