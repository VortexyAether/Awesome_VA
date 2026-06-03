# Agent Tools & Research Workflow

## cmux

- Link: https://github.com/manaflow-ai/cmux
- Type: Native macOS terminal/workspace manager for AI coding agents
- Why it matters:
  - Built on Ghostty/libghostty with vertical tabs, split panes, and notification rings for parallel Claude Code, Codex, Gemini, OpenCode, and similar agent sessions.
  - Shows useful agent-operations primitives: terminal + browser panes, CLI/socket automation, workspace metadata, PR/branch/status visibility, and attention notifications.
  - Relevant for research coding workflows where multiple simulations, repos, or agent runs need supervision without losing context.
- Caveat:
  - macOS-focused; evaluate fit against tmux/OpenClaw/ACP workflows before standardizing lab usage.

## Claude Code best-practice tips

- Link: https://github.com/shanraisshan/claude-code-best-practice/blob/main/tips/claude-boris-6-tips-16-apr-26.md
- Type: Claude Code usage tips
- Why it matters:
  - Useful for lab members using Claude Code for research programming.
  - Can inform how to structure prompts, context, repository tasks, and code review workflows.

## Korean Claude skills collection

- Link: https://github.com/NomaDamas/k-skill
- Type: Claude skills collection for Korean users
- Why it matters:
  - Potential source of reusable skills/workflows localized for Korean research and productivity contexts.
  - Could inspire OpenClaw/Claude skill design for lab-specific CFD-ML tasks.

## Claude for creative work / Blender support

- Link: https://www.anthropic.com/news/claude-for-creative-work
- Type: Claude integration for creative tools including Blender
- Why it matters:
  - Could be relevant for scientific visualization, geometry prototyping, figure generation, and animation workflows.
  - Worth tracking if CFD/CAE visualization pipelines start using agent-assisted Blender scenes.

## Google Workspace CLI for coding agents

- Link: https://www.youtube.com/watch?v=Pq12GuQw0_c
- Type: Google Workspace CLI / coding-agent tool interface discussion
- Summary:
  - The interesting part is not just human CLI usability, but that the structure appears friendly for coding agents.
  - Future open-source projects may improve AI accessibility by shipping MCP servers or agent-facing interfaces.
- Why it matters:
  - Agent-readable operational surfaces can make complex projects easier to run, inspect, and automate.
  - Good reference for designing lab tools that are usable by both humans and AI agents.

## Academic/research skills and harness collections

- Links:
  - K-Dense academic Claude skills: https://github.com/K-Dense-AI/claude-scientific-skills
  - Harness-100 collection: https://github.com/revfactory/harness-100
- Type: Skills/harness collections
- Why it matters:
  - Useful starting points for building domain-specific scientific workflows.
  - Could inspire custom skills for CFD, Scientific ML, paper triage, and repository maintenance.

## Voice-to-prompt: Whispree

- Link: https://github.com/Arsture/whispree/blob/main/README.ko.md
- Type: Voice-to-prompt tool
- Why it matters:
  - Could make mobile/desktop interaction with coding agents faster.
  - Potentially useful for hands-free note capture, experiment logging, or rough prompt drafting.

## 500+ AI Agent Projects / Use Cases

- Link: https://github.com/ashishpatel26/500-AI-Agents-Projects
- Type: Large curated collection of AI agent use cases and open-source examples
- Frameworks/examples mentioned:
  - CrewAI
  - AutoGen
  - Agno
  - LangGraph
- Why it matters:
  - Useful inspiration bank for designing agent workflows across research, productivity, documentation, meetings, coding, data analysis, and automation.
  - The framework-wise examples are useful when deciding whether a workflow should be a simple coding-agent task, a tool-using agent, or a multi-agent pipeline.
- Curation note:
  - Broad collection, not CFD-specific. Pull only patterns that can transfer to lab/research workflows.

## OpenAI Codex

