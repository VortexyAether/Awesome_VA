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

## Foundational thermal model for residential buildings

- Link: https://arxiv.org/abs/2605.01364
- Type: Physics-informed transformer for building thermal dynamics
- Why it matters:
  - Targets calibration-light or zero-shot transfer across buildings, climates, and control strategies rather than one-building curve fitting.
  - Embeds derivative enrichment, Euler-style integration, static building features, and temporal attention into a thermal dynamics model.
  - Useful application anchor for thermal digital twins where sensor coverage and building-specific calibration are practical bottlenecks.
- Maturity: paper-only
- Priority: Medium

## Hybrid ML and physical modeling for continuous-fiber composite 3D printing

- Link: https://arxiv.org/abs/2605.03186
- Type: Hybrid physics/data-driven manufacturing model
- Why it matters:
  - Models feedstock deformation in robotic 3D printing using physical viscoelastic components plus neural ODEs for drying and crystallization behavior.
  - Connects thermal stresses, residual-stress relief, material state evolution, and robotic path planning in a practical manufacturing setting.
  - Relevant to intelligent engineering workflows where process planning needs a fast but physics-grounded digital twin.
- Maturity: paper-only
- Priority: Medium

## Physics-based Digital Twins for Integrated Thermal Energy Systems

- Link: https://arxiv.org/abs/2605.06756
- Type: Active-learning digital twin for thermal energy systems
- Why it matters:
  - Couples Modelica system simulation with SINDyC, probabilistic MvG-SINDyC, FNN, and GRU surrogates for real-time supervisory control.
  - Demonstrates active learning on a glycol heat-exchanger subsystem, reducing required simulation trajectories to roughly one-fifth versus random sampling while preserving key heat-transfer outputs.
  - Strong thermal/control signal because it compares interpretable, probabilistic, and neural surrogates under data-efficiency constraints rather than only reporting black-box accuracy.
- Possible use: Use as an application anchor for thermal digital-twin proposals and for active-learning data selection in heat-transfer/control surrogates.
- Maturity: paper-only
- Priority: High

## Reduced-Order Modeling of Parameterized Visco-Plastic Shallow Flows

- Link: https://arxiv.org/abs/2605.06526
- Type: Non-intrusive reduced-order model for non-Newtonian shallow flows
- Why it matters:
  - Targets Herschel-Bulkley free-surface flows with moving fronts, yield surfaces, and nonsmooth rheology.
  - Useful reminder that tensor/ROM approaches can still be competitive for structured parameterized flow families where neural operators are not automatically the best tool.
  - Relevant to slurry, lava, debris-flow, coating, and other industrial non-Newtonian flow surrogates.
- Possible use: Compare ROM-style parameter-to-field reconstruction with FNO/GNO baselines on non-Newtonian or shallow-flow datasets.
- Maturity: paper-only
- Priority: Medium

## Fast prediction of lattice thermal conductivity with ML surrogates

- Link: https://arxiv.org/abs/2605.11610
- Type: Materials/thermal-property surrogate
- Why it matters:
  - Targets lattice thermal conductivity prediction, an expensive bottleneck in materials screening and thermal design.
  - Relevant to heat-transfer workflows where material-property evaluation feeds into downstream simulation or optimization loops.
  - Useful thermal-adjacent reminder that surrogate modeling is not only field prediction; property and closure models can also be high-leverage acceleration points.
- Possible use: Track for thermal-material screening and property-surrogate references.
- Maturity: paper-only
- Priority: Medium

## Real-time control of multiphase processes with learned operators

- Link: https://arxiv.org/abs/2603.25308
- Type: Learned-operator control for multiphase processes
- Why it matters:
  - Puts learned operators inside a real-time control setting for nonlinear multiphase dynamics, not just offline prediction.
  - Relevant to thermal-fluid process control where sensors are sparse and phase transitions make classical reduced models brittle.
  - Good anchor for thinking about surrogate-in-the-loop MPC and closed-loop validation.
- Possible use: Review when designing a control benchmark around two-phase cooling, reactor flow, or multiphase process optimization.
- Maturity: paper-only
- Priority: High

## Chrono-Gymnasium

- Link: https://arxiv.org/abs/2605.14911
- Type: Distributed high-fidelity mechanical simulation framework
- Why it matters:
  - Wraps Project Chrono multibody dynamics in a Gymnasium-compatible distributed framework using Ray.
  - Useful workflow pattern for solver-backed RL and optimization in mechanical systems.
  - Not CFD-specific, but relevant to engineering-agent benchmarks where an agent must run high-fidelity simulators and report verifiable artifacts.
- Possible use: Study its Gymnasium/Ray interface pattern for future OpenFOAM or FluidX3D reinforcement-learning/control wrappers.
- Maturity: paper/framework
- Priority: Medium

## Therm-FM

- Link: https://arxiv.org/abs/2605.22663
- Code/model repo: https://github.com/haiyangxin/Therm-FM
- Type: PDE-foundation-model adaptation for 3D-IC thermal simulation
- Why it matters:
  - Adapts a pretrained PDE foundation model to steady-state and transient chip-level heat conduction instead of training a thermal predictor from scratch per design.
  - Uses thermal-equivalent multi-fidelity training: low-cost approximate simulations for domain adaptation plus limited high-fidelity samples for calibration.
  - Highly relevant to electronics cooling and heat-transfer surrogate workflows where cross-design reuse and sample efficiency are more important than one-off benchmark accuracy.
- Possible use: Build a small heat-conduction adaptation benchmark that reports target-design samples required, cross-geometry error, and calibration cost.
- Maturity: paper + GitHub repo
- Priority: High

## PINNsur: Physics-Informed Neural Networks for PDEs on Curved Surfaces

- Link: https://arxiv.org/abs/2605.27308
- Type: PINN framework for surface PDEs / geometry processing
- Why it matters:
  - Uses a neural field for surface normals and projects ambient-space derivatives onto curved surfaces.
  - Relevant to CAD/CAE geometries where surface PDEs, shell-like thermal problems, and mesh quality can dominate solver behavior.
  - Good reminder that geometry representation is part of the SciML problem, not only the network architecture.
- Possible use: Prototype curved-surface heat diffusion on FreeCAD-generated geometry and compare against FEM under mesh-quality perturbations.
- Maturity: paper-only
- Priority: Medium

## Collocation-DG equivalence for SBP spectral operators

- Link: https://arxiv.org/abs/2605.27327
- Type: Numerical-methods paper / discontinuous Galerkin and collocation equivalence
- Why it matters:
  - Shows when a summation-by-parts spectral collocation scheme is equivalent to DG semi-discretization with the same quadrature.
  - Useful for differentiable solver and neural-surrogate work that builds on DG/collocation operators: discretization equivalence and nullspace modes should be explicit.
  - Reinforces that solver-assisted ML needs a clear numerical contract, not only neural architecture claims.
- Maturity: paper-only
- Priority: Medium
