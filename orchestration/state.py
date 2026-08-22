from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class BenchmarkState:
    spec: dict[str, Any]
    run_id: str = field(default_factory=lambda: str(uuid4()))
    tasks: list[dict[str, Any]] = field(default_factory=list)
    results: list[dict[str, Any]] = field(default_factory=list)
    adversarial_findings: list[str] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)
    regressions: list[str] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    trace: list[dict[str, Any]] = field(default_factory=list)

    def record(self, actor: str, event: str, artifact: Any = None) -> None:
        self.trace.append({"step": len(self.trace) + 1, "actor": actor, "event": event, "artifact": artifact})
