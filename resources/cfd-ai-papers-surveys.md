# CFD-AI Papers & Surveys

## Dimension-bridging 3D RANS — 2D airfoil coefficients corrected toward 3D wing QoI

- Link: https://arxiv.org/abs/2608.27639
- Type: Paper / multi-fidelity aero QoI (cs.CE)
- Keywords: RANS, Gaussian functional regression, multi-fidelity, airfoil, wing, adaptive sampling
- One-line summary: Learns a GFR correction from 2D RANS aerodynamic coefficients to 3D RANS coefficients when reduced dimensionality changes the governing physics.
- Why it matters:
  - 2D rank is not a 3D wing receipt. Adaptive UQ sampling is the HD budget, not a denser 2D grid.
  - API 2026-08-27; Lao/Scott/Bui-Thanh/Laiu/Bement. Abstract: fewer HD evals than stationary kernels; NN kernel “millions of times” wall-clock.
  - Issue Board HTML: three QoIs **1.93×10⁶** on a single CPU with primal reuse. No public code.
- Caveat: k-ω SST held fixed. Family-shift width not the lead table. Test withheld.
- Possible use: Cite when a 2D RANS surrogate is sold for 3D design — demand the HD correction + adaptive UQ.
- Maturity: paper-only
- Priority: High

## Inverse-PINN two-axis diagnosis — field accuracy can hide the wrong coefficient

- Link: https://arxiv.org/abs/2608.15373
- Type: Paper / inverse-PINN diagnosis
- Keywords: PINN, inverse, identifiability, residual profile, field RMSE
- One-line summary: Separates finite-sample resolution under a stated observation protocol from the signed parameter preference encoded by the final field and residual view.
- Why it matters:
  - Matching the field is not recovering the coefficient. The two can even move in opposite directions.
  - Zhang/Tao. Abstract: matched-forward MAE **2.34%–17.46%**; displacement vs signed log-error in 240 RBA runs **r=.994** (237/240 direction).
  - Issue Board HTML: 24 intervention fields, field rel L2 vs parameter relative error **r = 0.057**; Allen–Cahn / Buckley–Leverett / Burgers MAE% **2.34 / 6.69 / 17.46**. No public code.
- Caveat: 1D synthetic scalar PDEs. Diagnostic coordinates, not an oracle-free estimator. Test withheld.
- Possible use: Cite when an inverse PINN quotes field RMSE — demand coefficient error on the same observation protocol.
- Maturity: paper-only
- Priority: High

## SnapPINN — freeze velocity, then Poisson from one sparse snapshot

- Link: https://arxiv.org/abs/2608.26711
- Type: Paper / sparse-sensing PINN (physics.flu-dyn + physics.comp-ph)
- Keywords: PINN, sparse snapshot, dissipation, pipe DNS, Poisson
- One-line summary: Reconstructs 3D velocity, gradients, pressure, and TKE dissipation from one sparse noisy velocity snapshot by freezing a sine-MLP velocity net, then solving Poisson pressure.
- Why it matters:
  - Bulk velocity is not a dissipation receipt. Gradient QoI needs a separate gate.
  - API 2026-08-27; Barta/Bauer/Bagheri. 3D DNS turbulent pipe, **100** cases. Seeding **0.07–17.59%** of the DNS grid.
  - Bulk U **<0.5%** even at extreme sparsity; dissipation **~50%** at f=0.07%; a-posteriori Re_τ **4–24%**. No public code.
- Caveat: One pipe geometry. The 50% dissipation error is a sparsity limit, not a win. Test withheld.
- Possible use: Cite when a sparse-sensor PINN quotes bulk velocity — demand dissipation / gradient QoI at the same seeding.
- Maturity: paper-only
- Priority: High

## Mortar mixer — Np–Re plus numerical dissipation %

- Link: https://arxiv.org/abs/2608.27423
- Type: Paper / classical mortar FEM rotating mixer (physics.flu-dyn + math.NA)
- Keywords: mortar, ALE, mixer, power number, numerical dissipation, SUPG
- One-line summary: Couples rotor and stator with mortar cells in a matrix-free high-order CG Navier–Stokes solver and reports both the experimental Np–Re curve and energy-balance numerical viscosity.
- Why it matters:
  - A learned mixer head needs a rotating-geometry skeleton that does not hide dissipation.
  - API 2026-08-27; Campos/Munch/Ferreira/Boffito/Banquy/Blais. 2D Rushton torque; 3D pitched-blade **Np vs Re = 1–2000**.
  - Numerical dissipation **1% (Re=200) / 10% (Re=2000)**. Ideal strong scaling on large problems. No code link in the API.
- Caveat: Classical numerics, not AI. Code unverified.
- Possible use: Cite as the rotating-geometry substrate before attaching a learned mixer head — require Np–Re plus dissipation %.
- Maturity: paper-only
- Priority: High

