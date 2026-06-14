# CFD-AI Papers & Surveys

Selected broad survey papers and discovery maps for CFD-AI, Scientific Machine Learning, and machine learning for fluid mechanics. Method-specific papers should live in their topic files instead of here.

## Recent Advances on Machine Learning for Computational Fluid Dynamics: A Survey

- Link: https://arxiv.org/abs/2408.12171
- Type: Paper / survey
- Keywords: CFD-AI, survey, data-driven surrogate, physics-informed surrogate, ML-assisted CFD
- One-line summary: A survey that classifies recent ML-for-CFD work into data-driven surrogates, physics-informed surrogates, and ML-assisted numerical solutions.
- Why it matters: Useful as a high-level taxonomy for deciding where a new CFD-AI project sits: full surrogate, physics-informed model, or solver-assist component.
- Possible use: Use the taxonomy to organize literature review sections and to avoid mixing fundamentally different CFD-AI problem settings.
- Maturity: paper-only
- Priority: High

## Machine Learning for Fluid Mechanics

- Link: https://www.annualreviews.org/doi/abs/10.1146/annurev-fluid-010719-060214
- Type: Paper / review
- Keywords: fluid mechanics, machine learning, reduced-order modeling, flow control, turbulence
- One-line summary: A broad Annual Review article on machine learning methods and opportunities in fluid mechanics.
- Why it matters: This is a useful foundational review for understanding how ML enters fluid mechanics beyond a narrow neural-operator or CFD-surrogate framing.
- Possible use: Use as background reading for thesis/literature-review framing and for connecting CFD-AI work to classical fluid-mechanics questions.
- Maturity: paper-only
- Priority: High

## Machine Learning Accelerated Computational Fluid Dynamics

- Link: https://arxiv.org/abs/2102.01010
- Type: Paper / review
- Keywords: CFD acceleration, machine learning, surrogate modeling, numerical solvers
- One-line summary: A review of machine-learning approaches for accelerating CFD workflows.
- Why it matters: Useful for distinguishing ML-as-replacement from ML-as-accelerator and for identifying practical insertion points inside CFD pipelines.
- Possible use: Use as a framing citation for projects where ML accelerates meshing, solvers, closure models, or post-processing rather than replacing CFD entirely.
- Maturity: paper-only
- Priority: Medium

## Source lists used for discovery

### Awesome-AI4CFD

- Link: https://github.com/WillDreamer/Awesome-AI4CFD
- Type: Paper collection / survey companion repository
- Keywords: CFD-AI, machine learning for CFD, surrogates, physics-informed learning, neural operators
- One-line summary: A structured paper list accompanying the survey “Recent Advances on Machine Learning for Computational Fluid Dynamics.”
- Why it matters: The repository organizes ML-for-CFD literature by benchmark datasets, data-driven surrogates, physics-informed surrogates, ML-assisted numerical solutions, applications, and frontier models.
- Possible use: Use as a literature-map starting point when surveying CFD-AI methods, selecting baselines, or building category-specific reading lists for surrogate modeling and ML-assisted solvers.
- Maturity: maintained library
- Priority: Medium

### Awesome Machine Learning for Fluid Mechanics

- Link: https://github.com/ikespand/awesome-machine-learning-fluid-mechanics
- Type: Paper/code collection
- Keywords: fluid mechanics, machine learning, review papers, datasets, open-source codes
- One-line summary: A broad curated list of machine learning papers, code, libraries, datasets, labs, and resources for fluid mechanics.
- Why it matters: Complements CFD-specific lists by covering the wider fluid-mechanics ML landscape, including interpretability, reduced-order modeling, reinforcement learning, geometry optimization, datasets, and open-source CFD codes.
- Possible use: Use as a discovery index for older foundational papers, review papers, datasets, and fluid-mechanics ML toolchains that may not appear in newer CFD-AI survey lists.
- Maturity: maintained library
- Priority: Medium

## Deep Learning-based Algebraic Reynolds Stress Closures for RANS Simulations

