# GPU OpenFOAM & HPC CFD

## OpenFOAM GPU acceleration guide

- Link: https://openfoam.tistory.com/entry/OpenFOAM-%ED%95%B4%EC%84%9D-%EC%86%8D%EB%8F%84-25%EB%B0%B0-%EC%98%AC%EB%A6%AC%EB%8A%94-%EB%B2%95-GPU-%EA%B0%80%EC%86%8D%ED%99%94-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C-2026
- Type: Korean OpenFOAM GPU acceleration overview
- Summary:
  - Compares GPU acceleration approaches such as RapidCFD, AmgX, PETSc, and native approaches.
  - Mentions large motorBike benchmark-style performance claims.
- Why it matters:
  - Useful for deciding whether conventional OpenFOAM workflows can be accelerated instead of fully rewriting solvers.
  - Relevant when comparing GPU OpenFOAM vs JAX/native differentiable CFD paths.
- Follow-up:
  - Verify benchmark conditions, solver compatibility, and reproducibility before relying on speedup claims.

## GALÆXI

- Link: https://arxiv.org/abs/2605.28627
- Type: Open-source architecture-agnostic high-order DGSEM framework for compressible CFD
- Why it matters:
  - Targets complex compressible turbulent flows on unstructured hexahedral grids with GPU acceleration.
  - Supports both NVIDIA CUDA and AMD HIP pathways, which matters as HPC systems become more heterogeneous.
  - Strong signal for surrogate workflows because reliable high-order data generation is often the bottleneck before ML begins.
- Possible use: Track as a high-fidelity solver/data-generation reference when comparing GPU CFD infrastructure against OpenFOAM, JAX solvers, and neural surrogates.
- Maturity: paper / open-source toolchain claim
- Priority: High

