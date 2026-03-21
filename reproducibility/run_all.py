"""
Factor Skyline — Reproducibility Harness Entry Point

Runs all 20 table scripts, serializes results to JSON, and produces
a timestamped summary report.
"""

import importlib
import json
import os
import random
import sys
import traceback
from datetime import datetime

import numpy as np

# ---------------------------------------------------------------------------
# Fixed seed for deterministic reproducibility
# ---------------------------------------------------------------------------
SEED = 123456
random.seed(SEED)
np.random.seed(SEED)

# ---------------------------------------------------------------------------
# Table registry
# ---------------------------------------------------------------------------
TABLES = [
    "tables.table_01_template_widths",
    "tables.table_02_escape_density",
    "tables.table_03_activation_distribution",
    "tables.table_04_centerage_statistics",
    "tables.table_05_interage_statistics",
    "tables.table_06_entropy_budget",
    "tables.table_07_shared_independent_layers",
    "tables.table_08_correlation_decay",
    "tables.table_09_randomness_tests",
    "tables.table_10_survival_factor",
    "tables.table_11_primorial_epochs",
    "tables.table_12_residue_class_balance",
    "tables.table_13_short_intervals",
    "tables.table_14_prime_gaps",
    "tables.table_15_sieve_geometry",
    "tables.table_16_explicit_formula",
    "tables.table_17_zero_geometry",
    "tables.table_18_cramer_model",
    "tables.table_19_twin_primes",
    "tables.table_20_goldbach_statistics",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_serializable(obj):
    """Recursively convert an object into something json.dumps can handle."""
    if isinstance(obj, dict):
        return {str(k): _make_serializable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_make_serializable(v) for v in obj]
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return _make_serializable(obj.tolist())
    if isinstance(obj, (int, float, bool, str, type(None))):
        return obj
    return str(obj)


def _short_name(module_name):
    """'tables.table_01_template_widths' -> 'table_01_template_widths'"""
    return module_name.rsplit(".", 1)[-1]


def _table_number(module_name):
    """'tables.table_01_template_widths' -> '01'"""
    name = _short_name(module_name)
    parts = name.split("_")
    if len(parts) >= 2 and parts[1].isdigit():
        return parts[1]
    return "00"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "tables", "output", timestamp)
    os.makedirs(output_dir, exist_ok=True)

    results_summary = []
    ok_count = 0
    err_count = 0

    print(f"Factor Skyline Reproducibility Harness")
    print(f"Timestamp : {timestamp}")
    print(f"Seed      : {SEED}")
    print(f"Output    : {output_dir}")
    print(f"Tables    : {len(TABLES)}")
    print("-" * 60)

    for module_name in TABLES:
        short = _short_name(module_name)
        num = _table_number(module_name)
        entry = {
            "module": module_name,
            "short_name": short,
            "status": None,
            "error": None,
        }

        try:
            module = importlib.import_module(module_name)
            raw_result = module.run()
            result = _make_serializable(raw_result)

            out_path = os.path.join(output_dir, f"table_{num}.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            entry["status"] = "ok"
            ok_count += 1
            print(f"  [OK]  {short}")

        except Exception as exc:
            entry["status"] = "error"
            entry["error"] = f"{type(exc).__name__}: {exc}"
            err_count += 1
            print(f"  [ERR] {short}: {exc}")
            traceback.print_exc(file=sys.stderr)

        results_summary.append(entry)

    # ------------------------------------------------------------------
    # Summary report
    # ------------------------------------------------------------------
    summary = {
        "timestamp": timestamp,
        "seed": SEED,
        "output_dir": output_dir,
        "total": len(TABLES),
        "ok": ok_count,
        "errors": err_count,
        "tables": results_summary,
    }

    summary_path = os.path.join(output_dir, "summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("-" * 60)
    print(f"Done: {ok_count} ok, {err_count} errors")
    print(f"Summary written to: {summary_path}")

    return 0 if err_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
