# CFD-AI Papers & Surveys

Curated paper maps, survey papers, and review resources for CFD-AI, Scientific Machine Learning, and machine learning for fluid mechanics.

## Awesome-AI4CFD

- Link: https://github.com/WillDreamer/Awesome-AI4CFD
- Type: Paper collection / survey companion repository
- Keywords: CFD-AI, machine learning for CFD, surrogates, physics-informed learning, neural operators
- One-line summary: A structured paper list accompanying the survey “Recent Advances on Machine Learning for Computational Fluid Dynamics.”
- Why it matters: The repository organizes ML-for-CFD literature by benchmark datasets, data-driven surrogates, physics-informed surrogates, ML-assisted numerical solutions, applications, and frontier models.
- Possible use: Use as a literature-map starting point when surveying CFD-AI methods, selecting baselines, or building category-specific reading lists for surrogate modeling and ML-assisted solvers.
- Maturity: maintained library
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

## Awesome Machine Learning for Fluid Mechanics

- Link: https://github.com/ikespand/awesome-machine-learning-fluid-mechanics
- Type: Paper/code collection
- Keywords: fluid mechanics, machine learning, review papers, datasets, open-source codes
- One-line summary: A broad curated list of machine learning papers, code, libraries, datasets, labs, and resources for fluid mechanics.
- Why it matters: Complements CFD-specific lists by covering the wider fluid-mechanics ML landscape, including interpretability, reduced-order modeling, reinforcement learning, geometry optimization, datasets, and open-source CFD codes.
- Possible use: Use as a discovery index for older foundational papers, review papers, datasets, and fluid-mechanics ML toolchains that may not appear in newer CFD-AI survey lists.
- Maturity: maintained library
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

## Turbulence Modeling in the Age of Data

- Link: https://arxiv.org/abs/1804.00183
- Type: Paper / review
- Keywords: turbulence modeling, data-driven modeling, RANS, LES, closure models
- One-line summary: A review focused on how data-driven methods interact with turbulence modeling and closure problems.
- Why it matters: Turbulence closure is one of the most important and failure-prone targets for CFD-AI, so this is a key grounding reference before proposing learned turbulence models.
- Possible use: Use to frame turbulence-surrogate work, RANS/LES closure discussions, and the limitations of purely data-driven turbulence modeling.
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
