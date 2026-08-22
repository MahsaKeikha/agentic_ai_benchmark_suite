import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import run_system


def spec(tasks, **updates):
    value = {"tasks": tasks, "baseline": {}, "regression_tolerance": 0.05}
    value.update(updates)
    return value


SCENARIOS = [
    ("healthy_scores", spec([{"id": "a", "observed_score": 0.9, "pass_threshold": 0.7, "weight": 1.0}]), "pass"),
    ("below_threshold", spec([{"id": "a", "observed_score": 0.4, "pass_threshold": 0.7, "weight": 1.0}]), "fail"),
    ("weighted_mix", spec([{"id": "a", "observed_score": 0.9, "pass_threshold": 0.6, "weight": 2.0}, {"id": "b", "observed_score": 0.7, "pass_threshold": 0.6, "weight": 1.0}]), "pass"),
    ("regression", spec([{"id": "a", "observed_score": 0.7, "pass_threshold": 0.5}], baseline={"weighted_score": 0.9}, regression_tolerance=0.05), "fail"),
    ("gaming_signal", spec([{"id": "a", "observed_score": 1.0, "pass_threshold": 0.5, "gaming_signal": True}]), "fail"),
    ("leakage_signal", spec([{"id": "a", "observed_score": 0.9, "pass_threshold": 0.5, "expose_reference": True, "answer": "hidden"}]), "fail"),
    ("difficulty_weighting", spec([{"id": "a", "observed_score": 0.8, "pass_threshold": 0.7, "difficulty": "hard", "weight": 2.0}]), "pass"),
    ("two_task_failure", spec([{"id": "a", "observed_score": 0.9, "pass_threshold": 0.7}, {"id": "b", "observed_score": 0.2, "pass_threshold": 0.7}]), "fail"),
]


def main():
    rows = []
    for name, payload, expected in SCENARIOS:
        actual = run_system(payload)["status"]
        rows.append({"scenario": name, "expected": expected, "actual": actual, "passed": actual == expected})
    passed = sum(row["passed"] for row in rows)
    result = {"system_id": "F38", "version": "1.0.0", "scenario_count": len(rows), "passed": passed, "pass_rate": passed / len(rows), "scenarios": rows}
    Path("benchmarks").mkdir(exist_ok=True)
    Path("benchmarks/heldout_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["pass_rate"] != 1.0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
