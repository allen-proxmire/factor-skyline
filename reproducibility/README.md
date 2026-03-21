# Factor Skyline Reproducibility Harness

This folder contains the complete reproducibility infrastructure for the Factor Skyline monograph and papers. Its purpose is to regenerate every numerical result cited in the four-part monograph, verify all 20 verification tables against their theoretical predictions, and ensure that every run is deterministic, timestamped, and independently reproducible. The harness uses fixed random seeds, isolated output directories, and a stable JSON schema so that results can be compared across machines, dates, and software versions without ambiguity.

---

## Folder Structure

The reproducibility harness is organized into five directories, each with a distinct role:

- **`scripts/`** — Core computational scripts inherited from the main repository. These include `FS_coordinates.py` (the ground-truth FS-coordinate system), `FS_prime-coordinates.py` (prime-only coordinate output), and `generate_map.py` (architectural map rendering). These scripts are not modified by the harness; they serve as shared infrastructure.

- **`tables/`** — The 20 table computation scripts, one per verification table in the monograph. Each script exposes a single `run()` function that returns a dictionary of results. These are the primary units of computation in the harness.

- **`tables/output/`** — Timestamped output directories created by each run of the harness. Each subdirectory contains 20 JSON files (one per table) and a `summary.json` report. Old runs are never overwritten or deleted.

- **`utils/`** — Shared utility modules for use by the table scripts. Currently contains stubs for `skyline.py` (FS-coordinate helpers), `primes.py` (prime generation and factorization), `plotting.py` (visualization), and `io.py` (file I/O and serialization). These will be populated as table computations are implemented.

- **`notebooks/`** — Jupyter notebooks for interactive exploration, visualization, and pedagogical walkthroughs of the verification results. Currently empty; notebooks will be added as the harness matures.

---

## How to Run the Harness

From the `reproducibility/` directory, run:

```
python run_all.py
```

This executes all 20 table scripts in sequence and produces:

- **Deterministic seeding.** Both Python's `random` module and NumPy's random number generator are seeded with the fixed value `123456` at the start of every run and again within each table script. This guarantees identical output across runs, machines, and platforms.

- **Timestamped output directory.** Each run creates a new folder under `tables/output/` named with the current timestamp in `YYYYMMDD_HHMMSS` format. All output files for that run are written inside this folder.

- **JSON output per table.** Each table script produces a single JSON file (`table_01.json` through `table_20.json`) containing its computed results.

- **Summary report.** After all tables have run, a `summary.json` file is written to the output directory containing the timestamp, seed value, per-table status, any error messages, and the path to the output directory.

---

## Table Index

The 20 verification tables span the full scope of the Factor Skyline architecture, from basic coordinate geometry through advanced correlation and randomness diagnostics.

| Table | Name | What It Verifies |
|-------|------|------------------|
| 01 | Template Widths | Distribution of FS column widths (least prime factors) across the primorial template for integers 1 through N. |
| 02 | Escape Density | Escape density product D(p) against the Mertens asymptotic e^(-gamma)/ln(p) for increasing prime thresholds. |
| 03 | Activation Distribution | Distribution of activation events (prime squares) and epoch lengths between consecutive activations. |
| 04 | Centerage Statistics | Statistical properties of FS-x and FS-y coordinates at the center of each activation epoch. |
| 05 | Interage Statistics | Statistical properties of inter-epoch gaps and escape distribution across epoch boundaries. |
| 06 | Entropy Budget | Entropy decomposition of the FS-x increment sequence into template, escape, and activation contributions. |
| 07 | Shared and Independent Layers | Shared-layer / independent-layer decomposition for arithmetic correlations at various offsets. |
| 08 | Correlation Decay | Decay rate of prime-prime, Mobius-Mobius, and divisor-divisor correlations as a function of offset. |
| 09 | Randomness Tests | Sub-Poisson variance, autocorrelation decay, and other randomness diagnostics for the escape sequence. |
| 10 | Survival Factor | Hardy-Littlewood survival factors for twin primes, cousin primes, and other prime constellations. |
| 11 | Primorial Epochs | Structure and periodicity of primorial templates and their interaction with activation epochs. |
| 12 | Residue Class Balance | Equidistribution of primes across residue classes mod p for small primes p. |
| 13 | Short Intervals | Prime count in short intervals [n, n+h] against escape density predictions for various window sizes. |
| 14 | Prime Gaps | Distribution of prime gaps in both classical and FS-x coordinates, including maximal gap statistics. |
| 15 | Sieve Geometry | Geometric sieve structure: coverage layer removal fractions compared against exact counts. |
| 16 | Explicit Formula | Reconstruction of the prime counting function from smooth trend plus oscillatory zero contributions. |
| 17 | Zero Geometry | Spacing statistics of Riemann zeta zeros against GUE predictions and primorial resonance frequencies. |
| 18 | Cramer Model | Maximal prime gap statistics against the Cramer conjecture bound and FS epoch-constrained predictions. |
| 19 | Twin Primes | Twin prime counts and survival factors against the Hardy-Littlewood prediction and template persistence. |
| 20 | Goldbach Statistics | Goldbach representation counts for even integers against the escape-pair density prediction. |

