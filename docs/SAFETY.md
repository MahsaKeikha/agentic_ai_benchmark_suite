# Safety and Benchmark Integrity

Benchmark results can create false confidence when task leakage, cherry-picked scenarios, hidden weighting, or unreported baseline changes are present. F38 therefore treats benchmark integrity as a first-class safety property.

The reference implementation fails a run when explicit gaming signals are present, rejects duplicate task identifiers and invalid score ranges, records provenance evidence, and reports regressions separately from aggregate quality.

A passing result is not a certification of model safety. High-impact deployment decisions require domain-specific evaluation, independent review, representative data, and human authorization outside this reference suite.