## PINN remedies — FP64 and alignment fix disjoint slices

- Link: https://arxiv.org/abs/2608.25327
- Type: Paper / PINN verification (cs.LG + cs.AI)
- Keywords: PINN, FP64, SSM, alignment, seed, convection
- One-line summary: Shows under pre-registered seed-paired controls that FP32→FP64 and SSM+sub-sequence alignment repair disjoint equation/seed slices; neither substitute for the other.
- Why it matters:
  - Precision is not architecture. Residual/stopping criteria are not solution success.
  - API 2026-08-26; Zhang/He/Hu/Yuan/Jiao. 11 pages. Pre-registered **144-run** + independent **85-run**. Success = Rel ℓ2 < 0.05.
  - Hard convection β=50: alignment **2/5** (FP32) / **3/5** (FP64); unaligned SSM **0/5**; vanilla MLP 0/5→1/5. Reaction backbone alone 3/5–4/5. Tight L-BFGS tolerance lowers median error with success counts unchanged.
- Caveat: 1D convection/reaction/wave. No public code → Test withheld.
- Possible use: Cite when a PINN “fix” is only FP64 or only a new backbone — demand per-seed success, not a median residual.
- Maturity: paper-only
- Priority: High

## Entropy-stable ALE moving-wall NS

- Link: https://arxiv.org/abs/2608.25146
- Type: Paper / classical entropy-stable ALE (math.NA + math.AP)
- Keywords: entropy-stable, ALE, moving wall, SBP, NACA, compressible NS
- One-line summary: Recasts compressible Euler/NS on moving domains in ALE form and proves entropy-conservative/stable moving-wall conditions through a high-order SBP semi-discretization.
- Why it matters:
  - Learned FSI heads need a hard hyperbolic/entropy skeleton before a residual lottery.
  - API 2026-08-25; Galimberti/Nuca/Dalcin/Guardone/Parsani. 57 pages, 15 figures. No-slip in wall-relative velocity.
  - Issue Board cases: isentropic vortex, annular Poiseuille, heaving-pitching NACA-0012, 2-DOF airfoil, supersonic.
- Caveat: Classical numerics, not AI. Code link not in API.
- Possible use: Cite as the moving-wall entropy substrate before attaching a learned surrogate head.
- Maturity: paper-only
- Priority: High

## JICF chapter — LOSO splits by QoI

- Link: https://arxiv.org/abs/2608.26064
- Code: https://github.com/KjayJunIOR/parametric-sindy-jax-gridsearch
- Type: Book chapter + unlicensed JAX SINDy (physics.flu-dyn)
- Keywords: jet-in-cross-flow, LOSO, QoI, SINDy, MLP, ROM
- One-line summary: Maps injector spacing to unburnt H₂, wall heat, and bulk temperature, then shows leave-one-sample-out error is QoI-dependent; parametric SINDy is a compact field ROM, not a better bulk RMSE.
- Why it matters:
  - Decision QoI is not field RMSE. Offline response surfaces are not dynamic ROMs.
  - API 2026-08-26; Eduku/Popov/Jacobs. 18 pages. Non-monotonic spacing; favorable region near 8D.
  - Issue Board HTML: LOSO bulk T **1.46%** (all <4%), wall heat **27.2%**, H₂ **21.7%**. SINDy Reynolds-stress nRMSE **+6.7%** vs POD. GitHub ★0, SPDX NOASSERTION, pushed 2026-08-26.
- Caveat: Small-sample hydrogen JICF. Unlicensed → Test withheld. Do not transfer to exterior RANS.
- Possible use: Cite when a CFD-ML pitch quotes one QoI — demand the holdout column for the decision quantity.
- Maturity: paper + unlicensed early repo
- Priority: High

## When a neural surrogate cannot accelerate a solver

- Link: https://arxiv.org/abs/2608.23075
- Type: Paper / closed-loop surrogate negative result (astro-ph.IM + astro-ph.HE + cs.LG + physics.comp-ph)
- Keywords: surrogate, Amdahl, closed-loop, UQ gating, radiation hydrodynamics
- One-line summary: Shows that a 5.8× cheaper inner-block surrogate cannot accelerate a stiff multiphysics loop once runtime share, offline-rank confounding, and a correct OOD gate are measured together.
- Why it matters:
  - Per-call speedup is not loop acceleration; only the share of wall clock sets Amdahl's cap.
  - API 2026-08-24; Thümmler/Kuroda. Target block **16.9%** of critical-rank wall clock → **~1.2×** cap. Fourteen-network Spearman **+0.73** collapses to **−0.04** under control. States **73×** off manifold; gate defers **96.8–99.7%**; gated loop **0.94–0.96×**. Density bias **−19.9%** / 6000 steps. No public code.