---

## Output Format

Every table script returns a Python dictionary with the following stable schema:

```json
{
    "table": "XX",
    "name": "Human-Readable Title",
    "status": "ok",
    "placeholder_value": 0.12696983303810846,
    "notes": "Computation not yet implemented"
}
```

The fields are:

- **`table`** — The two-digit table number (01 through 20), as a string.
- **`name`** — The human-readable title of the table.
- **`status`** — Either `"ok"` (computation succeeded) or `"error"` (computation failed).
- **`placeholder_value`** — A deterministic float produced by the seeded random number generator. This field will later hold the primary computed result.
- **`notes`** — Free-text annotations. Currently indicates placeholder status; will later contain verification summaries.

As real computations are implemented, additional keys will be added to each table's output dictionary. The five core fields listed above will remain stable across all future versions to ensure backward compatibility with analysis scripts.

---

## Timestamped Run Structure

Each invocation of `run_all.py` creates an isolated output directory:

```
tables/output/
    20260321_122818/
        table_01.json
        table_02.json
        ...
        table_20.json
        summary.json
    20260321_143012/
        table_01.json
        ...
        summary.json
```

Runs are never overwritten. This allows direct comparison of results across dates, code versions, and environments. The `summary.json` file in each directory records the exact timestamp, seed, and per-table status, making every run fully self-documenting.

---

## Error Handling

The harness is designed to run all 20 tables regardless of individual failures:

- **Exception catching.** If any table script raises an exception, the harness catches it, records the error type and message, and continues to the next table. No single failure aborts the run.

- **Error recording.** Errors are recorded in `summary.json` with full exception type and message for each failed table. The summary also reports the total count of successes and failures.

- **Console output.** During execution, each table prints either `[OK]` (success) or `[ERR]` (failure with error message) to the console. A final summary line reports the totals.

- **Exit code.** The harness exits with code `0` if all 20 tables succeed, or code `1` if any table fails. This supports integration with CI/CD pipelines and automated testing.

---

## Philosophy of Reproducibility

Mathematical reproducibility requires more than correct code. It requires that every numerical claim in a publication can be regenerated independently, on any machine, at any future date, and produce identical results. The Factor Skyline harness achieves this through three design principles.

**Deterministic seeding** ensures that all pseudo-random computations produce identical output across runs. Both Python's `random` module and NumPy's random number generator are seeded with a fixed value at the start of every run and again within each table script. This eliminates platform-dependent variation and makes every output byte reproducible. **Timestamped isolation** ensures that no run can contaminate another. Each invocation creates its own output directory, and old results are never modified. This allows longitudinal comparison as the codebase evolves: if a computation changes, the change is visible as a difference between timestamped directories, not as an unexplained mutation of a shared file. **Stable schemas** ensure that analysis tools, comparison scripts, and human readers can rely on a fixed output format. The JSON schema returned by each table script is a contract: the five core fields will persist across all future versions, even as additional fields are added. This decouples the harness from downstream consumers and prevents format drift from breaking the reproducibility chain.

---

## Future Work

The current harness establishes the scaffolding; the following extensions are planned as the project matures:

- **Real computations.** Each of the 20 placeholder table scripts will be replaced with full implementations that compute the verification data cited in the monograph. The `placeholder_value` field will be replaced by structured numerical results, while the core schema fields remain stable.

- **Jupyter notebooks.** Interactive notebooks will be added to the `notebooks/` directory for visualization, exploration, and pedagogical walkthroughs of the verification results. These will import the shared utilities in `utils/` and read directly from the timestamped output directories.

- **Continuous integration.** A GitHub Actions workflow will be added to run the full harness on every push and pull request, ensuring that all 20 tables pass and that no code change silently breaks a numerical result.

- **Makefile targets.** A top-level Makefile will provide convenient entry points for common operations: `make tables` to run all 20 tables, `make clean` to remove output directories, `make compare` to diff two timestamped runs, and `make notebooks` to execute all notebooks and verify their outputs.
