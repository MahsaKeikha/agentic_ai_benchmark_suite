from orchestration.orchestrator import run_system


def test_smoke() -> None:
    result = run_system({"tasks": [{"id": "smoke", "observed_score": 0.9}]})
    assert result["status"] == "pass"
    assert [item["actor"] for item in result["trace"]] == [
        "task_designer_agent",
        "evaluator_agent",
        "adversarial_agent",
        "statistics_agent",
        "reporting_agent",
    ]
