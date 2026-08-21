from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ReportingAgent:
    name: str = "reporting_agent"

    def run(self, state) -> dict:
        integrity_ok = not state.adversarial_findings
        regression_free = not state.regressions
        report = {
            "run_id": state.run_id,
            "metrics": state.metrics,
            "integrity_ok": integrity_ok,
            "regression_free": regression_free,
            "adversarial_findings": list(state.adversarial_findings),
            "regressions": list(state.regressions),
            "evidence_count": len(state.evidence),
            "status": "pass" if integrity_ok and regression_free else "fail",
        }
        state.record(self.name, "report_generated", report)
        return report
