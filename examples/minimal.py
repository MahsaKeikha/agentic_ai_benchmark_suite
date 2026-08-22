import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import run_system  # noqa: E402

result = run_system({"tasks": [{"id": "quality", "observed_score": 0.9, "pass_threshold": 0.7}]})
assert result["status"] == "pass"
print(result["status"], result["metrics"])
