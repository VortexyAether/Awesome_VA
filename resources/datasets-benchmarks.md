# Datasets & Benchmarks

Flow datasets, SciML benchmarks, reproducibility references, metrics, and evaluation protocols.

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
