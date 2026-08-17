# Datasets & Benchmarks

Flow datasets, SciML benchmarks, reproducibility references, metrics, and evaluation protocols.

## U3DWind — urban low-altitude wind dataset + UAM benchmark

- Link: https://arxiv.org/abs/2607.04495
- Code/data: https://github.com/hweifluids/LatticeUrbanWind
- Type: Urban CFD / UAM wind dataset + NWP-LBM toolkit
- Keywords: urban air mobility, low-altitude wind, building turbulence, gust hazards, lattice Boltzmann, vertiport, route feasibility
- One-line summary: Releases a low-altitude urban wind field dataset/benchmark aimed at UAM stability, route, and vertiport decisions, with a live LatticeUrbanWind NWP-LBM coupling toolkit for high-resolution city-scale generation.
- Why it matters:
  - Moves acceptance from pixel/field MAE toward UAM decision QoI under building-induced turbulence and gusts.
  - Issue Board HTML harvest: relative \(L_2\) **0.094** class with other \(L_2\) **0.13–0.18** and ensemble Brier-style probabilistic scores; claimed ~**460×** acceleration vs a reference workflow is setting-dependent.
  - Live repo ★**22**, pushed 2026-08-02 — inspectable substrate for Urban_Flighter-adjacent benches.
- Caveat: GitHub license **NOASSERTION** at 2026-08-17 API check → clarify SPDX before product use. Lattice lineage vs industrial RANS/LES acceptance is separate. Do not treat acceleration claims as universal.
- Possible use: Smoke-test README/sample generation; map hazard/route metrics into Urban_Flighter acceptance notes after license gate.
- Maturity: paper + public toolkit (license gate)
- Priority: High

## Free-stream transition iLES database (ERCOFTAC T3-class)

- Link: https://arxiv.org/abs/2606.20139
- Dataset: https://doi.org/10.5281/zenodo.17166216
- Type: Transition / turbulence high-fidelity database
- Keywords: bypass transition, iLES, ERCOFTAC T3, free-stream turbulence, RANS validation, full-field 3D time-resolved
- One-line summary: Provides wall-resolved iLES-style full-field 3D time-resolved data filling gaps left by classic ERCOFTAC T3 experiments for modern transition-model and ML development.
- Why it matters:
  - Transition ML/RANS work needs measurement-channel fidelity and inlet turbulence length-scale gates, not only integral skin-friction curves.
  - Zenodo primary surface makes the corpus citable and downloadable.
- Caveat: Flat-plate bypass focus; complex industrial geometry transition transfer is separate. Age ~2 months at curation.
- Possible use: Cite when building transition acceptance channels next to T3A/T3C5-style tables; inspect Zenodo packing before local Save.
- Maturity: paper + Zenodo dataset
- Priority: Medium-High

## TIDE — 3D incompressible DNS ensemble benchmark

- Link: https://arxiv.org/abs/2608.04222
- Code: https://github.com/Dyloong1/TIDE-dataset-benchmark
- Dataset: https://huggingface.co/datasets/ydai17/TIDE
- DOI: https://doi.org/10.5281/zenodo.21589489
- Type: 3D turbulence DNS corpus + SciML benchmark harness
- Keywords: 3D turbulence, DNS ensemble, neural operator benchmark, physical fidelity, forced/decay transfer, residual checks
- One-line summary: Releases a 256³ fp64 incompressible DNS corpus with independent ensembles across 15 configurations and a five-task benchmark that scores physical fidelity beside pointwise error.
- Why it matters:
  - Breaks the 2D / single-realization habit that lets models fit one trajectory’s statistics without learning dynamics.
  - Main forecasting configs: learned baselines barely beat persistence and still make about twice the error of a spectral solver given the true equations; low RMSE can still warp small scales.
  - Forced→decay split exposes missing conditioning on external drive — a reusable acceptance idea for CFD surrogates under regime change.
- Caveat: Periodic-box spectral DNS, not wall-bounded product meshes; ~2.6 TB corpus. Code MIT / data CC-BY-4.0; early stars at curation.
- Possible use: Adopt TIDE-style ensemble + residual + fidelity metrics when designing Urban_Flighter / CFD-ML acceptance gates beyond field RMSE.
- Maturity: paper + public code/dataset (early)
- Priority: High

## Bound-preserving FV WENO multiphase (classical trust substrate)

- Link: https://arxiv.org/abs/2608.00746
- Type: Paper / classical multiphase finite-volume scheme
- Keywords: finite volume, WENO, multiphase, Phase-Field, bound preservation, conservation
- One-line summary: Builds a consistent, conservation/equilibrium/bound-preserving finite-volume WENO scheme for compressible two-/N-phase flows with a Phase-Field mechanism.
- Why it matters:
  - ML multiphase benches still need a classical trust floor for conservation and interface bounds.
  - Useful counterweight to “neural replaces solver” claims next to Neptuna-class datasets.
