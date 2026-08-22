# Agentic AI Benchmark Suite

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

F38 is a multi-agent reference implementation for designing, executing, challenging, analyzing, and reporting AI benchmarks.

## Architecture

Five agents own distinct responsibilities:

1. **Task Designer** validates task identity, weights, difficulty, and benchmark inputs.
2. **Evaluator** executes bounded 0 to 1 scoring contracts per task.
3. **Adversarial Agent** checks leakage, gaming signals, duplicate identities, and suspicious score spread.
4. **Statistics Agent** computes weighted score, pass rate, variance, and baseline regressions.
5. **Reporting Agent** applies fail-closed integrity, regression, pass-rate, and minimum-score gates.

A benchmark fails when integrity checks fail, baseline regressions exceed tolerance, the required pass rate is missed, or the minimum weighted score is not met.

## Reproduce

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python evals/run_benchmarks.py
python evals/heldout_suite.py
python examples/minimal.py
python examples/complete.py
python run.py
```

CI runs the complete gate on Python 3.10, 3.11, and 3.12. Python 3.12 publishes the held-out result artifact.

## L3 evidence

The promotion path requires all CI jobs green on the exact promotion commit, the eight-scenario held-out suite at 8/8 expected behavior, clean-checkout examples, artifact publication, and benchmark evidence recorded in `benchmarks/RESULTS.md`.

## Limitations

This is a benchmark-engineering reference implementation. Passing bundled scenarios does not establish universal model quality, statistical significance, or production safety. Benchmark conclusions remain bounded by the task set, scoring contract, baselines, and threat model.

See `docs/ARCHITECTURE.md`, `docs/EVALUATION.md`, `docs/SAFETY.md`, and `docs/L3_AUDIT.md`.
