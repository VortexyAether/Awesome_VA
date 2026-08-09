# CAD, Geometry & AI-assisted Design

## CADCON — wrong design intent can be worse than none

- Link: https://arxiv.org/abs/2607.23191
- Type: Paper / causal audit of design-intent header conditioning for CAD program completion
- Keywords: CadQuery, design intent, header conditioning, derangement control, executable B-rep, LoRA, text-to-CAD
- One-line summary: Tests whether CAD code LLMs actually use design-intent headers under execution-level B-rep scoring, with a derangement-trained control that breaks circular “header helps” claims.
- Why it matters:
  - Wrong intent can hurt more than no intent: wrong-header adherence falls below no-header (0.43 → 0.30/0.21 text/token at 40% prefix in reported conditional completion).
  - Derangement control stays immune to wrong headers (interaction p≤4.2e-3 across 3 seeds) — a reusable evaluation pattern for any intent/tool schema.
  - Unconditioned 0% prefix baseline is 0/100 executable, so “agent wrote CAD” still needs executable gates.
- Caveat: Small coder model (1.5B LoRA) and five-feature header set; not full industrial GD&T. First-party monorepo not harvested at curation.
- Possible use: Steal wrong/masked/none + executable B-rep assertion arms when adding intent tools to FreeCAD/CadQuery agents; do not score “header present” as a win by itself.
- Maturity: paper-only
- Priority: High

## OmniMech — industrial mechanical drawing→CAD multimodal benchmark

- Link: https://arxiv.org/abs/2608.05539
- Type: Paper / industrial drawing-to-CAD benchmark (data release pending)
- Keywords: mechanical drawings, GD&T, orthographic, B-rep, STEP, VLM, executable CAD, manufacturing
- One-line summary: Proposes a million-scale industrial mechanical benchmark with 251k+ fully dimensioned and toleranced orthographic drawings paired with native CAD, multi-view, mesh, STEP, B-rep, and semantic annotations for executable CAD evaluation.
- Why it matters:
  - Moves VLM CAD eval beyond coarse general 3D objects toward millimeter tolerances and manufacturing drawings.
  - Forces metrics beyond visual mesh dumps: executable CAD validity, dimensional/tolerance grounding, multi-view consistency.
  - Complements Ortho2CAD / Drawing-Recode / CADENA with an industrial GD&T-oriented test surface.
- Caveat: Data/eval/tool URLs not verified live at curation — Watch / Save-when-released. cs.CV venue gravity; do not treat IoU leaderboards as BRep kernel validity.
- Possible use: Revisit when dataset drops; add STEP/B-rep validity + dimension consistency gates to VA CAD-agent eval checklists.
- Maturity: paper; dataset promised
- Priority: High

## RA-CAD — post-execution critique for state-aware text-to-CAD

- Link: https://arxiv.org/abs/2608.05714
- Type: Paper / agentic CAD Generate–Execute–Critique–Rewrite loop
- Keywords: text-to-CAD, ReAct agent, post-execution critique, state-aware repair, parametric CAD
- One-line summary: Learns how post-execution critique is interpreted and turned into corrective rewrite actions inside a state-aware Generate–Execute–Critique–Rewrite CAD agent loop.
- Why it matters:
  - External or frozen critics do not guarantee the agent uses feedback effectively across steps.
  - Complements TraceCAD (persistent repair state) and CADENA (stepwise RE) with a critique-utilization layer after code execution.
  - Aligns agentic CAD with verification-after-execute rather than one-shot program emit.
- Caveat: No first-party monorepo harvested at curation; Issue Board HTML metric columns still need a clean PDF table map before hard numeric claims.
- Possible use: Steal the harness shape (execute → state-aware critique → rewrite reward) when designing FreeCAD/CadQuery agent loops; Save when code lands.
- Maturity: paper-only
- Priority: Medium

## Ortho2CAD — orthographic drawings to editable CadQuery

- Link: https://arxiv.org/abs/2607.08891
- Code: https://github.com/AdityaJoglekar/Ortho2CAD
- Type: Paper + open VLM CAD reconstruction workflow
- Keywords: orthographic drawings, CadQuery, VLM, geometry-grounded RL, hidden lines, parametric CAD
- One-line summary: Translates raster first-angle orthographic drawings with hidden lines and dimensions into editable CadQuery programs via supervised fine-tuning and geometry-grounded reinforcement learning.
- Why it matters:
  - Much industrial geometry intent still lives as 2D drawings; CAE needs parametric 3D, not mesh-only reconstructions.
  - Reports 100% syntactic validity on evaluated settings and >7% average relative IoU gain vs next-best baseline.
  - Complements Drawing-Recode / CADENA / CADIR with an open drawing→code path.
- Caveat: IoU/validity ≠ manufacturing, BRep feature semantics, or sim-ready watertight geometry. License null via GitHub API at curation — verify before redistribution.
- Possible use: Test Ortho2CAD CadQuery outputs against FreeCAD/mesh/BC naming contracts before treating drawings as automatic CFD geometry sources.
- Maturity: paper + open repo (early)
- Priority: High

## CADENA — stepwise CAD reverse engineering

