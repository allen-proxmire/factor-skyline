# The Factor Skyline: A Unified Architecture for Multiplicative Number Theory

[![DOI](https://zenodo.org/badge/1135940602.svg)](https://doi.org/10.5281/zenodo.18275273)

---

## Overview

The **Factor Skyline** is a geometric ontology of the integers in which each integer *n* becomes a column of width lpf(*n*) (least prime factor) and height *n*/lpf(*n*), placed cumulatively along a horizontal axis. The resulting two-dimensional landscape is governed by five emergent concepts — width, height, activation, coverage, and escape — all deriving from a single primitive function. This repository contains a four-part monograph developing the FS framework as a unified architectural, statistical, dynamical, and meta-mathematical theory: Part I establishes the coverage architecture and derives the prime number theorem, Dickman smoothness, and Chebyshev conservation from geometric first principles; Part II develops the correlation and randomness theories, proving that all arithmetic correlations arise from CRT independence of width layers; Part III establishes the entropy, ergodic, and universality theories, identifying the escape density D(*p*) as a renormalization coupling constant; and Part IV examines the framework's own meta-structure, proving that lpf is the sole primitive and that the parity barrier — a 0.26-bit-per-integer information gap — is the precise structural limit separating the framework's 66 proved theorems from the major open conjectures.

---

## Repository Structure

- **`FS_monograph.md`** — The unified four-part monograph assembling the complete FS framework: 66 theorems, 12 definitions, 14 chapters, 20 verification tables, and a comprehensive back matter.

- **`FSPapers_01_architectural_foundation.md`** — Part I as a standalone paper: the five primitives, templates, coverage protection, template persistence, FS-x footprint invariance, geometric PNT, Dickman smoothness, Mobius structure, divisor geometry, and the conservation law. (22 theorems.)

- **`FSPapers_02.1_correlations_and_randomness.md`** — Part II as a standalone paper: the shared-layer / independent-layer decomposition, Hardy-Littlewood pair correlations, Chowla mechanism, divisor correlations, omega non-mixing, GUE level repulsion, sub-Poisson escape, the 73/27 template-stochastic split, entropy budget, and the unified randomness principle. (14 theorems.)

- **`FSPapers_03_information_dynamics_universality.md`** — Part III as a standalone paper: entropy theory (the 68.5/31.5 split), ergodic theory (quasi-ergodicity, mixing dichotomy), universality theory (three classes, 12 universal structures, GUE from incommensurability), the renormalization flow, and the triple correspondence. (17 theorems.)

- **`FSPapers_04_meta_structure.md`** — Part IV as a standalone paper: lpf as sole primitive, three minimal meta-axioms, emergence hierarchy, three dualities, renormalization group, Kolmogorov complexity, pseudo-randomness, the parity barrier as a methodological (not Godelian) limit, T_FS as a first-order theory, and the computational-mathematical mirror. (13 theorems.)

- **`FS_architectural_map.png`** — A high-resolution hierarchical diagram showing the four-part structure, all 14 chapters, cross-part theorem dependencies, and the global flow from lpf through D(*p*) to the parity barrier.

- **`FS_glossary.md`** — A 30-entry glossary organized into four conceptual clusters (Architectural, Statistical, Dynamical/Universal, Meta-Structural), with definitions, provenance, and cross-references.

- **`FS_coordinates.py`** — Python implementation of the FS-coordinate system. Computes (*n*, *x*_FS, *y*_FS) for integers 1 through *N* using SymPy.

- **`FS_prime-coordinates.py`** — Variant that outputs FS-coordinates for primes only.

- **`The Factor Skyline_manuscript.md`** — The founding manuscript describing the FS construction and its conceptual motivation.

---

## Getting Started

**For a first reading,** start with the [Architectural Map](FS_architectural_map.png) to see how the 14 chapters and 4 parts interrelate, then read the monograph (`FS_monograph.md`) in order: Part I (architecture) → Part II (statistics) → Part III (foundations) → Part IV (meta-theory). Each part builds on the previous; cross-references are explicit.

**For quick reference,** consult the [Glossary](FS_glossary.md) for precise definitions of all core terms.

**For a focused reading,** each `FSPapers_0X` file is a self-contained paper readable independently, with its own abstract, theorems, proofs, tables, and references.

**For computational exploration,** run `FS_coordinates.py` to generate FS-coordinate tables and verify the numerical results in the monograph.

---

## Reproducibility

All numerical tables in the monograph (Tables A.1 through A.20) are generated from the FS-coordinate system implemented in `FS_coordinates.py`. The verification data includes:

- **FS-coordinate tables** for *n* = 1 to 30 (and beyond)
- **Escape density convergence** (D(*p*) vs Mertens asymptotic)
- **PNT verification** (pi(*N*) vs *N* D(sqrt *N*) for *N* up to 10^5)
- **Conservation law** (theta(*x*)/*x* convergence)
- **Pair correlations, Mobius correlations, divisor correlations, omega correlations**
- **Sub-Poisson variance, FS-x autocorrelation, entropy decomposition**
- **Zero spacing statistics and explicit formula reconstruction**

To reproduce any table, install SymPy (`pip install sympy`) and run the corresponding computation. All scripts use only standard Python and SymPy — no proprietary dependencies.

---

## Core Concepts

- **lpf as sole primitive.** The entire FS framework — all 66 theorems across four parts — derives from a single function: lpf(*n*), the least prime factor. (Part IV, Theorem IV.1.)

- **Template architecture.** The combined coverage of primes 2, 3, ..., *p* creates a repeating pattern with period *p*# that determines 73.3% of the skyline's structure deterministically. (Part I, Ch. 2; Part II, Theorem II.10.)

- **Shared/independent layer decomposition.** Every arithmetic correlation decomposes into contributions from shared layers (primes dividing the offset, creating correlation) and independent layers (primes not dividing the offset, creating decorrelation by CRT). (Part II, Theorem II.1.)

- **Entropy budget: 68.5% / 31.5%.** The primorial template provides 1.70 of the total 2.48 bits per integer in the FS-x increment sequence. The remaining 0.78 bits are genuine uncertainty, of which 0.26 bits are the irreducible escape entropy. (Part II, Theorem II.13.)

- **Renormalization flow D(*p*).** Template extension *p*_k# to *p*_{k+1}# defines a multiplicative renormalization with D(*p*) as the running coupling constant, flowing irreversibly from D = 1/2 toward the fixed point D = 0. (Part III, Theorem III.16.)

- **Parity barrier: 0.26 bits/int.** The precise structural limit separating the framework's proved results from the open conjectures. It is methodological (not Godelian), information-theoretic (0.26 bits/int), computational (escape layer as hard as primality), logical (Sigma-1-0 vs Pi-2-0), and universal (applies to all systems satisfying the FS axioms). (Part III, Theorem III.5; Part IV, Theorem IV.13.)

- **Universality classes.** Three classes of multiplicative systems — logarithmic thinning (the integers), constant density (polynomial rings over finite fields), and degenerate — determined by the asymptotic behavior of the escape density. (Part III, Theorem III.11.)

---

## Citation

If you reference or discuss this work, please cite:

```bibtex
@misc{proxmire2026factorskyline,
  author       = {Allen Proxmire},
  title        = {The Factor Skyline: An Ontological Lookout Over the Integers},
  year         = {2026},
  doi          = {10.5281/zenodo.18275273},
  url          = {https://doi.org/10.5281/zenodo.18275273},
  note         = {Monograph and supporting materials available at
                  https://github.com/allen-proxmire/factor-skyline}
}
```

---

## Contact and Contributing

Questions, feedback, and collaboration inquiries are welcome. Please open an issue on this repository or reach out via [GitHub Discussions](../../discussions).

This is an evolving research program. Contributions — whether numerical experiments, alternative proofs, extensions to new multiplicative systems, or independent verification of the monograph's results — are encouraged.
