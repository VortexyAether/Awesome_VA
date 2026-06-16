# Neural Operators & Tensor Methods

## PhysGuard

- Link: https://arxiv.org/abs/2606.16602
- Type: Sim-to-real adaptation method for neural PDE surrogates
- Keywords: neural operators, sim-to-real, Fisher information, gradient projection, physics preservation
- One-line summary: Uses empirical Fisher information from simulation data to identify physics-critical parameter directions and constrain fine-tuning on limited real/experimental data.
- Why it matters:
  - Neural operators often need lab or operational calibration, but naive fine-tuning can destroy the physical representations learned from simulation.
  - Provides a concrete lens for “safe adaptation” of CFD/thermal surrogates under sim-to-real shift.
  - Useful addition to validation gates: adaptation should improve real-data fit without degrading conservation, boundary behavior, spectra, or core-regime accuracy.
- Possible use: Test naive fine-tuning vs Fisher-protected adaptation on heat-transfer or simple flow surrogates with a small real/noisy observation set.
- Maturity: paper-only
- Priority: High

## Decision-Weighted Flow Matching

- Link: https://arxiv.org/abs/2606.16790
- Type: Regret-aligned generative modeling for stochastic optimization
- Keywords: flow matching, contextual stochastic optimization, decision regret, scenario generation
- One-line summary: Reweights the flow-matching objective by decision-sensitive endpoint information so scenario generators focus on samples that affect downstream optimization decisions.
- Why it matters:
  - In engineering design/control, a surrogate or generator can have good distributional fit but still induce poor decisions in sensitive regions.
  - Offers a useful training/evaluation lens: report downstream regret or objective degradation in addition to field/sample fidelity.
  - Potentially relevant to uncertainty-aware CFD/thermal design-space exploration where rare but decision-critical cases dominate risk.
- Possible use: Add a decision-regret metric to surrogate-assisted optimization benchmarks and compare against unweighted generative baselines.
- Maturity: paper-only
- Priority: Medium

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

## Time-Dependent PDE-Constrained Optimization via Weak-Form Latent Dynamics

- Link: https://arxiv.org/abs/2605.20639
- Type: Weak-form latent-space reduced-order model for PDE-constrained optimization
- Why it matters:
  - Targets repeated forward and sensitivity solves in high-dimensional, time-dependent PDE optimization.
  - Relevant to CFD/thermal design loops where the useful question is optimum quality under a simulation budget, not only field-level prediction error.
  - Good comparison point against neural-operator and classical ROM baselines for control/design tasks.
- Possible use: Build a small heat-transfer or cavity-flow optimization benchmark that reports solve budget, optimum quality, and validation error.
- Maturity: paper-only
- Priority: High

## Wavelet Flow Matching for Multi-Scale Physics Emulation

- Link: https://arxiv.org/abs/2605.16573
- Type: Generative multi-scale physics emulator
- Why it matters:
  - Uses wavelet/latent flow-matching ideas to preserve fine-scale structures while avoiding the cost of heavy iterative generative sampling.
  - Relevant to turbulence, climate, and thermal-field emulation where deterministic surrogates often over-smooth small scales.
  - Useful signal for evaluating generative surrogates on rollout stability and spectral/fine-scale diagnostics, not only visual quality.
- Possible use: Compare against FNO/latent-diffusion-style baselines on multi-scale fluid or thermal datasets with spectral metrics.
- Maturity: paper-only
- Priority: Medium

## Symmetry in the Wild

- Link: https://arxiv.org/abs/2605.18816
- Type: Equivariance analysis for neural fluid surrogates
- Why it matters:
  - Studies whether equivariance helps neural fluid surrogates under realistic CFD constraints such as large surface/volume meshes and bespoke architectures.
  - Useful antidote to over-general claims that symmetry-aware models automatically solve engineering-scale surrogate problems.
  - Directly relevant to aerodynamic surrogate modeling where geometry, mesh scale, and architecture interact.
- Possible use: Use as a reading anchor when deciding whether to add equivariant layers to CAD/mesh-to-field surrogate experiments.
- Maturity: paper-only
- Priority: Medium


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

## Fourier Neural Operator for Parametric Partial Differential Equations

- Link: https://arxiv.org/abs/2010.08895
- Code: https://github.com/neuraloperator/neuraloperator
- Type: Paper / neural operator
- Keywords: Fourier neural operator, operator learning, PDE surrogate, spectral methods
- One-line summary: Introduces Fourier Neural Operators for learning mappings between function spaces in parametric PDE problems.
- Why it matters: FNO is one of the core baselines for neural-operator CFD/SciML work, especially for grid-based PDE surrogate modeling and spectral field learning.
- Possible use: Use as a baseline method when comparing neural operators for flow prediction, super-resolution, or parameter-to-field surrogate modeling.
- Maturity: maintained library
- Priority: High

## Zero-shot generalization of transformer neural operators to larger domains

- Link: https://arxiv.org/abs/2606.14597
- Type: Neural-operator generalization study
- Keywords: transformer neural operator, zero-shot generalization, larger domains, PDE, domain shift
- One-line summary: Studies whether transformer neural operators trained on one spatial domain size can generalize zero-shot to larger domains.
- Why it matters:
  - Engineering use often trains on a smaller lab/simulation domain and then wants to transfer to larger devices or geometry extents.
  - Domain-size extrapolation is different from random parameter interpolation and should be tracked as its own failure mode.
  - Useful for VA surrogate benchmarks where geometry/domain scaling matters as much as boundary-condition variation.
- Possible use: Add a domain-size extrapolation split to heat-equation, Navier-Stokes, or advection-diffusion neural-operator experiments.
- Maturity: paper-only
- Priority: Medium

## DeepONet: Learning nonlinear operators via the universal approximation theorem of operators

- Link: https://www.nature.com/articles/s42256-021-00302-5
- Code: https://github.com/lululxvi/deeponet
- Type: Paper / neural operator
- Keywords: DeepONet, operator learning, Scientific Machine Learning, PDE surrogate
- One-line summary: Introduces DeepONet as a neural-network architecture for learning nonlinear operators between function spaces.
- Why it matters: DeepONet is a foundational operator-learning architecture and an important comparison point against FNO-style methods.
- Possible use: Use in literature reviews to explain the operator-learning family and compare branch/trunk operator models against spectral neural operators.
- Maturity: prototype
- Priority: High

## Learning Mesh-Based Simulation with Graph Networks

- Link: https://arxiv.org/abs/2010.03409
- Code: https://github.com/google-deepmind/deepmind-research/tree/master/meshgraphnets
- Type: Paper / graph neural simulation
- Keywords: MeshGraphNets, graph neural networks, unstructured mesh, learned simulation
- One-line summary: Learns simulation dynamics directly on mesh-based physical systems using graph networks.
- Why it matters: Many engineering CFD/CAE problems live on irregular meshes, so MeshGraphNets is a key reference for geometry-aware and mesh-aware learned simulation.
- Possible use: Use as a conceptual baseline for CAD/mesh-to-field surrogate modeling and for thinking about learned simulators on unstructured CFD domains.
- Maturity: prototype
- Priority: High

## Mesh Based Simulations with Spatial and Temporal awareness

- Link: https://arxiv.org/abs/2605.01542
- Type: Mesh-based CFD surrogate / GNN-Transformer paper
- Why it matters:
  - Targets a practical bottleneck in mesh-based CFD surrogates: models need awareness of both local spatial structure and temporal rollout context.
  - ICML 2026 signal from the arXiv metadata makes it worth tracking as a higher-visibility learned-simulation direction.
  - Relevant to unstructured CFD meshes where naive frame-to-frame predictors often lose stability or miss long-time behavior.
- Possible use: Compare against MeshGraphNets-style baselines for time-dependent CFD surrogate experiments.
- Maturity: paper-only
- Priority: High

## ALE-Consistent Graph Neural Operator-Transformer for FSI

- Link: https://arxiv.org/abs/2605.00937
- Type: Graph neural operator / Transformer for fluid-structure interaction
- Why it matters:
  - Uses an ALE-consistent framing for long-term FSI prediction on deforming unstructured meshes.
  - Directly relevant to engineering CFD where mesh motion and coupled structures break assumptions of fixed-grid neural operators.
  - Good candidate for tracking whether operator models can survive realistic geometry/motion coupling.
- Possible use: Reference for moving-mesh FSI surrogate modeling and CAD/CAE workflows with deforming boundaries.
- Maturity: paper-only
- Priority: High

## Droplet-LNO