- Link: https://arxiv.org/abs/2608.00799
- Code: https://github.com/zhemdi/cadena
- Type: Paper + open-source stepwise CAD reverse engineering
- Keywords: CAD reverse engineering, stepwise reconstruction, CadQuery DSL, intermediate geometry, RL, mesh-to-program
- One-line summary: Reconstructs a target mesh as an editable parametric CAD program by growing features step by step and comparing intermediate geometry, instead of emitting the full program in one pass.
- Why it matters:
  - Human engineers build feature-by-feature with intermediate checks; most AI CAD systems skip that loop and lose editability/validity.
  - Reported CADENA-RL vs SOV-CAD: median CD 0.15 vs 0.38, IoU 0.961 vs 0.84, invalid rate 0.3% vs 7.3%.
  - Complements CADIR-style editable IR and domain CAD foundation models with an open MIT implementation path.
- Caveat: Mesh→program reverse engineering is not automatically a full MCAD BRep semantic feature tree; some mechanical categories (e.g. tooling/gauges) remain hard. Watertight IoU assumptions need care for CAE handoff.
- Possible use: Test CADENA outputs against FreeCAD/CadQuery/OpenFOAM boundary-name and edit-history contracts before treating RE as sim-ready geometry.
- Maturity: paper + open-source (MIT, early stars)
- Priority: High

## TraceCAD — trace-guided repair for agentic CAD generation

- Link: https://arxiv.org/abs/2608.03062
- Type: Paper / verification-first recovery layer for CAD agents
- Keywords: agentic CAD, repair, persistent recovery state, dependency-region search, SimpleCADAPI, FreeCAD macro
- One-line summary: Adds a recovery layer that keeps requested features, modeling steps, failure evidence, and candidate outcomes as persistent state, then repairs localized dependency regions under execution and preservation checks.
- Why it matters:
  - Correction loops often lose which requirements already passed, which ops failed, and what was tried — TraceCAD treats that evidence as first-class state.
  - Ablations: removing persistent state nearly halves recovery; removing localized search more than doubles geometric regression and doubles code-agent invocations.
  - Runtime notes point at SimpleCADAPI + FreeCAD-compatible macros — a practical bridge next to editable IR work.
- Caveat: Dedicated public TraceCAD repo not found at curation (paper-only); depends on SimpleCADAPI (AGPL). Backend-LLM sensitive; geometric IoU/CD/HD ≠ manufacturing/printability gates.
- Possible use: Steal the harness contract (state + local search + preservation checks + skill memory) even before official code lands; pair with CADIR/CADENA artifact contracts.
- Maturity: paper-only / code unavailable at curation
- Priority: High

## Drawing-Recode — annotation grounding for raster 2D CAD → parametric code

- Link: https://arxiv.org/abs/2607.27558
- Type: Paper / manufacturing drawing digitization
- Keywords: raster CAD drawings, dimension annotations, annotation grounding loss, parametric CAD sequences, manufacturing digitization
- One-line summary: Recovers parametric CAD sequences from raster 2D drawings by explicitly grounding dimensional annotations to geometry via cross-attention and an Annotation Grounding Loss.
- Why it matters:
  - Pre-digital drawing archives are a real industrial bottleneck; many CAD codegen systems ignore or weakly use dimension text.
  - Under noise, reported MCD rise is about +3.7% vs +18.9% for a CAD2Program-style baseline.
  - Useful citation for “annotation-geometry binding” as a missing contract in drawing-to-CAD agents.
- Caveat: Authors note scanned industrial drawings remain limited/artificial; no public code/data harvested at curation.
- Possible use: Watch for code/data; use as a checklist item when evaluating drawing digitization agents (dims must bind to features, not only look readable).
- Maturity: paper-only
- Priority: Medium

## CADIR — cross-backend editable IR for agentic CAD

- Link: https://arxiv.org/abs/2608.00891
- Adjacent tool: https://github.com/NiJingzhe/SimpleCADAPI
- Type: Paper + adjacent open CAD API
- Keywords: CAD IR, agentic CAD, construction graph, CadQuery, build123d, editability, multi-backend
- One-line summary: Proposes a construction-graph style editable intermediate representation so agentic CAD generation preserves edit history and can target multiple backends instead of one-shot backend scripts or static geometry.
- Why it matters:
  - Engineering CAD agents fail when the artifact is a disposable script or mesh: feature history, topology refs, and backend handoff disappear.
  - Reported IR comparison metrics include exec success 1.0 with IoU/CD/HD gains over strong baselines.
  - SimpleCADAPI is a live adjacent LLM-friendly CAD API surface (AGPL-3.0) useful for Test, not a claimed official monorepo.
- Caveat: Geometric similarity ≠ manufacturability, BRep validity, or sim-ready watertight export; AGPL on SimpleCADAPI.
- Possible use: Map CADIR fields to FreeCAD/CadQuery/OpenFOAM handoff contracts (params, feature order, validation rules, named boundaries).
- Maturity: paper + adjacent OSS API
- Priority: High

## IndustryForge-27B — industrial multimodal CAD foundation model

