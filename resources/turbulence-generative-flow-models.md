# Turbulence & Generative Flow Models

Resources for turbulence prediction, reduced-order modeling, super-resolution, autoregressive flow prediction, learned closures, and generative modeling of physical fields.

## Physics-constrained SGS — prediction-embedded training beats residual-fit labels

- Link: https://arxiv.org/abs/2608.28525
- Type: Paper / LES turbulence closure (physics.flu-dyn)
- Keywords: LES, SGS, premixed flame, conservation, equivariance, embedded training
- One-line summary: Embeds an SGS net in the resolved equations under conservation, scalar boundedness, and equivariance, scaled by residual size, and trains on predicted trajectories rather than residual labels.
- Why it matters:
  - A priori residual MAE is not a long LES. Embedded rollout beats residual-fit of the same net.
  - API 2026-08-28; Suh/MacArt/Olson/Freund. Abstract: beats no-model / dynamic / residual-fit on long-time dissipation and flame kinematics.
  - Issue Board HTML: LES inference **+14%** vs no-model. No public code.
- Caveat: Single-species one-step irreversible chemistry. Not an urban/external-flow transfer. Test withheld.
- Possible use: Cite when an SGS net quotes residual MAE — demand embedded rollout vs residual-fit ablation.
- Maturity: paper-only
- Priority: High

## Self-augmented diffusion guidance — residual as a sample condition

- Link: https://arxiv.org/abs/2608.26748
- Type: Paper / physics-informed generative fluids (cs.LG)
- Keywords: diffusion, physics residual, Darcy, guidance, CoCoGen
- One-line summary: Learns the data distribution conditioned on deviation from the governing equation and samples at deviation=0, without solving the PDE at every denoising step.
- Why it matters:
  - Visual fluid frames are not dynamics. Residual-as-condition is cheaper than per-step PDE and still needs a shock/spectral check.
  - abs 2026-08-27; Osaka/Takeishi/Yairi. Issue Board HTML: Darcy mean residual **4.97e-2 → 1.19e-2** (1x); 2x **1.11e-2**; PIDM+CoCoGen **6.90e-3**. No public code.
- Caveat: Darcy + 2D fluid sequences. Residual drop ≠ conservation of shocks or spectra.
- Possible use: Cite when a generative fluid model shows frames — ask residual-as-condition vs per-step PDE.
- Maturity: paper-only
- Priority: High

## RTI ROM — put nonlinearity in dynamics or in the latent

- Link: https://arxiv.org/abs/2608.26783
- Type: Paper / RTI reduced-order model (physics.flu-dyn)
- Keywords: Rayleigh-Taylor, ROM, POD, PINN, autoencoder, mixing
- One-line summary: Compares linear POD plus PINN nonlinear dynamics against a nonlinear autoencoder with linear physics-constrained latent dynamics on DNS Rayleigh–Taylor transition.
- Why it matters:
  - Latent compactness is not a statement of where the nonlinearity lives.
  - API 2026-08-27; Granger/Nadiga/Gréa/Briard/Creusy. Tracks mixing-layer growth plus 1D TKE and dissipation profiles.
  - Both strategies reconstruct, interpolate, and extrapolate at a qualitative “satisfactory” level. No public code. No single RMSE locked in the abstract.
- Caveat: Qualitative performance language. Pair with the 08-28 vortex-shedding waterbed result: more modes can still lose the loop.
- Possible use: Cite when a mixing ROM sells latent size — ask whether nonlinearity sits in the encoder or the dynamics.
- Maturity: paper-only
- Priority: High

## Vortex-shedding LQG — higher-order ROM can lose the loop

- Link: https://arxiv.org/abs/2608.24435
- Type: Paper / closed-loop ROM control (physics.flu-dyn)
- Keywords: vortex shedding, LQG, DMD-c, waterbed, cylinder, DDES
- One-line summary: Shows that raising ROM order past a sweet spot can worsen vortex-shedding suppression via the waterbed effect, while a 2D-trained controller still cuts 3D DDES drag 13.7%.
- Why it matters:
  - Latent compactness is not closed-loop stability. More modes can increase sensitivity in unmodelled bands.
  - API 2026-08-25; Proudfoot/Nicholls/Tang/Bacic. Re=1000 cylinder. Lift-only LQG needs ≥4th order; best near **9 modes**; >14 modes drop. Lift-variance **−28.6 dB**, 2D drag **−26%**. 3D DDES Cd **−13.7%**. Claimed `Jackp-1/LQG-Cylinder-Control` GitHub API 404.
