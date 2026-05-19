# CAD, Geometry & AI-assisted Design

## CADAM

- Link: https://github.com/Adam-CAD/CADAM
- Live app: https://adam.new/cadam
- Type: Open-source text-to-CAD web application
- Why it matters:
  - Turns natural-language prompts and image references into OpenSCAD-based 3D models in the browser.
  - Supports parametric controls and exports to `.STL`, `.SCAD`, and `.DXF`, making it relevant to rapid CAD/CFD geometry prototyping.
  - Built around React/TypeScript, OpenSCAD WASM, Supabase, and Claude API; useful reference for text-to-CAD product architecture.
- Caveat:
  - Generated geometry still needs engineering validation before meshing, simulation, or fabrication.

## ForgeCAD

- Link: https://github.com/KoStard/ForgeCAD
- Type: AI-assisted parametric CAD generation
- Summary:
  - Generates CAD that can be adjusted by parameters.
  - Usable with CLI coding agents such as Claude Code or Codex.
  - Early tests looked plausible but still had errors.
- Why it matters:
  - CAD/geometry generation is a bottleneck in CFD/CAE workflows.
  - Agent-assisted parametric CAD could speed up early design iteration.
  - Needs robust validation for dimensions, constraints, tolerances, and manufacturability.

## FreeCAD + Python + Claude Code workflow

- Link: https://www.linkedin.com/posts/roman-likhachev-23a544174_part-1-using-claude-code-for-3d-cad-design-activity-7436038784623869952-7EVs?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD5oIrEBMTn8gvGtlY2eLkVvjVsMFaxHEgc
- Type: LLM-assisted CAD design workflow
- Summary:
  - Claude Code writes Python geometry.
  - FreeCAD watches/renders the script in real time.
  - User iterates through conversation and exports printable parts.
- Why it matters:
  - Similar workflow could be adapted for CFD geometry prototyping.
  - Still requires human engineering judgment about dimensions, tolerances, and part fit.

## Zero-to-CAD

- Link: https://arxiv.org/abs/2604.24479
- Dataset: https://huggingface.co/datasets/ADSKAILab/Zero-To-CAD-1m
- Type: Agentic synthesis of interpretable CAD programs
- Why it matters:
  - Focuses on CAD construction history / parametric program synthesis rather than only mesh or B-Rep outputs.
  - The 1M-scale Hugging Face dataset includes CadQuery programs, operation traces, multi-view renders, STL, and STEP exports for training/evaluating text/image-to-CAD models.
  - Relevant to CFD/CAE because reusable design intent and parameters matter for geometry sweeps and optimization.
  - Worth comparing with FreeCAD/Python agent workflows for controllability and downstream meshing robustness.

## FeatureFox

- Link: https://arxiv.org/abs/2604.26770
- Type: Panoptic graph segmentation for machining feature recognition in B-Rep CAD models
- Why it matters:
  - Automatic feature recognition is a practical bottleneck for CAD/CAM and manufacturability-aware automation.
  - Sample-efficient B-Rep feature recognition could support design-rule checks before simulation or fabrication.
  - Useful signal for graph-based CAD representations beyond generic 3D shape learning.

## LLM symbolic reflection for mechanical linkage design

- Link: https://arxiv.org/abs/2604.27962
- Type: LLM-assisted mechanical design optimization
- Why it matters:
  - Combines language-model topology exploration with numerical optimization for linkage parameters.
  - A concrete engineering-design example of agentic search plus deterministic optimization.
  - Pattern may transfer to CAD automation loops: symbolic design proposal → solver/optimizer → critique/refine.

## Design Structure Matrix modularization with LLMs

- Link: https://arxiv.org/abs/2604.28018
- Type: LLM-assisted engineering design modularization
- Why it matters:
  - Uses engineering context in DSM partitioning instead of treating modularization as only graph optimization.
  - Relevant to complex product/system architecture, CAD assembly planning, and design-automation workflows.
  - Useful weekly-synthesis candidate for “LLMs as context-aware engineering-design heuristics.”


## mcp-freecad

- Link: https://github.com/seansackowitz/mcp-freecad
- Type: MCP server for FreeCAD parametric modeling
- Why it matters:
  - Exposes many small FreeCAD operations as agent-callable MCP tools, with screenshots only when explicitly requested to keep token cost low.
  - Good direction for CAD automation: stable parametric/document/object operations instead of brittle GUI control.
  - Worth testing against CFD geometry workflows that need reproducible STEP/STL export and parameter sweeps.