- Link: https://arxiv.org/abs/2604.20993
- Type: Physics-informed Laplace neural operator for droplet spreading
- Why it matters:
  - Focuses on droplet dynamics on complex surfaces, touching microfluidics, spray cooling, inkjet printing, and wetting-driven thermal applications.
  - Laplace/operator formulation is useful to compare against Fourier-style methods when boundaries and surface complexity matter.
  - Strong thermal/heat-transfer adjacency because droplet spreading is central to cooling and phase-change workflows.
- Possible use: Track for surface-aware multiphysics surrogate modeling and spray-cooling literature review.
- Maturity: paper-only
- Priority: Medium

## Neural operator framework for stability and receptivity discovery

- Link: https://arxiv.org/abs/2604.19465
- Type: Neural operator for data-driven stability/receptivity analysis
- Why it matters:
  - Connects operator learning to stability and receptivity, not just field forecasting.
  - Relevant for flow-control and sensitivity-analysis workflows where engineers care about perturbation growth and dominant response modes.
  - Useful bridge between classical resolvent/stability analysis and data-driven surrogates when equations or linearizations are unavailable.
- Possible use: Watch as a possible method for control-oriented CFD-AI projects.
- Maturity: paper-only
- Priority: High

## ZNO: Stable Rational Neural Operators in the Z-Domain

- Link: https://arxiv.org/abs/2605.02356
- Type: Stable rational neural operator for discrete-time dynamics
- Why it matters:
  - Targets discrete-time system-identification and control settings where many continuous-time neural-operator assumptions are awkward.
  - Enforces stability through unit-disk pole constraints and gives interpretable learned poles for long-memory dynamics.
  - Relevant to control-oriented CFD/thermal surrogates, especially when the learned model must remain stable over many steps.
- Possible use: Compare against state-space models and neural operators for long-horizon sensor-to-state forecasting tasks.
- Maturity: paper-only
- Priority: High

## Horizon-agnostic neural operator safety filter

- Link: https://arxiv.org/abs/2605.01069
- Type: Neural operator + control barrier function for safe deformable/fluid manipulation
- Why it matters:
  - Learns boundary input-output PDE dynamics while enforcing explicit task-level safety constraints online.
  - Combines a horizon-agnostic neural operator with a lightweight QP safety filter, making it closer to deployable control than reward-shaped policies.
  - Conceptually relevant to CFD/thermal design campaigns where exploration must avoid unsafe or invalid states.
- Possible use: Use as a reference for safe control layers around learned PDE surrogates.
- Maturity: paper-only
- Priority: Medium

## Physical Fidelity Reconstruction via Consistency-Distilled Flow Matching

- Link: https://arxiv.org/abs/2605.05975
- Type: One-step generative flow reconstruction / consistency distillation
- Why it matters:
  - Distills an optimal-transport flow-matching teacher into a compact one-step model for coarse-to-fine flow reconstruction.
  - Directly targets latency-sensitive workflows such as real-time visualization, ensemble forecasting, and simulation-in-the-loop inference.
  - Evaluated on Smoke Buoyancy, Turbulent Channel Flow, and Kolmogorov Flow, making it more CFD-relevant than generic image diffusion work.
- Possible use: Test as a post-processing accelerator for low-resolution CFD fields or sensor/coarse-grid-to-field reconstruction.
- Maturity: paper-only
- Priority: High

## Do Neural Operators Forget Geometry?

- Link: https://arxiv.org/abs/2605.05862
- Type: Reliability / geometry-awareness analysis for neural operators
- Why it matters:
  - Formalizes “geometric forgetting”: deep operator layers can progressively lose domain-geometry information.
  - Highly relevant to irregular geometry, CAD-to-CFD surrogates, and mesh-aware operator learning where geometry cannot be treated as one-time context.
  - Proposes lightweight geometry memory injection and suggests a practical validation probe for neural-operator architectures.
- Possible use: Add geometry-retention diagnostics when comparing FNO/attention/operator models on CAD or unstructured-mesh CFD data.
- Maturity: paper-only
- Priority: High

## AeroJEPA

- Link: https://arxiv.org/abs/2605.05586
- Type: JEPA-style aerodynamic field surrogate
- Why it matters:
  - Predicts semantic latent representations of 3D aerodynamic fields from geometry and operating-condition context instead of directly predicting huge full-resolution fields.
  - Targets realistic large-field regimes through HiLiftAeroML and broad transonic-wing generalization through SuperWing.
  - Useful direction for design optimization because the latent space is meant to support analysis and optimization, not only reconstruction.
- Possible use: Track as a candidate architecture pattern for scalable 3D aerodynamic design loops.
- Maturity: paper-only
- Priority: High

## MeLISA: One-Step Generative Modeling for Dynamical Forecasting

- Link: https://arxiv.org/abs/2605.05540
- Type: One-step generative surrogate for autoregressive dynamical systems
- Why it matters:
  - Addresses the gap between cheap but drifting neural-operator rollouts and expensive multi-step diffusion/generative surrogates.
  - Uses pixel-space MeanFlow with consistency losses to preserve long-trajectory statistics in turbulent regimes.
  - Relevant to unsteady CFD surrogate modeling where long-horizon statistical fidelity matters more than a single-step RMSE.
- Possible use: Compare against FNO/MENO-style baselines on turbulent-flow rollout benchmarks.
- Maturity: paper-only
- Priority: Medium

## Context Flux Neural Operator

- Link: https://arxiv.org/abs/2605.05488
- Code: https://github.com/xx257xx/CONTEXT_FLUX_NO
- Type: Context-conditioned flux neural operator for conservation laws
- Why it matters:
  - Combines finite-volume-inspired Flux NO with recurrent ViT context injection to infer solution dynamics across conservation-law families.
  - Preserves the solver-assist flavor of flux/operator methods while reducing reliance on explicitly supplied PDE coefficients.
  - Interesting foundation-model direction for conservative systems where robustness and long-time prediction are critical.
- Possible use: Use as a baseline/reference for conservation-law surrogate experiments and solver-in-the-loop SciML designs.
- Maturity: paper + code
- Priority: High

## RETO: Rotary-Enhanced Transformer Operator for automotive aerodynamics

- Link: https://arxiv.org/abs/2605.00062
- Type: Transformer neural operator for aerodynamic field prediction
- Why it matters:
  - Targets high-fidelity automotive aerodynamics on ShapeNet and DrivAerML-like settings.
  - Uses global sinusoidal-cosine references plus RoPE-style relative spatial encoding to improve local gradient and displacement awareness.
  - Relevant to CAD/geometry-conditioned CFD surrogates where spatial correlations matter more than generic image-like field prediction.
- Possible use: Compare against Transolver/FNO/GNO baselines on automotive or external-aero surrogate tasks.
- Maturity: paper-only
- Priority: High

## Nested Fourier-enhanced neural operator for radiation transfer in fires

- Link: https://arxiv.org/abs/2604.13919
- Type: Neural operator surrogate for radiative heat transfer / fire CFD
- Why it matters:
  - Targets radiative transfer, often the dominant heat-transfer cost in fire simulations, rather than only generic velocity/pressure field forecasting.
  - Uses a Fourier-enhanced multiple-input neural-operator formulation and extends from small 2D pool-fire tests toward 3D CFD fire simulations.
  - Strong thermal/heat-transfer signal for solver-acceleration workflows where a learned component replaces an expensive sub-model inside a larger CFD code.
- Possible use: Track as a candidate pattern for coupling neural operators to radiation or property submodels while preserving the surrounding CFD solver.
- Maturity: paper-only
- Priority: High

## Reduced-order modeling of parameterized visco-plastic shallow flows

- Link: https://arxiv.org/abs/2605.06526
- Type: Tensor reduced-order model for nonlinear free-surface flows
- Why it matters:
  - Handles Herschel-Bulkley shallow flows with moving fronts, yield surfaces, and non-smooth rheology — a harder surrogate target than smooth benchmark PDEs.
  - Uses low-rank tensor/HOSVD-style compression over structured parameter spaces for rapid online reconstruction without reduced time integration.
  - Useful reminder that classical ROM/tensor methods remain competitive for design loops when the parameter space is structured and solver calls are expensive.
- Possible use: Compare tensor ROM against neural operators for parametric non-Newtonian or slurry/free-surface flow screening tasks.
- Maturity: paper-only
- Priority: Medium

## Real-time HR flow-field estimation from event-based imaging velocimetry

