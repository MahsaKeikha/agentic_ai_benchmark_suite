import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import run_system  # noqa: E402

spec = {
    "tasks": [
        {"id": "quality", "observed_score": 0.91, "pass_threshold": 0.75, "difficulty": "hard", "weight": 2.0},
        {"id": "safety", "observed_score": 0.95, "pass_threshold": 0.8, "difficulty": "hard", "weight": 2.0},
        {"id": "robustness", "observed_score": 0.84, "pass_threshold": 0.75, "difficulty": "medium", "weight": 1.0},
    ],
    "baseline": {"weighted_score": 0.82, "pass_rate": 1.0},
    "regression_tolerance": 0.05,
    "required_pass_rate": 1.0,
    "minimum_weighted_score": 0.8,
}
result = run_system(spec)
assert result["status"] == "pass"
assert result["report"]["integrity_ok"] is True
assert result["report"]["quality_ok"] is True
print(result["status"], result["metrics"])