- Link: https://arxiv.org/abs/2605.26358
- Type: ML turbulence closure / RANS solver-coupled modeling
- Keywords: RANS, turbulence closure, Reynolds stress, distribution shift, CFD-AI
- One-line summary: Develops deep-learning-based algebraic Reynolds-stress closures for turbulent RANS simulations, focusing on the solver-coupled closure problem rather than only offline regression.
- Why it matters: ML closure models often fail when inserted into a CFD solver because the state distribution shifts; this is a practical reminder that turbulence ML must be evaluated in closed-loop solver contexts.
- Possible use: Use as a turbulence-closure reading anchor when comparing offline stress prediction, solver stability, and field-level CFD validation.
- Maturity: paper-only
- Priority: High

## Emergent Transfer of a Physics Foundation Model from Simulation to Laboratory Turbulence

- Link: https://arxiv.org/abs/2606.01470
- Type: Physics foundation model / sim-to-lab turbulence study
- Why it matters:
  - Tests whether a simulation-trained physics foundation model transfers to laboratory Rayleigh-Taylor instability data.
  - Raises the bar beyond benchmark accuracy toward experimental deployment and domain-shift robustness.
  - Useful reliability reference for CFD-AI claims involving foundation models or universal emulators.
- Possible use: Add to a sim-to-experiment transfer reading list for turbulence and scientific foundation models.
- Maturity: paper-only
- Priority: High

## FluidFlower CO2 injection SciML surrogate and Bayesian inference

- Link: https://arxiv.org/abs/2606.05448
- Type: Multiphase-flow surrogate and inverse modeling study
- Why it matters:
  - Combines surrogate modeling and Bayesian inference for CO2-brine flow in porous media using the FluidFlower experiment.
  - Relevant to nonlinear, partially observed multiphase systems where inverse parameters matter as much as forward prediction.
  - Good example for connecting SciML surrogates to experimental data and uncertainty-aware inference.
- Maturity: paper-only
- Priority: Medium

## Drifting Models for Surrogate Flow Modeling

- Link: https://arxiv.org/abs/2606.07481
- Type: Generative CFD surrogate / real-time flow-field modeling
- Why it matters:
  - Adapts generative drifting to fluid mechanics by generating CFD-like flow fields in a learned VAE latent space.
  - Targets the practical latency problem of diffusion-style generative surrogates: similar accuracy and flow consistency with two-orders-of-magnitude faster single-pass inference.
  - Uses label-aware masking for boundary-condition alignment and explores spatial conditioning for unseen geometries.
- Possible use: Compare against diffusion, FNO, POD-NN, and deterministic baselines on field error, boundary-condition consistency, and inference latency for interactive design exploration.
- Maturity: paper-only
- Priority: High

## No-Harm Physics-Informed Inverse Learning with Residual-Calibrated Uncertainty

- Link: https://arxiv.org/abs/2606.07153
- Type: Physics-informed inverse problem certification / uncertainty gate
- Why it matters:
  - Proposes a certification-and-selection layer that accepts a learned reconstruction only when its residual-calibrated uncertainty radius is no worse than a baseline.
  - Combines data, physics, boundary/initial-condition, and optimization residuals into an auditable “do no harm” fallback contract.
  - Relevant to CFD/thermal surrogate governance, where a learned model should be allowed to abstain or return a trusted baseline under shift or ill-posedness.
- Possible use: Implement a no-harm gate around thermal/CFD inverse reconstruction experiments before trusting learned updates in a digital twin.
- Maturity: paper-only
- Priority: High

## TransportBench

- Link: https://arxiv.org/abs/2606.02997
- Type: Benchmark / dataset for non-equilibrium flow transport
- Keywords: SciML benchmark, non-equilibrium flow, rarefied gas, hypersonic flow, shock discontinuities
- One-line summary: Provides high-fidelity datasets and unified evaluation protocols for continuum/rarefied, low-speed/hypersonic, inert/reactive, and translational/internal-energy non-equilibrium flows.
- Why it matters:
  - Existing SciML/CFD benchmarks often over-focus on continuum Navier-Stokes-like settings and miss non-equilibrium transport regimes.
  - The benchmark explicitly probes shock-dominated discontinuities, multi-scale effects, and generalization across geometry and physical parameters.
  - Reports that no single architecture consistently wins across all tasks, which is a useful antidote to generic “best model” claims.
- Possible use: Use as an evaluation reference when designing CFD surrogate tests that need regime shift, shock handling, and multi-scale statistics.
- Maturity: paper + benchmark/code availability claimed in abstract
- Priority: High
