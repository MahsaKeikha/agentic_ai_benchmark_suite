# Evaluation Methodology

F38 evaluates the benchmark system itself through deterministic scenarios rather than claiming that bundled task scores are scientifically representative.

Required acceptance dimensions:

- valid task identity and positive weights
- score bounds from 0 to 1
- explicit task thresholds
- weighted aggregate score
- pass rate
- weighted standard deviation
- baseline regression checks with declared tolerance
- benchmark-integrity checks for leakage and gaming signals
- deterministic trace and evidence output

The CI evaluation suite includes a stable high-performance case, a regression case, and an integrity-failure case. Production benchmark programs should add held-out datasets, repeated runs, uncertainty estimates appropriate to sample size, inter-rater reliability where human labels are used, and versioned benchmark manifests.