- Link: https://arxiv.org/abs/2607.28050
- Type: Paper / domain-enhanced multimodal CAD foundation model
- Keywords: industrial CAD, multimodal FM, CadQuery, drawings, assemblies, COM API
- One-line summary: Domain-enhanced 27B multimodal model aimed at industrial CAD: engineering drawings and 3D screenshots to parametric scripts, Windows COM API use, and assemblies.
- Why it matters:
  - General VLMs underperform on industrial CAD surfaces; domain enhancement is the signal, not generic image-to-mesh demos.
  - Reported CadQuery accuracy jumps from ~7.8% to ~77.9%, overtaking a gpt-5.4 baseline on the paper bar.
  - Complements editable-IR work: weights/scripts alone still need an artifact contract for edit and CAE handoff.
- Caveat: Weights/code not linked at harvest; Windows COM path is enterprise-specific; benchmark construction opacity — Watch before Save.
- Possible use: Cite as industrial CAD-FM capability ceiling while preferring IR/MCP contracts for deployable agents.
- Maturity: paper-only / weights unavailable at curation
- Priority: Medium

## FORGE-SIM — multi-patch B-spline BRep reconstruction for IGA (Watch)

- Link: https://arxiv.org/abs/2607.26234
- Claimed code: https://github.com/Schindler-EPFL-Lab/FORGE-SIM (GitHub API 404 on 2026-08-04)
- Type: Vision-to-CAD/sim-ready geometry paper
- Keywords: B-spline, multi-patch BRep, IGA, thermal/modal simulation, sim-ready reconstruction
- One-line summary: Optimizes multi-patch B-spline BRep directly from sparse views so reconstructed geometry can feed isogeometric thermal and modal analysis without a mesh-only detour.
- Why it matters:
  - Points at the right CAD↔CAE handoff: watertight, simulation-native spline BRep rather than cosmetic meshes.
  - Observation fields can share the same spline basis, which is attractive for digital-twin reconstruction.
- Caveat: Claimed GitHub path returned Not Found at curation time — paper-only Watch until a live code/data release exists. Industrial feature-tree BRep editability is not the focus.
- Possible use: Watch for code release before any Save/Test action; keep as a sim-ready geometry north-star citation.
- Maturity: paper-only / code unavailable at curation
- Priority: Medium

## ArtisanCAD — CAD-IR and CATIA-MCP for editable industrial CAD agents

- Link: https://arxiv.org/abs/2607.05750
- Type: Industrial CAD agent architecture with expert-grounded knowledge distillation
- Keywords: CAD agent, CAD-IR, CATIA, MCP, B-Rep, editable geometry, procedural modeling
- One-line summary: Distills expert CATIA procedures into reusable skills through an executable CAD intermediate representation that records parameters, ordered operations, MCP tool bindings, dependencies, generated entities, and verification rules.
- Why it matters:
  - Text-to-CAD systems are only useful for engineering when feature dependencies, parametric editability, B-Rep validity, and verification rules survive generation.
  - CAD-IR is a strong pattern for agent-generated geometry: keep the procedural scaffold and tool bindings, not just the final shape.
  - The reported Text2CAD Chamfer Distance improvement from 14.83 to 9.88 is less important than the shift toward editable, auditable CAD procedures.
- Caveat: CATIA recordings and industrial macro logs may not transfer directly to FreeCAD/CadQuery/OpenSCAD workflows; public backend/tooling maturity needs checking.
- Possible use: Compare CAD-IR fields against the desired artifact contract for FreeCAD/OpenFOAM geometry handoff: named parameters, feature history, validation rules, and meshing boundary metadata.
- Maturity: paper-only
- Priority: High

## SplineNet — isogeometric deep learning for complex shells

- Link: https://arxiv.org/abs/2607.06026
- Type: CAD-native CAE / isogeometric deep-learning method for shell structures
- Keywords: CAD, CAE, isogeometric analysis, T-splines, Bézier extraction, DeepONet, shell mechanics
- One-line summary: Builds neural architectures directly from watertight spline/T-spline CAD representations, using Bézier extraction and Bernstein polynomial activations for data-free or data-driven shell analysis.
- Why it matters: CAD-to-CAE automation often loses exact geometry and boundary semantics during model/data exchange. SplineNet is a strong citation for keeping exact CAD geometry inside the learning/analysis architecture instead of treating geometry as a disposable mesh or image-like input.
- Caveat: Shell structures rather than CFD/turbulence; implementation, CAD-kernel compatibility, and examples need checking before reuse.
- Possible use: Use as an anchor for “CAD-native surrogate” arguments and for evaluating whether agent-generated geometry remains analysis-suitable downstream.
- Maturity: paper-only
- Priority: High

## Roshera-CAD

- Link: https://github.com/varun29ankuS/Roshera-CAD
- Type: Agent-native Rust B-Rep geometry kernel / MCP bridge
- Keywords: CAD agents, B-Rep, geometry kernel, validity certificates, MCP, verification
- One-line summary: Builds toward a CAD runtime where geometry operations return validity certificates, so agents can query, build, and verify mechanical parts instead of only producing plausible shapes.
- Why it matters:
  - CAD-to-CAE automation needs kernel-level truth artifacts: watertight/manifold checks, boundary semantics, and provenance for generated geometry.
  - The repo's “kernel cannot lie” framing is a useful benchmark for CAD-agent interfaces: every write should leave a checkable contract.
  - The included `roshera-mcp` surface makes it relevant to agent-readable engineering-tool workflows.