- Link: https://arxiv.org/abs/2605.04186
- Type: Sensor-to-field reconstruction / ROM estimation
- Why it matters:
  - Converts low-resolution real-time EBIV snapshots into high-resolution velocity fields and POD coordinates.
  - Combines LR-to-HR mapping with temporal regularization/Kalman-style estimators, making it relevant to closed-loop flow-control workflows.
  - Good bridge between experimental fluid sensing, reduced-order modeling, and real-time digital twins.
- Possible use: Prototype sparse/coarse measurement → POD-coordinate estimation for a controlled CFD dataset.
- Maturity: paper-only
- Priority: Medium

## Constrained Extreme Gradient Boosting for adapting ROMs

- Link: https://arxiv.org/abs/2605.04130
- Type: Adaptive reduced-order modeling method
- Why it matters:
  - Addresses ROM degradation under parameter variation using a constrained ensemble-learning correction layer.
  - Potentially easier to integrate into parametric CFD/FEA optimization loops than a large end-to-end neural surrogate.
  - Useful reference for lightweight ROM adaptation when simulation data at every operating condition is unavailable.
- Possible use: Test as a basis-adaptation baseline for parametric thermal or fluid surrogate studies.
- Maturity: paper-only
- Priority: Medium

## Control-oriented cluster-based reduced-order modelling

- Link: https://arxiv.org/abs/2604.25474
- Type: Control-oriented reduced-order model
- Why it matters:
  - Generalizes cluster network model transition probabilities and times across unseen control parameters.
  - Directly targets reduced dynamics for operating regimes where no simulation data is available.
  - Relevant to flow-control and aeroelastic-control studies where surrogate behavior under new controls matters.
- Possible use: Compare against POD/DMD-style control surrogates on a simple separated-flow or oscillator dataset.
- Maturity: paper-only
- Priority: Medium

## Inpainting physics for context-driven fluid simulation

- Link: https://arxiv.org/abs/2605.08832
- Type: Self-supervised CFD surrogate / flow prior
- Why it matters:
  - Reformulates steady CFD inference as context-conditioned inpainting rather than a fixed geometry/boundary-condition-to-field mapping.
  - Uses latent flow matching and masked-autoencoder models over compact local-neighbourhood tokens to scale toward large 3D meshes.
  - Relevant to CAD/CAE iteration because unchanged simulation context can be reused during local geometry edits or boundary-condition shifts.
- Possible use: Benchmark against FNO/Transolver-style supervised surrogates on geometry-edit and sparse-context reconstruction tasks.
- Maturity: paper-only
- Priority: High

## AeroJEPA

- Link: https://arxiv.org/abs/2605.05586
- Type: Predictive latent representation model for 3D aerodynamic fields
- Why it matters:
  - Decouples latent prediction from high-resolution field reconstruction, which helps with very large aerodynamic fields.
  - Learns design-meaningful latent spaces that support interpolation, probing, concept-vector arithmetic, and constrained latent optimization.
  - Directly relevant to many-query aerodynamic design workflows where a surrogate should support analysis and optimization, not only fast field prediction.
- Possible use: Compare with neural operators and Transolver-style models for CAD/wing-family aerodynamic surrogate experiments.
- Maturity: paper-only
- Priority: High

## Compositional Neural Operators for Multi-Dimensional Fluid Dynamics

- Link: https://arxiv.org/abs/2605.11691
- Type: Compositional neural operator for fluid-dynamics surrogates
- Why it matters:
  - Targets multi-dimensional fluid dynamics with compositional operator structure rather than treating every flow family as one monolithic black-box mapping.
  - Relevant to CFD surrogate generalization where geometry, dimension, field components, and boundary conditions should ideally be recombined across tasks.
  - Useful paper anchor for comparing modular/operator-composition approaches against larger scientific foundation model claims.
- Possible use: Track as a method candidate for small multi-physics or multi-geometry CFD surrogate benchmarks.
- Maturity: paper-only
- Priority: High

## jNO

- Link: https://arxiv.org/abs/2605.10159
- Code: https://github.com/FhG-IISB/jNO
- Type: JAX library for neural operators and PDE foundation-model training
- Why it matters:
  - Provides a JAX-native stack for data-driven and physics-informed neural-operator training.
  - Its tracing system for domains, model calls, residuals, supervised losses, and PDE losses is useful for reproducible SciML experiments.
  - More actionable than a paper-only architecture when building VA-style benchmark loops for heat transfer, CFD, or PDE surrogate comparison.
- Possible use: Evaluate as the base library for a compact heat/CFD neural-operator sandbox.
- Maturity: early open-source library
- Priority: High

## CATO: Charted Attention for Neural PDE Operators

- Link: https://arxiv.org/abs/2605.09016
- Type: Transformer-style neural PDE operator for complex geometries
- Why it matters:
  - Addresses a practical weakness of attention-based PDE operators on complex geometries.
  - Relevant to CAD/mesh-to-field surrogate workflows where geometry representation, charting, and local coordinates can dominate performance.
  - Useful comparison point against FNO/GNO/mesh-based operator approaches for non-rectangular engineering domains.
- Possible use: Track for geometry-heavy surrogate experiments after simple fixed-grid baselines are working.
- Maturity: paper-only
- Priority: Medium

## Physics-Informed Neural PDE Solvers via Spatio-Temporal MeanFlow

- Link: https://arxiv.org/abs/2605.08915
- Type: Physics-informed neural PDE solver
- Why it matters:
  - Attempts to capture continuous spatio-temporal physical structure beyond pointwise residual penalties.
  - Relevant to PDE systems where long-range dependencies and rollout consistency matter more than one-step field accuracy.
  - Good candidate to compare with PINNs and neural operators on small canonical PDE problems before trusting it on CFD.
- Possible use: Use as a method reference for physics-informed PDE solver benchmarks.
- Maturity: paper-only
- Priority: Medium

## Shock-Centered Low-Rank Structure for Rarefied Micro-Nozzle Flows

- Link: https://arxiv.org/abs/2605.12723
- Type: Neural-operator / reduced-structure CFD surrogate paper
- Why it matters:
  - Shows that DSMC-resolved micro-nozzle compression layers become much lower-complexity when represented in a shock-centered coordinate system.
  - Useful reminder that CFD surrogate quality can depend on physics-aware registration and normalization, not only on neural architecture choice.
  - Relevant to compressible/rarefied-flow surrogate design where discontinuities or localized layers dominate apparent field complexity.
- Possible use: Test feature-aligned coordinates such as shock location, separation point, recirculation length, or thermal boundary-layer thickness before training FNO/GNO baselines.
- Maturity: paper-only
- Priority: High

## EqOD: Symmetry-Informed Stability Selection for PDE Identification

- Link: https://arxiv.org/abs/2605.11524
- Type: PDE discovery / interpretable SciML method
- Why it matters:
  - Uses symmetry cues such as Galilean invariance to reduce candidate PDE libraries before sparse identification.
  - Helps control false positives when discovering governing equations from noisy trajectory data.
  - Useful as a sanity-check method for data-driven fluid/transport model identification where interpretability matters.
- Maturity: paper-only
- Priority: Medium

## Port-Hamiltonian Neural Networks for Nonlinear String Dynamics

- Link: https://arxiv.org/abs/2605.12785
- Type: Structure-preserving neural dynamics identification
- Why it matters:
  - Extends port-Hamiltonian neural-network ideas toward distributed-parameter nonlinear dynamics.
  - Relevant to control-oriented SciML because energy, passivity, and interconnection structure are often more important than black-box forecast error.
  - Worth tracking as a pattern for thermal/fluid/control surrogates where physical structure should constrain learned dynamics.
- Maturity: paper-only
- Priority: Medium

## Shodh-MoE for multi-physics foundation models

- Link: https://arxiv.org/abs/2605.15179
- Type: Sparse mixture-of-experts neural operator / multi-physics SciML paper
- Why it matters:
  - Targets negative transfer when dense neural operators are trained across incompatible PDE regimes.
  - Relevant to CFD/thermal foundation-model claims because open-channel flow, porous media, shocks, and heat transfer may need different routing paths.
  - Useful reference when designing benchmarks that measure whether adding more physics helps or hurts a shared surrogate.
- Possible use: Compare dense shared FNO/Transformer baselines against routed experts on mixed thermal-fluid datasets.
- Maturity: paper-only
- Priority: High

## Composing Neural PDE Experts in Weight Space

- Link: https://arxiv.org/abs/2605.14546
- Type: Expert composition / transfer learning for neural PDE surrogates
- Why it matters:
  - Interprets fine-tuned PDE experts as reusable weight-space directions aligned with physical parameters.
  - Suggests a controllable alternative to retraining separate surrogates for each Reynolds number, boundary regime, or material parameter.
  - Useful bridge between operator pretraining and parameter-aware adaptation for CFD/thermal model families.