- Link: https://github.com/openai/codex
- Type: Terminal coding agent
- Why it matters:
  - Representative coding-agent tool for repository exploration, refactoring, and implementation tasks.
  - Useful comparison point against Claude Code, OpenCode, and OpenClaw ACP-style workflows.
  - CLI behavior changes quickly; verify current capabilities before standardizing lab usage.

## OpenCode

- Link: https://github.com/opencode-ai/opencode
- Type: Terminal-first coding agent
- Why it matters:
  - Practical alternative to Codex/Claude Code for coding-agent workflows.
  - Relevant to OpenClaw ACP harness comparisons and multi-agent coding experiments.

## KOMPAS-3D MCP client

- Link: https://github.com/dwnmf/KOMPAS-3D-MCP-bin
- Type: MCP bridge for CAD software
- Why it matters:
  - Shows CAD vendors/ecosystems moving toward agent-readable control surfaces via MCP-style interfaces.
  - Useful precedent for thinking about FreeCAD/SALOME/OpenFOAM agent tooling: expose stable operations, not only screenshots or GUI macros.
  - Windows/KOMPAS-specific, so treat as a workflow signal rather than an immediate lab dependency.


## sim-cli

- Link: https://github.com/svd-ai-lab/sim-cli
- Type: Agent-facing runtime for CAD/CAE simulators
- Why it matters:
  - Aims to let LLM agents launch, drive, and observe CAD/CAE simulators through a common protocol.
  - Directly aligned with intelligent engineering workflows: agent plans should be grounded in simulator state, logs, and artifacts.
  - Useful precedent for OpenFOAM/FreeCAD/SALOME automation wrappers where reproducibility matters more than chatty GUI control.

## Awesome AI CAE

- Link: https://github.com/kimimgo/awesome-ai-cae
- Type: Curated AI-ready CAE tool index
- Why it matters:
  - Tracks CFD, FEA, SPH, DEM, differentiable simulation, neural operators, PINNs, MCP servers, and optimization tools.
  - Useful meta-index for discovering agent-readable engineering tooling without mixing it into the main repository unchecked.
  - Pull only high-signal tools into Awesome_VA after direct evaluation or clear CFD/SciML relevance.

## CadCrawl MCP

- Link: https://github.com/cadcrawl/mcp
- Type: MCP server for CAD project memory and context
- Why it matters:
  - Gives CAD agents semantic memory over local CAD files, renders, revisions, and existing engineering context.
  - Complements direct CAD-control MCP servers: before editing geometry, an agent needs to understand project history and design intent.
  - Relevant to intelligent engineering workflows where revision context and artifact retrieval matter as much as command execution.
- Curation note: Early-stage repository; evaluate on a real CAD folder before treating it as a dependable workflow component.

## CFD MLOps surrogate framework

- Link: https://github.com/RishabhMalviya/cfd-mlops
- Type: CFD surrogate training pipeline / MLOps example
- Why it matters:
  - Combines car-mesh CFD surrogate modeling, Transolver-style architecture, PyTorch DDP, and Kubeflow Pipelines.
  - Useful as a concrete example of moving CFD-ML from notebook experiments toward reproducible training pipelines.
  - Shows the workflow layer needed around neural surrogates: distributed training, pipeline orchestration, and dataset/version discipline.
- Curation note: Very new and unproven; keep as a workflow pattern rather than a recommended dependency.

## FreeCAD Robust MCP server

- Link: https://github.com/spkane/freecad-addon-robust-mcp-server
- Type: FreeCAD MCP bridge / workbench addon
- Why it matters:
  - Exposes FreeCAD through an agent-callable MCP surface, reducing reliance on brittle GUI automation.
  - Useful comparison point for CAD-agent workflows where operations, screenshots, object state, and exports need to be explicit.
  - More active than many tiny FreeCAD MCP experiments, so it is worth testing first when evaluating CAD-agent infrastructure.
- Curation note: Validate on parametric parts and downstream STEP/STL export before recommending for lab use.

## CadQuery MCP server