- Caveat: Neutrino GR hydro ≠ exterior RANS. Economics of gating still transfers. Test withheld.
- Possible use: Cite when a surrogate pitch quotes per-call speedup or holdout RMSE as deploy acceleration.
- Maturity: paper-only
- Priority: High

## Inverted PINN model selection — lower residual, worse solution

- Link: https://arxiv.org/abs/2608.21683
- Type: Paper / PINN verification (physics.comp-ph + physics.app-ph)
- Keywords: PINN, residual, admissibility, model selection, structural identity
- One-line summary: Finds that a smaller aggregate PDE residual systematically ranks a worse solution when a defining structural identity is penalized instead of hard-wired.
- Why it matters:
  - Scalar residual is not an admissibility receipt.
  - API 2026-08-21; Rabiu Musah. 64 matched pairs invert **83%** (Wilson 72–90%). Six architectures invert **46/48**. Vorticity–stream residual margin **9.37%** with **>6-order** identity violation. Source deletion leaves **97%** of reported structure. Lexicographic gate: identity → boundary trace → solvability integral → residual. No public code.
- Caveat: Single author, no code. Bench PDE ≠ engineering geometry.
- Possible use: Cite in PINN/NO selection checklists before residual competition.
- Maturity: paper-only
- Priority: High

## JXRGCM — Jin–Xin relaxation continuation for conservation-law PINNs

- Link: https://arxiv.org/abs/2608.22493
- Type: Paper / hyperbolic conservation PINN (math.NA)
- Keywords: PINN, Jin-Xin, relaxation, continuation, shock, entropy solution
- One-line summary: Anneals the Jin–Xin relaxation parameter with warm starts so a PINN can follow a shock layer toward the entropy solution instead of fitting one fixed scale.
- Why it matters:
  - Fixed-ε relaxation PINNs cannot track the singular limit.
  - API 2026-08-23; Lorin/Tang/Yang/Zhu. Sub-characteristic ε-independent stability; scalar L2 **O(ε^{1/4})**. Burgers / SWE dam-break / Sod. No public code.
- Caveat: 1D/standard shock benches. No engineering geometry gate.
- Possible use: Cite when a shock PINN uses a fixed relaxation penalty.
- Maturity: paper-only
- Priority: High

## Spinning quadrotor — hover thrust from passive wings

- Link: https://arxiv.org/abs/2608.23163
- Code: https://github.com/pyromania99/spinning-quadrotor-hover
- Type: Paper + unlicensed UAV hardware/code (cs.RO)
- Keywords: quadrotor, hover, passive lift, yaw, Urban_Flighter
- One-line summary: Holds a sustained yaw in hover so passive lifting surfaces produce thrust, cutting required motor thrust 22% in preliminary hardware tests.
- Why it matters:
  - Downstream hover QoI plus hardware beat field RMSE as the flight-efficiency receipt.
  - API 2026-08-24; Parkala/Kandath. ICUAS 2026 DOI 10.1109/ICUAS69441.2026.11598692. GitHub ★0, license unset, pushed 2026-06-09.
- Caveat: ★0 unlicensed. Spinning quadrotor ≠ default Urban_Flighter kinematics. Do not transfer −22%.
- Possible use: Inspect after license clarification; treat as a QoI-ladder example, not a kinematics transfer.
- Maturity: paper + unlicensed early repo
- Priority: High

## Low-fidelity aerofoil opt for curvilinear / cyclorotor kinematics

- Link: https://arxiv.org/abs/2608.20951
- Code: https://github.com/BenIrwin95/Low-Fidelity-Cyclorotor-Aerofoil-Optimiser
- Type: Paper + Apache-2.0 MATLAB shape-opt (physics.flu-dyn)
- Keywords: aerofoil, cyclorotor, multi-fidelity, Figure of Merit, streamtube, dynamic stall
- One-line summary: Optimises cyclorotor camber with a single-streamtube model and separate leading-/trailing-edge objectives, capturing most of the high-fidelity Figure-of-Merit gain at a fraction of the cost.
- Why it matters:
  - Downstream hover QoI plus a fidelity ladder beat field RMSE as the shape-search receipt.
  - API 2026-08-21; Irwin/Toal/Krishna. Four-blade LF opt takes **77%** of HF FM gain (HTML: 0.39 / 0.59 / 0.65). Pitch-kinematics opt also helps but cuts thrust.
  - GitHub ★0 Apache-2.0 pushed 2026-07-29.
- Caveat: ★0. Hovering cyclorotor ≠ quad-rotor kinematics. 2D URANS HF.
- Possible use: Cite as a fidelity-ladder example; do not transfer the 77% number across kinematics families.
- Maturity: paper + early Apache repo
- Priority: High

## Point-cloud quality metrics that actually predict meshfree error