## freecad-mcp

- Link: https://github.com/blwfish/freecad-mcp
- Type: MCP server for AI-assisted FreeCAD modeling
- Why it matters:
  - Smaller FreeCAD MCP bridge with tool coverage for AI-assisted 3D CAD modeling.
  - Useful comparison point for deciding what a minimal CAD-agent interface should expose.
  - Treat as early-stage until validation on real parametric parts and downstream meshing is checked.

## TOOLCAD

- Link: https://arxiv.org/abs/2604.07960
- Type: Tool-using LLMs for text-to-CAD generation
- Why it matters:
  - Treats CAD generation as long-horizon tool use with reinforcement learning rather than one-shot text-to-shape prediction.
  - Relevant to agentic CAD automation where valid modeling actions, constraints, and edit history matter.
  - Good comparison point for FreeCAD/CadQuery/OpenSCAD agent workflows.
- Possible use: Use as a paper anchor when evaluating whether CAD agents should learn tool-use policies or rely on scripted prompting.
- Maturity: paper-only
- Priority: High

## Pointer-CAD

- Link: https://arxiv.org/abs/2603.04337
- Type: B-Rep and command-sequence CAD generation
- Why it matters:
  - Unifies B-Rep geometry with command sequences using pointer-based selection of edges and faces.
  - Accepted by CVPR 2026, making it a visible signal in CAD representation learning.
  - Useful for downstream CAE because editable B-Rep/feature history is more valuable than mesh-only geometry.
- Possible use: Track for parametric CAD reconstruction and future CAD-to-mesh automation pipelines.
- Maturity: paper-only
- Priority: High

## Text2CAD

- Link: https://github.com/Toommo2/Text2CAD
- Type: Agent-driven natural-language to CAD workflow
- Why it matters:
  - Attempts to turn natural language into deterministic and validated CAD artifacts rather than only visual 3D previews.
  - Relevant to CFD/CAE automation because downstream meshing and simulation require reproducible geometry files and validation hooks.
  - Early-stage, but the emphasis on validation is the right direction for engineering use.
- Curation note: Evaluate generated geometry quality and export formats before using in a real CAD-to-CFD loop.

## CADFS

- Link: https://arxiv.org/abs/2605.01925
- Project: https://voyleg.github.io/cadfs/
- Type: FeatureScript CAD program dataset and framework for VLM/LLM CAD generation
- Why it matters:
  - Reconstructs 450k real-world CAD models as clean executable FeatureScript programs spanning a wider operation set than sketch-extrude-only datasets.
  - Emphasizes editable design history, representation-aligned descriptions, and multimodal annotations rather than mesh-only generation.
  - Strongly relevant to CAD-to-CAE automation because parametric construction history is what enables sweeps, constraints, and downstream meshing checks.
- Possible use: Evaluate as a dataset/model reference for executable CAD reconstruction and text/image-conditioned parametric CAD.
- Maturity: paper + dataset/project page
- Priority: High

## Cascaded Discrete Diffusion for CAD generation

- Link: https://arxiv.org/abs/2605.05031
- Type: Discrete diffusion model for CAD command and parameter generation
- Why it matters:
  - Models CAD as heterogeneous discrete commands and parameters instead of perturbing CAD tokens in a generic continuous embedding space.
  - Cascades command diffusion and parameter diffusion, which better matches the validity constraints of executable CAD sequences.
  - Useful signal for CAD-to-CAE workflows because valid construction history matters more than visually plausible shape samples.
- Possible use: Compare against autoregressive CAD command generation and CADFS/Zero-to-CAD style executable-program approaches.
- Maturity: paper-only
- Priority: High

## Agent-Aided Design for Dynamic CAD Models / AADvark

- Link: https://arxiv.org/abs/2604.15184
- Type: Agentic CAD system for dynamic assemblies
- Why it matters:
  - Extends agent-aided design beyond static objects toward assemblies with moving parts and degrees of freedom.
  - Highlights a practical bottleneck for industrial CAD agents: reasoning about dynamic part interactions, not only generating geometry.
  - Relevant to engineering workflows where mechanism design, constraints, and simulation readiness matter.
- Possible use: Use as a paper anchor for evaluating CAD agents on assemblies such as hinges, linkages, pistons, valves, and other moving components.
- Maturity: paper/prototype
- Priority: Medium

## Tessa Labs freecad-mcp