- Caveat: Fair Source / FSL-1.1-Apache-2.0 today, and README claims need local build/test before relying on certificate semantics or performance.
- Possible use: Smoke-test a simple parametric part and inspect which validity certificate fields survive export/import into downstream meshing.
- Maturity: early open repository / watch-test
- Priority: High

## FutureCAD / LLM-driven CAD with B-Rep primitive grounding

- Link: https://arxiv.org/abs/2603.11831
- Type: Text-to-CAD framework with executable program generation and B-Rep grounding
- Keywords: CAD generation, B-Rep, CadQuery, LLM, primitive grounding, feature modeling
- One-line summary: Combines LLM-generated CadQuery programs with text-based B-Rep primitive grounding so feature operations such as fillet/chamfer can target explicit faces and edges.
- Why it matters:
  - Engineering CAD automation needs editable feature-based construction and primitive selection, not only visually plausible mesh outputs.
  - B-Rep grounding is directly relevant to downstream CAE because named faces/edges, boundary metadata, and feature history determine meshing and boundary-condition assignment.
  - Good comparison point for FreeCAD/CadQuery/OpenSCAD agents: can the system preserve design intent and selectable geometry through edits?
- Possible use: Test generated CadQuery scripts for execution, STEP export, face/edge naming stability, meshability, and parameter-edit robustness.
- Maturity: paper-only
- Priority: High

## Surrogate-assisted crash safety design with foundation-model orchestration

- Link: https://arxiv.org/abs/2606.17577
- Type: CAE design workflow combining surrogate modeling, optimization, geometry morphing, and LLM/VLM orchestration
- Keywords: CAE, crash safety, foundation model, surrogate-assisted design, conformal prediction, geometry morphing
- One-line summary: Uses a CAE-trained surrogate with conformal intervals, NSGA-II search, topology-preserving bumper geometry morphing, and an LLM/VLM interface for pedestrian-protection design exploration.
- Why it matters:
  - Shows a realistic role for foundation models in engineering: orchestrate validated CAE tools rather than replace high-fidelity solvers.
  - The combination of surrogate uncertainty, design constraints, geometry generation, and human-facing explanation is a useful pattern for CAD-to-CAE automation.
  - Safety-critical setting reinforces the need for high-fidelity fallback and artifact trails before trusting generated designs.
- Possible use: Adapt the workflow pattern to CFD/thermal design loops: natural-language constraints, surrogate candidates, geometry morphing, uncertainty gate, and high-fidelity recheck.
- Maturity: workshop paper / workflow case study
- Priority: Medium

## LLM-based visual code completion for aerospace geometric design

- Link: https://arxiv.org/abs/2606.16806
- Type: Aerospace CAD visual-programming copilot / dataset
- Keywords: aerospace geometry, visual programming, Grasshopper, CAD copilot, AVPD
- One-line summary: Proposes an LLM/VLM visual code-completion copilot for aerospace design, plus Wingbuilder Grasshopper components and an Aerospace Visual Programming Dataset.
- Why it matters:
  - Aerospace CAD automation needs explainable, domain-specific geometry abstractions rather than generic text-to-shape previews.
  - Visual programming tasks with ground-truth expert workflows are a better benchmark substrate than unconstrained chat demos.
  - Relevant to VA's CAD-to-CAE automation lens because visual programs can preserve editable design intent and downstream parameter sweeps.
- Possible use: Use AVPD/Wingbuilder as a reference when designing Grasshopper/CadQuery/FreeCAD tasks for agentic geometry-generation evaluation.
- Maturity: paper + plugin/dataset described
- Priority: Medium

## AI+CAD data representation architecture

- Link: https://arxiv.org/abs/2606.16797
- Type: CAD representation survey / position paper
- Keywords: AI+CAD, industrial-grade CAD, parametric feature modeling, B-Rep, data representation
- One-line summary: Argues that CAD AI should prioritize industrial usability and representation architecture over visual plausibility, moving from solid modeling toward parametric feature modeling.
- Why it matters:
  - Mesh-like visual outputs are insufficient for engineering workflows that require editability, constraints, feature history, manufacturability, and CAE handoff.
  - Useful citation for separating CAD generation research from generic 3D generation.
  - Reinforces VA's rubric: CAD AI artifacts should be evaluated by BRep/feature semantics and downstream meshing/simulation robustness.
- Possible use: Turn its representation taxonomy into a local CAD-agent evaluation checklist.
- Maturity: paper-only
- Priority: High

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

## IterCAD

- Link: https://arxiv.org/abs/2606.13368
- Type: Iterative multimodal CAD generation/editing agent
- Why it matters:
  - Frames CAD generation as a closed-loop, multi-turn interaction between a multimodal agent and an executable CAD sandbox instead of one-shot text-to-CAD.
  - Covers drawing-to-code, text-to-code, and interactive editing, which better matches real engineering workflows.
  - Introduces IterCAD-Bench and CD-TR/AUC-TR metrics to jointly account for code executability and geometric precision while reducing survivor bias.
