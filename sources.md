# Radar Sources and Queries

Use this file to keep daily sciML / Engineering AI collection consistent.

The goal is not maximum coverage. The goal is high-signal items that can influence VA's research judgment, experiments, writing, or engineering workflow.

## Primary sources

- arXiv
- Papers with Code
- GitHub search / trending
- Semantic Scholar, when available
- Hugging Face papers/models, when relevant
- University and lab blogs
- Major conference proceedings
- Tool repositories for CAD, CFD, OpenFOAM, MCP, agents, and scientific visualization

## arXiv query set

Rotate through these rather than using one broad query every day.

```text
"CFD" "machine learning"
"fluid" "neural operator"
"turbulence" "deep learning"
"surrogate model" "fluid"
"thermal" "digital twin"
"sparse sensors" "flow reconstruction"
"spectral" "neural operator" "turbulence"
"OpenFOAM" "machine learning"
"CAD" "B-Rep" "language model"
"geometry" "surrogate" "CFD"
"MCP" "CAD"
"physics-informed" "inverse" "fluid"
```

## GitHub query set

```text
CFD neural operator
OpenFOAM AI
CAD MCP
BRep language model
fluid surrogate model
scientific machine learning turbulence
physics informed neural operator fluid
sparse sensor flow reconstruction
digital twin surrogate CFD
```

## Positive selection signals

Prefer items with at least one of these:

- Real CFD, thermal, CAD, or engineering workflow relevance.
- Code, dataset, benchmark, or reproducible artifact.
- Validation beyond average field RMSE.
- Geometry-family, boundary-condition, or sensor-distribution shift.
- Solver-in-the-loop, OpenFOAM/Fluent/CAD integration, or deployment evidence.
- Clear connection to VA's possible experiments or writing.

## Downgrade signals

Downgrade or reject items with:

- Pure AI hype without engineering validation.
- Toy PDE only, unless it introduces a reusable diagnostic.
- No clear artifact and no clear technical novelty.
- Generic LLM-agent demo without CAD/CFD/engineering operation surface.
- Only qualitative images with no metrics or reproducibility path.

## Action labels

Use one action label per item:

- `Read` — worth reading carefully.
- `Save` — useful reference but not urgent.
- `Test` — code/tool/benchmark should be tried.
- `Cite` — likely useful for writing/proposal/thesis framing.
- `Watch` — promising but immature.
- `Ignore` — seen and intentionally skipped.
