# CFD-AI Papers & Surveys

Selected broad survey papers and discovery maps for CFD-AI, Scientific Machine Learning, and machine learning for fluid mechanics. Method-specific papers should live in their topic files instead of here.

## Interpreting CFD surrogates through sparse autoencoders

- Link: https://arxiv.org/abs/2507.16069
- Type: Interpretability method for graph-based CFD surrogates
- Keywords: CFD surrogate, sparse autoencoder, graph neural network, interpretability, audit
- One-line summary: Trains sparse autoencoders on frozen node embeddings from graph-based CFD surrogates to extract latent feature dictionaries for post-hoc interpretation.
- Why it matters:
  - CFD surrogate trust should include whether learned latent features correspond to meaningful flow structures or numerical artifacts.
  - Complements uncertainty and validation gates with an internal representation audit for MeshGraphNet/Transolver-style models.
  - Useful warning that a surrogate can look accurate while relying on brittle or non-physical latent shortcuts.
- Possible use: Run SAE probes on a trained cylinder/airfoil graph surrogate and compare discovered features with vortices, boundary layers, pressure gradients, and mesh artifacts.
- Maturity: workshop paper
- Priority: Medium

## Validated LBM dataset and pipeline for turbulent 3D obstructed channel flows

- Link: https://arxiv.org/abs/2606.16765
- Type: Validated CFD dataset-generation pipeline / surrogate benchmark seed
- Keywords: LBM, turbulent channel flow, 3D obstructed geometry, neural operators, dataset validation
- One-line summary: Presents a reproducible cumulant-LBM pipeline for 3D obstructed channel-flow data at Re=1,000–10,000, with grid convergence and experimental checks against Strouhal number, drag coefficients, and turbulent fluctuations.
- Why it matters:
  - Moves CFD surrogate evaluation toward verified data-generation pipelines rather than unvalidated synthetic fields.
  - Useful for testing forecasting, super-resolution, and error-correction neural operators with turbulent-energy-cascade and physics-informed metrics.
  - Good template for VA-style dataset manifests: geometry generator, solver config, convergence evidence, experimental anchors, split definition, and metric contract.
- Possible use: Use as a benchmark-design reference before training FNO/U-Net/graph surrogates on generated 3D turbulent flow data.
- Maturity: paper / pipeline described
- Priority: High

## Geometry-conditioned latent surrogate for spray interface breakup

- Link: https://arxiv.org/abs/2606.16587
- Type: Multiphase CFD surrogate / geometry-conditioned latent model
- Keywords: two-phase flow, spray formation, nozzle design, AMR, VOF, geometry-conditioned surrogate
- One-line summary: Learns transient spray breakup from 797 two-phase nozzle simulations by encoding AMR cell-density fields as a compact proxy for where the solver concentrates resolution.
- Why it matters:
  - Directly connects geometry variation to transient multiphase behavior, a practical CAD-to-CFD surrogate setting.
  - Treats adaptive-mesh behavior as useful physical/numerical structure instead of ignoring discretization changes.
  - Relevant for nozzle/cooling/spray design loops where interface topology and breakup timing matter more than smooth global field error.
- Possible use: Compare against full-state latent surrogates on geometry-held-out spray cases; report interface location, breakup timing, conservation, and downstream design objective error.
- Maturity: paper-only
- Priority: High

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

## Machine learning for rarefied gas transport in vacuum and micro/nano systems

- Link: https://arxiv.org/abs/2606.14039
- Type: Perspective / verification agenda for rarefied-gas ML
- Keywords: rarefied gas, DSMC, moment closure, gas-surface interaction, verification, micro/nano flow
- One-line summary: Surveys how machine learning is entering rarefied-gas modeling and argues that the central problem is a regime-specific verification agenda rather than only better headline accuracy.
- Why it matters:
  - Rarefied, hypersonic, vacuum, and micro/nano gas-transport settings break many assumptions behind continuum CFD surrogate benchmarks.
  - Useful checklist source for learned collision physics, operator learning, moment closures, DSMC field surrogates, and gas-surface models.
  - Helps separate credible engineering deployment from toy PDE surrogate demonstrations.
- Possible use: Build a VA validation checklist for rarefied/hypersonic surrogate claims: Knudsen-regime coverage, wall interaction model, DSMC/high-fidelity comparison, conservation/residual checks, and fallback rules.
- Maturity: paper / perspective
- Priority: High

## Fully GPU-based workflow for hypersonic physics emulators

- Link: https://arxiv.org/abs/2606.13742
- Type: GPU-native data-generation and physics-emulator workflow
- Keywords: hypersonic flow, GPU workflow, physics emulator, surrogate pretraining, workflow automation
- One-line summary: Proposes a GPU-based pipeline that integrates accelerated hypersonic data generation, surrogate pretraining, and physics-aware emulator training.
- Why it matters:
  - Treats the emulator as part of an end-to-end engineering workflow rather than a standalone model trained after simulation data already exists.
  - Hypersonic flows stress surrogate reliability through shocks, steep gradients, and thermal/aerodynamic coupling.
  - Relevant to VA because data-generation throughput, artifact lineage, and validation cases are the bottleneck for useful design-space exploration.
