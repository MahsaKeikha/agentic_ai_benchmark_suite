from __future__ import annotations


def evaluate_task(task: dict) -> dict:
    score = float(task.get("observed_score", task.get("score", 0.0)))
    if not 0.0 <= score <= 1.0:
        raise ValueError(f"score for {task['id']} must be between 0 and 1")
    passed = score >= float(task.get("pass_threshold", 0.7))
    return {
        "task_id": task["id"],
        "score": score,
        "passed": passed,
        "difficulty": task.get("difficulty", "medium"),
        "weight": float(task.get("weight", 1.0)),
    }
