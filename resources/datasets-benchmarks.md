# Datasets & Benchmarks

Flow datasets, SciML benchmarks, reproducibility references, metrics, and evaluation protocols.

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