- Caveat: Not an ML method; code release not harvested at curation.
- Possible use: Keep as numerics reference substrate when scoring multiphase surrogates on conservation/bound metrics.
- Maturity: paper-only
- Priority: Medium

## Neptuna — multiphase shock-driven flow ML benchmark

- Link: https://arxiv.org/abs/2607.22280
- Code: https://github.com/tumaer/Neptuna
- Type: Multiphase CFD-ML benchmark framework / dataset claim
- Keywords: multiphase flow, shock-driven flows, bubble collapse, droplet breakup, composite loss, CFD benchmark
- One-line summary: Introduces a large-scale shock-driven compressible multiphase benchmark claim (2.4 TB 2D/3D) and evaluates multiple surrogate families under composite losses that include interface/structure terms.
- Why it matters:
  - Multiphase shock problems break MSE-only leaderboards; interface and spectral/structure metrics are first-class trust signals.
  - Useful anchor for “no single model wins everywhere” evaluation culture in CFD-ML.
- Caveat: GitHub repo exists but had 0 stars and null license via API at curation; local schema/access/license verification still required before treating the 2.4 TB claim as a ready local benchmark.
- Possible use: Inspect README/license/sample layout, then decide whether to adopt composite multiphase metrics in VA benchmark checklists.
- Maturity: paper + early public repo (verify before use)
- Priority: Medium

## BubbleSH — deformable bubble-swarm DNS dataset

- Link: https://arxiv.org/abs/2607.07275
- Dataset: https://doi.org/10.5281/zenodo.21229301
- Type: Multiphase-flow dataset and generative dynamics benchmark
- Keywords: CFD dataset, bubbly flow, DNS, multiphase dynamics, spherical harmonics, trajectory prediction, shape prediction
- One-line summary: Provides transient 3D bubble-swarm direct numerical simulations with bubble trajectories, velocities, and spherical-harmonic shape evolution.
- Why it matters:
  - Multiphase CFD surrogates need benchmarks where interaction, morphology, and chaotic rollout distributions matter, not only dense-field RMSE.
  - The trajectory-plus-shape metric framing is useful for evaluating generative or probabilistic dynamics models under local perturbation sensitivity.
  - Zenodo lists a concrete 9.2 GB `Data.zip` and 4.4 kB README under CC-BY-4.0, making it a real dataset candidate rather than only a paper claim.
- Caveat: Bubble-swarm dynamics are specialized; schema, train/test splits, and baseline scripts need inspection before local use.
- Possible use: Inspect the README and sample metadata, then decide whether BubbleSH belongs in a generative multiphase surrogate benchmark suite.
- Maturity: paper + Zenodo dataset
- Priority: High

## GraphBU — MILP instance generation with graph-native block units

- Link: https://arxiv.org/abs/2607.06532
- Type: Structure-preserving synthetic benchmark generation for MILP instances
- Keywords: MILP, benchmark generation, graph structure, solver policy, feasibility, optimization
- One-line summary: Generates MILP instances from local subproblems plus explicit interfaces so solver-facing block/coupling structure is preserved better than template-only or summary-statistic generation.
- Why it matters: Engineering-AI benchmarks need synthetic families that preserve the structures downstream tools actually use. GraphBU is MILP-specific, but its `local unit + interface + compatibility check` pattern is a useful analogy for CFD/CAE benchmark generation around geometry, boundary conditions, coupling interfaces, and solver policy behavior.
- Caveat: Not a CFD or mesh benchmark; code/data availability and dataset-specific failure cases still need follow-up.
- Possible use: Cite when arguing that engineering surrogate benchmarks should preserve domain structure rather than only match broad statistics.
- Maturity: paper-only
- Priority: High

## Zero-To-CAD-1m

- Link: https://huggingface.co/datasets/ADSKAILab/Zero-To-CAD-1m
- Paper: https://arxiv.org/abs/2604.24479
- Type: CAD dataset / text-to-3D and image-to-3D benchmark resource
- Keywords: CAD, CadQuery, synthetic data, construction sequence, parametric CAD, 3D generation
- One-line summary: A large Autodesk AI Lab dataset of executable CadQuery CAD programs with operation traces, renders, STL, and STEP exports.
- Why it matters: CAD-to-CAE automation needs editable construction histories and reliable exports, not just mesh-only shapes; this dataset is a strong reference point for parametric CAD generation and evaluation.
- Possible use: Train or benchmark CAD agents/models that produce executable geometry for downstream meshing, design sweeps, and validation loops.
- Maturity: Hugging Face dataset / Apache-2.0
- Priority: High

## PDEBench: An Extensive Benchmark for Scientific Machine Learning