- Link: https://arxiv.org/abs/2608.20872
- Type: Paper / meshfree verification (math.NA + cs.CE)
- Keywords: meshfree, point cloud, GFDM, quality metrics, verification
- One-line summary: Tests which point-cloud quality metrics actually correlate with GFDM collocation error across elliptic and hyperbolic, 2D and 3D cases, and shows that several popular metrics do not.
- Why it matters:
  - “Point clouds are easier than meshes” is not a verification statement until quality predicts error.
  - API 2026-08-21; Abdolahzadeh/Davydov/Michel/Suchde. Six reliable indicators (Issue Board: RE, GFL2, GFL1, DJM, FD, IMPF). No public code.
- Caveat: Tied to GFDM collocation. Authors caveat transfer to other meshfree schemes.
- Possible use: Cite when a meshfree pitch skips a discretization-quality gate.
- Maturity: paper-only
- Priority: High

## Urban flood GO-OED — place sensors for the decision, not coverage

- Link: https://arxiv.org/abs/2608.21182
- Type: Paper / Bayesian OED + NN flood surrogate (stat.AP + physics.geo-ph)
- Keywords: urban flood, GO-OED, PO-OED, sensor placement, QoI, tRIBS-Urban
- One-line summary: Shows that single-sensor placement on a Detroit 2014 flood surrogate flips with the learning target: point depth stays local, regional mean/max depth can go nonlocal.
- Why it matters:
  - Coverage and expected inundation are not the decision package.
  - API 2026-08-21; Cheng/Tran/Dong et al. 2,576 candidate sites. Parameter EIG does not transfer evenly into predictive-uncertainty cuts. No public code.
- Caveat: Single sensor. Michigan geometry ≠ Korean cities.
- Possible use: Cite when an urban sensor map is coverage-first — ask which QoI the EIG actually maximises.
- Maturity: paper-only
- Priority: High

## Implicit-adjoint FV CHT topology optimization (JAX)

- Link: https://arxiv.org/abs/2608.19426
- Code: https://github.com/smyng91/topology_optimization
- Type: Paper + MIT 2D FV / adjoint TO (math.NA)
- Keywords: adjoint, finite volume, conjugate heat transfer, topology optimization, JAX, Brinkman
- One-line summary: Builds a self-contained 2D staggered-MAC finite-volume CHT topology optimizer whose discrete advection keeps uniform temperature as an exact nullspace and whose sensitivities come from an implicit-function adjoint, not unrolled iteration.
- Why it matters:
  - Density-based thermofluid TO is only reproducible if the discrete energy operator and the adjoint match the residual that is actually solved.
  - API 2026-08-19; Sam Yang. Stokes–Brinkman or Darcy + energy at fixed solid volume. MMS + directional Taylor remainder. Four benches: volume-to-point tree / Darcy convection / Stokes–Brinkman conjugate cooling / Dirichlet sandwich.
  - GitHub `smyng91/topology_optimization` ★0, **MIT**, pushed 2026-08-19. Distinct from the same author's 08-22 `smyng91/hvac_designer`.
- Caveat: 2D staggered MAC. Not 3D / turbulence / compressible. ★0 newborn.
- Possible use: Smoke-test the uniform-T nullspace and Taylor remainder before treating a pretty cooling tree as a TO receipt.
- Maturity: paper + early MIT repo
- Priority: High

## Implicit sweep BGK on unstructured grids (ORNL)

- Link: https://arxiv.org/abs/2608.19150
- Type: Paper / unstructured DG kinetic solver (cs.CE)
- Keywords: BGK, unstructured, implicit sweep, DG, Kokkos, Sod, Frontier
- One-line summary: Solves multidimensional BGK with a nodal DG implicit sweep on unstructured grids so boundary-layer CFL does not set the time step, and checks the continuum limit on 2D/3D unstructured Sod.
- Why it matters:
  - Kinetic demos that stay Cartesian hide the geometry that actually forces implicit sweeps.
  - API 2026-08-19; Evans/Glasby/Hauck et al. Third-order B-stable DIRK. H100 **>20×** vs 64-core EPYC 9654. Frontier run: 2.77 trillion phase-space DoF / 1536 nodes / 6144 MI250X.
- Caveat: No dedicated public solver URL. Kinetic ≠ RANS product. `tahandy/ToroExact` is a Sod reference, not this code.
- Possible use: Cite when a kinetic paper only shows Cartesian shocks — ask for unstructured continuum-limit Sod.
- Maturity: paper-only
- Priority: High

## IGR adjoint — shock sensitivities without freezing limiters

- Link: https://arxiv.org/abs/2608.09759
- Type: Paper / compressible Euler adjoint (math.NA + math.OC)
- Keywords: IGR, adjoint, shock capturing, limiter freeze, Euler, sensitivities
- One-line summary: Derives forward and adjoint sensitivities for information-geometric regularization of compressible Euler so shocks become smooth inviscid profiles and grid-refined sensitivities match FD/AD without freezing limiters.
- Why it matters:
  - Frozen shock sensors / limiters are a common way to make adjoints look stable while reporting the wrong shape gradient.
  - API 2026-08-10; Schäfer. Periodic-BC IGR system; refinement → FD/AD match. HTML conversion empty (0 B).
