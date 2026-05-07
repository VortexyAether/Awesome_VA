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

- Link: https://www.linkedin.com/posts/roman-likhachev-23a544174_part-1-using-claude-code-for-3d-cad-design-i-activity-7442571132618260480-GaND
- Type: LLM-assisted CAD design workflow
- Summary:
  - Claude Code writes Python geometry.
  - FreeCAD watches/renders the script in real time.
  - User iterates through conversation and exports printable parts.
- Why it matters:
  - Similar workflow could be adapted for CFD geometry prototyping.
  - Still requires human engineering judgment about dimensions, tolerances, and part fit.

## Corrected FreeCAD + Python + Claude Code workflow link

- Link: https://www.linkedin.com/posts/roman-likhachev-23a544174_part-1-using-claude-code-for-3d-cad-design-activity-7436038784623869952-7EVs?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD5oIrEBMTn8gvGtlY2eLkVvjVsMFaxHEgc
- Note:
  - Corrected LinkedIn URL for the FreeCAD + Python + Claude Code CAD workflow.

## Zero-to-CAD

- Link: https://arxiv.org/abs/2604.24479
- Type: Agentic synthesis of interpretable CAD programs
- Why it matters:
  - Focuses on CAD construction history / parametric program synthesis rather than only mesh or B-Rep outputs.
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
