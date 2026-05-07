# Differentiable & Python PDE Solvers

JAX/Python PDE and CFD solver resources for differentiable simulation, AMR, inverse/design workflows, and fast research prototypes.

## JAX-AMR

- Link: https://github.com/Ashwin3919/JAX-amR
- Tech report / test cases: https://github.com/Ashwin3919/JAX-amR/blob/main/tech-report.md
- Type: JAX-based adaptive mesh refinement / differentiable CFD tooling
- Feature notes:
  - Adaptive mesh refinement
  - Dimensionless computation
  - Explicit time advancing with RK3
  - High-order spatial reconstruction with WENO-5
  - Lax-Friedrichs Riemann solver
  - Point-implicit chemical source advancing
  - CPU/GPU/TPU capability
  - Parallel computation on GPU/TPU for the core solver in the current version
- Why it matters:
  - Useful reference for AMR implementations in JAX.
  - Potential building block for differentiable CFD workflows.
  - Combines high-order finite-volume ingredients with accelerator-friendly implementation choices.
  - The test cases are useful for comparing solver behavior and AMR design choices.

## JANC

- Link: https://github.com/JA4S/JANC
- Type: Differentiable compressible reacting flow solver with JAX-based AMR
- Description:
  - “A cost-effective, differentiable compressible reacting flow solver featured with JAX-based adaptive mesh refinement.”
- Why it matters:
  - Directly relevant to compressible/reacting CFD + Scientific ML.
  - Good candidate for studying JAX-based solver design and GPU-friendly AMR.
  - Potential reference for coupling CFD solvers with neural operators or inverse/design workflows.

## JAXFLUIDS

- Link: https://github.com/tumaer/JAXFLUIDS
- Type: Differentiable fluid dynamics package in JAX
- Why it matters:
  - Directly relevant to differentiable CFD, inverse design, and ML-coupled solver experiments.
  - Useful comparison point for JAX-AMR/JANC-style accelerator-friendly CFD design.
  - Check documentation and example maturity before relying on it for production-grade studies.

## LEX v1.6.0

- Paper: https://doi.org/10.5194/gmd-19-1103-2026
- Journal page: https://gmd.copernicus.org/articles/19/1103/2026/
- Type: JAX-based large-eddy simulation model with GPU acceleration and automatic differentiation
- Why it matters:
  - Shows LES implemented in JAX for atmospheric turbulence/cloud and gray-zone modeling.
  - Combines GPU acceleration with automatic differentiation, making it relevant to learned SGS modeling.
  - Good bridge between differentiable CFD, climate/weather modeling, and physics-ML parameterization research.

## Solver-in-the-loop differentiable coastal hydrodynamics

- Link: https://arxiv.org/abs/2604.07129
- Type: End-to-end differentiable hydrodynamics / inverse-problem framework
- Why it matters:
  - Demonstrates a solver-in-the-loop route for inverse design/estimation problems where full model replacement is risky.
  - Coastal hydrodynamics is not heat transfer, but the pattern transfers to CFD inverse problems, bathymetry/geometry estimation, and engineering optimization loops.
  - Good reference for coupling differentiable programming with legacy numerical models.

## Learning subgrid interfacial area in two-phase flows

- Link: https://arxiv.org/abs/2604.23946
- Type: Learned closure / multiphase-flow subgrid modeling
- Why it matters:
  - Targets interfacial area density, a closure quantity that strongly affects heat and mass transfer in two-phase flows.
  - Emphasizes regime-dependent inductive bias rather than a generic black-box model.
  - Relevant to boiling, reactors, thermal systems, and multiphase CFD surrogate/closure work.

## google/jax-cfd

- Link: https://github.com/google/jax-cfd
- Type: JAX-based CFD framework / research prototype
- Why it matters:
  - Representative starting point for JAX-native CFD experiments.
  - Useful for differentiable simulation, ML-CFD prototypes, and educational solver studies.
  - Best treated as a research/prototyping framework rather than a production CFD solver.

## AeroJAX

- Link: https://github.com/arriemeijer-creator/AeroJAX
- Type: Experimental differentiable aerodynamics / JAX flow-simulation project
- Why it matters:
  - Targets real-time flow simulation, control, inverse design, and neural-operator integration.
  - Relevant to aircraft/control-oriented CFD-ML ideation.
  - Experimental and young; keep as a project to watch, not a validated solver baseline.

## LSTM-PINN for steady-state electrothermal transport

- Link: https://arxiv.org/abs/2604.14201
- Type: Physics-informed neural network for coupled heat/fluid/electric fields
- Why it matters:
  - Addresses strongly coupled heat transfer, fluid flow, and electric-potential transport where standard PINNs can struggle with multi-field scale imbalance.
  - Relevant to electronics cooling, electrothermal devices, and multiphysics thermal workflows.
  - Useful caution/comparison point for whether sequence-style memory helps preserve consistency in steady coupled PDE settings.
- Maturity: paper-only
- Priority: Medium

## Physics-informed ML for pouch-cell temperature estimation

- Link: https://arxiv.org/abs/2604.14566
- Type: Battery thermal-management surrogate / temperature estimator
- Why it matters:
  - Directly targets temperature estimation for pouch cells with indirect liquid cooling.
  - Practical thermal-management example where full finite-element simulation is too expensive for online use.
  - Good application anchor for physics-informed surrogates in battery and transport electrification workflows.
- Maturity: paper-only
- Priority: Medium