- Caveat: Periodic BC only in the abstract. No public code. Engineering walls / complex geometry not shown.
- Possible use: Cite when a shock-shape adjoint “works” after freezing sensors — ask for the unfrozen refinement plot.
- Maturity: paper-only
- Priority: High

Selected broad survey papers and discovery maps for CFD-AI, Scientific Machine Learning, and machine learning for fluid mechanics. Method-specific papers should live in their topic files instead of here.

## Complementary PINNs — SIREN+causal on DFG cylinder wake

- Link: https://arxiv.org/abs/2608.19632
- Code: https://github.com/deveshshah1/Navier_Stokes_Exploration_with_PINNs
- Type: Paper + MIT PINN ablation (cs.LG + physics.flu-dyn)
- Keywords: PINN, vortex shedding, SIREN, causal weighting, DFG, Schäfer–Turek, OpenFOAM
- One-line summary: Shows PINN training tricks on the unsteady cylinder wake compose as complementary pairs, not as a longer method list: SIREN plus causal weighting recovers shedding, and stacking more techniques can collapse the field.
- Why it matters:
  - Isolated Fourier features, causal weights, hard BCs, SIREN, or extra data leave Re=100 shedding essentially at the untreated baseline.
  - HTML Table 2: SIREN+causal **Ux/Uy/p Rel.L2 7.8% / 17.1% / 16.7%**, St **0.300**, wake correlation **0.988**. Adding self-adaptive → **21.8 / 75.7 / 37.9**. Fourier+SIREN+causal → **58.1 / 99.8 / 98.1**.
  - Abstract headline 4.1% average Rel.L2 vs OpenFOAM is the unlocked regime, not the default Table-2 pairing. Re=20 steady Rel.L2 ≤3%; untreated Re=100 is 68 / 86 / 118%.
- Caveat: 2D laminar icoFoam DFG. Do not copy the pairing to 3D/high-Re. Repo ★0 MIT, pushed 2026-08-20.
- Possible use: Cite when a PINN write-up lists many tricks — require the pair table and the stack-collapse column.
- Maturity: paper + early MIT repo
- Priority: High

## Intrusive vs non-intrusive ROM for Carreau GNF

- Link: https://arxiv.org/abs/2608.18259
- Type: Paper / non-Newtonian ROM comparison (physics.flu-dyn)
- Keywords: ROM, Carreau, DEIM, RBF, intrusive, lid-driven cavity, settling sphere
- One-line summary: Compares ROM-FULL, ROM-DEIM, and ROM-RBF on the same POD snapshots for Carreau generalized Newtonian cavity and settling-sphere flows.
- Why it matters:
  - Same offline basis, three online contracts: full nonlinear reassembly, hyper-reduced DEIM, non-intrusive RBF interpolation.
  - Abstract: FULL is most accurate but pays full-order reassembly; RBF is fastest and breaks outside the training rheology; DEIM is the efficiency–accuracy compromise even when data are sparse.
- Caveat: No public code. 2D benches. Not a turbulence / external-aero transfer.
- Possible use: Cite when a “one surrogate” pitch hides solver-access vs millisecond interpolation vs rheology OOD.
- Maturity: paper-only
- Priority: High

## PINN inverse granular pipe flow from sparse sensors

- Link: https://arxiv.org/abs/2608.18641
- Type: Paper / inverse PINN (physics.flu-dyn)
- Keywords: PINN, granular flow, sparse sensing, inverse, KTGF, pipe flow
- One-line summary: Reconstructs steady granular pipe fields from sparse observations plus continuum constitutive residuals when inlet/outlet/wall BCs are unknown.
- Why it matters:
  - Inverse CFD with missing BCs is the actual industrial sensor setting, not a forward residual lottery.
  - HTML Fig.6: full-field relative error axial velocity **1.1×10⁻²**, solids fraction 1.6×10⁻², granular temperature 3.7×10⁻². Data-volume collapse: axial velocity **1.1×10⁻² → 1.4×10⁻¹**. Random supervision ~7.5×10⁻³ on axial velocity.
- Caveat: CFD/KTGF labels, not DEM or lab probes. Steady pipe. No public code.
- Possible use: Cite when a sparse-sensor PINN reports one Rel.L2 without a data-budget collapse curve.
- Maturity: paper-only
- Priority: High

## Data-driven hypersonic NEQ ROM with catalytic surfaces

