from __future__ import annotations

from dataclasses import dataclass

from TOOLS.scoring_tool import evaluate_task


@dataclass
class EvaluatorAgent:
    name: str = "evaluator_agent"

    def run(self, state) -> list[dict]:
        results = [evaluate_task(task) for task in state.tasks]
        state.results = results
        state.evidence.extend({"source": self.name, "task_id": item["task_id"], "score": item["score"]} for item in results)
        state.record(self.name, "tasks_evaluated", {"count": len(results)})
        return results
