from __future__ import annotations

from dataclasses import dataclass

from SKILLS.task_design import design_tasks


@dataclass
class TaskDesignerAgent:
    name: str = "task_designer_agent"

    def run(self, state) -> list[dict]:
        tasks = design_tasks(state.spec)
        state.tasks = tasks
        state.evidence.append({"source": self.name, "claim": "task_set_validated", "count": len(tasks)})
        state.record(self.name, "tasks_designed", {"count": len(tasks)})
        return tasks
