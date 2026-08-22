# Agentic AI Benchmark Suite (F38)

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A multi-agent reference implementation for designing, executing, challenging, analyzing, and reporting AI benchmarks with explicit task contracts, deterministic scoring, adversarial integrity checks, baseline comparison, statistical analysis, reproducibility records, held-out evaluation, and fail-closed reporting gates.

F38 is intended for engineers, researchers, evaluation teams, and students who need a benchmark architecture that makes the benchmark itself inspectable. It treats benchmark construction, scoring, integrity, statistics, and reporting as separate responsibilities rather than collapsing all evaluation logic into one script or one model judge.

It is a benchmark-engineering reference system. Passing a benchmark does not establish universal model quality, statistical significance, production safety, or suitability for every deployment context.

## Why this repository exists

A benchmark can produce a precise-looking number while still being invalid or misleading. Common problems include unclear task definitions, duplicate tasks, data leakage, scoring drift, hidden weighting, weak baselines, benchmark overfitting, insufficient adversarial coverage, and reports that ignore integrity failures.

F38 makes these concerns explicit through a staged multi-agent workflow:

```text
benchmark goal
     |
     v
Task Designer
     |
     v
Evaluator
     |
     v
Adversarial Agent
     |
     v
Statistics Agent
     |
     v
Reporting Agent
     |
     v
fail-closed benchmark result
```

Each stage produces evidence that remains available for later review.

## Agents and responsibilities

| Agent | Responsibility | Core question |
|---|---|---|
| Task Designer | Define and validate benchmark tasks, task identity, difficulty, weights, and expected inputs | Is the benchmark task set well-formed and fit for the claimed purpose? |
| Evaluator | Execute bounded scoring contracts for each task | Was each task scored consistently under the declared rules? |
| Adversarial Agent | Check leakage, duplication, gaming signals, suspicious patterns, and benchmark integrity | Can the benchmark be gamed or invalidated by contamination or design flaws? |
| Statistics Agent | Compute weighted score, pass rate, variance, and baseline regressions | What do the results show under the declared aggregation and comparison rules? |
| Reporting Agent | Apply integrity, regression, pass-rate, and minimum-score gates and synthesize the report | Is the result eligible to be reported as passing? |

The agent boundaries are intentional. For example, the Reporting Agent cannot turn a failed integrity check into a successful benchmark simply because the aggregate score is high.

## Architecture

```text
benchmark configuration + task cases
              |
              v
       Task Designer Agent
              |
              v
        Task Registry
              |
              v
         Evaluator Agent
              |
              v
      deterministic scoring
              |
              v
      Adversarial Agent
              |
              v
       integrity findings
              |
              v
       Statistics Agent
              |
              v
 scorecard + baseline comparison
              |
              v
        Reporting Agent
              |
              v
     fail-closed review gate
              |
              v
      benchmark result package
```

The repository separates agents, skills, tools, benchmarks, configuration, evaluation, CI, and documentation so each layer can be tested independently.

## Skills layer

Reusable benchmark procedures live under `SKILLS/`:

```text
SKILLS/
├── task_design.py
├── rubric_design.py
├── adversarial_testing.py
├── statistical_analysis.py
└── report_synthesis.py
```

### Task design

Defines benchmark units that are specific, reproducible, and comparable. A strong task definition should identify:

- task identifier
- capability being tested
- input contract
- expected output form
- scoring contract
- difficulty or category
- weight
- failure conditions
- source provenance where relevant

Task identity matters because duplicate or near-duplicate cases can distort benchmark results.

### Rubric design

Separates scoring criteria from narrative interpretation. Rubrics should be explicit, bounded, and stable across runs. If weights or thresholds change, the benchmark version should change as well.

### Adversarial testing

Checks the benchmark itself for leakage, contamination, duplication, gaming opportunities, suspicious score concentration, and other integrity concerns.

### Statistical analysis

Supports aggregation, variance analysis, baseline comparison, and regression detection. Statistics should be deterministic wherever practical.

### Report synthesis

Combines the benchmark evidence into a report without overriding failed gates or hiding integrity findings.

