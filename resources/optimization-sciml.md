# Optimization for Scientific Machine Learning

## Verified residual-specific explicit derivative kernels

- Link: https://arxiv.org/abs/2606.29702
- Type: Explicit differentiation / PINN and CFD adjoint verification infrastructure
- Keywords: PINNs, CFD adjoints, derivative kernels, residual Jacobian actions, partial-jet propagation, numerical verification
- One-line summary: Builds residual-specific explicit derivative kernels as a verifiable complement to nested automatic differentiation for derivative-heavy scientific computing.
- Why it matters:
  - Generic AD can become costly for high-order PDE residuals and complex discretized operators; explicit kernels expose the derivative path instead of hiding it in nested transforms.
  - The paper reports floating-point-level residual/gradient agreement, often 2–4x complete PINN training speedups, and lower peak GPU memory in most cases.
  - The finite-volume CFD residual example verifies tangent-action and transpose-action kernels with Taylor-remainder, inner-product, and reduced-gradient consistency checks before using them in a GPU-resident discrete-adjoint inversion workflow.
- Caveat: Code/reproduction harness still needs checking, and residual-specific kernels add per-operator implementation/verification cost.
- Possible use: Cite when arguing that CFD-AI/Engineering-AI trust depends on auditable derivative and residual primitives, not only field-prediction accuracy.
- Maturity: paper-only
- Priority: High

## SNAP-FM — sparse projection for physics-constrained generation

- Link: https://arxiv.org/abs/2607.00095
- Type: Constrained generative modeling / sparse nonlinear optimization
- Keywords: flow matching, physics constraints, conservation laws, boundary conditions, sparse KKT systems, ExaModels.jl, MadNLP.jl
- One-line summary: Enforces physics constraints during generative sampling by exploiting block-sparse nonlinear projection structure instead of treating projection as dense tensor post-processing.
- Why it matters:
  - Generative physical surrogates can look plausible while violating conservation laws, boundary conditions, or nonlinear invariants.
  - SNAP-FM makes inference-time constraint satisfaction a solver/composability problem, which is the right engineering trust boundary.
  - Useful counterweight to “AI solver” hype: the interesting part is the sparse optimization backend that forces outputs back onto the physical constraint set.
- Caveat: Industrial CFD geometry, noisy observations, code/reproduction surface, and benchmark breadth still need checking.
- Possible use: Cite when framing validation-gated or constraint-projected flow matching / diffusion surrogates.
- Maturity: paper-only
- Priority: High

## DSGNAR — well-conditioned PINN training

- Link: https://arxiv.org/abs/2607.02194
- Type: Physics-informed neural network optimization framework
- Keywords: PINNs, Gauss-Newton, sketching, ill-conditioning, numerical optimization, Navier-Stokes
- One-line summary: Frames PINN underperformance as an ill-conditioned optimization problem and proposes Doubly-Sketched Gauss-Newton with Adaptive Ratio regularization/step control.
- Why it matters:
  - Reinforces that solver-grade SciML needs numerical conditioning and diagnostics, not only new network architectures.
  - Reports improvements across nonlinear, chaotic, multi-scale, high-dimensional, and Navier-Stokes benchmarks, making it a useful citation for PINN failure-mode discussions.
  - Good comparison point for neural-operator and differentiable-solver workflows that claim classical-solver precision.
- Caveat: Code/repro harness and industrial-boundary-condition performance still need checking; treat the reported precision as a research claim, not deployment evidence.
- Possible use: Cite when arguing for conditioning checks and optimizer baselines in PINN/CFD surrogate evaluations.
- Maturity: paper-only
- Priority: High

## Multi-agent FEA-AI hybrid optimization for IPMSM design

- Link: https://arxiv.org/abs/2606.09037
- Type: Multi-agent engineering design optimization workflow
- Keywords: multi-agent system, FEA, uncertainty-aware surrogate, genetic algorithm, motor design, RAG
- One-line summary: Combines local LLM/RAG problem definition, automated FEA data generation, LLM-guided resampling, deep-ensemble uncertainty surrogates, and FEA-AI hybrid GA search for permanent-magnet motor design.
- Why it matters:
  - Strong workflow pattern for engineering automation: produce a design card, DOE plan, simulation logs, failure analysis, surrogate/UQ model, and fallback-triggered high-fidelity evaluations.
  - Treats surrogate uncertainty as a routing signal for when to trust fast inference and when to call expensive FEA.
  - Relevant to VA's CAD/CFD/thermal automation because the same contract can govern geometry sweeps, solver failures, retraining, and optimization candidates.
