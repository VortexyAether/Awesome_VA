# Agent Tools & Research Workflow

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

## GPT subscription ecosystem tools

- Shared tools:
  - Code agents: Codex GUI/CLI, OpenCode CLI
  - Video/image generation: Sora
  - LaTeX alternative: Prism
  - macOS browser: Atlas
  - Browser automation agent: Operator
- Why it matters:
  - Useful map of tools available around GPT subscriptions.
  - Helps compare Claude Code / Codex / OpenCode workflows for research coding, writing, and automation.

## Mobile coding-agent / SSH workflow idea

- Source: shared note about mobile Claude Code SSH support.
- Why it matters:
  - If mobile coding agents support SSH robustly, remote experiment management from a phone becomes practical.
  - Relevant for launching/checking simulations away from workstation.

## Google Workspace CLI for coding agents

- Link: https://www.youtube.com/watch?v=Pq12GuQw0_c
- Type: Google Workspace CLI / coding-agent tool interface discussion
- Shared context:
  - The interesting part is not just human CLI usability, but that the structure appears friendly for coding agents.
  - Future open-source projects may improve AI accessibility by shipping MCP servers or agent-facing interfaces.
- Why it matters:
  - Agent-readable operational surfaces can make complex projects easier to run, inspect, and automate.
  - Good reference for designing lab tools that are usable by both humans and AI agents.

## Academic/research skills and harness collections

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
  - Pull only high-signal tools into Awosome_VA after direct evaluation or clear CFD/SciML relevance.