## Tools layer

F38 includes benchmark infrastructure under `TOOLS/`:

```text
TOOLS/
├── task_registry.py
├── scoring_tool.py
├── statistics_tool.py
├── adversarial_tool.py
├── scorecard.py
├── run_manifest.py
├── result_store.py
└── review_gate.py
```

### Task registry

Provides a structured inventory of benchmark tasks. Production extensions should version tasks, prevent accidental identity collisions, and retain task provenance.

### Scoring tool

Applies bounded scoring logic. Scores should remain within the declared range and should not depend on hidden post-processing.

### Statistics tool

Computes aggregate measures such as weighted score, pass rate, variance, and baseline regressions.

### Adversarial tool

Records integrity findings such as duplicate identities, suspicious score spread, leakage signals, or benchmark-gaming concerns.

### Scorecard

Provides a structured representation of benchmark outcomes rather than relying only on prose.

### Run manifest

Captures the identity of a benchmark run. A useful run manifest can include benchmark version, task-set version, system-under-test version, configuration, environment, timestamp, and result artifact references.

### Result store

Persists benchmark results and artifacts for later comparison and audit.

### Review gate

Implements the final fail-closed decision logic. A high score does not override an integrity failure.

## End-to-end workflow

A typical F38 run follows this sequence:

1. Define the benchmark objective and capability claims.
2. Load or register benchmark tasks.
3. Validate task identifiers, weights, difficulty labels, and input contracts.
4. Execute each task under the declared scoring contract.
5. Record raw task-level results.
6. Run adversarial integrity checks against the benchmark and result set.
7. Compute deterministic aggregate statistics.
8. Compare results against configured baselines.
9. Check pass rate, weighted score, variance, regressions, and integrity status.
10. Apply the fail-closed review gate.
11. Produce a report that preserves both passing evidence and failure evidence.
12. Store the run manifest and result artifacts for reproducibility.

This workflow makes it easier to distinguish a model failure from a benchmark design failure.

## Quick start

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run static checks and tests:

```bash
ruff check .
pytest -q
```

Run the primary benchmark suite:

```bash
python evals/run_benchmarks.py
```

Run the held-out suite:

```bash
python evals/heldout_suite.py
```

Run examples:

```bash
python examples/minimal.py
python examples/complete.py
```

Run the main entry point:

```bash
python run.py
```

CI executes the complete gate on Python 3.10, 3.11, and 3.12. Python 3.12 publishes the held-out result artifact.

## Benchmark input model

A benchmark task should be explicit enough that another evaluator can reproduce the intended test. Depending on the benchmark, useful fields include:

- unique task ID
- capability category
- prompt or input payload
- context or evidence inputs
- expected behavior
- forbidden behavior
- scoring dimensions
- weight
- pass threshold
- difficulty
- source provenance
- contamination notes
- baseline result

Production benchmark suites should use validated schemas and versioned task definitions.

## Scoring discipline

F38 uses bounded scoring contracts. The reference implementation keeps scores between 0 and 1 and validates the declared task weighting.

Scoring should make the following explicit:

- per-task score definition
- rubric dimensions
- weight normalization
- aggregation rule
- pass threshold
- missing-output handling
- partial-credit behavior
- tie behavior
- baseline comparison rule

If a score depends on a model judge, that judge should itself be versioned and evaluated. Deterministic checks should remain deterministic wherever possible.

## Weighted score and pass rate

Aggregate performance should not be represented by one number alone. F38 tracks both weighted score and pass rate so a system cannot hide many failed tasks behind a few high-weight successes.

A useful report can include:

- weighted score
- unweighted average
- pass rate
- per-category score
- minimum task score
- variance
- baseline delta
- regression count
- integrity status

The benchmark design should explain why each metric matters.

## Baselines and regression detection

A benchmark is more useful when it can detect performance changes over time.

F38 supports baseline comparison so a new system version can be evaluated against a prior reference. Regression logic should specify:

- baseline identity
- comparison metric
- tolerated delta
- per-task or aggregate scope
- whether regressions are blocking