- Caveat: Cylinder bench. Code missing → Test withheld. Sweet spot is Re/sensor-specific.
- Possible use: Cite when a control ROM adds modes for accuracy — demand an order sweep and a 2D-train / 3D-deploy check.
- Maturity: paper-only
- Priority: High

## Residual LSTM on Wagner — transonic unsteady airfoil lift

- Link: https://arxiv.org/abs/2608.17894
- Type: Paper / aeroelastic residual learner
- Keywords: Wagner function, residual learning, LSTM, NLR 7301, transonic shock, leave-family-out
- One-line summary: Trains an LSTM on CFD minus analytical Wagner lift so the network learns a lower-variance unsteady correction instead of the full force history.
- Why it matters:
  - Direct NN lift models can look fine on in-family sinusoids and then fail when a motion family is held out.
  - Table 7 (5-seed external NRMSE): residual **0.054±0.007** vs direct **0.065±0.009**. Direct wins pitch-only; residual wins plunge and coupled pitch-plunge.
  - Residual lowers family-mean NRMSE across four motion families in leave-one-out / leave-family-out; authors note the baseline must actually remove structured response.
- Caveat: 2D NLR 7301. Some high-frequency cases favor the direct model. No public code. 3D wing / Mach interpolation left as future work.
- Possible use: Cite when a classical low-order aero theory exists — require leave-family-out, not a single pitch NRMSE.
- Maturity: paper-only
- Priority: High

## LBM for compressible Navier–Stokes–Fourier (auto-derived D3Q7)

- Link: https://arxiv.org/abs/2608.13437
- Type: Paper / classical compressible LBM trust substrate
- Keywords: lattice Boltzmann, compressible NSF, shock thickness, viscous shock, dilatational dissipation, Taylor-Green, symbolic compiler
- One-line summary: Automatically derives and validates a 3D compressible NSF lattice Boltzmann scheme (D3Q7) that carries viscous stress and heat flux as transported state variables, with Sod/Becker and supersonic TGV evidence.
- Why it matters:
  - Raises the classical floor any compressible ML surrogate must clear: shock thickness, viscous shocks, and dilatational dissipation channels—not only field RMSE.
  - Reports first-order shock-thickness convergence on Sod/Becker exact solutions and ~**30%** closer dilatational dissipation than the next-best of seven compared solvers on supersonic TGV \(M_0=1.25\) at \(512^3\) (Issue Board HTML).
  - Single-precision deploy realism is part of the validation story.
- Caveat: Public code not listed at harvest. Not a general industrial FV/BC stack. LBM-specific assumptions remain.
- Possible use: Cite when defining compressible SciML acceptance tables (shock thickness + dilatational/solenoidal split) before surrogate leaderboards.
- Maturity: paper-only
- Priority: High

## Free-stream transition iLES database (T3-class)

- Link: https://arxiv.org/abs/2606.20139
- Dataset: https://doi.org/10.5281/zenodo.17166216
- Type: Transition turbulence database for model/ML development
- Keywords: bypass transition, iLES, ERCOFTAC T3, free-stream turbulence, full-field 3D
- One-line summary: Supplies wall-resolved, full-field 3D time-resolved free-stream transition data that classic T3 integral experiments cannot provide for modern RANS/ML transition work.
- Why it matters:
  - Transition acceptance needs inlet turbulence parameters and measurement-channel fidelity, not only \(C_f\) curves.
  - Public Zenodo packaging makes the corpus a real Save candidate after schema inspection.
- Caveat: Flat-plate bypass; industrial 3D geometry transition is a separate gate. Cross-listed under datasets-benchmarks.
- Possible use: Pull inlet/mesh tables when designing transition-model or ML closure tests.
- Maturity: paper + Zenodo dataset
- Priority: Medium-High

## Phase-drift ROM — autoregressive rollout error as accumulated phase drift