- Link: https://arxiv.org/abs/2608.14445
- Type: Paper / thermochemistry reduced-order model
- Keywords: hypersonic, chemical non-equilibrium, catalytic wall, heat flux, ROM, wall QoI
- One-line summary: Extends a Scherding-class data-driven ROM to hypersonic reactive flows with localized catalytic-surface discontinuities that create sharp wall-chemistry and heat-transfer jumps.
- Why it matters:
  - Field-RMSE surrogates routinely miss catalytic-patch discontinuities that dominate wall heat flux and species fluxes.
  - Issue Board HTML reports ~**50%** overall simulation-cost cut on a catalytic BL setting (\(Re_x\in[1.4\times10^5,10^6]\)).
  - Makes **wall QoI + cost** the acceptance surface, not volumetric cosmetics.
- Caveat: No public code harvested. Depends on hypersonic thermochemistry libraries (Mutation++ lineage) — not urban low-speed air. Transfer the evaluation pattern, not the library stack.
- Possible use: Cite when defining wall-heat-flux / species-jump gates for process or reentry-adjacent surrogates.
- Maturity: paper-only
- Priority: High

## Exact BC on implicit geometries for continuum PINNs

- Link: https://arxiv.org/abs/2606.07579
- Type: Paper / hard vs soft PINN boundary enforcement
- Keywords: PINN, implicit geometry, hard BC, traction, SDF, elastodynamics
- One-line summary: Interpolates boundary data over implicit geometries and compares soft vs hard traction enforcement on first- and second-order plane-strain PINNs.
- Why it matters:
  - Complements BTF-PINN (interior-only Dirichlet): here the geometry is implicit and the contract is hard/soft traction.
  - All-soft tends to be slower/more accurate; all-hard faster/less accurate — BC choice is a gate, not a residual lottery.
  - First-order plane-strain reports higher relative accuracy; Issue Board Table 2 relative \(L^2\) ~\(1.868\times10^{-3}\) class.
- Caveat: Manufactured elastodynamic plane-strain. Fluid BC / industrial CAD transfer unproven. Code not confirmed.
- Possible use: Cite next to BTF-PINN when requiring an essential-BC contract on implicit/CAD-like boundaries.
- Maturity: paper-only
- Priority: High

## Conservative discrete FV structure vs learned rollout (1D DDP)

- Link: https://arxiv.org/abs/2606.01366
- Code: https://github.com/Airscker/DDP-benchmark
- Type: Paper + early structure-preserving benchmark
- Keywords: conservative finite volume, autoregressive rollout, drift-diffusion-Poisson, positivity, 1-step vs long horizon
- One-line summary: Shows that a classical conservative finite-volume core, not a learned next-state head, is what keeps long autoregressive rollouts stable on a 1D drift–diffusion–Poisson transport bench.
- Why it matters:
  - Headline rollout MSE **\(7.35\times10^{-9}\)** vs unconstrained **42.3**; Poisson recompute / charge projection / 4-step rollout training all stay \(O(10^1)\).
  - Wins rollout MSE on **60/64** configs but only **19/64** one-step MSE — 1-step leaderboards invert the engineering ranking.
  - README matches the paper; GitHub API description is stale/unrelated and should be ignored.
- Caveat: 1D plasma-transport prototype (Dirichlet potential, zero-flux walls; no Bohm/sheath). ★0 and license unset at 2026-08-18 → Cite/Test, not product Save.
- Possible use: Cite beside HERO / Diagnostics-for-Physics when refusing 1-step Rel \(L^2\) as DONE for conservation problems.
- Maturity: paper + immature public repo
- Priority: High

## Julia for CFD — ecosystem, performance, and composability survey

- Link: https://arxiv.org/abs/2608.12801
- Type: Paper / survey (CFD software + differentiable workflows)
- Keywords: Julia, CFD ecosystem, composability, automatic differentiation, accelerators, design/inference loops
- One-line summary: Critically maps Julia CFD projects and evidence for performance/composability when simulation must sit inside design, inference, optimization, and learning loops.
- Why it matters:
  - Engineering-AI value often comes from **software composition** (physics + numerics + AD + hardware), not only a new backbone.
  - Documents project families plus published scale/accelerator evidence and the real limits of differentiation/composition claims.
- Caveat: Survey — verify maturity/license of any cited project before adoption. Not a claim that Julia replaces production OpenFOAM/FLUENT stacks.
- Possible use: Use as a scouting map when comparing Julia vs JAX/Python differentiable CFD paths for agent-callable loops.
- Maturity: paper survey
- Priority: High

## BTF-PINN — Dirichlet BC without boundary training

- Link: https://arxiv.org/abs/2608.12823
- Type: Paper / PINN essential-boundary contract
- Keywords: PINN, Dirichlet BC, boundary-training-free, interior-only loss, flux-jump tests
- One-line summary: Solves homogeneous Dirichlet problems with an interior-only BTF-PINN strategy that avoids boundary collocation, penalty weights, and boundary-fitted parametric tricks.
- Why it matters:
  - Practical PINNs often fail as **BC lottery** (weight/collocation tuning) rather than as architecture races.
  - Offers a structural alternative for essential BC satisfaction; Issue Board HTML shows multi-case relative \(L_2\) tables including heat/flux-jump style tests.
