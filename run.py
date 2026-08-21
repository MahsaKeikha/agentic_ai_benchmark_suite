from __future__ import annotations

import json

from orchestration.orchestrator import run_system


if __name__ == "__main__":
    result = run_system({
        "tasks": [
            {"id": "reasoning", "observed_score": 0.91, "pass_threshold": 0.7, "difficulty": "hard"},
            {"id": "safety", "observed_score": 0.95, "pass_threshold": 0.8, "difficulty": "hard"},
        ],
        "baseline": {"weighted_score": 0.85, "pass_rate": 1.0},
    })
    print(json.dumps(result, indent=2, sort_keys=True))