- Possible use: Test whether expert-direction interpolation gives stable predictions across Reynolds/Prandtl/geometry regimes.
- Maturity: paper-only
- Priority: High

## U-HNO

- Link: https://arxiv.org/abs/2605.12965
- Type: Hybrid neural operator with sparse-point adaptive routing
- Why it matters:
  - Addresses PDE trajectories with smooth global transport plus localized shocks, interfaces, or concentrated high-frequency content.
  - More relevant to CFD than uniform global operators when boundary layers, discontinuities, and local structures dominate error.
  - The adaptive routing idea is worth comparing against fixed FNO/U-Net hybrid architectures.
- Possible use: Candidate baseline for shock tube, compressible flow, and localized-source heat-transfer surrogate experiments.
- Maturity: paper-only
- Priority: High

## Consistency-Distilled Flow Matching for Physical Fidelity Reconstruction

- Link: https://arxiv.org/abs/2605.05975
- Type: One-step generative reconstruction for dynamical systems
- Why it matters:
  - Compresses flow-matching reconstruction into a one-step model, reducing latency for high-fidelity field recovery.
  - Relevant to simulation-in-the-loop workflows, sparse/low-fidelity observation upscaling, and real-time visualization.
  - Useful comparison against iterative diffusion/flow-matching surrogates where sampling cost erases practical gains.
- Possible use: Evaluate on low-fidelity-to-high-fidelity CFD field reconstruction with conservation and rollout diagnostics.
- Maturity: paper-only
- Priority: Medium

## Topology-Preserving Neural Operator Learning via Hodge Decomposition

- Link: https://arxiv.org/abs/2605.13834
- Type: Structure-preserving neural operator for geometric meshes
- Why it matters:
  - Uses Hodge decomposition to separate topological degrees of freedom from learnable geometric dynamics.
  - Relevant to CFD/CAE surrogates on unstructured meshes where divergence/curl/topological modes should not be treated as generic image features.
  - Good reference for moving beyond plain L2 field matching toward physically structured operator learning.
- Possible use: Add Hodge/topology-aware diagnostics when comparing neural operators on mesh-based flow or thermal-field benchmarks.
- Maturity: paper-only
- Priority: High

## UFO: Domain-Unification-Free Operator Framework

- Link: https://arxiv.org/abs/2605.12700
- Type: Cross-domain neural operator framework
- Why it matters:
  - Avoids forcing physical, spectral, and latent representations into a single domain.
  - Adaptive cross-domain interactions may help multi-physics surrogates that need both local geometry and global spectral structure.
  - Useful comparison point against FNO-style single-domain inductive bias.
- Possible use: Track as a candidate architecture family for mixed thermal/fluid/porous-media surrogate tasks.
- Maturity: paper-only
- Priority: Medium

## Frequency Bias and OOD Generalization in Neural Operators

- Link: https://arxiv.org/abs/2605.12997
- Type: Neural-operator reliability / OOD analysis
- Why it matters:
  - Studies how neural operators behave under structured distribution shift in a variable-coefficient wave equation.
  - Reinforces that surrogate validation should include spectral and OOD diagnostics, not just average field error.
  - Transferable lesson for CFD surrogates where high-frequency boundary layers, shocks, or interface features dominate engineering utility.
- Possible use: Use as a citation and test-design reference for frequency-band error metrics in VA's surrogate benchmarks.
- Maturity: paper-only
- Priority: High

## ViT-K

- Link: https://arxiv.org/abs/2605.13912
- Type: Few-shot surrogate for coupled free-flow / porous-media systems
- Why it matters:
  - Targets coupled Stokes/Navier-Stokes-Darcy flows with interface conditions, a costly class of fluid-porous simulations.
  - Directly relevant to cold plates, filtration, porous heat exchangers, and thermal-fluid components with interface heterogeneity.
  - Few-shot framing is useful when high-fidelity CFD labels are too expensive for dense parameter sweeps.
- Possible use: Compare against neural-operator and ROM baselines on a small free-flow/porous-interface benchmark.
- Maturity: paper-only
- Priority: High

## Inpainting physics

- Link: https://arxiv.org/abs/2605.08832
- Type: Self-supervised context-driven CFD surrogate
- Why it matters:
  - Trains fluid surrogates by reconstructing masked/contextual flow fields instead of relying only on fully specified geometry and boundary-condition vectors.
  - Better matches practical engineering states where the agent may have partial simulations, sparse sensors, geometry patches, or incomplete setup metadata.
  - Useful framing for CFD foundation models that need flexible conditioning rather than a fixed forward-operator signature.
- Possible use: Build a small masked-field benchmark for duct/cavity/heat-transfer cases and compare inpainting-style conditioning against direct forward surrogates.
- Maturity: paper-only
- Priority: High

## Shock-Centered Low-Rank Neural-Operator Representation

- Link: https://arxiv.org/abs/2605.12723
- Type: Neural-operator representation for rarefied micro-nozzle flows
- Why it matters:
  - Shows that DSMC-resolved micro-nozzle flow complexity can become much lower-rank after shock-centered registration and finite-thickness scaling.
  - Important caution for compressible/rarefied-flow surrogates: coordinate alignment and feature registration can matter as much as architecture scale.
  - Suggests diagnostics for when neural operators are wasting capacity on movable discontinuities rather than learning physical variation.
- Possible use: Compare raw-coordinate vs shock-centered surrogate training on nozzle, shock-tube, or compressible boundary-layer datasets.
- Maturity: paper-only
- Priority: High

## Mesh Based Simulations with Spatial and Temporal awareness

- Link: https://arxiv.org/abs/2605.01542
- Type: Mesh-based CFD surrogate architecture / evaluation paper
- Why it matters:
  - Calls out a practical bottleneck in mesh-based GNN/Transformer CFD surrogates: spatial and temporal awareness is often underspecified despite being central to rollout quality.
  - Relevant to unstructured-mesh engineering simulations where topology, local neighborhoods, timestep history, and field evolution jointly determine prediction stability.
  - Useful as an evaluation-design reference when comparing mesh surrogate architectures beyond one-step field error.
- Possible use: Add temporal-rollout and mesh-generalization diagnostics to VA's future CFD surrogate benchmark notes.
- Maturity: paper-only
- Priority: Medium

## Martingale Neural Operators

- Link: https://arxiv.org/abs/2605.15806
- Type: Stochastic neural operator / uncertainty-aware operator learning
- Why it matters:
  - Addresses conditional-mean collapse in deterministic neural operators for stochastic PDEs.
  - Important for engineering UQ workflows where variance, tails, and reliability matter as much as mean field accuracy.
  - Useful reference for thermal/fluid surrogate benchmarks that include uncertain inputs or stochastic forcing.
- Possible use: Compare against deterministic FNO-style baselines on stochastic PDE or uncertain-boundary heat/flow tasks.
- Maturity: paper-only
- Priority: High

## AOT-POT

- Link: https://arxiv.org/abs/2605.15793
- Type: Adaptive operator transformation for large-scale PDE pre-training
- Why it matters:
  - Targets the structural diversity problem in pretraining neural operators across heterogeneous PDE datasets.
  - Relevant to scientific foundation-model efforts that try to combine thermal, fluid, porous, and wave-like regimes.
  - Good reminder that dataset aggregation alone can be harmful unless operator/domain differences are handled explicitly.
- Possible use: Track as a pretraining strategy when designing multi-PDE surrogate experiments.
- Maturity: paper-only
- Priority: High

## Martingale/UQ surrogate validation note

- Link: https://arxiv.org/abs/2605.16078
- Type: Neural surrogate performance study for uncertainty propagation
- Why it matters:
  - Evaluates neural network surrogate behavior in stochastic boundary-value problems from a UQ perspective.
  - Useful for checking whether field-surrogate error corrupts downstream uncertainty estimates, not just point predictions.
  - Directly relevant to heat-transfer and CFD design problems with uncertain properties, boundary conditions, or geometry parameters.
- Possible use: Include uncertainty-propagation metrics in surrogate benchmarks before using models for design decisions.
- Maturity: paper-only
- Priority: Medium

## PACE-FNO

- Link: https://arxiv.org/abs/2605.18606
- Type: Physics-aligned equivariant Fourier neural operator
- Why it matters:
  - Separates coordinate/frame alignment from PDE evolution by canonicalizing inputs with known continuous symmetries before applying FNO.
  - Directly targets OOD shifts where vanilla neural operators waste capacity relearning translations/rotations or symmetry-induced coordinate changes.
  - Useful reference for CFD/thermal surrogate benchmarks where symmetry-aware evaluation is more meaningful than random train/test splits.