- Possible use: Prototype an artifact manifest for emulator pipelines that records solver config, mesh/domain, seed, generated cases, training split, validation regimes, and failure cases.
- Maturity: paper-only
- Priority: High

## Feature-preserving Latent-EnKF for shock-dominated flow data assimilation

- Link: https://arxiv.org/abs/2606.12559
- Type: Data assimilation method for compressible flows with shocks
- Keywords: EnKF, data assimilation, shocks, compressible flow, latent representation, digital twin
- One-line summary: Addresses the failure of Gaussian ensemble assumptions in shock-dominated flows by moving flow data assimilation into a feature-preserving latent space.
- Why it matters:
  - CFD digital twins for compressible flows need shock/discontinuity location accuracy, not just smoothed field-level RMSE.
  - Useful reminder that uncertainty in feature location can create multimodal ensembles that vanilla EnKF handles poorly.
  - Provides a validation lens for learned surrogate/state-estimation pipelines under discontinuities.
- Possible use: Compare vanilla EnKF, localization tricks, and latent/feature-preserving updates on Burgers/Euler shock benchmarks using shock-location error and conservation residuals.
- Maturity: paper-only
- Priority: High

## Domain-validity-gated metamorphic testing of SciML surrogates

- Link: https://arxiv.org/abs/2606.17529
- Type: Validation framework / oracle-free SciML surrogate testing
- Keywords: metamorphic testing, CFD surrogate validation, MeshGraphNets, FNO, MR-card, claim ledger
- One-line summary: Screens candidate metamorphic relations for domain validity, then turns admitted relations into executable MR-cards with source cases, transformations, metrics, tolerances, and typed verdicts.
- Why it matters:
  - Directly addresses the oracle problem for CFD/SciML surrogates: exact expected fields may be unavailable, but valid relations can still become auditable tests.
  - Separates true model-level violations from invalid or out-of-domain test assumptions, as shown on cylinder-flow, compressible-airfoil, Burgers, and heat surrogates.
  - Strong pattern for VA validation harnesses: every claim should bind to a tracked artifact, tolerance, numerical-floor check, and relation-level verdict.
- Possible use: Implement MR-card assets around heat-transfer and flow surrogates before trusting them in design/control loops.
- Maturity: paper-only
- Priority: High

## GPU-native neural surrogate for kinetic Fokker-Planck rarefied/hypersonic flows

- Link: https://arxiv.org/abs/2606.15622
- Type: Learned closure inside a rarefied-flow particle simulation loop
- Keywords: Fokker-Planck, rarefied flow, hypersonic cylinder, GPU surrogate, learned closure
- One-line summary: Replaces expensive cubic-Fokker-Planck closure calculations with a GPU-native neural surrogate deployed directly in the particle simulation loop.
- Why it matters:
  - Shows a learned model inserted into an online solver component, not just a post-hoc field emulator.
  - Validation emphasizes runtime profiles, break-even cost, conservation/stability diagnostics, particle-per-cell sensitivity, and entropy-proxy fidelity.
  - Relevant to hypersonic/thermal surrogate governance because near-wall and high-order kinetic diagnostics matter more than smooth field RMSE.
- Possible use: Use its audit structure as a template for learned-closure experiments in rarefied or shock/heating regimes.
- Maturity: paper-only
- Priority: High

## Multiscale hypersonic boundary layer reconstruction via spectral binning and conditional diffusion

- Link: https://arxiv.org/abs/2606.15023
- Type: Probabilistic hypersonic near-wall reconstruction surrogate
- Keywords: hypersonic flow, boundary layer, conditional diffusion, spectral loss, uncertainty
- One-line summary: Reconstructs Mach-conditioned hypersonic Couette near-wall fields from limited top-wall observations using subdomain-wise conditional diffusion and bounded binned spectral power loss.
- Why it matters:
  - Hypersonic wall-bounded turbulence needs spectral/high-wavenumber fidelity, wall quantities, and uncertainty structure, not only average profile accuracy.
  - The subdomain/inpainting setup is a practical pattern for large 3D fields where one global generator may be too coarse or unstable.
  - Useful evaluation reference for sparse-sensor thermal/fluid digital twins under extreme regimes.
- Possible use: Add binned spectral metrics and wall-quantity diagnostics to surrogate reconstruction tests.
- Maturity: paper-only
- Priority: High

## ShipNet

- Link: https://arxiv.org/abs/2606.15356
- Type: Geometric deep-learning surrogate for ship hydrodynamics
- Keywords: ship design, hydrodynamics, geometric deep learning, hull pressure, free-surface waves
- One-line summary: Predicts hull-surface pressure coefficients and far-field free-surface wave elevation from hull point clouds and speed using a dynamic graph backbone.
- Why it matters:
  - A concrete geometry-to-hydrodynamics surrogate for design-space exploration with geometry-held-out evaluation and fast inference.
  - Also exposes a common risk: results are constrained by two parent hull families and inviscid potential-flow training data.
  - Good example for VA's CAD/CFD surrogate rubric: report geometry-family shift, solver fidelity limits, and downstream design-objective error.
- Possible use: Track as an application reference, but demand viscous/high-fidelity validation before treating it as engineering-grade.
- Maturity: paper-only
- Priority: Medium
