from __future__ import annotations

import pytest

from orchestration.orchestrator import run_system


def test_clean_benchmark_passes() -> None:
    result = run_system({
        "tasks": [
            {"id": "a", "observed_score": 0.9},
            {"id": "b", "observed_score": 0.8},
        ],
        "baseline": {"weighted_score": 0.8, "pass_rate": 1.0},
    })
    assert result["status"] == "pass"
    assert result["metrics"]["weighted_score"] == 0.85
    assert len(result["trace"]) == 5
    assert len(result["evidence"]) == 3


def test_regression_fails() -> None:
    result = run_system({
        "tasks": [{"id": "a", "observed_score": 0.6}],
        "baseline": {"weighted_score": 0.9, "pass_rate": 1.0},
        "regression_tolerance": 0.02,
    })
    assert result["status"] == "fail"
    assert "weighted_score" in result["regressions"]


def test_gaming_signal_fails_integrity() -> None:
    result = run_system({"tasks": [{"id": "a", "observed_score": 0.9, "gaming_signal": True}]})
    assert result["status"] == "fail"
    assert "benchmark_gaming_signal" in result["adversarial_findings"]


def test_duplicate_task_ids_are_rejected() -> None:
    with pytest.raises(ValueError, match="duplicate task id"):
        run_system({"tasks": [{"id": "x", "observed_score": 0.8}, {"id": "x", "observed_score": 0.9}]})


def test_invalid_score_is_rejected() -> None:
    with pytest.raises(ValueError, match="between 0 and 1"):
        run_system({"tasks": [{"id": "x", "observed_score": 1.2}]})


def test_empty_task_set_is_rejected() -> None:
    with pytest.raises(ValueError, match="at least one task"):
        run_system({"tasks": []})