- Link: https://github.com/mikekuniavsky/mcp-cadquery-server-public
- Type: MCP server for CadQuery artifact generation
- Why it matters:
  - Takes CadQuery code and returns 3MF, PNG, and GLB artifacts, which fits agentic CAD loops where code generation must be rendered and inspected.
  - CadQuery is attractive for CFD/CAE because parametric Python geometry can be versioned, swept, and regenerated.
  - Small early project, but the interface shape is useful for designing reproducible geometry-generation tools.

## sandraschi FreeCAD MCP

- Link: https://github.com/sandraschi/freecad-mcp
- Type: FreeCAD MCP server / webapp with CFD-extension ambition
- Why it matters:
  - Describes a FastMCP 3.2 server plus webapp for FreeCAD 3D CAD workflows, with FluidX3D/OpenFOAM CFD extensions in scope.
  - Useful signal that CAD MCP bridges are starting to target CAD-to-CFD handoff rather than only geometry creation.
  - Could inform a minimal FreeCAD → export → OpenFOAM/FluidX3D harness if the repo matures.
- Curation note: Very early repository with minimal adoption; inspect implementation before relying on it.

## CadGate

- Link: https://github.com/vericontext/cadgate
- Type: Verification gate for AI-generated CAD-as-code pull requests
- Why it matters:
  - Targets CadQuery/Build123d PR validation with geometric metric diffs, minimum-wall-thickness checks, DFM rules, and six-view rendered previews.
  - Strong pattern for agentic CAD workflows: generated geometry should enter through reproducible checks, not screenshots or trust in a chat transcript.
  - Relevant to CFD/CAE automation because CAD changes need dimensional, manufacturability, and export checks before meshing or simulation.
- Possible use: Adapt the idea into a GitHub Action for VA's CAD/CFD experiments: render, metric diff, export validation, and mesh-prep smoke test.
- Maturity: early open-source tool
- Priority: High

## TO-Agents

- Link: https://arxiv.org/abs/2605.21622
- Type: Multi-agent pipeline for preference-guided topology optimization
- Why it matters:
  - Converts natural-language design intent into validated topology-optimization solver inputs, renders the 3D result, then uses vision-language critique and a judge agent to revise solver parameters.
  - Directly addresses a real engineering-agent bottleneck: translating qualitative design preferences into controllable objective/constraint settings.
  - Useful reference for closed-loop design automation where solver artifacts, visual inspection, and parameter revision are all first-class.
- Possible use: Borrow the loop structure for CAD/CAE optimization experiments: intent contract → solver input → artifact render → critique → parameter update.
- Maturity: paper-only
- Priority: Medium

## Contractual Skills

- Link: https://arxiv.org/abs/2605.22634
- Type: GovernSpec-style framework for agent skill contracts
- Why it matters:
  - Proposes making goals, input boundaries, permissions, evidence requirements, output contracts, verification steps, approval points, and handoff rules inspectable inside skill files.
  - Maps well to engineering agents, where solver runs and CAD edits need explicit artifact requirements and human-approval boundaries.
  - Helpful framing for OpenClaw/ACP skill design: skills should define verifiable work contracts, not just loose instructions.
- Possible use: Define CFD/CAD skills with required artifacts such as `case_manifest.json`, `kpi_sources.json`, rendered previews, mesh checks, and rerun commands.
- Maturity: paper-only
- Priority: High

## sim-benchmark

- Link: https://github.com/svd-ai-lab/sim-benchmark
- Type: Solver-grounded benchmark for simulation agents
- Why it matters:
  - Benchmarks agents on real OpenFOAM and LTspice workflows with deterministic verification, not LLM-as-judge scoring.
  - Requires KPI values to include source provenance so the verifier can re-run extraction commands against produced artifacts.
  - Strong reference pattern for evaluating intelligent engineering agents: artifact correctness and reproducibility matter more than fluent explanations.
- Possible use: Adapt the result schema and provenance checks for VA's OpenFOAM/CAD-to-CAE agent experiments.
- Maturity: early benchmark
- Priority: High

## Agentic AI in Engineering and Manufacturing

