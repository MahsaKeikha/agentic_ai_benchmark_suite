from __future__ import annotations

import math


def aggregate(results: list[dict]) -> dict[str, float]:
    if not results:
        return {"weighted_score": 0.0, "pass_rate": 0.0, "stddev": 0.0}
    weights = [float(item["weight"]) for item in results]
    scores = [float(item["score"]) for item in results]
    total_weight = sum(weights)
    mean = sum(score * weight for score, weight in zip(scores, weights, strict=True)) / total_weight
    variance = sum(weight * (score - mean) ** 2 for score, weight in zip(scores, weights, strict=True)) / total_weight
    return {
        "weighted_score": round(mean, 6),
        "pass_rate": round(sum(1 for item in results if item["passed"]) / len(results), 6),
        "stddev": round(math.sqrt(variance), 6),
    }


def detect_regressions(metrics: dict[str, float], baseline: dict[str, float], tolerance: float) -> list[str]:
    regressions: list[str] = []
    for metric in ("weighted_score", "pass_rate"):
        if metric in baseline and metrics.get(metric, 0.0) < float(baseline[metric]) - tolerance:
            regressions.append(metric)
    return regressions
