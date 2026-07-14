# Factor Skyline

[![DOI](https://zenodo.org/badge/1135940602.svg)](https://doi.org/10.5281/zenodo.18275273)

A two-dimensional architecture of the integers. Each integer $n$ becomes a column of width $\mathrm{lpf}(n)$ (least prime factor) and height $n/\mathrm{lpf}(n)$. In the resulting landscape, **primes escape to the diagonal** ($y=n$) while **composites rain onto width-rays** ($y=n/p$) — the primorial wheel drawn as geometry. Everything follows from the single function $\mathrm{lpf}$ via five primitives: width, height, activation, coverage, escape.

## What it shows

- **Classical multiplicative number theory as structure.** The prime number theorem, Chebyshev's law, Mertens' theorem, the Dickman function, Erdős–Kac, and divisor averages all arise as geometric features of the skyline rather than analytic accidents.
- **Coverage protection.** The Hardy–Littlewood $k$-tuple constants satisfy $C_H = 2\prod_{q>2}\frac{q(q-2)}{(q-1)^2}\cdot(\dots) > 1$ — an exact identity from the residue-collision structure of the offsets, sharpening Theorem 4.7 to equality with the singular series.
- **Consecutive-prime sums (2026).** The count of consecutive-prime sums $p_k+p_{k+1}$ in a gap of width $W$ near $x$ is $\sim W/(2\ln(x/2))$, and the gap widths that can **never** hold two such sums are exactly $\{2,4,6,10\}$ — a complete, elementary theorem.
- **The Seven Sisters & the wheel (2026).** Which offsets $2p+k$ land on primes is decided by divisibility (the wheel); 100% coverage is impossible (unbounded gaps), but the wheel says which offsets to add.
- **The escape ridge (2026).** $x_{FS}(N)\sim 4e^{-\gamma}\,N^{3/2}/\ln^2 N$ — the extra $\sqrt N$ is the sieve's $p^2$ activation, and it explains the empirical escape-curve regression.

## Papers ([`papers/`](papers/))

**The four-part series**
| Part | Title |
|---|---|
| I | [Architectural Foundation](papers/FSPapers_01_architectural_foundation.pdf) |
| II | [Correlation Theory](papers/FSPapers_02_correlation_theory.pdf) · [Correlations & Randomness](papers/FSPapers_02.1_correlations_and_randomness.pdf) |
| III | [Information, Dynamics, and Universality](papers/FSPapers_03_information_dynamics_universality.pdf) |
| IV | [Meta-Structure](papers/FSPapers_04_meta_structure.pdf) |

**Prime-arithmetic notes (2026)** — [Consecutive-Prime Sums in Gaps](papers/FS_Consecutive_Prime_Sums_In_Gaps.pdf) · [The 2p Bracket Construction](papers/FS_2p_Bracket_Construction.pdf) · [Seven Sisters: Wheel & Asymptote](papers/FS_Seven_Sisters_Wheel_Asymptote.pdf) · [Synthesis: Doubling & the Wheel](papers/FS_Synthesis_Doubling_and_Wheel.pdf) · [The Escape Ridge](papers/FS_Escape_Ridge.pdf)

## Reproducibility

```
python reproducibility/run_all.py
```
Deterministic (seed 123456), timestamped tables, CI on push. See [`reproducibility/`](reproducibility/). PDFs build via `make papers` (pandoc + xelatex).

## Citation

```bibtex
@misc{proxmire2026factorskyline,
  author = {Allen Proxmire},
  title  = {The Factor Skyline: An Ontological Lookout Over the Integers},
  year   = {2026},
  doi    = {10.5281/zenodo.18275273},
  url    = {https://doi.org/10.5281/zenodo.18275273}
}
```

Part of the [Primes](../) collection. License in [LICENSE](LICENSE).