- Link: https://arxiv.org/abs/2604.09633
- Type: Industry interview study / agentic engineering workflow adoption
- Why it matters:
  - Synthesizes 30+ stakeholder interviews across enterprises, smaller firms, AI developers, and CAD/CAM/CAE vendors.
  - Finds near-term value in structured repetitive work and data-intensive synthesis, while higher-value agentic gains require orchestrating multi-step workflows across tools.
  - Highlights the real blockers VA should design around: fragmented machine-unfriendly data, security/regulatory constraints, weak legacy APIs, verification, auditability, and human-in-the-loop review.
- Possible use: Use as a framing citation for why engineering agents need artifact contracts, provenance, and approval gates rather than autonomous black-box tool use.
- Maturity: qualitative study
- Priority: High

## FoamPilot

- Link: https://github.com/elotech47/foampilot_csc7644
- Type: Natural-language OpenFOAM agent prototype
- Why it matters:
  - Uses retrieval over official OpenFOAM tutorials, then copies and surgically edits a valid template case rather than generating solver files from scratch.
  - This template-first pattern is safer for OpenFOAM automation because syntax, file layout, and solver conventions start from known-good cases.
  - Useful precedent for lab workflows where agents should modify validated cases and report mesh/convergence/post-processing artifacts.
- Curation note: Student/project prototype; evaluate robustness before relying on it.
- Priority: Medium

## SolidworksMCP-TS

- Link: https://github.com/vespo92/SolidworksMCP-TS
- Type: TypeScript MCP server for SolidWorks COM automation
- Why it matters:
  - Exposes SolidWorks modeling, sketching, drawing, export, analysis, and macro/VBA generation through MCP over stdio.
  - The direct-COM vs generated-VBA fallback is a useful implementation pattern for CAD APIs with awkward parameter limits.
  - Explicitly alpha/experimental, but it maps the right engineering surface: geometry creation, drawings, exports, mass/interference checks, and geometry validation.
- Possible use: Track as a Windows/SolidWorks reference when designing deterministic CAD-agent interfaces with validation and export hooks.
- Maturity: alpha / experimental
- Priority: Medium

## neka-nat FreeCAD MCP

- Link: https://github.com/neka-nat/freecad-mcp
- Type: FreeCAD MCP addon and server
- Why it matters:
  - One of the more visible FreeCAD MCP implementations, with a FreeCAD workbench/addon, RPC server, Claude Desktop setup, text-only feedback mode, and remote-connection controls.
  - Demonstrates practical workflows such as flanges, toy cars, and CAD generation from 2D drawings.
  - Useful comparison point against more engineering-heavy FreeCAD MCP servers when choosing between visual feedback, text feedback, and operation-level tool surfaces.
- Possible use: Evaluate alongside build123d-mcp and FreeCAD Robust MCP on the same parametric part → STEP/STL export → meshability checklist.
- Maturity: active open-source MCP server
- Priority: Medium

## Explainable Model Predictive Control with Hierarchical Causal Abduction

- Link: https://arxiv.org/abs/2605.10624
- Type: Explainable control / MPC framework
- Why it matters:
  - Connects model predictive control actions to causal and physics-informed explanations rather than leaving optimizer outputs opaque.
  - Relevant to intelligent engineering workflows where an agent must justify control recommendations and expose safety/constraint reasoning.
  - Useful conceptual anchor for thermal/HVAC/plant-control demos with audit trails.
- Maturity: paper-only
- Priority: Medium

## ZWCAD Mechanical MCP

- Link: https://github.com/john0909/ZWCAD-Mechanical-MCP
- Type: MCP server for ZWCAD Mechanical CAD automation
- Why it matters:
  - Exposes 200+ CAD operations including 2D/3D drawing, dimensioning, blocks, layers, BOM/title blocks, transforms, views, LISP execution, import, and export.
  - Strong signal that vendor-specific CAD ecosystems are moving toward agent-readable operation surfaces.
  - Useful comparison point when designing safer FreeCAD/SALOME/OpenFOAM agent interfaces.
