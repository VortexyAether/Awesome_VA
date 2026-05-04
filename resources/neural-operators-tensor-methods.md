# Neural Operators & Tensor Methods

## Adaptive Patching for Tensor Train

- Source: shared PDF `2602.22372v2.pdf`
- Type: Tensor train / adaptive patching method
- Why it matters:
  - Tensor decompositions are relevant for high-dimensional Scientific ML, reduced-order modeling, and efficient operator representations.
  - Adaptive patching may be useful when dealing with localized structure in simulation fields.
- Follow-up:
  - Add arXiv link and summary after the PDF metadata is available.
  - Check whether the method can be connected to neural operator compression, surrogate modeling, or CFD field representation.

## Mamba-3

- Link: https://arxiv.org/abs/2603.15569
- Type: State-space / efficient sequence model
- Why it matters:
  - Mamba-style models are relevant when Transformer inference cost is too high.
  - Scientific ML may benefit from efficient long-context/state-tracking models for time-series simulation data, reduced-order modeling, or trajectory modeling.
- Note:
  - Not directly CFD-specific, but worth tracking for model architecture trends.

## NVIDIA PhysicsNeMo

- Link: https://github.com/NVIDIA/physicsnemo
- Type: Physics-ML framework
- Why it matters:
  - Industrially visible framework for physics-informed learning, neural operators, and surrogate modeling.
  - Useful reference for GPU-oriented SciML workflows and NVIDIA ecosystem integrations.
  - Installation and dependency assumptions should be checked before adopting in a lab workflow.

## neuraloperator

- Link: https://github.com/neuraloperator/neuraloperator
- Type: Neural operator library
- Why it matters:
  - Representative implementation family for Fourier Neural Operator and related operator-learning methods.
  - Useful baseline for PDE surrogate modeling and CFD-ML literature comparisons.
  - Helps keep neural-operator notes tied to a maintained implementation rather than only papers.

## PDEBench

- Link: https://github.com/pdebench/PDEBench
- Type: Scientific ML benchmark suite for PDEs
- Why it matters:
  - Provides benchmark datasets/tasks for comparing PINNs, neural operators, and PDE surrogate models.
  - Useful when deciding whether a CFD-ML method is actually improving over known baselines.
  - Keep distinct from solver resources: it is primarily benchmark/data infrastructure.

## JetSCI

- Link: https://arxiv.org/abs/2604.22087
- Type: Hybrid JAX-PETSc framework for scalable differentiable simulation
- Why it matters:
  - Connects JAX autodiff workflows with PETSc-scale solvers, a practical bridge for SciML beyond toy PDEs.
  - Relevant to inverse problems, surrogate training loops, and data-driven constitutive models that still need HPC-grade simulation infrastructure.
  - Worth tracking for CFD/heat-transfer groups that want differentiability without abandoning established solver ecosystems.

## MENO: MeanFlow-Enhanced Neural Operators

- Link: https://arxiv.org/abs/2604.06881
- Type: Neural operator architecture for dynamical systems
- Why it matters:
  - Targets the loss of high-frequency/small-scale content in Fourier-style neural operators.
  - Directly relevant to turbulent-flow surrogates, long-rollout stability, and reduced-order CFD modeling.
  - Good candidate for comparison against FNO-style baselines on unsteady flow datasets.

## SIMR-NO

- Link: https://arxiv.org/abs/2603.28073
- Type: Spectrally informed multi-resolution neural operator for turbulent-flow super-resolution
- Why it matters:
  - Focuses on reconstructing high-resolution turbulent fields from under-resolved observations.
  - Useful for LES/DNS data compression, sensor-to-field reconstruction, and CFD post-processing acceleration.
  - Spectral constraints make it more relevant than generic image super-resolution for fluid data.

## Predictivity and Utility of Neural Surrogates of Multiscale PDEs

- Link: https://arxiv.org/abs/2604.20061
- Type: Position/analysis paper on neural PDE surrogates
- Why it matters:
  - Pushes against overclaiming “universal emulator” results for multiscale PDEs.
  - Useful as a sanity-check citation when evaluating neural-operator CFD papers and benchmark claims.
  - Helps frame when surrogates are actually useful versus when they only exploit low-dimensional benchmark structure.


## Hybrid Fourier Neural Operator-Lattice Boltzmann Method

- Link: https://arxiv.org/abs/2604.27158
- Type: Hybrid neural-operator / Lattice Boltzmann CFD acceleration
- Why it matters:
  - Uses FNO initialization and rollout coupling to accelerate LBM for steady and unsteady weakly compressible flows.
  - Reports large convergence-speed gains while preserving final steady-state accuracy, making it more practical than a pure black-box surrogate.
  - Useful pattern for lab CFD: ML as an accelerator inside a trusted solver loop rather than a full solver replacement.

## LESnets for wall-bounded turbulence

- Link: https://arxiv.org/abs/2604.26621
- Type: Physics-informed neural operator for LES-style turbulence prediction
- Why it matters:
  - Targets 3D wall-bounded turbulent flows where limited data, multiscale vortices, and long-rollout stability are hard.
  - Integrates large-eddy-simulation ideas into a physics-informed neural-operator framework.
  - Good candidate for comparison when evaluating neural operators on high-Reynolds-number wall turbulence, not just toy PDEs.

## DeepPropNet

- Link: https://arxiv.org/abs/2604.27298
- Type: Operator-learning predictor for thermal plasma properties
- Why it matters:
  - Learns mappings from operating conditions to thermodynamic and transport properties that are expensive to evaluate repeatedly.
  - Directly relevant to thermal/heat-transfer adjacent simulation loops where material/property calls dominate runtime.
  - The single-property and mixture-of-experts variants are useful references for property-surrogate design.

## GeoFunFlow-3D

- Link: https://arxiv.org/abs/2604.23350
- Type: Physics-guided generative flow matching for 3D aerodynamic inference
- Why it matters:
  - Focuses on high-fidelity aerodynamic fields over complex geometries, with explicit attention to physical consistency and high-frequency features.
  - Combines flow matching, topology-aware spatial modeling, and a high-order discrete engine to reduce physics-gradient issues.
  - Relevant to CAD-to-CFD surrogate workflows where geometry complexity matters as much as field prediction accuracy.

## AI models of unstable flow exhibit hallucination

- Link: https://arxiv.org/abs/2604.20372
- Type: Reliability analysis for AI fluid-dynamics models
- Why it matters:
  - Shows visually plausible but physically impossible predictions in unstable viscous-fingering flows.
  - Useful cautionary citation for CFD-ML papers: field realism is not enough if conservation laws and instability physics fail.
  - Reinforces the need for physics checks, rollout diagnostics, and solver-in-the-loop validation.

## Faster by Design

- Link: https://arxiv.org/abs/2604.18491
- Type: Expert-validated CFD dataset and neural surrogate for interactive aerodynamics
- Why it matters:
  - Uses a parametric LMP2-class CAD model and expert-validated RANS data instead of overly smooth public car datasets.
  - Directly connects CAD complexity, CFD validation, and neural surrogates for fast aerodynamic design iteration.
  - Strong weekly-synthesis candidate for “engineering-grade datasets are the bottleneck for useful CFD surrogates.”