- Caveat: Homogeneous Dirichlet core setting; inhomogeneous/complex CAD boundaries need extra work. Code not confirmed at curation.
- Possible use: Cite when reviewing PINN BC claims; require essential-BC contracts without boundary-weight green lights.
- Maturity: paper-only
- Priority: High

## HydroNet — data-guided FVM-PINN for 2D shallow water equations

- Link: https://arxiv.org/abs/2605.11001
- Code: https://github.com/psu-efd/HydroNet
- Type: Paper + open MIT tooling
- Keywords: PINN, finite volume, Roe Riemann solver, shallow water equations, unstructured mesh, conservation, data-guided residual
- One-line summary: Replaces strong-form PINN residuals for 2D SWE with a differentiable well-balanced Roe FVM loss on unstructured meshes and shows physics-only training can collapse without data guidance.
- Why it matters:
  - Strong-form residual PINNs struggle with local conservation, discontinuities, and boundary-conforming unstructured meshes used in real hydrodynamics.
  - Core engineering signal: physics-only FVM-PINN can satisfy a residual-looking minimum while collapsing to a trivial low-momentum state; data-guided λ-mixed FV residuals recover usable flow (Issue Board: L2(|u|) **0.166→~0.032** class).
  - GitHub `psu-efd/HydroNet` ★9, **MIT**, forks 3, Zenodo DOI 10.5281/zenodo.20099995.
- Caveat: 2D SWE focus; metropolitan flood digital-twin scale is a separate product problem. Re-check exact ablation tables in PDF before hard numeric citation.
- Possible use: Steal FV residual + data-guidance recipe for Urban/SWE PINN trust reviews; reject residual-only green lights on conservation problems.
- Maturity: paper + open code
- Priority: High


## Efficient Weak-Entropy PINN for hyperbolic conservation laws

- Link: https://arxiv.org/abs/2608.10389
- Type: Paper / PINN shock-capturing with entropy gates
- Keywords: PINN, weak entropy, Rankine-Hugoniot, hyperbolic conservation laws, shock metrics, S-Rate, S-Acc
- One-line summary: Puts entropy weak-form and Rankine-Hugoniot structure into the PINN loss and elevates shock-location metrics (S-Rate / S-Acc) beside field rel L2 for discontinuous solutions.
- Why it matters:
  - Residual-only PINNs can look smooth-L2 competitive while missing entropy-admissible shocks.
  - Makes metric separation itself the engineering signal: methods that win on smooth IC L2 can fail on nonlinear shocks.
  - Continues the "one-step RMSE is not DONE" line next to phase-drift ROM and conservation NO rollouts.
- Caveat: Exact table cells need PDF confirmation before hard numeric claims; no public code harvested at curation.
- Possible use: Require S-Rate/shock-position gates when reviewing Burgers/SWE/Euler PINN claims for Urban flood or conservation stacks.
- Maturity: paper-only
- Priority: High

## Data-driven micromixing surrogate (non-Newtonian) + multi-objective design

- Link: https://arxiv.org/abs/2608.08547
- Code: https://github.com/BimalenduMahapatra/surrogate-micromixer-optimization
- Type: Paper + early open process-CFD surrogate stack
- Keywords: micromixing, non-Newtonian, Carreau-Yasuda, GPR surrogate, NSGA-II, process CFD, multi-objective design
- One-line summary: Builds a mesh-converged FV CFD dataset for 2D sinusoidal micromixers, fits UQ-capable GPR surrogates for mixing index and pressure drop, then runs NSGA-II multi-objective geometry design.
- Why it matters:
  - Process-scale pattern: trust the CFD data gate first (Mesh3->4 MI delta<0.1%, dp delta<0.05%), then surrogate, then optimizer -- not field aesthetics alone.
  - Reports GPR **R2(MI)=0.9955** and **R2(dp)=0.9948**; authors prefer GPR over slightly stronger XGB because uncertainty is first-class.
  - Live repo with datasets + ML + NSGA-II code (stars 0, pushed 2026-07-08) makes the loop inspectable.
- Caveat: 2D creeping microchannel scope only. **No SPDX license** via GitHub API at curation -> Watch/Test, not product-Save.
- Possible use: Steal the CFD->GPR-UQ->NSGA-II QoI loop shape for process/Urban decision surrogates after license clarification.
- Maturity: paper + immature public repo (license blocked)
- Priority: High

## Adjoint shape optimization of oscillatory rarefied gas flows