- Possible use: Use as a template for a `design card → DOE → solver logs → surrogate/UQ → optimizer → high-fidelity fallback` artifact schema.
- Maturity: paper-only
- Priority: High

## Learning practically stabilizing output-feedback nonlinear controllers

- Link: https://arxiv.org/abs/2606.16930
- Type: Surrogate controller learning / nonlinear output-feedback control
- Keywords: surrogate controller, output feedback, recurrent dynamics, Lyapunov function, practical stability
- One-line summary: Trains a recurrent surrogate to imitate an expensive nonlinear controller-observer pair while jointly learning a Lyapunov candidate to encourage practical stability.
- Why it matters:
  - Control-loop surrogates need stability and constraint-satisfaction evidence, not just imitation loss.
  - Relevant to CFD/thermal digital twins where a learned controller may approximate an MPC or high-cost observer but must remain safe under rollout.
  - The probabilistic validation framing is a useful pattern for acceptance tests before deploying a surrogate controller.
- Possible use: Use as a control-safety reference when evaluating surrogate MPC or learned flow-control policies.
- Maturity: paper-only
- Priority: Medium

## Online Spectral Deflation for State Constrained Optimal Control Problems

- Link: https://arxiv.org/abs/2606.17971
- Type: Solver-native acceleration for PDE-constrained optimal control
- Keywords: state constraints, active set, spectral deflation, nonlinear thermal, conjugate heat transfer
- One-line summary: Reuses low reference eigenmodes by restricting them to changing inactive sets, accelerating Jacobi-CG solves without replacing the high-fidelity optimal-control system.
- Why it matters:
  - Provides a strong non-ML baseline for repeated thermal/CFD optimal-control solves.
  - Reports 55–98% CG iteration reduction across diffusion, convection-diffusion, nonlinear thermal, and conjugate heat-transfer benchmarks.
  - Useful reminder that engineering design loops often need robust linear-algebra reuse as much as learned surrogates.
- Possible use: Compare against surrogate-assisted thermal control on wall-time, active-set stability, optimum quality, and validation residuals.
- Maturity: paper-only
- Priority: High

## Graphical conditional generative modeling for digital twins

- Link: https://arxiv.org/abs/2606.16219
- Type: Parsimonious stochastic surrogate modeling for digital twins
- Keywords: digital twin, conditional generative modeling, uncertainty, model selection, QoI
- One-line summary: Discovers which candidate variables influence the full conditional law of a target quantity, not only its conditional mean, to build compact digital-twin surrogates.
- Why it matters:
  - Digital twins can become unmaintainable when every possible variable, data stream, and timescale is included by default.
  - For partially observed or coarse-grained systems, tail behavior, variability, and multimodality can matter more than mean prediction.
  - Strong fit for VA's trust lens: build twins around quantities of interest and stress/safety testing rather than unconstrained fidelity creep.
- Possible use: Apply the idea as a feature-selection/ablation lens for thermal-fluid twins: include a variable only if it changes the conditional distribution of the relevant QoI.
- Maturity: paper-only
- Priority: High

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

## Implicit discrete adjoint gas-kinetic scheme for all-Mach aerodynamic optimization

- Link: https://arxiv.org/abs/2606.14112
- Type: Solver-native adjoint shape optimization for CFD
- Keywords: aerodynamic shape optimization, discrete adjoint, gas-kinetic scheme, all-Mach, hypersonic boundary conditions
- One-line summary: Develops an implicit discrete adjoint gas-kinetic scheme for aerodynamic shape optimization across subsonic, transonic, supersonic, and hypersonic regimes.
- Why it matters:
  - Provides a strong non-ML baseline for design automation: robust solver-native adjoints remain hard to beat when gradients and boundary conditions matter.
  - Explicit treatment of adiabatic no-slip and isothermal wall adjoint boundary conditions is relevant to hypersonic/thermal design.
  - Useful comparison point for ML-assisted inverse design and surrogate-assisted optimization claims.
- Possible use: Use as a citation anchor when arguing that CFD surrogate optimizers should be compared against adjoint-based solver workflows, not only black-box search.
- Maturity: paper-only
- Priority: High

## CANN-EUCLID

