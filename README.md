# Factor Skyline

[![DOI](https://zenodo.org/badge/1135940602.svg)](https://doi.org/10.5281/zenodo.18275273)

The **Factor Skyline** is a geometric architecture for the integers in which each integer *n* is represented as a column of width lpf(*n*) (least prime factor) and height *n*/lpf(*n*), placed cumulatively along a horizontal axis. The resulting two-dimensional landscape — the skyline — is governed by five emergent concepts (width, height, activation, coverage, and escape), all deriving from the single primitive function lpf. This repository contains a four-part monograph developing the FS framework as a unified architectural, statistical, dynamical, and meta-mathematical theory of multiplicative number theory, together with a deterministic reproducibility harness that regenerates every numerical result cited in the monograph. The goal is a fully reproducible mathematical platform: every theorem, every table, and every verification can be independently checked from source.

---

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| **`monograph/`** | The unified four-part monograph (`FS_monograph.md`), the glossary (`FS_glossary.md`), the founding manuscript, and the original conceptual PDF. This is the primary scholarly output of the project. |
| **`papers/`** | The four standalone papers, each self-contained with its own abstract, theorems, proofs, and references. These correspond to Parts I through IV of the monograph but can be read independently. |
| **`modules/`** | The 18 individual derivation modules (ontology, PNT, sieve geometry, prime gaps, residue classes, primorial epochs, short intervals, Chebyshev, RH analogue, explicit formula, twin primes, Goldbach, Cramer, constellations, Mobius, smooth numbers, zero geometry, divisors). These are the working derivation layer between the monograph and the code. |
| **`maps/`** | The architectural map of the monograph in both Markdown and high-resolution PNG formats. Shows the four-part structure, all 14 chapters, and cross-part theorem dependencies. |
| **`reproducibility/`** | The full reproducibility harness: entry-point script, 20 verification table scripts, shared utilities, and timestamped output directories. See [reproducibility/README.md](reproducibility/README.md) for detailed documentation. |
| **`archive/`** | Earlier intermediate drafts (FS_01 through FS_09) that were later integrated into the monograph papers. Preserved for provenance; not part of the current scholarly output. |
| **`data/`** | Reserved for raw datasets and computed inputs. Currently empty. |
| **`.github/workflows/`** | GitHub Actions CI configuration for automated reproducibility checks on every push and pull request. |

---

## The Factor Skyline Architecture

The Factor Skyline begins with a single observation: every integer *n* > 1 has a least prime factor, and that least prime factor determines a natural column width. Placing these columns side by side along a horizontal axis produces a two-dimensional landscape in which:

- **Templates** emerge from the combined coverage of small primes. The primes up to *p* create a repeating pattern of width assignments with period *p*# (the primorial), which determines the majority of the skyline's structure deterministically.
- **Activations** occur at prime squares. When a new prime *p* reaches its square *p*^2, a new width-*p* layer enters the geometry, permanently claiming a fraction 1/*p* of the remaining uncovered positions.
- **Escapes** are the integers that slip through all active coverage layers — the primes. They appear as narrow spires of width 1 in the skyline.
- **Escape density** D(*p*) = product of (1 - 1/*q*) for primes *q* up to *p* governs the long-term frequency of primes. Its asymptotic decay (via Mertens' theorem) produces the prime number theorem as a geometric consequence.

This architecture unifies the four papers: Part I builds the geometric foundations, Part II derives correlation and randomness structure from CRT independence of width layers, Part III establishes entropy, ergodic, and universality theories with D(*p*) as a renormalization coupling constant, and Part IV examines the framework's own meta-structure, identifying the parity barrier as the precise limit of the architecture's deductive reach.

---

## The Four Papers

The monograph comprises four parts, each available as a standalone paper:

**Part I — Architectural Foundation.**
Establishes the five primitives (width, height, activation, coverage, escape), derives the primorial template, coverage protection, template persistence, FS-x footprint invariance, the geometric prime number theorem, Dickman smoothness, Mobius structure, divisor geometry, and the Chebyshev conservation law. 22 theorems.
[papers/FSPapers_01_architectural_foundation.md](papers/FSPapers_01_architectural_foundation.md)

**Part II — Correlations and Randomness.**
Develops the shared-layer / independent-layer decomposition, Hardy-Littlewood pair correlations, the Chowla mechanism, divisor correlations, omega non-mixing, GUE level repulsion, sub-Poisson escape statistics, the 73/27 template-stochastic split, the entropy budget, and the unified randomness principle. 14 theorems.
[papers/FSPapers_02.1_correlations_and_randomness.md](papers/FSPapers_02.1_correlations_and_randomness.md)

**Part III — Information, Dynamics, and Universality.**
Establishes the entropy theory (the 68.5/31.5 split), ergodic theory (quasi-ergodicity, mixing dichotomy), universality theory (three classes, 12 universal structures, GUE from incommensurability), the renormalization flow, and the triple correspondence between entropy, ergodicity, and universality. 17 theorems.
[papers/FSPapers_03_information_dynamics_universality.md](papers/FSPapers_03_information_dynamics_universality.md)

**Part IV — Meta-Structure.**
Proves that lpf is the sole primitive, identifies three minimal meta-axioms, derives the emergence hierarchy, three dualities, the renormalization group structure, Kolmogorov complexity bounds, pseudo-randomness characterization, the parity barrier as a methodological (not Godelian) limit, T_FS as a first-order theory with multiple models, and the computational-mathematical mirror. 13 theorems.
[papers/FSPapers_04_meta_structure.md](papers/FSPapers_04_meta_structure.md)

---

## Reproducibility Harness

The reproducibility harness ensures that every numerical claim in the monograph can be independently regenerated. It uses deterministic seeding (Python `random` and NumPy, seed 123456) so that all pseudo-random computations produce identical output across runs, machines, and platforms. Each invocation creates a timestamped output directory under `reproducibility/tables/output/YYYYMMDD_HHMMSS/`, ensuring that no run overwrites another and that longitudinal comparisons are straightforward. The harness executes 20 verification table scripts covering template widths, escape density, activation distribution, entropy budget, correlations, randomness tests, survival factors, prime gaps, sieve geometry, and more. Each table returns a stable JSON schema, and a `summary.json` report records the status of every table. The Makefile provides convenient targets for running, listing, comparing, and cleaning runs. GitHub Actions CI runs the full harness on every push and pull request, uploading timestamped results as build artifacts and failing the build if any table produces an error.

For full documentation, see [reproducibility/README.md](reproducibility/README.md).

---

## How to Run the Harness

From the repository root:

```
python reproducibility/run_all.py
```

This will:

- Seed both `random` and `numpy` with the fixed value 123456.
- Execute all 20 table scripts in sequence.
- Write individual JSON results (`table_01.json` through `table_20.json`) and a `summary.json` to a new timestamped directory under `reproducibility/tables/output/`.
- Print `[OK]` or `[ERR]` for each table to the console.
- Exit with code 0 if all tables succeed, or code 1 if any table fails.

Dependencies: Python 3.11+ and NumPy. Install with `pip install numpy`.

---

## Building the PDFs

The Makefile provides targets for exporting all Markdown documents to PDF using Pandoc with XeLaTeX:

```
make pdfs          # Export monograph, glossary, map, and all papers
make monograph     # Export monograph/FS_monograph.pdf
make glossary      # Export monograph/FS_glossary.pdf
make map           # Export maps/FS_architectural_map.pdf
make papers        # Export all papers/*.pdf
make pdf-clean     # Remove all generated PDFs
```

Requirements: [Pandoc](https://pandoc.org/) and a XeLaTeX distribution (e.g., TeX Live or MiKTeX).

---

## Continuous Integration

GitHub Actions runs the full reproducibility harness on every push and pull request. The workflow:

- Checks out the repository and sets up Python 3.11.
- Installs NumPy as the sole dependency.
- Executes `python reproducibility/run_all.py`.
- Uploads the timestamped output directory as a build artifact (`factor-skyline-output`).
- Fails the build if any table script exits with an error.

This ensures that every commit and every pull request is automatically verified against all 20 tables before merging.

---

## Citation

If you reference or discuss this work, please cite:

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

This project is released under the terms specified in the repository's license file. See [LICENSE](LICENSE) for details.

---

## Contact

Questions, feedback, and collaboration inquiries are welcome. Please open an issue on this repository or reach out via [GitHub Discussions](../../discussions).
