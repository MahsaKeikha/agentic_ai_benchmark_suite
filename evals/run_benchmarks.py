from __future__ import annotations

from orchestration.orchestrator import run_system

SCENARIOS = [
    {
        "name": "stable_high_performance",
        "spec": {
            "tasks": [{"id": "quality", "observed_score": 0.92}, {"id": "safety", "observed_score": 0.94}],
            "baseline": {"weighted_score": 0.85, "pass_rate": 1.0},
        },
        "expected": "pass",
    },
    {
        "name": "regression_detected",
        "spec": {
            "tasks": [{"id": "quality", "observed_score": 0.55}],
            "baseline": {"weighted_score": 0.9, "pass_rate": 1.0},
        },
        "expected": "fail",
    },
    {
        "name": "gaming_detected",
        "spec": {"tasks": [{"id": "quality", "observed_score": 0.95, "gaming_signal": True}]},
        "expected": "fail",
    },
]


def main() -> None:
    failures: list[str] = []
    for scenario in SCENARIOS:
        result = run_system(scenario["spec"])
        if result["status"] != scenario["expected"]:
            failures.append(scenario["name"])
    if failures:
        raise SystemExit(f"benchmark scenario failures: {', '.join(failures)}")
    print(f"{len(SCENARIOS)} benchmark scenarios passed")


if __name__ == "__main__":
    main()