- Link: https://arxiv.org/abs/2606.14565
- Type: Unsupervised constitutive model discovery from full-field data
- Keywords: constitutive modeling, full-field data, interpretable neural network, computational engineering, FEA
- One-line summary: Extends constitutive artificial neural networks toward unsupervised model discovery from full-field data rather than stress-supervised homogeneous-test data.
- Why it matters:
  - Engineering validation often has full-field displacement/strain/temperature artifacts but incomplete direct labels for material laws.
  - Interpretable constitutive discovery is useful for FEA and coupled thermal-structural workflows where black-box stress predictors are not enough.
  - Transfers conceptually to VA's broader “artifact-to-law” lens for simulation-backed design automation.
- Possible use: Track as a reference for using full-field measurement/simulation data to identify material/closure laws under limited direct supervision.
- Maturity: paper-only
- Priority: Medium

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

## NUCLEUS-MoE for pool boiling liquid cooling

- Link: https://arxiv.org/abs/2605.27722
- Type: Mixture-of-experts surrogate for boiling heat-transfer regimes
- Why it matters:
  - Targets pool boiling and liquid cooling, where phase change, turbulence, and operating conditions make one-size-fits-all surrogates fragile.
  - Regime-aware expert routing is a practical pattern for thermal-fluid models near transitions and critical heat flux boundaries.
  - Relevant to electronics cooling and data-center thermal design where uncertainty and safe operating envelopes matter.
- Possible use: Prototype a thermal surrogate that routes between single-phase, nucleate-boiling, transition, and high-risk regimes with solver fallback.
- Maturity: paper-only
- Priority: High

## ML-adapted finite-difference thermal profiling for a lunar rover

- Link: https://arxiv.org/abs/2605.27651
- Type: Physics-grid plus ML-correction thermal model
- Why it matters:
  - Uses a finite-difference thermal model adapted with machine learning for faster profiling under extreme radiative/environmental conditions.
  - Useful pattern for engineering thermal twins: keep an interpretable physical grid model, then learn corrections for speed or calibration.
  - Transfers conceptually to battery packs, electronics enclosures, and cooling subsystems where full thermal simulation is too slow for iteration.
- Maturity: paper-only
- Priority: Medium

## Physics-informed reward shaping for building energy control

- Link: https://arxiv.org/abs/2605.28232
- Type: Physics-informed RL reward design for thermal/energy control
- Why it matters:
  - Addresses comfort versus energy tradeoffs in building control by shaping SAC rewards with physics-informed terms.
  - Relevant to thermal-control agents because reward design is often the hidden failure mode, especially when comfort, grid, and equipment constraints conflict.
  - Useful as a non-CFD but control-relevant reference for preventing reward hacking in thermal-management loops.
- Maturity: paper-only
- Priority: Medium

## POD-AS-PRS for sensitivity-dominant fluid ROM parameters

- Link: https://arxiv.org/abs/2606.02315
- Type: Reduced-order modeling / active-subspace sensitivity method
- Why it matters:
  - Combines POD-style reduction with active subspaces to identify parameters that dominate fluid-dynamics model response.
  - Useful interpretable baseline or companion to neural surrogates when CFD design spaces are high-dimensional but only a few directions matter.
  - Helps prioritize simulation campaigns and parameter sweeps before training expensive surrogate models.
- Maturity: paper-only
- Priority: Medium

## Sensitivity-Conditioned Bernoulli Flow Matching for Topology Optimization

- Link: https://arxiv.org/abs/2606.02179
- Type: Generative surrogate / OOD generalization analysis for topology optimization
- Why it matters:
  - Studies why topology-optimization surrogates generalize unevenly under load and boundary-condition shifts.
  - Conditions generation on sensitivity information, which is closer to optimization physics than pure image-style layout prediction.
  - Relevant to CAD/design-automation agents where surrogate outputs must survive distribution shift and downstream verification.
- Possible use: Add sensitivity-distribution diagnostics to topology-optimization or CAD surrogate benchmarks.
- Maturity: paper-only
- Priority: High

## Continuous Data Assimilation with Learned Surrogate Dynamics

- Link: https://arxiv.org/abs/2606.00480
- Type: Learned-dynamics surrogate for data assimilation / control-oriented estimation
- Why it matters:
  - Studies continuous data assimilation when the real dynamics are unknown or too expensive and a learned surrogate is used instead.
  - Directly relevant to sensor-driven CFD/thermal digital twins where surrogate model error and partial observations interact.
  - Good reminder that surrogate quality should be evaluated inside the estimation/control loop, not only as offline prediction.
