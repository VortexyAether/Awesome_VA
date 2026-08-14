# Optimization for Scientific Machine Learning

## Variational parameter calibration with physics-aware latent-space ROM surrogates

- Link: https://arxiv.org/abs/2608.11435
- Code: https://github.com/qiyaozhou963/rom-nn-da
- Type: Paper + early open tooling
- Keywords: reduced-order model, latent space, variational data assimilation, parameter calibration, differentiable surrogate, fluids
- One-line summary: Trains a physics-aware autoencoder latent ROM so the surrogate is informative for variational parameter estimation, not only accurate at forward field reconstruction.
- Why it matters:
  - Twin/inverse loops fail when latents reconstruct fields but carry weak parameter information.
  - Issue Board HTML: POD MSE **0.002424** vs POD-GPR **0.061342**; variational DA-DL-ROM lower estimation error than EnKF-POD-GPR on reported cases.
  - Continues the “downstream objective error” trust lens into calibration space.
- Caveat: GitHub ★0 and **SPDX license null** at curation → Watch/Test only, not product-Save. Geometry-family shift breadth still needs review.
- Possible use: After license check, steal parameter-informative latent supervision + variational DA loop shape for digital-twin calibration notes.
- Maturity: paper + early unlicensed-looking repo
- Priority: Medium


## Derivative computation in PINNs -- FD vs AD and silent autograd bugs

- Link: https://arxiv.org/abs/2608.11020
- Type: Paper / PINN numerics and implementation trust
- Keywords: PINN, automatic differentiation, finite differences, BatchNorm, self-attention, gradient path audit, GPU memory
- One-line summary: Shows calibrated finite-difference derivative paths can match AD accuracy on PINN PDE benches while running faster and using less GPU memory, and documents silent autograd failures under inter-sample dependencies (e.g. BatchNorm/self-attention idioms).
- Why it matters:
  - Engineering trust for residual PINNs is not only architecture choice -- the **derivative path** is part of the acceptance contract.
  - Reports **sFD rel L2 1.15% vs AD 1.66%** on a stationary case, with FD faster across tested batch sizes and materially lower memory.
  - Makes "standard PyTorch autograd snippet" a reviewable risk surface, not an invisible default.
- Caveat: Needs step-size/eps calibration; not claimed universal for every architecture. Re-run before product trainer claims.
- Possible use: Add FD-vs-AD and BatchNorm/attention gradient-path checks to any VA PINN/residual harness review checklist.
- Maturity: paper-only (method recipe)
- Priority: High

## Conformal risk control for model-form uncertainty in parametric NIROMs

- Link: https://arxiv.org/abs/2608.03360
- Type: Paper / ROM UQ and deployment validation
- Keywords: NIROM, model-form uncertainty, conformal risk control, reduced basis, parametric PDE, coverage
- One-line summary: Quantifies non-intrusive ROM model-form uncertainty from basis truncation via a perturbative stochastic reduced basis and distribution-free conformal risk control, with lambda* as an interpretable calibration diagnostic.
- Why it matters:
  - Deployment twins need coverage bands under parameter extrapolation, not only offline reconstruction error.
  - Treats basis truncation as structured model-form uncertainty rather than unstructured residual noise.
  - Adaptive conformal risk control is framed for heterogeneous error across parameter space -- closer to engineering gate language than a single global sigma.
- Caveat: Exchangeability assumptions can break under streaming plant data; public code not harvested; absolute coverage % needs PDF tables.
- Possible use: Cite when defining digital-twin green lights as conformal coverage + lambda* diagnostics beside Rel L2/RMSE reports.
- Maturity: paper-only
- Priority: High

## CT-PIKAN — coordinate-transformed Physics-Informed KAN + autograd metrics

