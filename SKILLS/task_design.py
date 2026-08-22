from __future__ import annotations


def design_tasks(spec: dict) -> list[dict]:
    seed_tasks = list(spec.get("tasks", []))
    if not seed_tasks:
        raise ValueError("benchmark spec requires at least one task")
    seen: set[str] = set()
    tasks: list[dict] = []
    for index, item in enumerate(seed_tasks, start=1):
        task = dict(item)
        task_id = str(task.get("id") or f"task-{index}")
        if task_id in seen:
            raise ValueError(f"duplicate task id: {task_id}")
        seen.add(task_id)
        task["id"] = task_id
        task["difficulty"] = str(task.get("difficulty", "medium"))
        task["weight"] = float(task.get("weight", 1.0))
        if task["weight"] <= 0:
            raise ValueError("task weight must be positive")
        tasks.append(task)
    return tasks
