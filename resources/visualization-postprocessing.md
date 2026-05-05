# Visualization & Post-processing

## PyVista

- Link: https://github.com/pyvista/pyvista
- Type: Python 3D plotting and mesh analysis on VTK
- Why it matters:
  - Useful for quick CFD/mesh/volume visualization from Python workflows.
  - Complements ParaView rather than replacing it: good for automation, notebooks, and scripted post-processing.

## ParaView

- Link: https://github.com/Kitware/ParaView
- Type: Open-source scientific visualization application
- Why it matters:
  - Standard tool for CFD post-processing, field visualization, slices, contours, streamlines, and large scientific datasets.
  - Strong backend target for automated visualization pipelines and agent-controlled post-processing.

## ParaView MCP

- Link: https://github.com/llnl/paraview_mcp
- Type: MCP server for natural-language/multimodal control of ParaView
- Why it matters:
  - Provides a public, reusable bridge between LLM agents and ParaView.
  - Useful for CAD-to-CFD-to-visualization workflows where an agent needs to load results, inspect fields, and generate views.