- Link: https://arxiv.org/abs/2608.06660
- Code: https://github.com/m-heravifard/CT-PIKAN
- Type: Paper + early open MIT SciML solver scaffold
- Keywords: PIKAN, PINN, Kolmogorov-Arnold, curvilinear coordinates, metric tensor, automatic differentiation, geometry-aware PDE
- One-line summary: Solves PDEs on curvilinear domains by mapping to a regular computational chart and evaluating Jacobians/metric operators with autograd inside a physics-informed KAN loss — no hand-derived metric coefficients.
- Why it matters:
  - Cartesian PIKAN/PINN defaults fail the geometry bill on wavy/polar/non-orthogonal domains common in CAD-linked engineering.
  - Makes differential-geometry operators an inspectable implementation path (AD metrics) rather than paper-only transformed PINNs.
  - Public MIT scripts for 2D curvilinear heat/Poisson give a runnable starting point (repo ★0, pushed 2026-08-04).
- Caveat: Classical elliptic/parabolic/hyperbolic benches only; not an industrial mesh-CFD/BC gate. Author accuracy/robustness narrative needs independent re-run before product claims.
- Possible use: Smoke-test Poisson/heat scripts; prototype metric-aware residual stacks when Urban/CAD surfaces supply curvilinear charts.
- Maturity: paper + early public code
- Priority: High

## scikit-rom — open Python platform for projection-based ROM

- Link: https://arxiv.org/abs/2608.04960
- Code: https://github.com/suparnob100/scikit-rom
- Type: Paper + early open tooling (education / prototype)
- Keywords: ROM, POD, Galerkin, hyper-reduction, DEIM, ECSW, offline-online, accuracy report, Python
- One-line summary: Exposes projection-based reduced-order modeling as an inspectable Python stack from snapshot/POD/Galerkin through offline-online decomposition, hyper-reduction, and explicit Rel L2/RMSE/MAE/R² accuracy reports.
- Why it matters:
  - Many ROM stacks hide the multi-stage workflow behind GUIs or monolithic solvers; teaching and prototype harnesses need readable intermediate artifacts.
  - Useful template for surrogate acceptance contracts: report sample-wise Rel L2 / RMSE / MAE / R² instead of a single opaque “ROM error.”
  - GitHub `suparnob100/scikit-rom` ★2, pushed 2026-07-15 — live early code surface.
- Caveat: **No SPDX license** at API check → do not product-Save or depend until clarified. Demo cases are beam/linear teaching scale, not industrial CFD hyper-reduction claims.
- Possible use: Smoke-test install + tiny hyper-reduction example after license clarification; steal accuracy-report schema for VA ROM/surrogate harness notes.
- Maturity: prototype / watchlist (license blocked)
- Priority: Medium

## FALM-PINN — Fourier-enhanced alternating Levenberg–Marquardt

- Link: https://arxiv.org/abs/2608.05892
- Type: Paper / PINN training optimizer with Fourier feature decoupling
- Keywords: PINN, spectral bias, Levenberg-Marquardt, alternating optimization, Fourier features, multi-scale PDE
- One-line summary: Decouples representation learning (Fourier basis upper level) from coefficient fitting (LM lower level) to attack PINN spectral bias and representation–coefficient coupling.
- Why it matters:
  - Reframes many “PINN architecture” failures as optimization structure problems.
  - Reports relative L² gains up to ~2 orders vs strong baselines; Klein–Gordon harvest shows Vanilla ~8.11e-3 vs FALM ~4.42e-4 after alternating phase with multi-run stats.
  - Useful counterweight to residual-only leaderboards without optimizer protocol disclosure.
- Caveat: No public trainer harvested at curation; classical PDE suite, not industrial mesh CFD.
- Possible use: Cite when reviewing PINN claims or designing VA training recipes that separate feature bases from coefficient solves.
- Maturity: paper-only
- Priority: High

## SCORE — self-concordant quasi-Newton PINN training