A model that improves aggregate score while severely regressing on a critical category may still fail the release gate depending on the configured policy.

## Adversarial benchmark integrity

The Adversarial Agent evaluates the benchmark itself, not only the model being tested.

Important checks include:

- duplicate task IDs
- near-duplicate cases
- benchmark contamination or leakage
- suspiciously narrow score spread
- tasks that reveal the answer through formatting or metadata
- scoring shortcuts
- prompt-specific gaming
- overly repetitive patterns
- baseline memorization risk

Benchmark integrity failures should remain visible in the final report.

## Leakage and contamination

Leakage can invalidate benchmark claims. Examples include:

- benchmark cases appearing in training data
- public answer keys
- identical examples in development and held-out sets
- task metadata that reveals expected output
- test cases copied from model tuning prompts

F38 does not claim to solve contamination universally, but it treats contamination evidence as a first-class benchmark risk.

## Held-out evaluation

The repository includes a separate held-out suite. The purpose is to avoid treating the visible benchmark cases as the only evidence of system behavior.

A strong held-out process should keep cases isolated from routine implementation work and should record:

- held-out suite version
- expected behavior
- system version
- execution environment
- pass/fail result
- unexpected behavior

The repository's L3 path requires the eight-scenario held-out suite to achieve the expected 8/8 behavior for the promotion evidence described in `docs/L3_AUDIT.md`.

## Reproducibility

A benchmark result is meaningful only when the run can be reconstructed.

Record at minimum:

- benchmark version
- task-set version
- system-under-test version
- evaluator version
- rubric version
- configuration
- environment
- random seed where relevant
- timestamp
- raw task results
- aggregate statistics
- integrity findings
- baseline identity
- final gate result

`TOOLS/run_manifest.py` provides the architectural location for this run identity.

## Failure gates

A benchmark fails when configured integrity or quality requirements are not met. The reference implementation includes fail-closed behavior for conditions such as:

```text
TASK SET INVALID
DUPLICATE TASK IDENTITY
INTEGRITY CHECK FAILED
BASELINE REGRESSION EXCEEDED
PASS RATE BELOW REQUIREMENT
WEIGHTED SCORE BELOW REQUIREMENT
MINIMUM TASK SCORE FAILED
REVIEW REQUIRED
```

Human review should not silently rewrite a failed metric into a passing result. If an override mechanism is added in a production system, the original failure and the authorized exception should both remain visible.

## Reporting

A benchmark report should communicate more than the headline score.

A useful report includes:

- benchmark identity and version
- system-under-test identity
- task-set summary
- scoring rules
- weighted score
- pass rate
- per-category results
- baseline comparison
- regressions
- variance
- integrity findings
- failed cases
- known benchmark limitations
- final gate status

Reports should avoid broad claims that exceed the benchmark's tested scope.

## Observability and result provenance

A production benchmark platform should trace:

- task execution IDs
- evaluator invocations
- tool calls
- raw outputs
- scoring records
- integrity findings
- statistical calculations
- baseline comparisons
- gate decisions
- report versions

This makes it possible to determine whether a surprising benchmark change came from the model, the evaluator, the task set, the configuration, or the scoring logic.

## Evaluation of the benchmark itself

Benchmarks should be evaluated, not merely used.

Useful meta-evaluation questions include:

- Does the benchmark measure the claimed capability?
- Are tasks representative?
- Is task difficulty diverse?
- Are scores stable under irrelevant perturbations?
- Are scoring rules reproducible?
- Do judges agree where judgment is required?
- Can the benchmark detect known regressions?
- Can a weak system game the benchmark?
- Are critical failure modes represented?

Benchmark maintenance should include periodic refreshes and retirement of compromised or obsolete cases.

## CI and engineering quality

The repository includes GitHub Actions under `.github/workflows/ci.yml`.

CI should cover:

- syntax and import integrity
- unit tests
- task-schema checks
- scoring-bound checks
- task-weight validation
- adversarial integrity checks
- regression tests
- gate behavior
- benchmark execution
- held-out execution
- artifact publication

For larger benchmark platforms, add environment pinning, evaluator reproducibility, dependency locking, and artifact checksums.

