# OpenFOAM AI Workflows

AI-assisted OpenFOAM setup, automation, case validation, post-processing, and engineering workflow orchestration.

## SoPlasmaFoam

- Link: https://arxiv.org/abs/2607.05137
- Type: OpenFOAM-based plasma solver infrastructure
- Keywords: OpenFOAM, plasma simulation, adaptive mesh refinement, PETSc, GPU, dielectric barrier discharge, streamer discharge
- One-line summary: Presents an OpenFOAM solver for streamer and dielectric barrier discharges with adaptive mesh refinement and PETSc/GPU-oriented infrastructure.
- Why it matters:
  - Engineering AI needs robust solver substrates that agents can call, validate, and package into reproducible workflows.
  - The interesting signal is solver-grade infrastructure: coupled plasma transport/Poisson physics, AMR, backend performance, and benchmark-style validation.
  - Useful reminder that “AI for engineering” often depends on making classical solvers more automatable, inspectable, and performance-aware.
- Caveat: Plasma-specific and not itself an AI-agent system; code URL, license, OpenFOAM version, and example cases need follow-up before lab adoption.
- Possible use: Track as a solver-infrastructure reference for agentic OpenFOAM workflows and validation-gated multiphysics case automation.
- Maturity: paper-only from current source check
- Priority: Medium

## OpenFOAM MCP Server

- Link: https://github.com/webworn/openfoam-mcp-server
- Type: Tool / MCP server
- Keywords: OpenFOAM, MCP, CFD education, error resolution, LLM agents
- One-line summary: An LLM-powered MCP server for OpenFOAM that focuses on CFD education, Socratic questioning, and expert-style error resolution.
- Why it matters: OpenFOAM has a steep setup/debugging curve; an MCP layer can expose solver diagnostics and case reasoning to AI assistants without relying on brittle terminal-only prompting.
- Possible use: Evaluate as a reference for agent-assisted OpenFOAM case setup, log diagnosis, educational tutoring, and future CAD→CFD workflow automation.
- Maturity: prototype
- Priority: High

## MetaOpenFOAM: an LLM-based multi-agent framework for CFD

- Link: https://arxiv.org/abs/2407.21320
- Code: https://github.com/Terry-cyx/MetaOpenFOAM
- Type: Paper / engineering AI agent workflow
- Keywords: OpenFOAM, LLM agents, multi-agent framework, CFD automation
- One-line summary: Proposes a multi-agent LLM framework for automating parts of OpenFOAM-based CFD workflows.
- Why it matters: Directly relevant to agentic CFD workflow automation, especially case setup, execution, debugging, and post-processing around existing solvers.
- Possible use: Use as a reference when designing CAD→CFD→visualization orchestration agents or comparing MCP-based OpenFOAM automation approaches.
- Maturity: prototype
- Priority: High

## AI CFD Scientist

- Link: https://arxiv.org/abs/2605.06607
- Code: https://github.com/csml-rpi/AI-CFD-Scientist
- Type: Agentic CFD research pipeline / OpenFOAM workflow
- Why it matters:
  - Connects literature-grounded ideation, OpenFOAM execution, mesh-independence checks, diagnostic interpretation, source-code modification, figure generation, and LaTeX drafting in one inspectable workflow.
  - The repository exposes both a LangGraph orchestrator and skill-driven artifact contracts such as `lit.json`, `requirements.json`, `selected_mesh_spec.json`, and `analysis.json`.
  - Useful reference for VA-style intelligent engineering workflows because it treats solver artifacts and physics checks as first-class outputs, not just chat responses.
- Possible use: Compare its artifact schema and mesh/diagnostic gates against sim-benchmark/FoamPilot when designing a safer OpenFOAM agent harness.
- Maturity: early open-source research prototype
- Priority: High

## sim-plugin-openfoam

- Link: https://github.com/svd-ai-lab/sim-plugin-openfoam
- Related: https://github.com/svd-ai-lab/sim-cli · https://github.com/svd-ai-lab/sim-benchmark
- Type: OpenFOAM plugin for solver-grounded AI agent workflows
- Why it matters:
  - Lets AI coding agents operate OpenFOAM through `sim-cli`, with emphasis on running cases, inspecting results, and producing replayable CFD artifacts.
  - Complements AI CFD Scientist and FoamPilot by focusing on deterministic verification and artifact contracts rather than only natural-language interaction.
  - Useful pattern for lab-safe OpenFOAM automation: require rerunnable commands, KPI provenance, and structured outputs before trusting an agent's summary.
- Possible use: Evaluate as a reference interface for VA's OpenFOAM agent harness and compare its artifact schema with sim-benchmark.
- Maturity: early open-source plugin
- Priority: High

## AutoFOAM (paper + agent) — OOD execution gates and Physics-Validation Gap

- Link: https://arxiv.org/abs/2608.00003
- Code: https://github.com/AGN000/AutoFOAM
- Cases: https://github.com/AGN000/FoamAgentCases
- Type: Paper + self-refining autonomous OpenFOAM case-authoring agent
- Keywords: OpenFOAM, LLM agent, self-evolution, OOD execution, FOAM FATAL, solver routing, physics-validation gap, mesh templates
- One-line summary: Fine-tunes an LLM OpenFOAM agent on 252 prompts across 7 solvers and 13 mesh templates, then reports OOD execution metrics while explicitly separating run success from physics fidelity.
- Why it matters:
  - Moves NL→OpenFOAM automation from demo videos to tabulated OOD gates: 110/110 cases without FOAM FATAL, 106/110 exact solver routing (96.4%), mean execution reward r=0.64.
  - Seven-layer self-evolution (surgical FATAL patch, DPO when enough pairs, anchor mix, active learning on weakest family) is a reusable harness shape for long-horizon case setup.
  - Authors keep a **Physics-Validation Gap**: compile/run success is not residual, y⁺, or QoI acceptance — the right framing for Urban_Flighter / OpenFOAM agent checklists.
- Caveat: Main agent repo still license-null and low stars at 2026-08-09 refresh; FoamAgentCases is MIT. Do not treat FATAL-free rates as physics green lights.
- Possible use: Cite when defining agent acceptance as dual-layer (execution gates + physics QoI). Stress-test against sim-plugin-openfoam / AI CFD Scientist artifact contracts; Save product path only after license clarifies.
- Maturity: paper + early open-source research prototype
- Priority: High

## CFDTwin

- Link: https://arxiv.org/abs/2605.27725
- Type: GUI and Python toolkit for POD-NN surrogate modeling of ANSYS Fluent simulations
- Why it matters:
  - Turns expensive Fluent CFD result sets into POD-NN surrogate assets for design optimization, uncertainty analysis, and digital-twin workflows.
  - Important less because POD-NN is novel and more because the work packages surrogate modeling as an engineer-facing GUI/Python toolkit.
  - Useful reference for designing similar OpenFOAM/ParaView surrogate asset workflows with metadata, validation, and operating-envelope checks.
- Possible use: Build an OpenFOAM analogue that stores case metadata, geometry parameters, POD basis, neural network weights, and validation plots as one reproducible artifact.
- Maturity: paper / open-source toolkit announced
- Priority: High