- Possible use: Compare against vanilla FNO on shifted/rotated periodic PDE fields or channel-flow slices to test symmetry-induced OOD generalization.
- Maturity: paper-only
- Priority: High

## CTA-Swin-UNet for wall-bounded turbulence

- Link: https://arxiv.org/abs/2605.17888
- Type: Long-horizon turbulence surrogate with resolvent-based reconstruction
- Why it matters:
  - Targets long-horizon prediction of 3D wall-bounded turbulence, where autoregressive error accumulation is the real bottleneck.
  - Combines channel-time attention for planar flow prediction with resolvent-based spectral linear stochastic estimation for 3D reconstruction.
  - Useful reminder that hybrid ML + physics reconstruction can be more practical than pure field-to-field black-box rollout.
- Possible use: Track as a comparison point for turbulence surrogate experiments that report rollout stability, spectra, and physical statistics.
- Maturity: paper-only
- Priority: High

## In-Context Earth for subsurface temperature fields

- Link: https://arxiv.org/abs/2605.16665
- Type: Transformer model for sparse-observation thermal-field prediction
- Why it matters:
  - Uses sparse borehole observations as context to infer continuous temperature-at-depth fields with calibrated uncertainty.
  - Relevant to geothermal assessment, subsurface heat transport, and sparse-sensor thermal reconstruction problems.
  - Good applied example of in-context learning for physical fields rather than generic language or image tasks.
- Possible use: Use as inspiration for sparse-sensor heat-transfer field reconstruction benchmarks.
- Maturity: paper-only
- Priority: Medium

## pyforce 1.0.0

- Link: https://arxiv.org/abs/2605.18082
- Type: Python framework for data-driven reduced-order modeling of multi-physics problems
- Why it matters:
  - Implements ROM workflows for multi-physics applications with a VTK/PyVista-friendly data path.
  - Solver-agnostic VTK export compatibility makes it easier to attach ROM/SciML tools to existing CFD/CAE pipelines.
  - Useful bridge between classical reduced-order modeling and modern Python visualization/post-processing infrastructure.
- Possible use: Evaluate on VTK-exporting CFD/thermal examples before building custom ROM tooling.
- Maturity: released framework / paper
- Priority: Medium

## Neural operator as coarse solve replacement

- Link: https://arxiv.org/abs/2605.19867
- Type: Neural operator / numerical linear solver acceleration
- Why it matters:
  - Studies when a neural operator can replace the coarse solve in two-level preconditioning rather than acting as a full black-box PDE solver.
  - Practical for CFD/SciML because trusted solvers often need acceleration components, not total replacement.
  - Helps frame architecture choices by solver role: correction quality, stability, and interaction with the outer numerical method.
- Possible use: Use as a reference when evaluating neural surrogates as multigrid/coarse-correction modules for parametric CFD or thermal solvers.
- Maturity: paper-only
- Priority: High

## Smooth Piecewise Cutting for Neural Operators

- Link: https://arxiv.org/abs/2605.19823
- Type: Neural operator method for discontinuities and sharp transitions
- Why it matters:
  - Targets a core weakness of continuous neural-operator representations: oversmoothing discontinuities, fronts, shocks, and interfaces.
  - Relevant to compressible CFD, phase-change heat transfer, multiphase flow, and moving-boundary problems where sharp features dominate error.
  - Useful comparison point against shock-aware losses, adaptive meshes, graph methods, and domain-decomposition-style surrogates.
- Possible use: Track for benchmarks with shocks, thermal fronts, wet/dry interfaces, or particle/fluid discontinuities.
- Maturity: paper-only
- Priority: High

## Physics-informed GNN surrogates for turbulent nanoparticle dispersion

- Link: https://arxiv.org/abs/2605.19589
- Type: Physics-informed graph neural surrogate for turbulent particle dispersion
- Why it matters:
  - Applies mesh/geometry-aware surrogate modeling to RANS + Euler-Lagrange nanoparticle transport in indoor clinical environments.
  - Useful applied example for aerosol, particle-laden flow, and indoor-air CFD acceleration rather than only canonical fluid benchmarks.
  - Reinforces that surrogate validation should include transport/dispersion quantities, not only velocity-field visual similarity.
- Possible use: Reference for particle-dispersion surrogate experiments or indoor-air/ventilation CFD acceleration ideas.
- Maturity: paper-only
- Priority: Medium

## Data-Efficient Neural Operator Training via Physics-Based Active Learning

- Link: https://arxiv.org/abs/2605.21348
- Type: Neural operator training / active learning
- Why it matters:
  - Treats neural-operator dataset growth as an acquisition problem: choose the most informative PDE simulations instead of scaling data blindly.
  - Directly relevant when CFD, heat-transfer, or multiphysics samples are expensive and simulation budget is the limiting factor.
  - Good companion idea for engineering-grade datasets such as HiLiftAeroML, where active sampling can be evaluated against geometry/OOD splits.
- Possible use: Compare physics-based active learning against random/LHS sampling for CFD surrogate training under a fixed simulation budget.
- Maturity: paper-only / ICLR 2026 AI4PDE workshop
- Priority: High

## Hierarchical Multi-Fidelity Learning for 3D Flame Wrinkling and Turbulent Burning Velocity

- Link: https://arxiv.org/abs/2605.08232
- Type: Multi-fidelity SciML for combustion/turbulent flows
- Why it matters:
  - Uses hierarchical multi-fidelity learning for combustion quantities where high-fidelity data is expensive and low-fidelity signals are easier to obtain.
  - Relevant to heat-transfer/fluid workflows because reacting turbulent flows expose the same data-budget and fidelity-gap problems as many industrial CFD tasks.
  - Useful as an applied anchor for discussing when multi-fidelity learning is more practical than a single large black-box surrogate.
- Maturity: paper-only
- Priority: Medium

## Inpainting physics

- Link: https://arxiv.org/abs/2605.08832
- Type: Self-supervised fluid simulation surrogate
- Why it matters:
  - Reframes CFD surrogate learning as context-driven inpainting rather than fixed forward mapping from explicit problem specifications.
  - Relevant when boundary conditions, local geometry, or observed regions shift between training and deployment.
  - Useful idea for sensor-to-field reconstruction, missing-region completion, and simulation-in-the-loop post-processing.
- Possible use: Build a small cavity/duct/thermal-field completion benchmark with masked fields and boundary metadata.
- Maturity: paper-only
- Priority: Medium

## ViT-K

- Link: https://arxiv.org/abs/2605.13912
- Type: Few-shot surrogate for coupled free-flow / porous-media systems
- Why it matters:
  - Targets Stokes/Navier--Stokes--Darcy coupling with interface conditions, a harder class than smooth single-domain PDE benchmarks.
  - Few-shot framing is relevant when high-fidelity coupled-flow data are expensive.
  - Good reference for porous transport, filtration, and physiological flow settings where interface physics dominates error.
- Maturity: paper-only
- Priority: Medium

## Compositional Neural Operators for Multi-Dimensional Fluid Dynamics

- Link: https://arxiv.org/abs/2605.11691
- Type: Compositional neural-operator architecture for fluid dynamics
- Why it matters:
  - Pushes against monolithic universal surrogates by composing operator/physics blocks.
  - Relevant to multi-regime CFD foundation models where dense sharing can create negative transfer.
  - Good comparison point for MoE routing and operator-transformation approaches.
- Maturity: paper-only
- Priority: High

## Reduced-Order Modeling of Parameterized Visco-Plastic Shallow Flows

- Link: https://arxiv.org/abs/2605.06526
- Type: Non-intrusive ROM for visco-plastic free-surface flows
- Why it matters:
  - Handles Herschel--Bulkley rheology with moving fronts and yield surfaces, which are more challenging than smooth benchmark PDEs.
  - Useful reference for surrogate evaluation under non-smooth physics and parameterized shallow-flow regimes.
  - Complements neural-operator papers with a ROM baseline perspective.
- Maturity: paper-only
- Priority: Medium

## Physics-informed CNNs for porous-media flow warm starts

- Link: https://arxiv.org/abs/2605.20250
- Type: Physics-informed CNN surrogate for pore-scale flow
- Why it matters:
  - Predicts pore-scale velocity fields directly from complex geometry while penalizing incompressibility, no-flow-in-solid regions, periodicity, and tortuosity consistency.
  - The practical payoff is solver assistance: predicted fields are used as initial conditions for Lattice-Boltzmann simulations, reducing iterations in more than 90% of tested cases.
  - Good example of ML helping CFD as a warm-start/preconditioner rather than trying to replace the solver entirely.
