from __future__ import annotations

from AGENTS.adversarial_agent import AdversarialAgent
from AGENTS.evaluator_agent import EvaluatorAgent
from AGENTS.reporting_agent import ReportingAgent
from AGENTS.statistics_agent import StatisticsAgent
from AGENTS.task_designer_agent import TaskDesignerAgent
from orchestration.state import BenchmarkState

SYSTEM_ID = "F38"
SYSTEM_VERSION = "1.0.0"


def run_system(spec: dict) -> dict:
    state = BenchmarkState(spec=dict(spec))
    TaskDesignerAgent().run(state)
    EvaluatorAgent().run(state)
    AdversarialAgent().run(state)
    StatisticsAgent().run(state)
    report = ReportingAgent().run(state)
    return {
        "system_id": SYSTEM_ID,
        "version": SYSTEM_VERSION,
        "maturity": "L3 Gold Standard",
        "run_id": state.run_id,
        "tasks": state.tasks,
        "results": state.results,
        "metrics": state.metrics,
        "adversarial_findings": state.adversarial_findings,
        "regressions": state.regressions,
        "evidence": state.evidence,
        "trace": state.trace,
        "report": report,
        "status": report["status"],
    }