- Link: https://arxiv.org/abs/2210.07182
- Code: https://github.com/pdebench/PDEBench
- Type: Paper / benchmark
- Keywords: PDE benchmark, SciML, neural operators, reproducibility, surrogate modeling
- One-line summary: A benchmark suite for comparing Scientific Machine Learning methods across multiple PDE tasks.
- Why it matters: CFD-AI papers are hard to compare without shared datasets and metrics; PDEBench provides a structured benchmark reference for model evaluation.
- Possible use: Use to sanity-check new surrogate or neural-operator experiments before moving to custom CFD datasets.
- Maturity: maintained library
- Priority: High

## HiLiftAeroML

- Link: https://arxiv.org/abs/2605.19565
- Type: High-fidelity CFD dataset for aerodynamic surrogate modeling
- Keywords: CFD dataset, high-lift aircraft, aerodynamics, surrogate modeling, design sweep
- One-line summary: Open high-fidelity CFD dataset with 1,800 samples from 180 high-lift NASA CRM geometry variants across 10 angles of attack.
- Why it matters: Gives CFD-AI models a more engineering-native benchmark than clean toy PDEs or overly simplified airfoils, tying surrogate learning to geometry variation and high-lift aerodynamic design.
- Possible use: Use for neural operator/GNN/ROM surrogate comparisons, geometry-OOD evaluation, and active-learning experiments for aerodynamic design spaces.
- Maturity: paper / dataset announced
- Priority: High

## ShapeBench

- Link: https://arxiv.org/abs/2605.20763
- Type: Aerodynamic shape-optimization benchmark / diagnostic suite
- Keywords: aerodynamic shape optimization, CFD verification, surrogate modeling, benchmark, fidelity gap
- One-line summary: A scalable benchmark suite for aerodynamic shape optimization with validated fast surrogates and, where feasible, high-fidelity CFD pipelines for final verification.
- Why it matters: Moves CFD-AI evaluation from pure prediction error toward whether surrogate-guided optimization produces designs that survive expensive CFD rechecks.
- Possible use: Use as a template for VA-style CAD/CFD optimization audits: surrogate search, candidate selection, high-fidelity verification, and fidelity-gap reporting.
- Maturity: paper / benchmark announced
- Priority: High

## NED3 multimodal thermal-fluid datasets and software

- Link: https://arxiv.org/abs/2605.23037
- Type: Multimodal thermal-fluid dataset ecosystem / open-source software map
- Keywords: multiphase transport, thermal systems, electronics cooling, datasets, open-source software, digital twins
- One-line summary: A curated NED3 ecosystem of public datasets and software spanning boiling images, acoustic/thermal measurements, high-speed videos, IR thermography, CFD-generated fields, design files, and diagnostic tools.
- Why it matters: Thermal-fluid AI needs reusable raw-to-model pipelines, not just isolated CSV benchmarks; this paper connects datasets, metadata, decoders, surrogate tooling, and physically interpretable diagnostics.
- Possible use: Use the S+TD dimensionality framework to organize VA thermal/CFD datasets and identify which modalities need decoders, baseline models, and validation metrics.
- Maturity: paper / dataset and software ecosystem
- Priority: High

## Full-scale PWR flow-field CFD dataset for ML applications

- Link: https://arxiv.org/abs/2605.24763
- Type: Domain-specific high-fidelity CFD dataset / ML reconstruction benchmark
- Keywords: nuclear thermal-hydraulics, pressurized water reactor, CFD dataset, sparse reconstruction, ConvLSTM
- One-line summary: Builds full lower-plenum/core-inlet PWR CFD fields from public geometry and operating conditions, then evaluates partial field reconstruction and short-term autoregressive prediction.
- Why it matters: Shows how strongly domain physics, swirl/mixing, mesh resolution, and sensor placement shape ML surrogate performance; spatially aware ConvLSTM beats sequence-only and operator-learning baselines in this setting.
- Possible use: Use as a reference for sparse-sensor reconstruction benchmarks where CFD data are expensive and full experimental validation is limited.
- Maturity: paper / dataset framework
- Priority: Medium

## MUSE Text-to-CAD Benchmark

- Link: https://arxiv.org/abs/2605.28579
- Type: Text-to-CAD benchmark for manufacturability, functionality, and assemblability
- Keywords: CAD, text-to-CAD, manufacturability, functionality, assemblability, design automation
- One-line summary: A benchmark that evaluates Text-to-CAD generation beyond geometric similarity by checking whether generated CAD is manufacturable, functional, and assemblable.
- Why it matters: CAD automation for engineering cannot stop at visually plausible single parts; downstream CAE and manufacturing need valid assemblies, functional intent, and constraint-aware geometry.
- Possible use: Extend the evaluation idea with meshability, boundary-condition assignability, solver-run success, and KPI validity for CAD-to-CFD automation benchmarks.
- Maturity: paper / benchmark announced
- Priority: High