- Link: https://github.com/tessalabs-space/freecad-mcp
- Type: Engineering-focused MCP server for FreeCAD
- Why it matters:
  - Exposes FreeCAD operations for parametric CAD generation, design sweeps, drawings, rendering, defeaturing, meshing/export, and CAE handoff.
  - The inclusion of boundary-condition tagging and simulation-prep operations is especially relevant to CAD-to-CFD/thermal automation.
  - Good reference for designing an agent-readable CAD interface that preserves engineering metadata instead of only producing geometry.
- Possible use: Evaluate against mcp-freecad/freecad-mcp alternatives on a small parametric part → mesh/export → OpenFOAM or thermal handoff workflow.
- Maturity: early open-source MCP server
- Priority: High

## SolidWorks CAD Automation Pipeline

- Link: https://github.com/wikijerry/CAD-Automation-pipeline
- Type: Agentic SolidWorks 3D-to-2D drawing automation prototype
- Why it matters:
  - Automates SolidWorks 3D → 2D drawing generation with view selection, auto-dimensioning, validation, Python COM API hooks, and LLM integration.
  - Relevant to engineering automation beyond text-to-CAD: production workflows often need drawings, dimensions, checks, and revision artifacts.
  - Useful as a lightweight reference for how CAD agents might operate through deterministic CAD APIs rather than screenshots or free-form GUI control.
- Curation note: Very early and low-star; treat as an implementation signal to inspect, not as a dependable lab tool.
- Maturity: early prototype
- Priority: Medium

## Generalizable graph learning for 3D engineering AI

- Link: https://arxiv.org/abs/2604.07781
- Type: Physics-aware graph learning workflow for CAD/CAE/CFD assets
- Why it matters:
  - Converts heterogeneous 3D engineering assets such as FE models, CAD geometry, BiW representations, and CFD meshes into reusable graph representations.
  - Demonstrates both CAE vibration mode-shape classification and CFD field prediction, making it relevant beyond single-task toy geometry learning.
  - The explainable workflow framing is useful for engineering teams that need traceable model behavior across design stages.
- Possible use: Use as a reference when designing mesh/CAD graph features for CFD surrogate or CAE classification tasks.
- Maturity: paper-only
- Priority: High

## CADTestBench / CADTests

- Link: https://arxiv.org/abs/2605.07807
- Code: https://github.com/dimitrismallis/CADTestBench
- Dataset: https://huggingface.co/datasets/dimitrismallis/CADTestBench
- Type: Test-based benchmark for text-to-CAD evaluation
- Why it matters:
  - Evaluates generated CAD with executable CadQuery tests that verify geometric and topological prompt requirements directly.
  - Better matches engineering use than Chamfer/IoU-only scoring because multiple CAD models can satisfy the same prompt while still needing exact constraints.
  - The mutation-analysis refinement loop is a strong pattern for CAD agents: generate geometry, run deterministic tests, repair failures.
- Possible use: Adapt the CADTests idea to VA's CAD-to-CAE workflow: prompt/spec → executable CAD → test suite for dimensions, named features, wall thickness, exports, and meshability.
- Maturity: paper + code + dataset
- Priority: High

## build123d-mcp

- Link: https://github.com/pzfreo/build123d-mcp
- Type: MCP server for build123d programmatic CAD
- Why it matters:
  - Closes the feedback loop for AI-written build123d scripts by exposing execution, rendering, measurement, clearance, cross-sections, imports/exports, snapshots, and shape comparison as tools.
  - Particularly relevant for engineering workflows because it checks geometry incrementally instead of asking an agent to write a complete blind CAD script.
  - STEP/STL/DXF/SVG export and persistent session state make it a practical candidate for parametric geometry sweeps before meshing or simulation.
- Possible use: Test on a small bracket/duct/heat-sink part and require the agent to report volume, bounding box, cross-sections, clearance, and exported STEP/STL artifacts.
- Maturity: active early tool / PyPI package
- Priority: High

## BenchCAD

- Link: https://arxiv.org/abs/2605.10865
- Type: Industrial programmatic CAD benchmark
- Why it matters:
  - Provides 17,900 execution-verified CadQuery programs across 106 industrial part families, including gears, springs, drills, and other reusable engineering designs.
  - Evaluates visual QA, code QA, image-to-code generation, and instruction-guided code editing, so CAD automation is measured beyond visual similarity.
  - Highlights that current multimodal models often recover coarse outer shape but fail at faithful parametric operations such as sweeps, lofts, and twist-extrudes.
