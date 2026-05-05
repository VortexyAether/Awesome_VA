# Meshing & GPU Scientific Workflows

## NVIDIA PhysicsNeMo-Mesh

- Link: https://nvidia.github.io/physicsnemo/blog/2026/04/07/physicsnemo-mesh/
- Type: GPU-accelerated mesh processing for Scientific ML
- Why it matters:
  - Mesh generation and mesh processing are major bottlenecks in CFD/CAE workflows.
  - GPU-native mesh tooling could pair well with differentiable solvers and neural surrogate models.
  - Relevant to future workflows that combine meshing, AMR, CFD simulation, and neural operators.

## Classical mesh tools: Gmsh, SALOME, Pointwise

- Links:
  - Gmsh: https://gmsh.info/
  - SALOME: https://www.salome-platform.org/
  - Pointwise: https://www.pointwise.com/
- Type: Mesh generation and preprocessing tools
- Summary:
  - Gmsh, SALOME, and Pointwise are practical mesh tools used across CFD/CAE workflows.
  - SALOME can be powerful but often requires manual work.
  - Example context: airfoil mesh generation and OpenFOAM tutorials.
- Why it matters:
  - Modern CFD-ML workflows still depend on robust geometry and meshing pipelines.
  - Classical tools remain useful references even when exploring GPU/differentiable mesh workflows.
- Follow-up:
  - Collect concrete tutorials and reusable scripts for airfoil / conjugate heat transfer / OpenFOAM cases.

## Possible workflow direction

- Mesh generation / processing: PhysicsNeMo-Mesh or classical tools like SALOME/Gmsh/Pointwise
- Adaptive discretization: JAX-AMR / JANC-style AMR
- Solver layer: JAX-CFD or custom differentiable CFD solver
- Learning layer: neural operator / surrogate / control model

This is speculative, but the resource cluster points toward a more automated GPU-based CFD-ML pipeline.

## meshio

- Link: https://github.com/nschloe/meshio
- Type: Mesh file I/O converter
- Why it matters:
  - Practical bridge between mesh formats such as Gmsh, VTK, XDMF, and other CFD/FEA formats.
  - Useful for glue-code workflows where solvers, meshing tools, and post-processing libraries disagree on file formats.
