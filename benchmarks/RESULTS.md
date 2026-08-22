# F38 Held-out Benchmark Results

**Version:** 1.0.0  
**Verified code head:** `1539e0be36ece4ef7cad86886e0a88385d978693`  
**CI run:** `32540520377`  
**Artifact:** `f38-heldout-results`  
**Artifact digest:** `sha256:683132a2fd5d083f637905d75c10037fd18f559f6ddea669c3b8a89899d96153`

## Result

- Scenario count: 8
- Passed: 8
- Pass rate: 1.0
- Python 3.10: PASS
- Python 3.11: PASS
- Python 3.12: PASS

## Held-out scenarios

| Scenario | Expected | Result |
|---|---|---|
| healthy_scores | pass | PASS |
| below_threshold | fail | PASS |
| weighted_mix | pass | PASS |
| regression | fail | PASS |
| gaming_signal | fail | PASS |
| leakage_signal | fail | PASS |
| difficulty_weighting | pass | PASS |
| two_task_failure | fail | PASS |

These results validate the documented deterministic benchmark-engineering behaviors for this suite. They do not establish universal model quality, production safety, or statistical significance beyond the declared benchmark contract.
