# CFD-AI Papers & Surveys

Selected papers, surveys, and paper maps for CFD-AI, Scientific Machine Learning, and machine learning for fluid mechanics.

## Recent Advances on Machine Learning for Computational Fluid Dynamics: A Survey

- Link: https://arxiv.org/abs/2408.12171
- Type: Paper / survey
- Keywords: CFD-AI, survey, data-driven surrogate, physics-informed surrogate, ML-assisted CFD
- One-line summary: A survey that classifies recent ML-for-CFD work into data-driven surrogates, physics-informed surrogates, and ML-assisted numerical solutions.
- Why it matters: Useful as a high-level taxonomy for deciding where a new CFD-AI project sits: full surrogate, physics-informed model, or solver-assist component.
- Possible use: Use the taxonomy to organize literature review sections and to avoid mixing fundamentally different CFD-AI problem settings.
- Maturity: paper-only
- Priority: High

## Fourier Neural Operator for Parametric Partial Differential Equations

- Link: https://arxiv.org/abs/2010.08895
- Code: https://github.com/neuraloperator/neuraloperator
- Type: Paper / neural operator
- Keywords: Fourier neural operator, operator learning, PDE surrogate, spectral methods
- One-line summary: Introduces Fourier Neural Operators for learning mappings between function spaces in parametric PDE problems.
- Why it matters: FNO is one of the core baselines for neural-operator CFD/SciML work, especially for grid-based PDE surrogate modeling and spectral field learning.
- Possible use: Use as a baseline method when comparing neural operators for flow prediction, super-resolution, or parameter-to-field surrogate modeling.
- Maturity: maintained library
- Priority: High

## Learning Mesh-Based Simulation with Graph Networks

- Link: https://arxiv.org/abs/2010.03409
- Code: https://github.com/google-deepmind/deepmind-research/tree/master/meshgraphnets
- Type: Paper / graph neural simulation
- Keywords: MeshGraphNets, graph neural networks, unstructured mesh, learned simulation
- One-line summary: Learns simulation dynamics directly on mesh-based physical systems using graph networks.
- Why it matters: Many engineering CFD/CAE problems live on irregular meshes, so MeshGraphNets is a key reference for geometry-aware and mesh-aware learned simulation.
- Possible use: Use as a conceptual baseline for CAD/mesh-to-field surrogate modeling and for thinking about learned simulators on unstructured CFD domains.
- Maturity: prototype
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

## DeepONet: Learning nonlinear operators via the universal approximation theorem of operators

- Link: https://www.nature.com/articles/s42256-021-00302-5
- Code: https://github.com/lululxvi/deeponet
- Type: Paper / neural operator
- Keywords: DeepONet, operator learning, Scientific Machine Learning, PDE surrogate
- One-line summary: Introduces DeepONet as a neural-network architecture for learning nonlinear operators between function spaces.
- Why it matters: DeepONet is a foundational operator-learning architecture and an important comparison point against FNO-style methods.
- Possible use: Use in literature reviews to explain the operator-learning family and compare branch/trunk operator models against spectral neural operators.
- Maturity: prototype
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

## MetaOpenFOAM: an LLM-based multi-agent framework for CFD

- Link: https://arxiv.org/abs/2407.21320
- Code: https://github.com/Terry-cyx/MetaOpenFOAM
- Type: Paper / engineering AI agent workflow
- Keywords: OpenFOAM, LLM agents, multi-agent framework, CFD automation
- One-line summary: Proposes a multi-agent LLM framework for automating parts of OpenFOAM-based CFD workflows.
- Why it matters: Directly relevant to agentic CFD workflow automation, especially case setup, execution, debugging, and post-processing around existing solvers.
- Possible use: Use as a reference when designing CAD→CFD→visualization orchestration agents or comparing MCP-based OpenFOAM automation approaches.
- Maturity: prototype
- Priority: High

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
