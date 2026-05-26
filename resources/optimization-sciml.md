# Optimization for Scientific Machine Learning

## SpecMuon: Muon with Spectral Guidance

- Link: https://arxiv.org/abs/2602.16167
- Type: Optimizer for Scientific ML
- Summary:
  - Adapts the Muon optimizer idea for scientific computing / physics-informed learning.
  - Introduces spectral-aware guidance to handle ill-conditioned gradients, multi-scale spectral behavior, and stiffness.
- Why it matters:
  - PINNs and neural operators often fail because optimization is poorly conditioned, not because the architecture is impossible.
  - CFD applications frequently involve stiffness, multi-scale spectra, and hard physical constraints.
  - Since CFD-specific applications may still be sparse, this could be a good early exploration topic.
- Possible follow-up:
  - Test on PINN benchmarks, operator-learning problems, or differentiable CFD inverse problems.
  - Compare against AdamW, L-BFGS, Shampoo-like second-order-ish optimizers, and baseline Muon.

## Attention Residuals

- Link: https://github.com/MoonshotAI/Attention-Residuals/tree/master
- Type: Neural network architecture / residual connection method
- Summary:
  - Addresses information dilution in fixed residual connections.
  - Applies softmax attention over previous layer outputs to select and aggregate needed information data-dependently.
  - Introduces Block AttnRes to reduce memory overhead and support large models.
- Why it matters:
  - Potentially relevant to deep surrogate models, neural operators, and long-depth architectures where residual information routing matters.

## CLARA compartment-model generation for multiphase reactors

- Link: https://arxiv.org/abs/2604.26695
- Type: CFD-to-compartment-model reduction / control-oriented surrogate tooling
- Why it matters:
  - Automates reduced compartment-model generation from expensive multiphase CFD simulations.
  - Directly connects CFD, real-time control, design optimization, and interpretable surrogate modeling.
  - Strong candidate for lab discussion because it is closer to deployable engineering control than generic AI-for-PDE claims.

## Robust multi-jet active flow control

- Link: https://arxiv.org/abs/2604.26481
- Type: Active flow control / reinforcement-learning-inspired control framework
- Why it matters:
  - Addresses robustness of multi-jet actuation for airfoil flow control in weakly compressible flow.
  - Useful for connecting SciML/control papers to aerodynamic actuation and closed-loop CFD experiments.
  - Track as a control benchmark idea rather than only an architecture paper.


## Graph Neural ODE Digital Twins for reactor thermal-hydraulic forecasting

- Link: https://arxiv.org/abs/2604.07292
- Type: Control-oriented thermal-hydraulic surrogate / digital twin
- Why it matters:
  - Targets real-time supervisory control under partial observability, not just offline field prediction.
  - Connects graph neural dynamics, thermal-hydraulic systems, and robust forecasting for advanced reactors.
  - Useful anchor for thinking about CFD/SciML surrogates as control components with sensor limitations.
- Possible use: Compare against neural-operator or reduced-order baselines on sensor-to-state forecasting tasks.
- Maturity: paper-only
- Priority: High

## Safe active learning for sensor reliability qualification

- Link: https://arxiv.org/abs/2605.00868
- Type: Autonomous experiment planning / safe active learning
- Why it matters:
  - Uses Gaussian-process surrogate modeling to choose experiments under coupled thermal and hydrogen stress.
  - Relevant pattern for expensive engineering campaigns where failures, safety limits, or long test durations constrain exploration.
  - Transfers conceptually to CFD/thermal design-space exploration: sample efficiently without stepping into invalid or unsafe regimes.
- Maturity: paper-only
- Priority: Medium

## Buffet alleviation via linear stability adjoint

- Link: https://arxiv.org/abs/2605.04884
- Type: CFD shape optimization / stability adjoint
- Why it matters:
  - Replaces empirical transonic buffet-onset surrogates with a linear-stability eigenvalue constraint inside aerodynamic shape optimization.
  - Efficiently differentiates the dominant LST eigenvalue with respect to many shape variables using a coupled adjoint strategy.
  - Useful anchor for high-fidelity CFD optimization where the objective is not only drag but stability margin and flight-envelope safety.
- Possible use: Compare against ML surrogate-based buffet criteria when discussing trustworthy aerodynamic design constraints.
- Maturity: paper-only
- Priority: High

## Differentiable multiphysics co-optimization via implicit neural representations

- Link: https://arxiv.org/abs/2605.01040
- Type: Differentiable transient multiphysics optimization benchmark
- Why it matters:
  - Couples implicit neural geometry with a JAX-compiled Eulerian multiphysics solver for joint geometry, boundary-condition, material, and process optimization.
  - Includes heat transfer, phase change, moving boundaries, contact changes, and process controls in one end-to-end differentiable loop.
  - Useful as a compact benchmark for testing whether differentiable physics workflows survive messy transient multiphysics rather than only clean PDE demos.
- Maturity: paper-only
- Priority: Medium

## Spatial-correlation curriculum for PINNs

- Link: https://arxiv.org/abs/2605.15254
- Type: PINN training curriculum / optimization method
- Why it matters:
  - Uses spatial correlation to schedule Physics-Informed Neural Network training for nonlinear PDEs.
  - Explicitly relevant to fluid mechanics, heat transfer, and solid mechanics where PINN training can be unstable or inefficient.
  - Useful as a training-protocol reference when comparing PINNs against neural operators or classical solvers.
- Possible use: Test whether spatial-correlation curricula improve convergence on thermal diffusion or incompressible-flow PINN baselines.
- Maturity: paper-only
- Priority: Medium

## PI-SONet

- Link: https://arxiv.org/abs/2605.14332
- Type: Physics-informed symplectic neural operator for real-time optimal control
- Why it matters:
  - Learns a reusable solution map for parameterized Pontryagin Maximum Principle systems instead of rerunning a single-instance optimal-control solver.
  - Preserves Hamiltonian structure through a conditional symplectic operator and reports sub-second inference / large speedups on high-dimensional multi-agent control settings.
  - Useful for thinking about SciML surrogates as control-loop components where structure preservation matters as much as prediction speed.
- Possible use: Compare conceptually with thermal supervisory-control surrogates and flow-control settings where repeated optimal-control queries are the bottleneck.
- Maturity: paper-only
- Priority: Medium

## Accelerating Bayesian inverse design in CFD using neural operators

- Link: https://arxiv.org/abs/2605.26059
- Type: Bayesian inverse-design acceleration / neural operator surrogate
- Why it matters:
  - Keeps the Bayesian likelihood, priors, and sampler structure intact while swapping repeated CFD solves for a trained operator surrogate.
  - Evaluates whether posterior geometry and uncertainty trends survive surrogate substitution, which is a stronger test than one-shot reconstruction accuracy.
  - Relevant to aerodynamic and thermal design loops where sparse observations and uncertainty matter.
- Possible use: Use posterior preservation as a validation criterion for VA-style surrogate-assisted design optimization.
- Maturity: paper-only
- Priority: High