- Curation note: Vendor-specific and early; evaluate capability, safety boundaries, and reproducibility before using in a production workflow.
- Maturity: early open-source MCP server
- Priority: Medium

## TopSolid automation MCP

- Link: https://github.com/Julien38300/topsolid-automation-mcp
- Type: MCP server for TopSolid 7 CAD/PDM workflow
- Why it matters:
  - Attempts to connect MCP-compatible AI agents to TopSolid CAD/PDM operations.
  - Important because engineering agents need access to design context and PDM state, not just isolated geometry commands.
  - Useful workflow signal for CAD/PDM-aware research automation even if it is not an immediate lab dependency.
- Maturity: early community project
- Priority: Medium

## Agent-ready OpenAPI smell detection

- Link: https://arxiv.org/abs/2605.14312
- Type: Multi-agent documentation/API quality analysis for MCP-style tool exposure
- Why it matters:
  - Shows that stable REST APIs can still fail for agents when documentation lacks usable parameter semantics, examples, and task-planning affordances.
  - Directly relevant to engineering automation: CAD/CAE/OpenFOAM wrappers need agent-ready contracts, not only endpoints.
  - Useful checklist material before exposing internal lab tools through MCP or OpenAPI.
- Possible use: Audit OpenFOAM/CAD helper APIs for ambiguous parameters, missing schemas, unsafe defaults, and absent examples.
- Maturity: paper-only
- Priority: High

## SPIN structural planning for industrial agents

- Link: https://arxiv.org/abs/2605.14051
- Type: Validated DAG planning wrapper for industrial LLM agents
- Why it matters:
  - Enforces executable plan structure and repairs invalid DAGs before downstream tool execution.
  - Prefix-based execution control is attractive for expensive engineering workflows where an agent should stop once enough evidence exists.
  - Good pattern for CAD/mesh/solver pipelines: plan, validate, execute prefix, inspect artifacts, then continue only if needed.
- Possible use: Adapt the DAG contract idea to CAD-to-CFD workflows with explicit gates for geometry, mesh, solver, and post-processing.
- Maturity: paper-only
- Priority: Medium

## FermiLink

- Link: https://github.com/TaoELi/FermiLink
- Type: Agent framework for autonomous scientific simulations and HPC/workstation loops
- Why it matters:
  - Uses goal files, package knowledge bases, and long-running simulation loops for scientific computing workflows.
  - Supports local or HPC execution patterns and includes a code-optimization mode with deterministic benchmark/correctness checks.
  - Relevant as a higher-level harness pattern for multi-day CFD/thermal/SciML experiment campaigns.
- Possible use: Inspect as a reference design for VA-style goal-driven OpenFOAM/SciML campaigns with provenance and stop conditions.
- Maturity: early open-source / PyPI project
- Priority: Medium

## Lang2MLIP

- Link: https://arxiv.org/abs/2605.14527
- Type: Agentic workflow for machine-learning interatomic potential development
- Why it matters:
  - Turns MLIP development into a language-driven autonomous workflow spanning atomistic simulation, active learning, model training, and iteration.
  - Shows agentic SciML at the campaign-management layer rather than only as a coding assistant.
  - Useful pattern for CFD/SciML automation: propose cases, run trusted solvers, curate data, train surrogates, and report evidence.
- Possible use: Use as an analogy when designing an OpenFOAM/thermal surrogate campaign agent with explicit validation gates.
- Maturity: paper-only
- Priority: Medium

## Jarvis Onshape MCP

- Link: https://github.com/ReshefElisha/jarvis-onshape-mcp
- Type: MCP plugin for Onshape CAD automation
- Why it matters:
  - Exposes a real cloud CAD system through MCP/Claude Code rather than relying only on screenshots or mesh-only generation.
  - Combines vision decomposition, FeatureScript, and parametric iteration, which is closer to reusable engineering CAD than text-to-shape previews.
  - Strong signal that CAD agents need stable CAD APIs, editable construction history, and truth-telling about failed operations.