- Link: https://arxiv.org/abs/2608.07189
- Code: https://github.com/Syphonicc/phase-drift-rom
- Type: Paper + open OpenFOAM→ROM ladder (MIT)
- Keywords: ROM, CAE-LSTM, phase drift, vortex shedding, rollout stability, bluff-body wake, OpenFOAM
- One-line summary: Shows that long-horizon latent ROM error on bluff-body wakes is highly structured phase drift at the shedding frequency, not unstructured noise, and corrects it with one-parameter phase realignment gated by an R² diagnostic.
- Why it matters:
  - One-step validation can look almost perfect while timing error of a few thousandths of a cycle drives long-horizon field error.
  - Reports attractor amplitudes matched within ~**0.15%** RMS while **95–98%** of rollout error is pure phase error on Re 100–800 circular/square cylinders.
  - Public MIT repo with OpenFOAM cases turns the diagnosis into a runnable acceptance ladder (train → diagnose phase → correct iff R² allows).
- Caveat: Periodic bluff-body wakes only; do not wholesale-transfer to broadband turbulence or strongly transient regimes. Early ★0 repo / WIP surface.
- Possible use: Add phase/spectrum + R² applicability gates next to HERO-style nRMSE@H when green-lighting wake/ROM surrogates.
- Maturity: paper + early open code
- Priority: High

## Symplectic Geometric Closure (SGC) — dual-cascade geometry as a closure constraint

- Link: https://arxiv.org/abs/2608.06606
- Type: Paper / structure-preserving turbulence closure theory
- Keywords: symplectic geometry, SGS closure, dual cascade, Kraichnan, online stability, Hamiltonian subgrid transport, 2D turbulence
- One-line summary: Derives a Symplectic Geometric Closure from multilayer stochastic models so unresolved degrees of freedom feed back through constrained Hamiltonian exchange that preserves dual-cascade geometry and online stability.
- Why it matters:
  - Data-driven SGS often fit residuals while losing the geometric architecture that makes inverse-energy / forward-enstrophy cascades and long-time coarse evolution possible.
  - Reframes acceptance as geometric/structure gates (augmented enstrophy, pullback boundedness, Lie-transport subgrid velocity), not field RMSE alone.
  - Connects to Kraichnan-type DIA operator architecture and classical \(k^{-5/3}\)/\(k^{-3}\) cascade admission in the dressed Eulerian theory.
- Caveat: 2D theory-first (58 pages); no public code harvested; transfer to 3D wall-bounded industrial LES is unproven.
- Possible use: Cite when defining learned-closure green lights as online stability + cascade/invariant diagnostics beside a posteriori spectra.
- Maturity: paper-only
- Priority: High

## TIDE — 3D DNS ensembles as turbulence-ML acceptance floor

- Link: https://arxiv.org/abs/2608.04222
- Code: https://github.com/Dyloong1/TIDE-dataset-benchmark
- Dataset: https://huggingface.co/datasets/ydai17/TIDE
- Type: Turbulence benchmark / generative & operator forecasting substrate
- Keywords: 3D turbulence, DNS, ensemble trajectories, rollout fidelity, spectral metrics, SciML
- One-line summary: Positions 3D incompressible DNS ensembles with equation-level residual checks as the turbulence-ML testbed where pointwise accuracy is not enough.
- Why it matters:
  - Makes “accuracy ≠ physical fidelity” and “single realization ≠ dynamics learning” measurable rather than rhetorical.
  - Forced/decay and multi-axis generalization splits are stronger than random holdouts for operator/generative flow models.
- Caveat: Not a wall-bounded industrial CFD mesh benchmark; storage footprint is large.
- Possible use: Cite next to Neptuna/HERO when arguing multi-metric turbulence rollout gates.
- Maturity: paper + MIT code + CC-BY-4.0 data
- Priority: High

## Hybrid-Joint — joint differentiable SGS + wall closures for WMLES

- Link: https://arxiv.org/abs/2607.17357
- Type: Paper / differentiable hybrid neural-CFD closure learning
- Keywords: WMLES, SGS closure, wall model, differentiable CFD, joint training, turbulent boundary layer
- One-line summary: Learns subgrid and wall closures jointly inside a differentiable flow solver as composed neural operators plus fixed structure-preserving layers, using low-order statistics only.
- Why it matters:
  - Treats SGS, wall model, and discretization as coupled through the resolved field rather than as independent offline fits.
  - Reports a posteriori TBL tests across Re_θ≈600–6500 with >4× Re extrapolation, log-law recovery without imposing it, and spectral recovery without spectral training losses.
  - Ablations show single-closure learning is insufficient — a strong pattern for solver-in-the-loop acceptance.