- Possible use: Reuse the evaluation lens for FreeCAD/CadQuery/OpenSCAD agents: code validity, geometry fidelity, editability, exportability, and downstream meshability.
- Maturity: paper + benchmark proposal
- Priority: High

## ComAct / ComCADBench

- Link: https://arxiv.org/abs/2606.13239
- Type: Professional CAD software agent benchmark / COM-as-action paradigm
- Why it matters:
  - Argues that GUI-based professional-software agents are fragile, while COM-style executable abstractions can turn CAD manipulation into deterministic program synthesis.
  - Introduces ComCADBench for real industrial CAD software and ComActor as a self-correcting CAD agent trained for long-horizon tasks.
  - Strong signal for CAD/CAE automation: expose stable software action layers rather than relying on screenshots or brittle GUI macros.
- Possible use: Compare with FreeCAD/Python APIs, OpenCascade bindings, and MCP/COM bridges when designing agent surfaces for engineering tools.
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

## Memory-Augmented RL Agent for CAD Generation

- Link: https://arxiv.org/abs/2605.19748
- Type: Memory-augmented reinforcement-learning agent for CAD generation
- Why it matters:
  - Targets complex CAD models with long operation sequences, diverse operation types, and strong geometric constraints.
  - Signals a shift from one-shot LLM CAD code generation toward design-history-aware policies with persistent state.
  - Relevant to parametric CAD/CAE workflows where edit sequences, constraints, and recoverable intermediate states matter.
- Possible use: Compare against CadQuery/FeatureScript agent loops that use explicit memory, tests, and repair traces.
- Maturity: paper-only
- Priority: High

## Physics-in-the-Loop CAD Engineering Design

- Link: https://arxiv.org/abs/2605.19717
- Type: Hybrid agentic architecture for validated CAD engineering design
- Why it matters:
  - Embeds validated engineering tools and physical checks inside the CAD-agent loop instead of expecting an LLM to infer physics implicitly.
  - Strong pattern for CAD-to-CAE automation: generated geometry should be accepted only after deterministic validation and physics-aware feedback.
  - Complements FEA-feedback CAD-agent work by emphasizing architecture and knowledge-based tools around the generative model.
- Possible use: Use as a blueprint for a CAD→mesh→thermal/CFD artifact gate with dimensional checks, meshability, solver smoke tests, and repair loops.
- Maturity: paper-only
- Priority: High

## EngiAI

- Link: https://arxiv.org/abs/2605.19743
- Type: Multi-agent framework and benchmark suite for LLM-driven engineering design
- Why it matters:
  - Evaluates engineering-design agents across simulation, retrieval, and manufacturing-preparation steps, not just final text or visual output.
  - Useful for designing benchmarks where CAD, solver execution, documentation, and artifact validation are all separate failure points.
  - Reinforces that multi-agent engineering workflows need evidence logs and node-level evaluation.
- Possible use: Reference when structuring CAD/CAE agent benchmarks or OpenClaw workflows for engineering design automation.
- Maturity: paper-only
- Priority: High

## BrepForge

- Link: https://arxiv.org/abs/2605.19411
- Type: Factorized B-rep synthesis for CAD generation
- Why it matters:
  - Separates wireframe composition from boundary-conditioned surface instantiation to handle the topology/geometry coupling in B-rep CAD.
  - B-rep structure is critical for downstream CAE because faces, edges, topology, and feature identity drive meshing and boundary-condition assignment.
  - Useful counterweight to mesh-only or image-like 3D generation methods that lose engineering editability.
- Possible use: Track for parametric CAD reconstruction, named-face preservation, and CAD-to-mesh automation research.
- Maturity: paper-only
- Priority: High

## COSMO-Agent

- Link: https://arxiv.org/abs/2605.20190
- Type: Tool-augmented agent framework for CAD-CAE closed-loop optimization
- Why it matters:
  - Frames iterative industrial design as a CAD-CAE semantic-gap problem: simulation feedback must be translated into valid geometric edits under constraints.
  - Combines optimization, simulation, and modeling orchestration rather than treating CAD generation as a one-shot text-to-shape task.
  - Strongly aligned with CAD→mesh→CFD/FEA workflows where each edit must preserve parametric validity, downstream meshability, and physics intent.
- Possible use: Use as a reference architecture for an artifact-gated CAD-CAE loop: propose edit, regenerate CAD, run mesh/solver smoke test, compare KPI, and record provenance.
- Maturity: paper-only
- Priority: High

## Component influence-driven fastener reduction

- Link: https://arxiv.org/abs/2605.21026
- Type: CAD graph / robotic disassembly feedback for design simplification
- Why it matters:
  - Converts CAD contact-connection-constraint graphs and robotic disassembly planning outcomes into component influence scores.
  - Projects fastener-removal impact back onto CAD geometry as 3D heatmaps, making redesign guidance visible to engineers.
  - Useful design-automation pattern: analysis results become actionable geometry/design-change suggestions rather than only reports.
- Possible use: Adapt the pattern to CAD-to-CAE workflows: simulation bottleneck or failure attribution → geometry heatmap → constrained redesign suggestion → validation gate.
- Maturity: paper-only
- Priority: Medium

## SDFStent