- Maturity: paper-only
- Priority: High

## Simulation-aided intelligent sensing for hidden temperature fields

- Link: https://arxiv.org/abs/2606.04582
- Type: Sparse-sensor thermal-field reconstruction / simulation-aided surrogate
- Keywords: thermal sensing, temperature field reconstruction, sparse sensors, simulation data, digital twin
- One-line summary: Trains neural temperature-field reconstruction from randomized physics-based simulations, then infers unobservable internal fields from sparse embedded sensors in real time.
- Why it matters: Thermal-fluid digital twins often cannot instrument the most important internal locations; simulation-aided sensing is a practical bridge between physics models and online monitoring.
- Possible use: Prototype sparse sensor → full field reconstruction with Kriging, POD-NN, and neural-operator baselines on a heat-transfer benchmark.
- Maturity: paper-only
- Priority: High

## Laser-ion spectrum surrogate for regime mapping and closed-loop control

- Link: https://arxiv.org/abs/2606.06210
- Type: Physics-guided high-dimensional output surrogate with uncertainty quantification
- Keywords: physics surrogate, VAE, uncertainty quantification, regime transition, closed-loop control
- One-line summary: Uses a dual-branch β-VAE/MLP surrogate plus deep ensembles to predict proton spectra and map acceleration-regime transitions.
- Why it matters: Although outside CFD, it is a strong pattern for engineering surrogates that must predict full distributions, expose uncertainty, and support closed-loop facility control.
- Possible use: Borrow the “spectrum/distribution + scalar boundary + UQ” evaluation idea for thermal-fluid outputs with regime transitions.
- Maturity: paper-only
- Priority: Medium

## Bayesian surrogate and sensitivity analysis for flotation control

- Link: https://arxiv.org/abs/2606.06173
- Type: Gaussian-process decision support for industrial process control
- Keywords: process control, Bayesian modeling, global sensitivity analysis, SHAP, decision support
- One-line summary: Combines GP regression, Sobol sensitivity indices, and SHAP explanations to turn flotation experiment data into interpretable control guidance.
- Why it matters: Useful non-CFD process-control example where surrogate value comes from uncertainty, sensitivity, and operator-readable decisions rather than prediction alone.
- Possible use: Use as a template for reporting which design/control variables dominate a CFD or thermal process surrogate.
- Maturity: paper-only
- Priority: Medium

## REMAL residual-equilibrium active learning for multidisciplinary design analysis

- Link: https://arxiv.org/abs/2606.13245
- Type: Surrogate-based multidisciplinary design analysis / active learning
- Keywords: MDA, active learning, surrogate modeling, equilibrium consistency, coupled systems
- One-line summary: Uses residual equilibrium consistency in coupled multidisciplinary systems to guide active learning for surrogate-based design analysis.
- Why it matters:
  - In coupled engineering systems, each discipline surrogate can look accurate while the integrated equilibrium state is inconsistent.
  - The residual/equilibrium-manifold lens is useful for design automation, thermal-structural-fluid coupling, and digital twins where coupling variables must agree.
  - Moves surrogate evaluation from isolated component error toward coupled-system validity.
- Possible use: Add coupling residual and fixed-point consistency checks to surrogate-assisted design optimization experiments.
- Maturity: paper-only
- Priority: High

## Sequential feedback optimization for wind-farm power maximization

- Link: https://arxiv.org/abs/2606.08315
- Type: Real-time flow-control optimization benchmark
- Keywords: sequential feedback optimization, wind farm, MPC, extremum seeking, dynamic flow model
- One-line summary: Benchmarks sequential feedback optimization against adjoint-based economic MPC and extremum seeking control on a nine-turbine dynamic-flow wind-farm layout.
- Why it matters:
  - Compares steady-state power, transient behavior, and computational cost under identical constraints, which is the right deployment lens for control-oriented flow optimization.
  - Provides a practical reference for when a lower-cost online optimizer may beat heavier MPC in real-time feasibility.
  - Relevant to VA-style CFD/control surrogates where the final metric is operational objective improvement, not field RMSE alone.
- Possible use: Borrow the comparison structure for flow-control experiments: objective, transient response, convergence, actuator constraints, and wall-clock budget.
- Maturity: paper-only
- Priority: Medium
