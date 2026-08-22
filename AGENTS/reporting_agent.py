from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ReportingAgent:
    name: str = "reporting_agent"

    def run(self, state) -> dict:
        integrity_ok = not state.adversarial_findings
        regression_free = not state.regressions
        required_pass_rate = float(state.spec.get("required_pass_rate", 1.0))
        minimum_weighted_score = float(state.spec.get("minimum_weighted_score", 0.0))
        quality_ok = (
            state.metrics.get("pass_rate", 0.0) >= required_pass_rate
            and state.metrics.get("weighted_score", 0.0) >= minimum_weighted_score
        )
        report = {
            "run_id": state.run_id,
            "metrics": state.metrics,
            "integrity_ok": integrity_ok,
            "regression_free": regression_free,
            "quality_ok": quality_ok,
            "required_pass_rate": required_pass_rate,
            "minimum_weighted_score": minimum_weighted_score,
            "adversarial_findings": list(state.adversarial_findings),
            "regressions": list(state.regressions),
            "evidence_count": len(state.evidence),
            "status": "pass" if integrity_ok and regression_free and quality_ok else "fail",
        }
        state.record(self.name, "report_generated", report)
        return report