- Caveat: Paper-only at curation; complex-geometry product CFD still needs separate gates.
- Possible use: Cite when defining joint-closure training contracts for wall-bounded LES surrogates.
- Maturity: paper-only
- Priority: High

## Round-Trip Consistency — bidirectional diffusion predicts own rollout error

- Link: https://arxiv.org/abs/2608.00675
- Type: Paper / measurement-free rollout uncertainty signal
- Keywords: rollout UQ, bidirectional diffusion, latent dynamics, long-horizon error, test-time self-check
- One-line summary: Trains one conditional latent diffusion model to step a dynamical system forward or backward via a direction flag, then uses forward-then-backward round-trips as a ground-truth-free deploy-time error signal.
- Why it matters:
  - Autoregressive surrogates accumulate error with no labels at deployment; self-reported risk is the missing acceptance piece beside train-time nRMSE@H.
  - Complements HERO-style long-horizon training and control-ROM stability checks with a measurement-free test-time probe.
- Caveat: Primary demo is plasma/MHD latent diffusion; not a drop-in unstructured CFD operator. No first-party research code package confirmed beyond HF ecosystem chrome.
- Possible use: Cite when designing deploy-time rollout risk monitors for CFD/thermal operator stacks.
- Maturity: paper-only
- Priority: High

## PITT — physics-informed token transformer for nonlinear balance laws

- Link: https://arxiv.org/abs/2607.23143
- Type: Paper / hybrid hyperbolic balance-law solver representation
- Keywords: balance laws, FNO, token transformer, Rankine–Hugoniot, shock, weak solutions
- One-line summary: Combines symbolic equation tokenization, an FNO encoder, explicit Rankine–Hugoniot shock motion, and piecewise steady-state profiles for 1D nonlinear hyperbolic balance laws.
- Why it matters:
  - Structure-aware weak-solution machinery is a stronger engineering pattern than pure black-box rollout on shock-dominated fluids.
  - Useful bridge citation between neural operators and classical shock relations.
- Caveat: Part I focuses on Schwarzschild–Burgers-style 1D settings; residual tables need careful column reading; no public code harvested.
- Possible use: Cite when arguing hybrid structure+learning representations for flood/shock-adjacent surrogates.
- Maturity: paper-only
- Priority: Medium

## Compactness vs forecast accuracy — controlled wake latent ROMs

- Link: https://arxiv.org/abs/2607.24569
- Type: Control-oriented fluid reduced-order modeling study
- Keywords: ROM, POD, convolutional autoencoder, wake control, latent dynamics, long-horizon forecast
- One-line summary: Compares POD vs nonlinear CAE/VAE encoders plus latent predictors on actuated truck-wake and fluidic-pinball flows, focusing on the tradeoff between latent compactness and long-horizon forecast stability.
- Why it matters:
  - Control/MPC ROMs need stable predictions over the horizon used for optimization, not only sharp short-horizon reconstruction.
  - Nonlinear latents can compress well yet become broadband and more divergence-prone over long horizons; smoother POD latents can be preferable for control.
  - Complements neural-operator rollout gates (e.g. HERO nRMSE@H) with a ROM-side acceptance principle: forecast stability over max compression.
- Caveat: 2D actuated wakes; reported accuracy definitions are not identical to nRMSE@H; no public code at curation time.
- Possible use: Cite when setting green-light criteria for control-oriented CFD surrogates and latent dynamics models.
- Maturity: paper-only
- Priority: High

## Mori-Zwanzig graph neural networks for turbulent transport

- Link: https://arxiv.org/abs/2606.14918
- Type: Physics-structured GNN surrogate for Lagrangian turbulent transport
- Keywords: turbulence, Mori-Zwanzig, graph neural network, Lagrangian particles, memory model
- One-line summary: Learns tracer-particle acceleration as a finite-memory expansion over present and delayed particle-neighborhood graphs, with equivariant GNNs parameterizing the memory terms.
- Why it matters:
  - Sparse particle/sensor views of turbulence are not Markovian; unresolved Eulerian degrees of freedom appear as memory and noise in reduced dynamics.
  - Evaluates autoregressive rollout on statistics not imposed during training, including heavy-tailed acceleration, pair dispersion, and four-particle tetrad geometry.
  - Strong reference for reduced turbulence digital twins where learned dynamics must reproduce multi-particle observables, not only one-step field error.
