# F38 L3 Gold Standard Audit

F38 is eligible for L3 only when the exact promotion commit satisfies all of the following:

- five substantive benchmark agents with explicit agent, skill, and tool separation
- validated task identities, bounded scores, weights, thresholds, difficulty, and baselines
- fail-closed integrity, regression, pass-rate, and minimum-score reporting gates
- adversarial checks for duplicate IDs, reference leakage, benchmark gaming, and suspicious score spread
- deterministic primary scenarios plus an eight-scenario held-out suite
- unit, integration, malformed-input, adversarial, and regression tests
- minimal and complete examples runnable from a clean checkout
- Python 3.10, 3.11, and 3.12 CI green
- Python 3.12 held-out artifact publication
- benchmark evidence recorded in `benchmarks/RESULTS.md`
- version 1.0.0, MIT license, citation, contribution, security, and changelog metadata

L3 denotes a reproducible and independently reviewable benchmark-engineering reference implementation. It is not a claim that the bundled benchmark establishes universal AI quality or safety.
