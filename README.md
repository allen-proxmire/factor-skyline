# Factor Skyline

[![DOI](https://zenodo.org/badge/1135940602.svg)](https://doi.org/10.5281/zenodo.18275273)

---

## EXPDB Binding Constraint Analysis (2026)

**[Binding Constraints After Guth-Maynard: A Structural Analysis of the EXPDB Pipeline](papers/EXPDB-Analysis/GuthMaynard_BindingConstraints.md)**

A computational analysis of the [Analytic Number Theory Exponent Database](https://teorth.github.io/expdb/) (EXPDB) pipeline after the Guth-Maynard (2024) large value estimate. We ran the full pipeline (482 hypotheses, scipy-based polytope backend), identified the binding constraints, and performed a complete sensitivity analysis.

**Key results:**

- The GM result creates a **cusp at sigma = 7/10** where Ingham (1940) and GM (2024) meet at A = 30/13, determining theta_PNTALL = 17/30
- **Sensitivity:** d(theta)/d(||A||) = 169/900. The attack surface is narrow: an epsilon-improvement needs to hold on an interval of width ~0.006 around sigma = 0.70
- The **bottleneck is purely in A(sigma)** for theta_PNTALL; the energy exponent A*(sigma) only enters at the GAPSQUARE level
- **Pipeline completeness verified:** no unexploited transformation chain changes the binding value
- **Succession landscape:** after the cusp, the next bottlenecks migrate rightward through Ivic (2003), Ivic (1980), TTY (2024), and onward to the Density Hypothesis

| | |
|---|---|
| ![A(sigma) envelope](PAPERS/EXPDB-Analysis/A_sigma_envelope.png) | ![Sensitivity heat map](PAPERS/EXPDB-Analysis/sensitivity_heatmap.png) |
| *Zero-density envelope with binding constraints* | *Sensitivity cone at the cusp* |

**Full paper, figures, and code:** [`PAPERS/EXPDB-Analysis/`](PAPERS/EXPDB-Analysis/)

**Companion papers:**
- [EXPDB-Skyline: A Polyhedral Reinterpretation](PAPERS/EXPBD-Skyline/EXPDB-Skyline_A-Polyhedral-Reinterpretation.md) - identifies the master polytope P from which all EXPDB outputs descend
- [Background analysis](PAPERS/EXPDB-Analysis/GuthMaynard_EXPDB_Analysis.md) - how GM fits into the EXPDB polyhedral framework

---

## Factor Skyline: Multiplicative Structure of the Integers

The Factor Skyline is a geometric architecture for the integers in which each integer *n* is represented as a column of width lpf(*n*) (least prime factor) and height *n*/lpf(*n*). The resulting two-dimensional landscape is governed by five emergent concepts (width, height, activation, coverage, and escape), all deriving from the single primitive function lpf. The project develops the Factor Skyline as a unified architectural, statistical, dynamical, and meta-mathematical theory of multiplicative number theory.

The Factor Skyline is one instance of **[Architectural Distillation](https://github.com/allen-proxmire/architectural-distillation)** (AD), a general methodology for extracting structure from systems composed of interacting mechanisms.

### The Four Papers

| Part | Title | Theorems |
|------|-------|----------|
| I | [Architectural Foundation](PAPERS/FSPapers_01_architectural_foundation.md) | 22 |
| II | [Correlations and Randomness](PAPERS/FSPapers_02.1_correlations_and_randomness.md) | 14 |
| III | [Information, Dynamics, and Universality](PAPERS/FSPapers_03_information_dynamics_universality.md) | 17 |
| IV | [Meta-Structure](PAPERS/FSPapers_04_meta_structure.md) | 13 |

---

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| **`PAPERS/EXPDB-Analysis/`** | EXPDB binding constraint analysis after Guth-Maynard (2024). Papers, figures, pipeline report. |
| **`PAPERS/EXPBD-Skyline/`** | EXPDB-Skyline polyhedral reinterpretation paper. |
| **`compute/`** | Pipeline code, gap test harness, plotting scripts, and the EXPDB clone with scipy cdd replacement. |
| **`monograph/`** | The unified four-part Factor Skyline monograph. |
| **`PAPERS/`** | All standalone papers (FS Parts I-IV, EXPDB analyses, evaluations). |
| **`modules/`** | 18 derivation modules for the Factor Skyline theory. |
| **`reproducibility/`** | Deterministic reproducibility harness for all FS numerical claims. |
| **`maps/`** | Architectural maps of the monograph structure. |
| **`archive/`** | Earlier drafts, preserved for provenance. |

---

## Reproducibility

```
python reproducibility/run_all.py
```

Deterministic seeding (seed 123456), 20 verification tables, timestamped output, GitHub Actions CI on every push. See [reproducibility/README.md](reproducibility/README.md).

---

## Citation

```bibtex
@misc{proxmire2026factorskyline,
  author       = {Allen Proxmire},
  title        = {The Factor Skyline: An Ontological Lookout Over the Integers},
  year         = {2026},
  version      = {v1.0},
  doi          = {10.5281/zenodo.18275273},
  url          = {https://doi.org/10.5281/zenodo.18275273},
  note         = {Monograph and supporting materials available at
                  https://github.com/allen-proxmire/factor-skyline}
}
```

---

## License

See [LICENSE](LICENSE) for details.

## Contact

Questions, feedback, and collaboration inquiries are welcome. Please open an issue or reach out via [GitHub Discussions](../../discussions).
