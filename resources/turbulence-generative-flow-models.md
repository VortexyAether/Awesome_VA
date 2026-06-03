# Turbulence & Generative Flow Models

Resources for turbulence prediction, reduced-order modeling, super-resolution, autoregressive flow prediction, learned closures, and generative modeling of physical fields.

## Turbulence Modeling in the Age of Data

- Link: https://arxiv.org/abs/1804.00183
- Type: Paper / review
- Keywords: turbulence modeling, data-driven modeling, RANS, LES, closure models
- One-line summary: A review focused on how data-driven methods interact with turbulence modeling and closure problems.
- Why it matters: Turbulence closure is one of the most important and failure-prone targets for CFD-AI, so this is a key grounding reference before proposing learned turbulence models.
- Possible use: Use to frame turbulence-surrogate work, RANS/LES closure discussions, and the limitations of purely data-driven turbulence modeling.
- Maturity: paper-only
- Priority: High

## Watchlist themes

- Turbulent-flow super-resolution and spectral consistency metrics
- Autoregressive flow-field prediction and rollout stability
- Learned RANS/LES closure models
- Generative models for physical fields
- Sensor-to-field reconstruction and sparse observation assimilation

## LESnets for wall-bounded turbulence

- Link: https://arxiv.org/abs/2604.26621
- Type: Physics-informed neural operator for LES-style wall turbulence prediction
- Why it matters:
  - Focuses on 3D wall-bounded turbulent flows where multiscale vortices and long-rollout stability are difficult for generic PINO models.
  - Brings LES intuition into neural-operator design rather than treating turbulence as only a high-dimensional image sequence.
  - Useful candidate for evaluating high-Reynolds-number surrogate claims beyond low-dimensional benchmark PDEs.
- Possible use: Track as a comparison point for wall-bounded turbulence datasets and PINO variants.
- Maturity: paper-only
- Priority: High

## Realizability-Constrained Machine Learning for Turbulence Closures in Wake Flows

- Link: https://arxiv.org/abs/2605.12304
- Type: Physics-constrained learned turbulence closure
- Why it matters:
  - Addresses numerical instability, residual stagnation, and non-physical behavior that can appear when symbolic-regression or ML turbulence closures are embedded in CFD solvers.
  - Reinforces that learned closures need realizability and stability constraints, not only offline fit quality.
  - Directly relevant to wake-flow modeling and any attempt to put ML closures into production-like CFD loops.
- Possible use: Use as a reference for closure-model validation gates: realizability, solver convergence, residual behavior, and physical stress constraints.
- Maturity: paper-only
- Priority: High

## Physical Fidelity Reconstruction via Consistency-Distilled Flow Matching

- Link: https://arxiv.org/abs/2605.05975
- Type: Distilled generative model for coarse-to-fine fluid reconstruction
- Why it matters:
  - Distills an optimal-transport flow-matching teacher into a one-step consistency model for faster high-fidelity flow reconstruction.
  - Evaluates on Smoke Buoyancy, Turbulent Channel Flow, and Kolmogorov Flow with spectrum-oriented physical fidelity checks.
  - Relevant to simulation-in-the-loop visualization and ensemble workflows where iterative diffusion/flow-matching sampling is too slow.
- Possible use: Benchmark distilled reconstruction against deterministic super-resolution and FNO-style baselines using spectrum, gradient, and conservation diagnostics.
- Maturity: paper-only
- Priority: Medium

## Dynamic-Probabilistic Consistency Gap in Chaotic Surrogate Modeling

- Link: https://arxiv.org/abs/2605.31547
- Type: Chaotic dynamical-system surrogate / uncertainty training analysis
- Why it matters:
  - Shows that finite-horizon probabilistic objectives can produce uncertainty estimates that are not dynamically consistent with local tangent dynamics.
  - Identifies failure modes such as core collapse, noise masking, and blind uncertainty.
  - The KAFFEE framework uses differentiable EKF-style covariance transport through learned Jacobians, a useful idea for long-rollout fluid or thermal surrogates.
- Possible use: Add uncertainty/dynamics consistency checks to CFD surrogate validation beyond one-step RMSE.
- Maturity: paper-only
- Priority: High

## Emergent transfer of a physics foundation model to laboratory turbulence

- Link: https://arxiv.org/abs/2606.01470
- Type: Paper / physics foundation model for turbulence
- Keywords: turbulence, Rayleigh-Taylor instability, physics foundation model, simulation-to-experiment transfer, Walrus
- One-line summary: Fine-tunes a continuum-dynamics foundation model on a few DNS Rayleigh-Taylor cases and tests zero-shot transfer to noisy laboratory turbulence data.
- Why it matters: The paper targets the hard question of whether simulation-trained physics foundation models can leave the idealized DNS regime and explain laboratory behavior.
- Possible use: Use as a reading anchor for sim-to-real validation, sparse/noisy experimental transfer, and foundation-model claims in fluid mechanics.
- Maturity: paper-only
- Priority: High

## 4D-flow MRI data assimilation with resolvent analysis for stenotic turbulence

- Link: https://arxiv.org/abs/2606.03838
- Type: Paper / experimental-computational flow analysis
- Keywords: data assimilation, resolvent analysis, 4D-flow MRI, stenotic flow, PINN
- One-line summary: Couples 4D-flow MRI, PINN-based data assimilation, RANS-compatible mean-field recovery, stability analysis, and resolvent analysis for stenotic turbulent flow.
- Why it matters: It is a concrete example of sparse experimental velocity data being converted into physics-consistent fields and coherent-structure analysis, rather than only doing black-box reconstruction.
- Possible use: Use as a workflow reference for sensor/MRI/PIV data assimilation pipelines before applying modal or stability analysis to experimental flows.
- Maturity: paper-only
- Priority: Medium