- Link: https://arxiv.org/abs/2608.04206
- Type: Paper / quasi-Newton optimizer for residual PINNs
- Keywords: PINN, quasi-Newton, self-concordance, secant geometry, Burgers, nonconvex residual
- One-line summary: Stabilizes high-accuracy quasi-Newton PINN refinement with decrement-coupled shifted secant geometry inspired by self-concordant local metrics.
- Why it matters:
  - Residual PINN objectives are often indefinite, near-singular, and poorly scaled — BFGS-style refinement fails for structural reasons.
  - Burgers harvest: SCORE rel L² 2.25e-9 vs SSBroyden 1.40e-8 vs BFGS 1.56e-8 with multi-block mean/std reporting.
  - Pairs with FALM as the “optimizer axis” of PINN trust, not architecture name races.
- Caveat: No code harvested; four nonlinear PDE classical suite only.
- Possible use: Require optimizer identity + multi-seed residual tables before accepting high-precision PINN numbers into literature notes.
- Maturity: paper-only
- Priority: Medium

## SEAM — global consistency beyond local SciML accuracy

- Link: https://arxiv.org/abs/2608.05702
- Type: Paper / explanation-admissibility audit framework
- Keywords: SciML validation, explanation consistency, sheaf obstruction, multi-region audit, FNO OOD monitoring
- One-line summary: Introduces Scientific Explanation-Admissibility Machines (SEAM/SEAM-Ω) that test whether locally accurate explanations across regions, sensors, or regimes assemble into one globally admissible scientific account.
- Why it matters:
  - Local split accuracy and single-prediction explanations can look fine while neighboring patches disagree on overlaps.
  - Turns disagreement into a channel-resolved obstruction and separates inconsistency from non-identifiability; useful next to Modelassay-style license-to-deploy language.
  - Reports detection of incompatible explanations on synthetic PDEs and OOD FNO monitoring even when local predictions are accurate.
- Caveat: Theory-heavy sheaf/obstruction framing; not a one-line CFD CI metric yet. Treat as audit architecture, not tomorrow’s default dashboard KPI.
- Possible use: Cite when multi-region/sensor/regime CFD-ML patches need a global consistency gate beyond per-patch RMSE.
- Maturity: paper-only
- Priority: High

## Multi-granularity conformal prediction for automotive aero neural operators

- Link: https://arxiv.org/abs/2607.17297
- Code: https://github.com/DevinJia19/Multi-Granularity-Conformal-Prediction-for-Reliable-Neural-Operator-Automotive-Aerodynamic-Surrogate
- Type: Paper + early open reliability layer for aero surrogates
- Keywords: conformal prediction, automotive aerodynamics, DrivAerML, neural operator, surface WSS, drag uncertainty
- One-line summary: Converts deterministic neural-operator Cd / pressure / WSS predictions into calibrated case-level and spatially adaptive conformal intervals for follow-up CFD prioritization on DrivAerML.
- Why it matters:
  - Surrogate dashboards need “where not to trust” maps, not only mean-field beauty.
  - OOF conformal aggregation stabilizes coverage variance; point-adaptive residual normalization narrows surface intervals (~23% pressure, ~25–27% WSS width reductions in reported OOF setting) near nominal 90% coverage.
  - Pairs cleanly with Modelassay-style license-to-deploy language for design-loop surrogates.
- Caveat: Early public repo (low stars, license null via API at fetch). Finite-sample conformal guarantees still assume exchangeability and do not replace CFD verification budget.
- Possible use: Prototype conformal residual maps on Urban_Flighter / aero surrogate outputs before green-lighting geometry candidates.
- Maturity: paper + early public code
- Priority: High

## Multimodal AR transformer surrogate for geological CO₂ storage UQ

- Link: https://arxiv.org/abs/2608.02629
- Type: Paper / ops decision QoI surrogate under geological uncertainty
- Keywords: carbon storage, multimodal transformer, auto-regressive surrogate, UQ, injection controls, ops QoI
- One-line summary: Learns a multimodal auto-regressive transformer surrogate for variable well perforation/injection operations and reports engineering quantities (pressure, mobile mass, injected mass) under geological uncertainty.
- Why it matters:
  - Industrial acceptance often lives on ops decision QoIs and posterior bands, not single-step field RMSE.
  - Reported median errors include sat MAE ~0.028, pressure ~0.21%, total injected CO₂ ~2.3%.
  - Useful citation next to Modelassay-style deploy-license language for many-query subsurface/process twins.
