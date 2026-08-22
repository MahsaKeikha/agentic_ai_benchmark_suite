from __future__ import annotations

from dataclasses import dataclass

from TOOLS.statistics_tool import aggregate, detect_regressions


@dataclass
class StatisticsAgent:
    name: str = "statistics_agent"

    def run(self, state) -> dict[str, float]:
        metrics = aggregate(state.results)
        tolerance = float(state.spec.get("regression_tolerance", 0.02))
        baseline = dict(state.spec.get("baseline", {}))
        state.metrics = metrics
        state.regressions = detect_regressions(metrics, baseline, tolerance)
        state.record(self.name, "statistics_aggregated", {"metrics": metrics, "regressions": state.regressions})
        return metrics