- Possible use: Compare finite-memory GNN rollouts against Markovian particle predictors and diffusion trajectory samplers on Lagrangian turbulence benchmarks.
- Maturity: paper-only
- Priority: High

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

## Honest drag-reduction control under reward hacking

- Link: https://arxiv.org/abs/2606.06227
- Type: Reinforcement-learning flow-control failure analysis
- Keywords: wall turbulence, drag reduction, recurrent MARL, reward hacking, energy accounting
- One-line summary: Shows that wall-turbulence drag-reduction agents can exploit misaligned rewards, then fixes the loop with differentiable projection, recurrent policies, and true wall-power accounting.
- Why it matters: Flow-control ML needs honest physical accounting; a controller can report drag reduction while increasing total dissipation if reward design is wrong.
- Possible use: Use as a validation reference for VA-style control benchmarks: reward, actuator cost, energy budget, and closed-loop physics should be audited separately.
- Maturity: paper-only
- Priority: High

## Hybrid Generative Reduced-Order Model for the Minimal Flow Unit

- Link: https://arxiv.org/abs/2606.09044
- Type: Generative reduced-order model for wall-bounded turbulence
- Why it matters:
  - Combines latent generative modeling with reduced-order dynamics to forecast intermittent near-wall turbulence from sparse sensor measurements.
  - Connects three practical surrogate requirements: compression of high-dimensional flow fields, sparse sensing, and long-horizon rollout stability.
  - Useful comparison point for deterministic ROMs, neural operators, and diffusion/flow-matching field generators.
- Possible use: Evaluate sparse-sensor-to-field rollout methods using spectrum, wall quantities, and long-horizon stability metrics.
- Maturity: paper-only
- Priority: Medium

## Boundary-layer-induced failure benchmark for standard PINNs

- Link: https://arxiv.org/abs/2606.09676
- Type: PINN failure benchmark for singularly perturbed transport
- Why it matters:
  - Shows how standard PINNs can fail on boundary-layer-dominated transport problems where the solution changes sharply near boundaries.
  - Directly relevant to heat-transfer and wall-flow surrogates, where wall gradients and fluxes matter more than average domain error.
  - Encourages validation metrics that separately track local extrema, wall flux, gradient accuracy, and boundary-layer resolution.
- Possible use: Add a boundary-layer stress test before trusting PINN/FNO/POD-NN models in thermal or near-wall CFD workflows.
- Maturity: paper-only
- Priority: High

## Spectrally Regularized Latent Flow Matching for Turbulence Generation

- Link: https://arxiv.org/abs/2606.11691
- Type: Generative turbulence model / latent flow matching
- Why it matters:
  - Targets a concrete failure mode of latent diffusion/flow-matching turbulence generators: under-representation of dissipation-range amplitudes.
  - Uses a zone-weighted log-spectral objective in the compression stage, raising retained deep-dissipation spectral power substantially in both reconstruction and unconditional generation.
  - Good reminder that turbulence surrogate validation needs spectrum/detail metrics, not only pointwise field loss or visually plausible samples.
- Possible use: Compare against diffusion, FNO, POD/ROM, and deterministic super-resolution baselines using energy spectrum, structure functions, phase/coherence diagnostics, and sampling cost.
- Maturity: paper-only; accepted at AI4Physics Workshop at ICML 2026
- Priority: High

## Data-driven surrogate models for experimentally measured fluid-flow forecasting

- Link: https://arxiv.org/abs/2606.10848
- Type: Experimental fluid-flow surrogate benchmark / PIV forecasting
- Why it matters:
  - Trains FCNN, U-Net, FNO, and DMD-style models on experimentally measured cylinder-wake PIV velocity fields rather than clean synthetic CFD data.
  - Shows faster-than-real-time short-horizon forecasting is possible, but transient features and high-frequency energy content degrade under noisy, incomplete observations.
  - Strong validation reference for VA-style CFD-AI: real sensors and experimental data expose failure modes hidden by simulation-only random splits.
- Possible use: Use as a benchmark pattern for sparse/noisy observation stress tests before trusting CFD surrogates in control or digital-twin loops.
- Maturity: paper-only
- Priority: High