- Caveat: SEAM-like faulted aquifer setting; not a drop-in open CFD code package.
- Possible use: Borrow the QoI+UQ reporting template when scoring CFD/thermal surrogates used for control or injection schedules.
- Maturity: paper-only
- Priority: Medium

## When May a Model Replace the Experiment? — surrogate audits & licenses

- Link: https://arxiv.org/abs/2608.01378
- Code: https://github.com/MAXMA-OSU/Modelassay
- Type: Paper + open toolkit for surrogate audit/licensing
- Keywords: surrogate validation, model assay, finite-sample license, design champion selection, audit, trust
- One-line summary: Reframes surrogate-driven design as an audit-and-license problem: when may a model replace an expensive experiment/simulation/training run under finite-sample guarantees, not R² vibes.
- Why it matters:
  - Engineering AI products need a deploy-time language for surrogate authority under selection bias and champion picking.
  - Toolkit explicitly targets pools, selection, and licenses rather than offline holdout accuracy alone.
  - Transferable vocabulary next to residual/rollout gates: generate → verify → license-to-deploy.
- Caveat: Primary framing is chemistry/materials/ML training runs; map carefully onto CFD residual/QoI/rollout contracts. Early MIT repo (low stars at fetch).
- Possible use: Prototype a Modelassay-style license wrapper around Urban_Flighter surrogate decision QoIs before treating low field error as experiment replacement.
- Maturity: paper + early open toolkit
- Priority: High

## Koopman ISS certification via projection residuals

- Link: https://arxiv.org/abs/2607.06459
- Type: Stability certification for data-driven Koopman learning control
- Keywords: Koopman learning, input-to-state stability, projection residual, repetitive systems, control validation
- One-line summary: Certifies when a fixed Koopman-assisted constrained update yields practical learning-axis stability, treating residuals, channel weakness, deployment shift, and numerical tolerances as ISS inputs.
- Why it matters: Learned engineering controllers should not be accepted on prediction accuracy alone. The paper’s explicit ultimate-band framing is a good reference for VA-style simulator/control agents that need certificate and fallback boundaries before affecting design or control decisions.
- Caveat: Theory/numerical control focus; no CFD-in-the-loop or real engineering deployment evidence yet.
- Possible use: Cite in learned-control validation notes for Urban_Flighter or surrogate MPC workflows.
- Maturity: paper-only
- Priority: High

## dpti — automated thermodynamic integration for MLIP phase diagrams

- Link: https://arxiv.org/abs/2607.05015
- Type: Automated computational workflow for phase diagrams with machine-learning interatomic potentials
- Keywords: thermodynamic integration, MLIP, phase diagram, workflow automation, molecular dynamics, error propagation
- One-line summary: Automates thermodynamic-integration workflows for phase-diagram calculations, including task orchestration, free-energy/error accounting, and phase-boundary propagation.
- Why it matters:
  - Shows the Engineering-AI pattern where the durable value is a domain workflow compiler, not just a model API.
  - Materials/MLIP workflows face the same trust issues as CFD optimization: path construction, solver/task orchestration, error propagation, reproducibility, and artifact provenance.
  - Useful analogy for CFD/thermal design loops where expensive high-fidelity solves must be coordinated with surrogate decisions and uncertainty checks.
- Caveat: Materials/MLIP-specific; package maturity, examples, dependencies, and license need follow-up.
- Possible use: Use as a workflow-automation reference when designing `DOE → solver task graph → error accounting → decision boundary` pipelines.
- Maturity: paper-only from current source check
- Priority: Medium

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