## L3 Gold Standard evidence

F38 labels the repository **L3 Gold Standard** according to the library's documented promotion criteria.

The promotion path requires:

- all CI jobs green on the exact promotion commit
- the eight-scenario held-out suite at 8/8 expected behavior
- clean-checkout examples
- artifact publication
- benchmark evidence recorded in `benchmarks/RESULTS.md`

See `docs/L3_AUDIT.md` for the repository-specific evidence.

This maturity label describes reproducibility and reviewability of the reference implementation. It does not establish universal model quality or statistical significance beyond the benchmark design.

## Extending F38

Common extensions include:

- domain-specific benchmark packs
- multimodal tasks
- tool-use benchmarks
- agentic workflow benchmarks
- latency and cost metrics
- safety and policy benchmarks
- robustness suites
- multilingual benchmarks
- human preference studies
- pairwise model comparison
- statistical significance testing
- confidence intervals
- bootstrap analysis
- hidden test sets
- benchmark rotation
- contamination detection pipelines
- evaluator ensembles
- leaderboard generation

New benchmark dimensions should remain explicit about task definition, scoring, validity assumptions, and failure conditions.

## Example use cases

F38 can serve as a reference architecture for:

- LLM capability evaluation
- agentic system evaluation
- regression testing across model versions
- prompt-system comparison
- RAG evaluation
- tool-use benchmark design
- internal model-selection studies
- safety evaluation
- academic benchmark engineering
- teaching reproducible AI evaluation

## Repository map

```text
.github/workflows/ci.yml
AGENTS/
├── task_designer_agent.py
├── evaluator_agent.py
├── adversarial_agent.py
├── statistics_agent.py
└── reporting_agent.py
SKILLS/
├── task_design.py
├── rubric_design.py
├── adversarial_testing.py
├── statistical_analysis.py
└── report_synthesis.py
TOOLS/
├── task_registry.py
├── scoring_tool.py
├── statistics_tool.py
├── adversarial_tool.py
├── scorecard.py
├── run_manifest.py
├── result_store.py
└── review_gate.py
benchmarks/
├── cases.json
└── RESULTS.md
config/default.yaml
docs/
├── ARCHITECTURE.md
├── EVALUATION.md
├── SAFETY.md
└── L3_AUDIT.md
evals/
examples/
tests/
run.py
pyproject.toml
CHANGELOG.md
CITATION.cff
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
```

## Design principles

1. Define benchmark claims before designing tasks.
2. Give every task a stable identity and explicit scoring contract.
3. Keep scoring bounded and reproducible.
4. Separate benchmark execution from benchmark integrity review.
5. Compare against versioned baselines.
6. Track pass rate and failure distribution, not only aggregate score.
7. Treat leakage and gaming as first-class benchmark risks.
8. Preserve run manifests and raw results for reproducibility.
9. Fail closed when integrity or configured performance gates fail.
10. Keep benchmark conclusions bounded by the tested task set and threat model.

## Limitations

F38 is a benchmark-engineering reference implementation. Passing bundled scenarios does not establish universal model quality, statistical significance, production safety, or suitability for a particular deployment. Benchmark conclusions remain bounded by the task set, scoring contract, baselines, evaluator quality, configuration, and threat model.

## Documentation

See:

- `docs/ARCHITECTURE.md`
- `docs/EVALUATION.md`
- `docs/SAFETY.md`
- `docs/L3_AUDIT.md`
- `benchmarks/RESULTS.md`

## Citation, contribution, and security

The repository includes:

- `CITATION.cff` for academic and technical citation
- `CONTRIBUTING.md` for contribution guidance
- `SECURITY.md` for vulnerability reporting and benchmark-integrity concerns
- `CHANGELOG.md` for version history

## License

MIT. See `LICENSE`.

## Responsible use

Use F38 as a benchmark-engineering and multi-agent evaluation reference. Validate that the task set, scoring contract, evaluator behavior, baselines, and threat model actually support the claims you intend to make. Do not treat a benchmark score as evidence for capabilities, safety, or deployment readiness that the benchmark did not test.