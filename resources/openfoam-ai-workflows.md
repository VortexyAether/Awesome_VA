# OpenFOAM AI Workflows

AI-assisted OpenFOAM setup, automation, case validation, post-processing, and engineering workflow orchestration.

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

## AutoFOAM

- Link: https://github.com/AGN000/AutoFOAM
- Type: Self-refining autonomous OpenFOAM case-authoring agent
- Why it matters:
  - Targets natural-language-to-OpenFOAM workflows, including autonomous mesh generation through the gmsh OCC API.
  - Explicitly frames self-refinement and anti-collapse defenses, which are important for long-horizon CFD case setup agents.
  - Useful as a reference or stress-test target when comparing OpenFOAM MCP/plugin approaches, not yet as a trusted production workflow.
- Possible use: Evaluate generated cases against deterministic mesh/case validation gates and compare with sim-plugin-openfoam and AI CFD Scientist artifact contracts.
- Maturity: early open-source research prototype
- Priority: Medium

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