- Possible use: Compare its Onshape/FeatureScript loop with FreeCAD/CadQuery MCP approaches for CAD-to-CAE workflows.
- Maturity: early open-source tool
- Priority: High

## FreeCAD MCP with FluidX3D/OpenFOAM extensions

- Link: https://github.com/sandraschi/freecad-mcp
- Type: FreeCAD MCP server with CFD extension ambitions
- Why it matters:
  - Combines a FastMCP FreeCAD server/webapp with explicit FluidX3D and OpenFOAM extension direction.
  - Very early, but the CAD-to-CFD interface shape is directly aligned with VA's geometry → meshing → simulation automation interest.
  - Useful scouting target alongside more mature FreeCAD MCP servers to see which operations are essential for CFD handoff.
- Curation note: Low-star and early-stage; inspect before use, treat as a design signal rather than a dependable dependency.
- Priority: Medium

## Code as Agent Harness

- Link: https://arxiv.org/abs/2605.18747
- Type: Survey / framing paper for code-centered agent harnesses
- Why it matters:
  - Frames code as the operational substrate for agent reasoning, action, environment modeling, and execution-based verification.
  - Useful for engineering agents because CAD/CAE automation needs executable harnesses that expose state, artifacts, logs, and provenance.
  - Helps distinguish durable workflow infrastructure from chat-only prompting.
- Possible use: Use as a design reference for OpenFOAM/FreeCAD/SALOME harnesses where agents must act through auditable code and checks.
- Maturity: paper-only
- Priority: Medium

## PROTEA

- Link: https://arxiv.org/abs/2605.18032
- Type: Offline evaluation and iterative refinement for multi-agent LLM workflows
- Why it matters:
  - Scores intermediate workflow nodes and overlays failure evidence on the workflow graph instead of only judging final outputs.
  - Relevant to CAD→mesh→solve→postprocess pipelines where failures propagate and need localization.
  - The backward node-evaluation idea is useful when only final references or KPIs are available.
- Possible use: Borrow the node-level evaluation pattern for multi-step engineering-agent workflows and nightly regression tests.
- Maturity: paper-only
- Priority: Medium

## AutoCAD MCP Server

- Link: https://github.com/wade20250715/autocad-mcp-server
- Type: MCP bridge for AutoCAD automation
- Why it matters:
  - Early example of exposing DWG/AutoCAD operations through an agent-callable Model Context Protocol surface.
  - Useful signal that commercial CAD tools may become controllable through structured agent APIs rather than GUI macros alone.
  - Relevant to engineering workflow automation where CAD edits, drawing inspection, and artifact export should be explicit and logged.
- Curation note: Very early and low-signal repository; inspect security, API coverage, and reproducibility before any real use.

## TIA Portal MCP

- Link: https://github.com/Czarnak/tia-portal-mcp
- Type: MCP bridge for Siemens SIMATIC TIA Portal automation
- Why it matters:
  - Extends the MCP/control-surface pattern from CAD into industrial automation software.
  - Interesting for agentic engineering workflows where electrical/control logic, PLC projects, and mechanical/thermal design may eventually need connected automation.
  - Useful precedent for wrapping specialized engineering applications with safe, typed operations instead of brittle screen control.
- Curation note: Very early; treat as a workflow signal, not a dependable dependency.

## Firefly: verified tool-call data from real MCP servers

- Link: https://arxiv.org/abs/2605.17558
- Type: Tool-call data generation / MCP evaluation pipeline
- Why it matters:
  - Generates verified tool-call data by exploring real MCP servers and grounding tasks in observed API behavior.
  - Useful for engineering agents because simulator/CAD/CAE tool use fails on concrete API details, side effects, and artifact states that synthetic tasks often miss.
  - Suggests a practical pattern for lab tooling: first discover valid operations and outcomes, then synthesize training/evaluation tasks with checkable ground truth.
- Possible use: Adapt the idea to FreeCAD/OpenFOAM helper tools so agent benchmarks verify produced files, logs, and KPIs instead of relying on LLM-as-judge.
- Maturity: paper-only
- Priority: High

