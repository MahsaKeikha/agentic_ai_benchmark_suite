# Agentic AI Benchmark Suite

F38 is a multi-agent reference implementation for designing, executing, challenging, analyzing, and reporting AI benchmarks.

## Maturity

**L2 candidate.** The suite is deterministic and CI-gated, but L3 requires broader held-out suites, independent reproduction, and published benchmark artifacts.

## Architecture

Five agents own distinct responsibilities:

1. **Task Designer** validates task identity, weights, difficulty, and benchmark inputs.
2. **Evaluator** executes bounded 0 to 1 scoring contracts per task.
3. **Adversarial Agent** checks leakage, gaming signals, duplicate identities, and suspicious score spread.
4. **Statistics Agent** computes weighted score, pass rate, variance, and baseline regressions.
5. **Reporting Agent** issues a reproducible pass/fail report with integrity and regression evidence.

The benchmark fails when integrity checks fail or when configured baseline regressions exceed tolerance. Scores outside the declared range and malformed task sets are rejected instead of silently normalized.

## Reproduce

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python evals/run_benchmarks.py
python run.py
```

CI runs these gates on Python 3.10, 3.11, and 3.12.

## Benchmark contract

A benchmark specification contains a non-empty `tasks` list. Each task may define `id`, `observed_score`, `pass_threshold`, `difficulty`, and `weight`. Optional `baseline` values and `regression_tolerance` enable regression detection.

## Limitations

This repository demonstrates benchmark engineering patterns. Its bundled scenarios are intentionally small and offline. They do not establish universal model quality, safety, or statistical significance for a production deployment.

See `docs/ARCHITECTURE.md`, `docs/EVALUATION.md`, and `docs/SAFETY.md` for design details.