- Link: https://arxiv.org/abs/2605.22009
- Type: SDF-based geometry deformation for virtual stenting and CFD preparation
- Why it matters:
  - Makes patient-specific stent-induced geometry updates interactive, reducing a practical bottleneck before CFD simulation.
  - Good example of AI/geometry tooling helping CFD by improving preprocessing rather than replacing the solver.
  - Relevant pattern for CAD-to-CFD workflows: learned deformation field → validated geometry → downstream simulation.
- Maturity: paper-only
- Priority: Medium

## Memory-Augmented Reinforcement Learning Agent for CAD Generation

- Link: https://arxiv.org/abs/2605.19748
- Type: Memory-augmented RL for CAD operation-sequence generation
- Why it matters:
  - Long CAD histories require state, constraint, and dependency tracking; one-shot generation is brittle.
  - Reinforces that CAD agents need persistent design memory and repair loops around executable geometry.
  - Useful reference for stress-testing FreeCAD/CadQuery agents on long parametric models.
- Maturity: paper-only
- Priority: Medium

## pcb-designer-ai-agent

- Link: https://github.com/assalas/pcb-designer-ai-agent
- Type: Open-source AI agent for PCB design automation
- Why it matters:
  - Not a CFD/CAD geometry tool directly, but it is a useful EDA example of agentic placement/routing/validation workflows.
  - Relevant as a pattern for engineering agents that must call domain tools instead of only generating text.
  - Treat as inspiration for validation-loop architecture, not as a direct VA CFD workflow dependency.
- Maturity: early open-source repo
- Priority: Low

## Hylos

- Link: https://arxiv.org/abs/2605.24728
- Type: Operability-contract architecture for spatial/CAD agents
- Why it matters:
  - Argues that visually plausible 3D is not enough; useful spatial AI needs entities, frames, surfaces, constraints, provenance, admissible actions, effect diffs, and validation outcomes.
  - Introduces a transaction boundary for spatial changes with commit, review, rollback, deferral, and capability-gap outcomes.
  - Strong conceptual fit for CAD-to-CAE agents where geometry edits must preserve invariants and remain mesh/simulation-ready.
- Possible use: Define an “operable CAD artifact” schema for VA workflows before letting agents revise geometry.
- Maturity: systems/position preprint
- Priority: High

## Memory-Augmented Reinforcement Learning Agent for CAD Generation

- Link: https://arxiv.org/abs/2605.19748
- Type: Memory/RL framework for tool-using CAD generation agents
- Why it matters:
  - Wraps a geometric kernel as a structured toolchain and adds planning, execution, verification, case memory, and skill memory.
  - Addresses a real CAD-agent failure mode: semantically similar examples can be geometrically infeasible retrieval traps.
  - Reinforcement learning over retrieval and policy optimization points toward CAD agents that self-correct without massive new annotated datasets.
- Possible use: Compare against prompt-only CadQuery/FreeCAD agents on long operation sequences with deterministic geometry checks.
- Maturity: paper-only
- Priority: Medium

## VFEAgent

- Link: https://arxiv.org/abs/2605.28978
- Type: Paper / multimodal FEA automation agent
- Keywords: finite element analysis, multimodal agent, verification-first synthesis, engineering automation
- One-line summary: A multimodal multi-agent framework that extracts FEA specifications from images and problem descriptions, then generates and verifies executable simulation code.
- Why it matters: It frames engineering-agent reliability around structured specification extraction, self-debugging, fallback mechanisms, executability, and physical validity rather than chat-only assistance.
- Possible use: Compare against CFD/CAE automation workflows where an agent must turn sketches or descriptions into solver-ready cases with validation gates.
- Maturity: paper-only
- Priority: High

## MUSE text-to-CAD benchmark

- Link: https://arxiv.org/abs/2605.28579
- Project: https://dong7313.github.io/muse-benchmark/
- Type: Benchmark / text-to-CAD evaluation
- Keywords: text-to-CAD, B-Rep assembly, manufacturability, functionality, assemblability, VLM judge
- One-line summary: Benchmarks complex editable B-Rep assembly generation using code checks, geometry checks, and design-intent rubrics for manufacturability, functionality, and assemblability.
- Why it matters: CAD generation for CAE cannot stop at visual or geometric similarity; downstream simulation and manufacturing need executable geometry and engineering-intent alignment.
- Possible use: Use the failure-cascade framing as a validation template for CAD-to-mesh-to-CFD agent workflows.
- Maturity: benchmark / project page
- Priority: High

## Multi-patch neural solver with isogeometric mappings

- Link: https://doi.org/10.1007/s00366-026-02351-z
- Type: Neural PDE solver on CAD/NURBS domains
- Why it matters:
  - Solves PDEs over computer-aided design domains by using multi-patch isogeometric mappings and patch-local neural networks in each parametric space.
  - Uses custom output layers for strong Dirichlet boundary conditions and interface neural networks for conformity across NURBS patches.
  - Relevant to CAD-to-CAE automation because it treats CAD geometry as a solver-native representation instead of only a pre-meshing artifact.
- Possible use: Use as a reference for simple CAD-domain heat-conduction experiments before moving to full CFD/thermal workflows.
- Maturity: journal paper
- Priority: Medium

## LLM-enabled CAD–structural analysis via MCP

