# Architecture

F38 uses a sequential benchmark lifecycle with explicit ownership boundaries. `BenchmarkState` is the shared run ledger. The Task Designer validates the benchmark task set before any scores are accepted. The Evaluator enforces bounded score contracts. The Adversarial Agent searches for benchmark-integrity problems. The Statistics Agent computes aggregate metrics and compares them with declared baselines. The Reporting Agent converts the run into a reproducible decision artifact.

No agent may redefine another agent's output silently. Failures such as duplicate IDs, invalid scores, benchmark gaming signals, integrity findings, and configured regressions are surfaced in state and reflected in the final report.

The included implementation is offline and deterministic by design so CI results do not depend on external model providers or network services.
