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