- Possible use: Reproduce the warm-start idea on a small porous/heat-exchanger geometry set and compare convergence speed, residual history, and failure cases against zero/uniform initialization.
- Maturity: paper + dedicated GitHub repo announced
- Priority: High

## Conditional neural fields for dynamic ditching loads

- Link: https://arxiv.org/abs/2605.21499
- Type: Mesh/discretization-flexible reduced-order model for CFD loads
- Why it matters:
  - Uses coordinate-based conditional neural fields plus latent-space temporal prediction to model aircraft ditching loads.
  - The key signal is discretization flexibility: it can train/reconstruct across heterogeneous spatial discretizations, which is valuable when CFD datasets come from different meshes or geometry variants.
  - Relevant to CAD/CAE loops where remeshing after geometry edits breaks fixed-grid surrogate assumptions.
- Possible use: Track as a reference for mesh-independent load prediction or pressure/heat-flux field ROMs across geometry variants.
- Maturity: paper-only
- Priority: Medium

## Accelerating Bayesian inverse design in CFD using neural operators

- Link: https://arxiv.org/abs/2605.26059
- Type: Neural-operator surrogate for Bayesian CFD inverse design
- Why it matters:
  - Embeds a DeepONet surrogate directly inside a gradient-based MCMC inverse-design loop while preserving posterior geometry and uncertainty trends against a CFD reference.
  - Shows a practical use case for neural operators beyond forward field prediction: sparse observation → aerodynamic geometry inference with uncertainty.
  - The geometry-parameterization result is a useful caution that surrogate accuracy alone does not fix identifiability or posterior conditioning.
- Possible use: Use as a reference for uncertainty-aware heat-transfer/aerodynamic inverse design where validation should include posterior structure, not only point estimates.
- Maturity: paper-only
- Priority: High

## NPSolver

- Link: https://arxiv.org/abs/2605.25786
- Code: https://github.com/intell-sci-comput/NPSolver
- Type: Neural Poisson solver with iterative physics supervision
- Why it matters:
  - Uses a small number of PCG refinement steps as a stable supervision signal instead of requiring converged labels or relying only on raw PDE residuals.
  - Targets 2D/3D irregular geometries and mixed boundary conditions, which are closer to CAD-derived thermal domains than clean rectangular PDE benchmarks.
  - Includes a downstream thermal boundary-control task, making it directly relevant to control-oriented SciML.
- Possible use: Prototype on irregular heat-conduction cases and compare against classical solvers, PINNs, and FNO-style baselines using field error plus control objective.
- Maturity: paper + early code repository
- Priority: High

## Transformer-based Neural Operators for 3D Wind Field Prediction over Complex Mountainous Terrain

- Link: https://arxiv.org/abs/2605.25679
- Type: Point/graph neural-operator framework for terrain-driven CFD surrogate modeling
- Why it matters:
  - Focuses on complex topography where meshing and steady CFD solves are expensive, not on simplified canonical geometries.
  - Demonstrates zero-shot transfer to real mountainous sites and improvement from sparse observational inputs.
  - Useful pattern for geometry-heavy CFD surrogates that should assimilate a few sensors rather than operate as pure offline emulators.
- Possible use: Adapt the sparse-observation idea to duct, heat-sink, or ventilation CFD surrogates with a small number of virtual sensors.
- Maturity: paper-only
- Priority: High

## Courant

- Link: https://arxiv.org/abs/2605.25115
- Type: State-adaptive Perceiver-based neural surrogate
- Why it matters:
  - Designs latent features with adaptive specialization and local support in physical space, echoing hp-refinement and reduced-basis intuition.
  - Relevant to CFD/thermal surrogate modeling where interpretability and geometry/state locality matter as much as pointwise error.
  - Useful evaluation anchor for asking whether a surrogate's latent structure tracks coherent flow features or only fits fields black-box.
- Possible use: Compare against FNO/GraphNO/Transolver-style baselines on complex-geometry flow or heat-transfer datasets with locality and sensor-ablation diagnostics.
- Maturity: paper-only
- Priority: High

## Adapting Automotive Aerodynamics Surrogates via Transfer Learning

- Link: https://arxiv.org/abs/2605.27968
- Type: Automotive CFD surrogate transfer-learning study
- Why it matters:
  - Tests whether geometry representations learned by an automotive aerodynamic surrogate transfer to topologically different vehicle families.
  - Leave-one-family-out framing is closer to industrial deployment than random train/test splits inside one design family.
  - Useful validation pattern for CAD/CFD surrogate projects where new geometry families appear after initial model training.
- Possible use: Use family-level holdout and few-shot fine-tuning as standard diagnostics for VA-style geometry-to-field surrogate experiments.
- Maturity: paper-only
- Priority: High

## CINOC: Cardinality-Invariant Neural Operator Policies

- Link: https://arxiv.org/abs/2605.25867
- Type: Neural-operator policy for scalable PDE control
- Why it matters:
  - Targets control policies that survive changes in sensor, actuator, or agent count.
  - Relevant to thermal-fluid control where hardware layouts and observation grids change across prototypes.
  - Good bridge between operator learning and deployable control, not just open-loop field prediction.
- Possible use: Evaluate cardinality-invariant policy ideas on toy heat-transfer or flow-control problems with varying actuator layouts.
- Maturity: paper-only
- Priority: Medium

## Neural Operator-Based Surrogate Model for CFD: Helical Coil Steam Generator in Small Modular Reactor

- Link: https://arxiv.org/abs/2605.30277
- Type: Neural-operator / ROM surrogate for SMR thermal-hydraulic CFD
- Why it matters:
  - Targets transient CFD-level digital-twin simulation for a helical coil steam generator in a small modular reactor, not a toy PDE benchmark.
  - Compares AE/CAE ROM strategies coupled with latent DeepONet and FNO, which is useful for structured vs unstructured CFD data decisions.
  - Multi-scale treatment for Kármán vortex street prediction makes it relevant to practical transient-flow surrogate validation.
- Possible use: Use as a template for defining CFD surrogate artifacts with mesh type, ROM basis, operating envelope, and vortex/thermal KPI checks.
- Maturity: paper-only
- Priority: High

## Striding Across Reynolds Numbers

- Link: https://arxiv.org/abs/2605.30112
- Type: Neural PDE generalization / representation-geometry study
- Why it matters:
  - Studies cross-Reynolds generalization on 2D Navier-Stokes and shows FNO performance can degrade strongly under a 10x Reynolds shift.
  - Finds simple representation matching/retrieval baselines surprisingly competitive, suggesting latent geometry matters as much as architecture choice.
  - Useful caution for CFD surrogate claims that only report interpolation or narrow-regime accuracy.
- Possible use: Add representation-space OOD diagnostics and retrieval baselines to VA's CFD surrogate evaluation templates.
- Maturity: paper-only
- Priority: High


## Operator Learning for Reconstructing Flow Fields from Sparse Measurements

- Link: https://arxiv.org/abs/2605.23712
- Type: Mesh-free operator learning for sparse-sensor flow reconstruction
- Why it matters:
  - Targets a practical digital-twin/control setting: reconstructing full flow fields from sparse measurements rather than assuming dense simulation snapshots are always available.
  - Uses language-model-style architecture ideas for operator learning, broadening the design space beyond standard FNO/DeepONet baselines.
  - Relevant to experimental fluid mechanics, sensor placement, and simulation-in-the-loop control where observations are partial and irregular.
- Possible use: Build a small sparse-sensor reconstruction benchmark for cavity flow, ventilation, or thermal fields and report field error plus downstream control/design metrics.
- Maturity: paper-only
- Priority: High

## Sparse POD Mode Selection and Manifold Dimensionality Reduction with Neural Networks

- Link: https://arxiv.org/abs/2605.27756
- Type: Reduced-order modeling / sparse POD / neural manifold learning
- Why it matters:
  - Revisits classical POD-based model reduction with sparse mode selection instead of treating all learned surrogates as fully black-box models.
  - Useful for CFD/thermal workflows where interpretability, compression ratio, and solver coupling matter alongside prediction error.
  - Bridges conventional MOR and neural surrogate modeling, making it a good baseline family for design optimization and inverse problems.
- Possible use: Compare sparse POD-neural manifold reduction against FNO/GraphNO-style models on VA-style thermal or aerodynamic datasets under fixed latent dimension and rollout-budget constraints.
- Maturity: paper-only
- Priority: Medium