## mcp-cad

- Link: https://github.com/PaulGregoryBaker/mcp-cad
- Type: MCP layer for sheet-metal manufacturing orchestration
- Why it matters:
  - Early attempt to expose sheet-metal/manufacturing workflow operations as an agent-addressable MCP layer.
  - Interesting because sheet metal has hard manufacturing constraints, making it a better engineering-agent testbed than unconstrained visual CAD generation.
  - Treat as a workflow signal, not a dependency, until implementation surface, tests, and artifact validation are clearer.
- Maturity: very early open-source project
- Priority: Low

## ChainCaps

- Link: https://arxiv.org/abs/2605.26542
- Type: MCP proxy / composition-safe tool-use architecture
- Why it matters:
  - Addresses permission laundering, where individually allowed tools compose into an unsafe end-to-end effect.
  - Propagates sink-specific capability budgets by intersection so data can lose but not gain authority through tool chains.
  - Directly relevant to engineering agents that may combine CAD files, solver logs, local scripts, web APIs, and messaging surfaces.
- Possible use: Borrow the capability-attenuation pattern when designing CAD→CFD agents with file/export/network boundaries.
- Maturity: paper-only / reference proxy described
- Priority: High

## Device Context Protocol

- Link: https://arxiv.org/abs/2605.26159
- Type: Safety-first protocol for LLM-driven constrained-device control
- Why it matters:
  - Proposes compact device frames plus manifest-level capability scoping, type/range checks, dry-run evaluation, and units-as-types.
  - Relevant when LLM/agent workflows touch physical engineering systems such as fans, pumps, thermal rigs, sensors, or embedded controllers.
  - Good design language for keeping hallucinated or prompt-injected calls away from hardware.
- Possible use: Adapt the manifest/dry-run/unit-check pattern for lab automation tools before allowing real actuator control.
- Maturity: paper-only / reference firmware described
- Priority: Medium

## FreeCAD MCP Server by JakobThiessen

- Link: https://github.com/JakobThiessen/FreeCad_MCP_Server
- Type: FreeCAD MCP bridge / Sketcher, Part, and PartDesign automation
- Why it matters:
  - Connects AI assistants to a live FreeCAD instance through an MCP server and XML-RPC FreeCAD addon.
  - Useful comparison point for agent-readable parametric CAD control surfaces.
  - Early-stage and should be validated on dimensions, constraints, STEP/STL export, and downstream meshing before real CFD use.
- Maturity: early open-source prototype
- Priority: Medium

## ParaView-CLI

- Link: https://github.com/adricortes/Paraview-CLI
- Type: Headless ParaView / scientific visualization CLI for agents
- Why it matters:
  - Aims to expose VTK/VTU/OpenFOAM/Exodus/CGNS visualization through a pvpython server and lightweight client.
  - Useful for CFD agent workflows where post-processing and figures need to be scriptable, reproducible, and verifier-friendly.
  - Complements OpenFOAM automation: a solver run is not enough unless artifacts and visuals can be regenerated.
- Maturity: early open-source prototype
- Priority: Medium

## Physics Is All You Need? Physicist-supervised AI development of scientific software

- Link: https://arxiv.org/abs/2605.30353
- Type: Case study of AI coding agents for scientific software
- Why it matters:
  - Documents 12 work days and 57 agent sessions building CLAX-PT, a differentiable JAX scientific module, under physicist supervision.
  - Shows that oracle tests can miss physically invalid fixes: the agent optimized symptoms and even produced a calibrated correction with no physical meaning.
  - The useful guardrails are directly transferable to CAD/CFD agents: diverse parameter tests, shared changelogs, and explicit rules against unphysical numerical patches.
- Possible use: Add these guardrails to OpenFOAM/CAD automation agent prompts and review checklists.
- Maturity: case study
- Priority: High

## Unveiling Multi-regime Patterns in SciML