- Link: https://arxiv.org/abs/2608.06910
- Type: Paper / multiscale AP adjoint + MEMS drag shape optimization
- Keywords: adjoint, asymptotic-preserving, GSIS, rarefied gas, MEMS, shape optimization, drag reduction, multiscale kinetic
- One-line summary: Builds a fast-converging asymptotic-preserving adjoint GSIS with macroscopic synthetic equations so gradient-based shape optimization can cut oscillatory rarefied/MEMS gas damping across Knudsen–Strouhal regimes.
- Why it matters:
  - Multiscale design needs adjoints that stay consistent near continuum while retaining kinetic accuracy when rarefied — not black-box reverse mode on a single regime model.
  - Paper HTML optimization tables report drag reductions of **35.5% / 44.3% / 52.6%** vs rounded initial geometry under stated constrained cases (oscillating cylinder / comb / accelerometer-family demos).
  - Fourier analysis claims spectral radius <0.5 for the synthetic acceleration (error halved per iteration in the infinite-domain idealization).
- Caveat: Rarefied MEMS scope; not RANS airfoil product CFD. No first-party public optimizer package found at curation — treat % as paper-reported.
- Possible use: Cite next to AP-adjoint UGKS when writing multiscale UQ/sensitivity/shape-opt method notes with explicit QoI (drag/damping).
- Maturity: paper-only
- Priority: High

## Asymptotic-preserving adjoint UGKS for sensitivity analysis

- Link: https://arxiv.org/abs/2608.03236
- Type: Paper / multiscale adjoint method for continuum–rarefied gas dynamics
- Keywords: UGKS, adjoint, asymptotic-preserving, sensitivity analysis, UQ, multiscale kinetic, dual consistency
- One-line summary: Builds a dual-consistent discrete adjoint for the unified gas-kinetic scheme with an asymptotic-preserving macroscopic projection and microscopic lifting so gradients stay consistent across continuum and rarefied regimes.
- Why it matters:
  - Multiscale UQ/sensitivity fails when adjoints ignore stiff cross-scale coupling or inherit under-relaxation/time-step pollution from the forward solver.
  - Provides a kinetic counterpart to engineering CFD adjoint hygiene: dual consistency + AP structure, not black-box reverse-mode only.
  - Cavity Re 100/1000 and thermal-disturbance benches support method claims (method paper, not a single % leaderboard).
- Caveat: Rarefied/kinetic focus; no public code linked at curation; RANS/airfoil product CFD transfer is separate work.
- Possible use: Cite when designing multiscale UQ or sensitivity loops where surrogate/adjoint gradients must respect regime coupling.
- Maturity: paper-only
- Priority: Medium

## Newton–Krylov correction of steady CFD surrogates (OOD airfoils)

- Link: https://arxiv.org/abs/2608.04400
- Type: Paper / solver-coupled surrogate deploy pattern
- Keywords: CFD surrogate, Newton-Krylov, OOD geometry, residual convergence, airfoil optimization, warm-start
- One-line summary: Uses neural surrogate predictions as high-quality initial guesses for Newton–Krylov iterations so steady CFD keeps classical residual convergence under OOD geometries from real optimization trajectories.
- Why it matters:
  - Practical CFD-ML deploy failure mode is OOD geometry, not offline holdout RMSE.
  - Abstract reports median residual L₂ ratio improved by over seven orders of magnitude on OOD airfoils, with lower field/aero error, plus 15.5× generation-level speedup in supercritical airfoil optimization vs CFD.
  - Reusable harness pattern: fast global prediction + terminal classical solve, not surrogate-alone green lights.
- Caveat: No public code harvested at curation; steady CFD scope; 3D flying-wing extension is exploratory. Confirm solver family/details from the PDF before product claims.
- Possible use: Cite when defining Urban_Flighter / CFD surrogate acceptance as residual + force error under geometry shift, with optional warm-start acceleration.
- Maturity: paper-only
- Priority: High

## AC-PINN — artificial compressibility PINN for unsteady Navier–Stokes

- Link: https://arxiv.org/abs/2608.04191
- Type: Paper / PINN formulation with honest unsteady failure modes
- Keywords: PINN, artificial compressibility, incompressible Navier-Stokes, cylinder wake, shedding, data assimilation
- One-line summary: Relaxes the divergence-free constraint with artificial compressibility so PINN residuals become ordinary, then shows plain forward AC-PINN collapses to a steady symmetric cylinder branch unless sparse velocity data are assimilated.
- Why it matters:
  - Counterweight to residual-only “PINN solved NS” claims: Re=100 cylinder without data does not recover von Kármán shedding.
  - Quantifies ε–divergence/velocity error trade-offs on Taylor–Green; with sparse sensors, wake and frequency recover relative to a FEM reference.
  - Useful validation honesty template for any unsteady fluid PINN review.
- Caveat: 2D classical benches only; AC parameter is problem-dependent; recovery quality is bounded by the reference solver fidelity.
- Possible use: Require shedding/limit-cycle diagnostics (not only residual norms) before accepting unsteady NS-PINN results into VA literature notes.
- Maturity: paper-only
- Priority: High

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