- Possible use: Use as a benchmark reference for VA's executable-CAD and CAD-to-CAE validation experiments alongside CADTests/CADTestBench.
- Maturity: paper / benchmark
- Priority: High

## CAD-feature enhanced ML for sheet-metal bending effort estimation

- Link: https://arxiv.org/abs/2605.12266
- Type: CAD graph / manufacturability ML paper
- Why it matters:
  - Shows that B-rep geometry alone can miss process-specific meaning such as surface role and bend intent.
  - Directly supports a CAD-to-CAE automation principle: downstream models need engineering semantics, not only raw topology and coordinates.
  - Useful reference for adding named faces, manufacturing roles, boundary-condition intent, and feature metadata to agent-generated CAD.
- Possible use: Design a small schema for CAD semantic tags that survives export into meshing/CFD setup.
- Maturity: paper-only
- Priority: High

## Nonlinear Parametric Model Embedding for Shape Design

- Link: https://arxiv.org/abs/2605.11759
- Type: Dimensionality reduction for parametric shape design
- Why it matters:
  - Extends parametric model embedding beyond linear reductions while preserving backmapping to the original design parameters.
  - Relevant to simulation-based shape optimization where high-dimensional CAD parameters make surrogate modeling and design-space exploration brittle.
  - Useful framing for blade/duct/heat-exchanger design loops: reduce design variables without losing a path back to executable geometry.
- Maturity: paper-only
- Priority: Medium

## PINN-based 2D turbine blade design screening

- Link: https://arxiv.org/abs/2605.07131
- Type: PINN surrogate for aerodynamic blade design
- Why it matters:
  - Targets rapid preliminary screening of turbine blade geometries across operating conditions.
  - Connects PINN-style SciML to a concrete thermal-fluid design problem instead of a generic PDE benchmark.
  - Useful as an application anchor for Carnot battery / turbomachinery / energy-system design loops, with validation caveats for off-design and complex geometries.
- Maturity: paper-only
- Priority: Medium

## CADCLAW

- Link: https://github.com/sunnyday-technologies/CADCLAW
- Type: STEP assembly validation suite / MCP-exposed CAD checks
- Why it matters:
  - Runs automated assembly checks for inventory, interference, adjacency, dimensional constraints, orientation, floating parts, color/material metadata, tolerance stacking, BOM-vs-CAD drift, disassembly, and rendering.
  - Fits the missing validation layer between AI-generated CAD and downstream CAE: geometry should produce evidence before meshing or simulation.
  - MCP exposure makes it relevant to agentic CAD workflows where assistants need callable validation tools instead of visual inspection alone.
- Possible use: Use after CadQuery/build123d/FreeCAD generation to gate STEP artifacts before OpenFOAM meshing or thermal simulation.
- Maturity: early open-source tool with DOI / validate before lab adoption
- Priority: High

## KiCAD MCP Server

- Link: https://github.com/mixelpixx/KiCAD-MCP-Server
- Type: MCP server for PCB CAD / EDA automation
- Why it matters:
  - Lets LLM assistants interact directly with KiCAD projects, moving engineering agents from advisory chat toward real design-artifact inspection and modification.
  - Although EDA rather than CFD, it is a strong signal for agent-callable engineering software surfaces and artifact-aware workflows.
  - Useful precedent for CAD/CAE MCP design: expose stable operations, project state, and validation hooks instead of relying on screenshots alone.
- Curation note: Evaluate on a sandbox KiCAD project before trusting edits to real designs.
- Maturity: active open-source tool
- Priority: Medium

## neka-nat/freecad-mcp

- Link: https://github.com/neka-nat/freecad-mcp
- Type: MCP server for FreeCAD automation
- Why it matters:
  - Exposes FreeCAD as an agent-callable parametric CAD environment, making it relevant to reproducible geometry generation and CAD-to-CAE workflows.
  - More visible than many small FreeCAD MCP experiments, so it is a useful candidate for comparison testing.
  - Could support VA-style duct, heat-sink, bracket, and parametric sweep workflows if paired with export and meshability checks.
- Possible use: Sandbox a simple heat-sink/duct generation task and require named faces, bounding box, STEP/STL export, and mesh pre-check evidence.
- Maturity: active early tool
- Priority: High

## multiCAD-mcp

- Link: https://github.com/AnCode666/multiCAD-mcp
- Type: Multi-CAD MCP bridge
- Why it matters:
  - Attempts to expose multiple CAD tools through a common MCP-style interface for AI assistants.
  - Important ecosystem signal: CAD-agent infrastructure is fragmenting across vendor/tool bridges, making common artifact contracts more important.
  - Useful comparison point for whether VA's workflows should target one robust open CAD API first or design a tool-agnostic validation layer.
