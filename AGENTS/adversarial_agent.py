from __future__ import annotations

from dataclasses import dataclass

from TOOLS.adversarial_tool import adversarial_checks


@dataclass
class AdversarialAgent:
    name: str = "adversarial_agent"

    def run(self, state) -> list[str]:
        findings = adversarial_checks(state.tasks, state.results)
        state.adversarial_findings = findings
        state.record(self.name, "adversarial_checks", {"findings": findings})
        return findings
