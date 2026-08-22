# Contributing

Contributions should improve benchmark rigor, reproducibility, or clarity without weakening integrity gates.

Before opening a pull request:

1. Add or update tests for changed behavior.
2. Add deterministic benchmark scenarios when evaluation semantics change.
3. Run `ruff check .`, `pytest -q`, `python evals/run_benchmarks.py`, and `python run.py`.
4. Document changes to task contracts, scoring, baselines, or integrity checks.
5. Do not introduce hidden network dependencies into the default CI path.

Changes that alter benchmark meaning should include migration notes and an explicit explanation of comparability with earlier results.