- Curation note: Validate supported CAD tools, operation coverage, and export reliability before relying on it.
- Maturity: early open-source tool
- Priority: Medium

## FreeCAD AI workbench

- Link: https://github.com/ghbalf/freecad-ai
- Type: AI assistant workbench for FreeCAD
- Why it matters:
  - Provides an in-FreeCAD natural-language assistant for generating and modifying 3D models.
  - Useful UX reference for AI-assisted parametric CAD inside an engineering application rather than only through external chat.
  - Needs deterministic validation before generated models are used for meshing, manufacturing, or simulation.
- Possible use: Compare with MCP-based FreeCAD workflows: embedded assistant UX vs external agent with explicit tools and evidence logs.
- Maturity: active early tool
- Priority: Medium

## cadgate

- Link: https://github.com/vericontext/cadgate
- Type: CAD-as-code validation CLI / GitHub Action
- Why it matters:
  - Validates AI-generated CadQuery/build123d pull requests with geometric metric diff, minimum wall thickness, DFM rules, and six-view rendered previews.
  - Directly addresses the CAD-agent bottleneck: engineering artifacts need deterministic evidence, not only plausible-looking generated geometry.
  - Useful pattern for CAD-to-CAE workflows where generated parts must pass dimension, manufacturability, export, and meshability gates before simulation.
- Possible use: Adapt its PR-gate pattern for VA's parametric heat-sink/duct generation workflows.
- Maturity: early open-source tool
- Priority: High

## manifold-mcp

- Link: https://github.com/zhicwan/manifold-mcp
- Type: MCP server for manifold-3d geometry generation
- Why it matters:
  - Validates LLM-generated TypeScript geometry snippets and streams outputs to a live three.js preview with STL/3MF export.
  - Useful lightweight reference for agentic geometry generation where validation and export are built into the tool surface.
  - More manufacturing/prototyping-oriented than full CAE, but the validate-preview-export loop transfers well to CAD automation.
- Possible use: Compare with CadQuery/build123d/FreeCAD MCP flows for simple parametric parts.
- Maturity: early open-source MCP server
- Priority: Medium

## Text2CAD-Bench

- Link: https://arxiv.org/abs/2605.18430
- Type: Benchmark for LLM-based text-to-parametric-CAD generation
- Why it matters:
  - Covers 600 human-curated examples across basic geometry, complex topology, freeform surfaces, and application-diverse CAD tasks.
  - Uses both non-expert geometric descriptions and expert-like procedural prompts, making it more realistic than primitive sketch-extrude benchmarks.
  - Shows current models degrade sharply on advanced features, which is exactly where engineering CAD automation becomes useful.
- Possible use: Use as an evaluation reference when building text/spec-to-CadQuery, FeatureScript, or FreeCAD agent tests.
- Maturity: paper-only / benchmark announced
- Priority: High

## Self-Improving CAD Generation Agents with FEA Feedback

- Link: https://arxiv.org/abs/2605.17448
- Type: CAD-agent benchmark / FEA-feedback workflow
- Why it matters:
  - Requires agents to produce fully assembled multi-part STEP files from free-form engineering briefs, then validates them with finite element analysis.
  - Reports that strong coding agents still fail strict first-attempt engineering requirements, exposing the gap between plausible CAD and usable CAD.
  - Strong evidence that CAD automation needs simulation feedback, typed requirements, and repair loops.
- Possible use: Adapt the task pattern to CAD-to-CFD/thermal workflows: generated STEP → geometry checks → mesh → solver smoke test → repair.
- Maturity: paper-only
- Priority: High

## Jarvis Onshape MCP

- Link: https://github.com/ReshefElisha/jarvis-onshape-mcp
- Type: MCP plugin for Onshape CAD automation
- Why it matters:
  - Lets Claude Code-style agents drive real Onshape CAD using vision decomposition, parametric iteration, and FeatureScript-oriented workflows.
  - Complements FreeCAD/CadQuery MCP efforts with a cloud-CAD path that may fit collaborative design and revision workflows.
  - Useful signal for agent-readable CAD interfaces where truthfulness about current model state matters as much as command generation.
- Curation note: Evaluate permissions, API reliability, export formats, and downstream mesh/CAE handoff before using in lab workflows.
- Maturity: early open-source MCP tool
- Priority: Medium