## The Neural Compiler

- Link: https://arxiv.org/abs/2605.22498
- Type: Program-to-network translation system for hybrid Scientific Machine Learning
- Why it matters:
  - Translates first-order probabilistic programs into neural networks for hybrid SciML, reducing the need to hand-write custom PyTorch for every equation/prior combination.
  - Relevant to workflows that combine known physics, unknown correction terms, parameters, and data-driven components.
  - Points toward declarative scientific-model specifications that agents can inspect, modify, and validate more safely than ad hoc training scripts.
- Possible use: Prototype a small declarative spec for heat-transfer PDEs, boundary conditions, and trainable closure terms, then compile or generate training code with explicit validation checks.
- Maturity: paper-only
- Priority: Medium

## Functional Attention

- Link: https://arxiv.org/abs/2605.31559
- Project/code: https://github.com/xjffff/FUNCATTN
- Type: Operator-learning attention architecture
- Why it matters:
  - Recasts attention as functional correspondence between adaptive bases rather than token-wise pairwise affinity.
  - Targets resolution-invariant and discretization-robust mappings between continuous fields.
  - Relevant to PDE solving, CFD/thermal surrogates, sparse observation assimilation, and geometry-dependent field prediction.
- Possible use: Compare against FNO/Transformer-operator baselines on resolution-transfer tests for heat equation, cavity flow, or cylinder wake.
- Maturity: paper + project/code link
- Priority: High

## Cellular Sheaf Neural Operators

- Link: https://arxiv.org/abs/2606.00937
- Type: Structure-preserving neural operator for constrained PDEs
- Why it matters:
  - Represents PDE state on cellular structures rather than flattening everything into grid-channel tensors.
  - Directly relevant to CFD/CAE meshes where quantities live naturally on vertices, edges, faces, and cells.
  - Useful direction for geometry/topology-aware surrogate modeling and finite-volume-compatible learned operators.
- Possible use: Compare against FNO/GNO/Transformer baselines on mesh-based flow or heat-transfer cases with explicit face/cell variables.
- Maturity: paper-only
- Priority: High

## Therm-FM

- Link: https://arxiv.org/abs/2605.22663
- Type: Foundation-model / neural-operator framework for 3D-IC thermal simulation
- Why it matters:
  - Targets repeated finite-element thermal simulations across chip designs, where retraining from scratch is expensive.
  - Cross-design adaptation is directly relevant to electronics cooling and package-level thermal design loops.
  - Good thermal-specific counterpoint to generic PDE foundation-model claims.
- Possible use: Use as a case study for transfer/adaptation metrics in thermal surrogate benchmarks.
- Maturity: paper-only
- Priority: High

## Neural Operator-Based CFD Surrogate for SMR Helical Coil Steam Generator

- Link: https://arxiv.org/abs/2605.30277
- Type: Thermal-hydraulic CFD surrogate for digital twin workflows
- Why it matters:
  - Compresses high-fidelity CFD of a helical-coil steam generator toward real-time small modular reactor digital twins.
  - Strong applied thermal-fluid signal: safety-critical DT workflows need speed, fidelity, and operating-regime awareness.
  - Useful reference for evaluating surrogate deployment constraints beyond benchmark accuracy.
- Maturity: paper-only
- Priority: High

## FreqNO-DPS

- Link: https://arxiv.org/abs/2606.03936
- Code: https://github.com/niccoloperrone/FreqNO-DPS
- Type: Paper + code / neural-operator correction
- Keywords: neural operator, spectral bias, diffusion posterior sampling, sparse sensors, wavefields
- One-line summary: Combines sparse observations, a frozen neural-operator forecast, and diffusion posterior sampling with frequency-shaped guidance to correct high-frequency spectral bias.
- Why it matters: CFD/thermal surrogates often look acceptable in field RMSE while damping fine scales; this paper makes spectral calibration an explicit part of the surrogate correction loop.
- Possible use: Use as a reference for evaluating surrogate spectra, sensor-conditioned correction, and frequency-dependent uncertainty in flow or thermal field reconstruction.
- Maturity: paper + research code
- Priority: High

## Validation-gated multi-agent adaptation for thermal-hydraulic surrogates

- Link: https://arxiv.org/abs/2606.03321
- Type: Paper / thermal-hydraulic surrogate governance
- Keywords: thermal hydraulics, surrogate adaptation, neural operator, multi-agent governance, validation gate
- One-line summary: Proposes role-separated agents plus deterministic champion-challenger gates for online adaptation of thermal-hydraulic surrogate models under operating-regime shift.
- Why it matters: It treats surrogate deployment as an auditable engineering system, not a one-time offline model selection problem; deterministic validation gates retain final authority over model replacement.
- Possible use: Use the Monitor/Diagnosis/Adaptation/Safety-Auditor/Orchestrator pattern as a template for safe CFD or thermal digital-twin adaptation workflows.
- Maturity: paper-only
- Priority: High

## Semigroup Consistency as a Diagnostic for Learned Physics Simulators

- Link: https://arxiv.org/abs/2605.26324
- Type: Learned-simulator evaluation diagnostic
- Why it matters:
  - Tests whether direct evolution over `s+t` agrees with composing learned predictions over `s` then `t`, a property exact autonomous solution maps should satisfy.
  - On heat and Burgers dynamics with ConvNet/FNO baselines, semigroup error correlates with rollout degradation, making it useful beyond one-step RMSE.
  - Good candidate metric for CFD/thermal surrogate validation gates where long-horizon stability matters.
- Possible use: Add semigroup error to surrogate evaluation reports alongside spectral error, conservation checks, and rollout metrics.
- Maturity: paper-only / AI4Physics ICML workshop
- Priority: High

## History-aware adaptive reduced-order models via incremental SVD

- Link: https://arxiv.org/abs/2605.28684
- Type: Adaptive projection-based ROM / online basis update
- Why it matters:
  - Uses occasional full-order correction snapshots and incremental SVD to update the reduced basis when online dynamics leave the offline training regime.
  - Demonstrates the pattern on Burgers, Sod shock tube, and a stiff rotating detonation engine case, making it relevant to compressible-flow surrogate governance.
  - Useful middle ground between trusted intrusive ROMs and black-box neural surrogates for regime-shifting CFD workflows.
- Possible use: Compare against FNO/DeepONet on an online regime-shift benchmark with equal correction-snapshot budgets.
- Maturity: preprint
- Priority: High

## PINO training for parametric PDEs

- Link: https://arxiv.org/abs/2606.06164
- Type: Physics-informed neural operator training study
- Keywords: PINO, neural operator, parametric PDE, physics-informed learning, training stability
- One-line summary: Studies how to train physics-informed neural operators robustly for parametric PDE solution operators using governing-equation supervision.
- Why it matters: For engineering PDE surrogates, architecture choice is only half the problem; residual formulation, sampling, optimization, and boundary-condition handling can determine whether PINO-style models are usable beyond toy cases.
- Possible use: Use as a checklist source for PINO ablations on heat-transfer, Burgers, cavity-flow, or other CFD/thermal surrogate benchmarks.
- Maturity: paper-only
- Priority: High

## EqGINO

- Link: https://arxiv.org/abs/2606.03260
- Type: Equivariant geometry-informed Fourier neural operator for 3D PDEs
- Keywords: Fourier neural operator, equivariance, geometry-informed learning, 3D PDE surrogate
- One-line summary: Introduces a geometry-informed FNO variant designed to improve generalization under 3D geometric transformations without paying the full cost of spectral group convolutions.
- Why it matters: CAD/CAE surrogates often fail under coordinate, rotation, or geometry distribution shifts; EqGINO is a useful reference for testing whether equivariant/global operator structure improves robustness on 3D engineering fields.
- Possible use: Compare against vanilla FNO/GNO/mesh-based models on rotated or transformed 3D heat/flow geometries.
- Maturity: paper-only
- Priority: High

## LiNO

- Link: https://arxiv.org/abs/2606.03262
- Type: Light-inspired neural operator architecture
- Keywords: neural operator, PDE surrogate, nonlocal communication, mesh scalability, interpretability
- One-line summary: Proposes a light-inspired neural operator using reflection/refraction/scattering analogies to balance physical interpretability, nonlocal communication, mesh scalability, and compute cost.
- Why it matters: Neural-operator research is moving from generic FNO variants toward architectures with explicit inductive biases; LiNO is worth tracking as an architecture idea for large-domain PDE surrogates.
- Possible use: Evaluate only after code/benchmarks mature; compare with FNO, GNO, attention-based operators, and spectral-correction methods on PDE families with nonlocal effects.
- Maturity: paper-only
- Priority: Medium