- Link: https://doi.org/10.1016/j.autcon.2026.107030
- Type: MCP-based CAD-to-structural-analysis automation paper
- Why it matters:
  - Shows Model Context Protocol being applied to CAD and structural-analysis automation in a peer-reviewed construction automation context.
  - Strong ecosystem signal that MCP can become an engineering workflow interface, not only a generic LLM tool demo.
  - Relevant to CAD-to-CAE agent design where geometry edits, analysis setup, and artifact validation need a common callable protocol.
- Possible use: Compare its workflow boundary with FreeCAD/Onshape/OpenFOAM automation patterns when defining VA's CAD-to-CAE stack.
- Maturity: journal paper
- Priority: High

## onshape-cli

- Link: https://github.com/am-will/onshape-cli
- Type: Agent-friendly CLI/API layer for Onshape CAD
- Why it matters:
  - Exposes Onshape document, sketch, feature, assembly, drawing, measurement, render, and export operations through Python and Node CLIs with machine-readable JSON responses.
  - Designed as a tool layer for AI coding agents rather than an autonomous CAD agent, which keeps responsibility boundaries clearer.
  - Useful reference for deterministic CAD automation: API commands, validation, measurement, and STEP/STL/IGES/3MF/Parasolid export beat brittle browser control.
- Possible use: Test on a small public Onshape part and require bounding-box/mass-property checks plus STEP/STL export evidence before meshing.
- Maturity: active early open-source tool
- Priority: High

## archicad-mcp

- Link: https://github.com/Boti-Ormandi/archicad-mcp
- Type: MCP server for Archicad automation via Tapir JSON API
- Why it matters:
  - Uses a compact tool surface with live schema search and a script-first Python execution layer over 173 underlying Archicad commands.
  - Good design reference for CAD/BIM agents: expose stable schemas and let complex multi-step logic run near the CAD API instead of chaining many chatty tool calls.
  - Multi-instance discovery and property lookup are useful patterns for larger engineering projects with several open models.
- Curation note: Archicad/BIM-specific; treat as an interface-design reference unless a BIM workflow becomes relevant.
- Maturity: active early open-source tool
- Priority: Medium

## FreeCad_MCP_Server

- Link: https://github.com/JakobThiessen/FreeCad_MCP_Server
- Type: MCP server plus FreeCAD workbench bridge
- Why it matters:
  - Connects MCP clients to a running FreeCAD instance through a local XML-RPC workbench bridge, with Sketcher, Part, PartDesign, constraints, screenshots, and STEP/STL export tools.
  - Useful comparison point for FreeCAD-agent architecture: external MCP server plus in-app addon, rather than only headless Python generation.
  - Highlights practical constraints such as GUI dependency, topology naming instability, and the need to queue operations onto the FreeCAD GUI thread.
- Possible use: Compare against other FreeCAD MCP servers on a repeatable heat-sink/duct generation and export smoke test.
- Maturity: early open-source tool
- Priority: Medium

## cadlens-mcp

- Link: https://github.com/cadlens-co/cadlens-mcp
- Type: MCP server for parsing CAD drawing files into structured data
- Why it matters:
  - Parses DWG, DXF, DWF, DWFX, DGN, and PDF CAD drawings through the CADLens API and returns entity, layer, metadata, and summary views to MCP clients.
  - Complements CAD-control servers: agents often need to understand existing drawings before creating or modifying geometry.
  - Useful for drawing-review and legacy-CAD ingestion workflows where AutoCAD is unavailable or GUI automation would be brittle.
- Curation note: Requires an external CADLens API key; avoid uploading sensitive CAD without approval.
- Maturity: active early open-source MCP server
- Priority: Medium

## Attributed Feature Graphs for Engineering Design

- Link: https://arxiv.org/abs/2606.06405
- Type: CAD feature representation for data-driven engineering design
- Keywords: CAD, feature graph, design automation, data-driven design, CAD-to-CAE
- One-line summary: Represents CAD models as attributed graphs over engineering features such as extrusions, ribs, pockets, and their relationships.
- Why it matters: CAD-to-CAE automation needs design intent and feature semantics, not only point clouds or meshes; feature graphs can support interpretability, design-rule checks, meshability reasoning, and solver setup.
- Possible use: Explore feature-graph extraction as an intermediate artifact for boundary tagging, design sweeps, and surrogate conditioning.
- Maturity: paper-only
- Priority: High

## UniCAD

- Link: https://arxiv.org/abs/2606.05058
- Type: Unified benchmark and model for multi-modal multi-task CAD
- Keywords: CAD benchmark, multimodal CAD, text-to-CAD, point-to-CAD, CAD question answering
- One-line summary: Introduces a benchmark and universal model covering point-to-CAD reconstruction, text/image-to-CAD generation, and CAD question answering.
- Why it matters: CAD-AI is moving from isolated demos toward shared multi-task evaluation; useful for tracking whether CAD models are becoming broad engineering assistants rather than single-task shape generators.
- Possible use: Use the task taxonomy to evaluate future CAD-agent workflows across reconstruction, generation, inspection, and explanation.
- Maturity: paper-only
- Priority: Medium

## BRepCLIP