- Link: https://arxiv.org/abs/2605.29153
- Type: SciML optimization diagnostics / failure-mode analysis
- Why it matters:
  - Argues that SciML models can fall into distinct hyperparameter-dependent training regimes with different failure modes.
  - Useful caution against reporting only best-seed results for PINNs, neural operators, or surrogate models.
  - Supports regime-aware diagnostics for research agents that tune SciML experiments automatically.
- Possible use: Require experiment dashboards to show regime/failure-mode evidence, not only final validation loss.
- Maturity: paper-only
- Priority: Medium
## SchGen

- Link: https://arxiv.org/abs/2605.30345
- Type: LLM-based PCB schematic generation / semantic engineering representation
- Why it matters:
  - Converts natural-language hardware intent into editable PCB schematics using semantic editing primitives and pin-name-based wiring.
  - The key lesson is representation design: complex engineering artifacts are easier for LLMs when actions, connectivity, and constraints are explicit instead of buried in verbose geometry/tool syntax.
  - Useful analogy for CAD/CAE automation, where CadQuery/FreeCAD/OpenSCAD agents may need operation-level intermediate representations and validation hooks.
- Possible use: Borrow the semantic-operation representation idea when designing CAD-to-CFD agent interfaces.
- Maturity: paper-only
- Priority: Medium


## GPU Forecasters

- Link: https://arxiv.org/abs/2605.31464
- Type: LLM-based selective surrogate for GPU kernel runtime optimization
- Why it matters:
  - Treats language models as runtime forecasters for proposed GPU kernels, not only as kernel generators.
  - Useful when coding-agent/evolutionary kernel search can generate many candidates but real GPU compilation/execution is the bottleneck.
  - The selective/defer-to-GPU framing is a practical pattern for expensive engineering evaluation loops.
- Possible use: Explore as a prefilter for custom CUDA/JAX kernels in SciML workflows where measurement budget is limited.
- Maturity: paper-only
- Priority: Medium

## PithTrain

- Link: https://arxiv.org/abs/2605.31463
- Type: Agent-native MoE training framework / benchmark
- Why it matters:
  - Introduces agent-task efficiency as a metric for how easily coding agents can understand, operate, and extend a framework.
  - Useful meta-pattern for lab infrastructure: tooling should optimize for human readability, reproducibility, and agent-operability, not only raw throughput.
  - Relevant to future CFD/CAD automation stacks where agents will maintain scripts, pipelines, and validation harnesses.
- Possible use: Borrow the agent-operability checklist idea for CFD/thermal automation repositories.
- Maturity: paper-only
- Priority: Medium

## Knowledge-graph multi-agent framework for virtual commissioning models

- Link: https://arxiv.org/abs/2606.03255
- Type: Paper / industrial engineering multi-agent workflow
- Keywords: multi-agent system, knowledge graph, virtual commissioning, PLC, NX MCD, engineering automation
- One-line summary: Uses graph-grounded multi-agent workflows to understand production systems, generate executable NX Open scripts, and map PLC variables to simulation objects.
- Why it matters: It shows a practical pattern for agentic engineering: deterministic extraction into shared structured context first, then grounded generation and ranked mapping suggestions.
- Possible use: Adapt the pattern to CFD/CAE automation by extracting CAD, mesh, solver, and post-processing metadata into a graph before letting agents modify workflows.
- Maturity: paper-only
- Priority: Medium

## AAS-native automatic PDDL generation for production-system planning

- Link: https://arxiv.org/abs/2606.02167
- Type: Paper / digital-twin-to-planning workflow
- Keywords: Asset Administration Shell, PDDL, automated planning, digital twin, design automation
- One-line summary: Generates PDDL planning problems from standardized AAS capability models so engineers can evaluate production-system layouts without hand-writing planning domains.
- Why it matters: This is a clean example of turning engineering digital-twin metadata into executable planning artifacts, a pattern that can transfer to simulation workflow planning.
- Possible use: Use as an analogy for generating CFD/CAE workflow plans from structured asset/case metadata instead of raw natural-language prompts.
- Maturity: paper-only
- Priority: Medium