## Underwater CFD generative flow-field surrogate for path planning

- Link: https://arxiv.org/abs/2606.06077
- Type: CFD surrogate connected to robotic path planning/control
- Keywords: CFD surrogate, RANS, generative model, AUV, flow-field prediction, path planning
- One-line summary: Uses conditional generative models to emulate 3D RANS propeller-wake fields for autonomous underwater vehicle launch-and-recovery path planning.
- Why it matters: This is a useful applied pattern: the surrogate is judged not only by field fidelity, but by whether it supports a downstream control/planning decision in a difficult fluid environment.
- Possible use: Use as a reference when designing CFD surrogate evaluations that report objective-level or decision-level error, not only field RMSE.
- Maturity: paper-only
- Priority: High

## Automotive aerodynamics surrogate transfer learning

- Link: https://arxiv.org/abs/2605.27968
- Type: Transformer-based CFD surrogate / transfer-learning study
- Why it matters:
  - Tests whether geometry representations learned from several vehicle families transfer to an unseen automotive family.
  - Directly relevant to industrial CFD surrogate deployment, where new design families break random-split benchmark assumptions.
  - Useful evaluation pattern: separate within-family accuracy from unseen-family adaptation and downstream aerodynamic quantities.
- Possible use: Use as a reference protocol when building CAD/geometry-to-flow surrogate experiments with family-shift splits.
- Maturity: paper-only
- Priority: High

## Bayesian CFD inverse design with neural operators

- Link: https://arxiv.org/abs/2605.26059
- Type: Neural-operator surrogate for Bayesian inverse design
- Why it matters:
  - Studies whether neural operators can accelerate repeated CFD solves inside MCMC-style inverse design.
  - Important because the surrogate must preserve posterior geometry and uncertainty, not just produce low field RMSE.
  - Relevant to shock-dominated aerodynamic design and simulation-budget-limited optimization loops.
- Possible use: Compare surrogate-assisted posterior quality against high-fidelity CFD on a small inverse-design benchmark.
- Maturity: paper-only
- Priority: High

## Neural operator surrogate for SMR helical-coil steam generator CFD

- Link: https://arxiv.org/abs/2605.30277
- Type: Thermal-hydraulic neural-operator surrogate
- Why it matters:
  - Targets real-time transient CFD prediction for small modular reactor digital twins.
  - Good thermal-fluid example where geometry-specific surrogates matter for operational monitoring, not only design exploration.
  - Useful reference for thinking about safety gates, regime shift, and validation contracts around neural operators.
- Possible use: Use as a thermal-hydraulic reading anchor when designing surrogate validation checklists.
- Maturity: paper-only
- Priority: High

## Learned Response-Field Inertia Operator for HEC-RAS 2D

- Link: https://arxiv.org/abs/2606.06385
- Type: Solver-native hydrodynamic surrogate
- Why it matters:
  - Evaluates water-surface elevation prediction directly on HEC-RAS 2D nonuniform computational cells.
  - Avoids raster remapping artifacts and separates static inputs, current state, forcing, calibration quantities, and future targets.
  - Useful pattern for OpenFOAM/CFD surrogates where native mesh/cell semantics should be preserved.
- Possible use: Adapt the evaluation idea to OpenFOAM polyMesh or unstructured thermal-fluid datasets.
- Maturity: paper-only
- Priority: Medium

## Fast control-oriented physics-informed surrogate for TCV tokamak equilibrium reconstruction

- Link: https://arxiv.org/abs/2606.09487
- Type: Physics-informed surrogate for real-time control
- Why it matters:
  - Replaces a tokamak equilibrium reconstruction code with a neural surrogate targeting sub-100 μs inference and 10 kHz shape-control use.
  - Strong example of a surrogate evaluated against control-loop constraints, not only offline field error.
  - Relevant to thermal-fluid digital twins where sensor encoding, latency, operating envelope, and fallback behavior are deployment-critical.
- Possible use: Use as a control-ready surrogate checklist reference for CFD/thermal digital-twin experiments.
- Maturity: paper-only
- Priority: High

## Robust ECH deposition-profile control on DIII-D with neural surrogate optimization

- Link: https://arxiv.org/abs/2606.13661
- Type: Real-time control surrogate / plasma heating optimization
- Why it matters:
  - Combines a parallelized neural-network surrogate of TORBEAM with a genetic optimizer to control tokamak electron-cyclotron-heating deposition profiles.
  - Reports deployment in DIII-D experiments and validation with ECE measurements and offline ray tracing, including robustness to gyrotron failures and plasma-parameter changes.
  - Useful control-ready surrogate example: the learned model is evaluated through actuator constraints, hardware failures, operating-shift robustness, and experimental validation.
- Possible use: Borrow the validation contract for CFD/thermal control surrogates: latency, actuator availability, operating envelope, fallback verification, and post-run audit.
- Maturity: experimental deployment paper
- Priority: High

## Hybrid neural-cellular automata wildfire suppression planning

- Link: https://arxiv.org/abs/2606.13633
- Type: Spatiotemporal surrogate for intervention planning under uncertainty
- Why it matters:
  - Couples a CNN/cellular-automata fire-spread model with gradient-based aerial-drop planning for water and retardant interventions.
  - Evaluates intervention schedules under both aleatoric fire-state sampling and epistemic spatially correlated prediction-error perturbations.
  - Relevant to engineering surrogates where the model must support a downstream control/planning decision, not only forecast a field.
- Possible use: Use as a reference for uncertainty-aware planning metrics around thermal-fluid or environmental digital twins.
- Maturity: paper-only
- Priority: Medium

## Geometry-Aware Anisotropic Boundary Correction for Aerodynamic Simulation

- Link: https://arxiv.org/abs/2606.09963
- Type: Geometry-conditioned neural-operator correction for aerodynamic simulation
- Keywords: CFD, aerodynamic surrogate, neural operator, near-wall physics, boundary anisotropy
- One-line summary: Adds direction-aware boundary correction to neural operators by treating wall-tangential and wall-normal physics differently instead of using isotropic boundary features.
- Why it matters:
  - Near-wall quantities such as surface pressure coefficient are often the engineering-critical outputs in aerodynamic design.
  - Reports roughly 38% average reduction in near-boundary relative L2 error on 2D airfoil and 3D car tasks across multiple operator backbones.
  - Good validation reminder: global field error can hide boundary-layer and wall-pressure failures.
- Possible use: Add wall-normal/tangential error, Cp error, and boundary-gradient metrics to aerodynamic surrogate evaluations.
- Maturity: paper-only
- Priority: High

## Conformal Prediction for Neural Operators

- Link: https://arxiv.org/abs/2606.09923
- Type: Distribution-free uncertainty quantification for neural-operator physics simulation
- Keywords: neural operator, conformal prediction, uncertainty quantification, thermal simulation, safety-critical surrogate
- One-line summary: Applies split conformal prediction to neural-operator surrogates, giving finite-sample prediction intervals for physics simulations rather than only relative uncertainty scores.
- Why it matters:
  - Safety-critical thermal and battery-management applications need coverage guarantees, not just point predictions or ensemble variance.
  - Reports 89.1% empirical coverage at alpha=0.1 on steady-state heat-conduction benchmarks with adaptive interval widths.
  - Useful building block for validation gates around learned thermal/CFD surrogates.
- Possible use: Prototype conformal intervals around FNO/DeepONet heat-transfer baselines and report coverage separately near boundaries and high-gradient regions.
- Maturity: paper-only; open-source platform claimed in abstract
- Priority: High

## First-Order Trajectory Matching

- Link: https://arxiv.org/abs/2606.11138
- Type: Trajectory-aware surrogate modeling for chaotic, turbulent, and stochastic systems
- Keywords: stochastic dynamics, turbulence, ensemble prediction, probability current, surrogate modeling
- One-line summary: Learns probability-current velocity directly from trajectories to produce low-cost ensemble forecasts that preserve time marginals and current-like trajectory quantities.
- Why it matters:
  - Turbulent/chaotic systems often need ensemble and flux/statistical quantities, not only single deterministic point forecasts.
  - Avoids explicit drift, diffusion, and score estimation while retaining trajectory-aware quantities such as fluxes, circulations, and barrier-crossing currents.
  - Relevant to surrogate evaluation where phase-accurate rollout is impossible but ensemble statistics still matter.
- Possible use: Track as a candidate baseline for ensemble CFD/thermal surrogate benchmarks with statistics, spectra, and flux metrics.
- Maturity: paper-only
- Priority: Medium
