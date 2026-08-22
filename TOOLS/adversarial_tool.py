from __future__ import annotations


def adversarial_checks(tasks: list[dict], results: list[dict]) -> list[str]:
    findings: list[str] = []
    ids = [task["id"] for task in tasks]
    if len(ids) != len(set(ids)):
        findings.append("duplicate_task_ids")
    if any("answer" in task or "gold" in task for task in tasks if task.get("expose_reference", False)):
        findings.append("reference_leakage")
    if results and max(item["score"] for item in results) - min(item["score"] for item in results) > 0.8:
        findings.append("extreme_score_spread")
    if any(task.get("gaming_signal") for task in tasks):
        findings.append("benchmark_gaming_signal")
    return findings