- Link: https://arxiv.org/abs/2606.05515
- Type: Multimodal representation learning on native CAD B-Rep primitives
- Keywords: B-Rep, CAD understanding, contrastive learning, face-edge tokens, multimodal pretraining
- One-line summary: Aligns native CAD boundary-representation primitives with image and language embeddings through contrastive pretraining.
- Why it matters: Exact B-Rep faces, edges, curves, and topology are closer to downstream CAD/CAE workflows than generic meshes; BRepCLIP is a signal that CAD representation learning is shifting toward native engineering geometry.
- Possible use: Track for CAD retrieval, feature recognition, natural-language CAD inspection, and solver-prep metadata extraction.
- Maturity: paper-only
- Priority: High

## GuideCAD

- Link: https://arxiv.org/abs/2606.07024
- Code: https://github.com/mskimS2/GuideCAD
- Type: Lightweight multimodal CAD generation via prefix embeddings
- Keywords: CAD generation, text-to-CAD, image-to-CAD, construction sequence, parameter-efficient training
- One-line summary: Maps image embeddings into prefix embeddings so a pretrained LLM and transformer decoder can generate executable 3D CAD construction sequences from visual-textual context.
- Why it matters:
  - Keeps the focus on CAD construction sequences rather than only mesh/point-cloud outputs, which is more useful for editable engineering workflows.
  - Uses a small trainable mapping layer instead of full multimodal fine-tuning, making the approach more practical for resource-limited CAD experiments.
  - Provides both paper and code/dataset release, so it can be inspected as a benchmark/reference for future CAD-agent validation loops.
- Possible use: Test generated sequences through CadQuery/FreeCAD execution, export, watertightness, and named-boundary checks before treating outputs as CAE-ready.
- Maturity: paper + early code
- Priority: Medium

## freecad-ai

- Link: https://github.com/ghbalf/freecad-ai
- Type: AI-powered FreeCAD assistant workbench
- Why it matters:
  - Provides a FreeCAD-native assistant workflow for generating 3D models from natural language.
  - Useful UX/reference point for CAD agents operating inside the CAD environment instead of through screenshots alone.
  - For CAE use, generated geometry still needs deterministic validation, named boundaries, export checks, and meshability tests.
- Curation note: Treat as an implementation signal; validate on parametric engineering parts before depending on it.
- Priority: Medium

## Neural Deformation Field for industrial NURBS geometry optimization

- Link: https://arxiv.org/abs/2606.07198
- Type: Differentiable parametrization and shape optimization for industrial CAD geometry
- Keywords: CAD, NURBS, neural deformation field, shape optimization, differentiable geometry
- One-line summary: Uses a neural displacement field over multi-patch NURBS control points to morph industrial CAD surfaces under physical/design constraints.
- Why it matters:
  - Works closer to native CAD surface representations than mesh-only or point-cloud generation approaches.
  - Relevant to CAD-to-CAE automation because shape optimization needs geometry edits that remain exportable, constrainable, and solver-ready.
  - Useful complement to feature-graph and B-Rep representation work: optimization should preserve engineering semantics, not only visual shape.
- Possible use: Test whether NURBS morphing workflows preserve named boundaries, patch continuity, export validity, and meshability for CFD cases.
- Maturity: paper-only
- Priority: High

## Constrained natural-language interface for FEniCS multi-physics simulations

- Link: https://arxiv.org/abs/2606.10928
- Type: LLM-assisted but constrained finite-element simulation interface
- Keywords: FEniCS, Gmsh, finite element, multi-physics, constrained LLM interface, simulation safety
- One-line summary: Restricts the LLM to prompt parsing, structured JSON, and limited geometry generation while deterministic human-written FEniCS/UFL templates own the solver core.
- Why it matters:
  - A strong safety architecture for engineering agents: do not let the LLM freely write weak forms or solver templates on the critical path.
  - Validates deterministic templates against analytical and published 2D/3D benchmarks, while separately measuring parser and geometry-generation success.
  - Transfers to CAD/CAE automation where intent parsing, geometry helpers, solver routing, and validation should be separate audited layers.
- Possible use: Prototype a VA-style `prompt → JSON spec → validated template → artifact report` workflow for FEA/CFD tasks.
- Maturity: paper-only
- Priority: High

## DeepJEB++

- Link: https://arxiv.org/abs/2606.12994
- Type: Simulation-labeled 3D engineering dataset generation pipeline
- Keywords: engineering dataset, 3D generation, FEA labels, jet-engine bracket, foundation model, data augmentation
- One-line summary: Expands a small seed set of jet-engine brackets into a 15,360-sample simulation-labeled 3D dataset through 2D latent diffusion augmentation, 3D lifting, VLM filtering, and automated FEA labeling.
- Why it matters:
  - Attacks the practical bottleneck of geometry-plus-physics labeled data for data-driven engineering design.
  - Includes manufacturability, label fidelity, and distributional consistency checks rather than only visual plausibility.
  - Useful reference for building CAD/CAE datasets where geometry generation and simulation labeling must be automated together.
- Possible use: Compare with SimJEB/DeepJEB-style datasets when designing VA benchmark data for geometry-to-stress/flow/thermal surrogate models.
- Maturity: paper-only; dataset release claimed
- Priority: Medium
