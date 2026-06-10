# Best Anchors

People, papers, and technical lineages that should stay close to the top of the radar.

This is not a citation-ranking page. It is a VA-oriented map of representative work that repeatedly informs CFD-AI, SciML, turbulence surrogates, reduced-order modeling, sparse modeling, and engineering automation.

Affiliation notes below follow VA's current working notes and should be checked before formal citation or public bios.

---

## 1. Sangseung Lee — Inha University

Focus for this repository: deep-learning flow-field prediction, CNN interpretation for wake flows, rough-wall drag prediction, and data-driven CFD representation learning.

### Representative papers

#### Data-driven prediction of unsteady flow fields over a circular cylinder using deep learning

- Link: https://arxiv.org/abs/1804.06076
- Type: Paper
- Keywords: cylinder wake, flow-field prediction, CNN, unsteady flow
- Why it matters: Early and directly relevant example of using deep learning for unsteady CFD field prediction, with a canonical wake-flow setup that remains useful for surrogate sanity checks.
- VA-use: Benchmark / cite / compare against newer neural-operator and generative-flow approaches.
- Priority: High

#### Prediction of laminar vortex shedding over a cylinder using deep learning

- Link: https://arxiv.org/abs/1712.07854
- Type: Paper
- Keywords: vortex shedding, laminar wake, deep learning, cylinder flow
- Why it matters: A compact reference for learning coherent wake dynamics before moving to harder turbulent or geometry-shifted cases.
- VA-use: Use as a simple baseline lineage for wake-surrogate discussions.
- Priority: Medium

#### Mechanisms of a Convolutional Neural Network for Learning Three-dimensional Unsteady Wake Flow

- Link: https://arxiv.org/abs/1909.06042
- Type: Paper
- Keywords: CNN interpretability, 3D wake flow, unsteady CFD, representation learning
- Why it matters: Looks inside what CNNs learn for 3D wake prediction rather than only reporting field error.
- VA-use: Cite when arguing that interpretability and learned physical structure matter for CFD-AI, not just accuracy.
- Priority: High

#### Deep learning approach in multi-scale prediction of turbulent mixing-layer

- Link: https://arxiv.org/abs/1809.07021
- Type: Paper
- Keywords: turbulent mixing layer, multi-scale prediction, deep learning, flow fields
- Why it matters: Moves from canonical laminar wake prediction toward turbulent multi-scale flow reconstruction/prediction.
- VA-use: Compare with modern spectral, diffusion, and neural-operator methods for multi-scale turbulence.
- Priority: Medium

#### Predicting drag on rough surfaces by transfer learning of empirical correlations

- Link: https://arxiv.org/abs/2106.05995
- Type: Paper
- Keywords: rough-wall turbulence, drag prediction, transfer learning, empirical correlations
- Why it matters: Strong engineering-AI example: using transfer learning to connect empirical drag correlations and rough-surface prediction.
- VA-use: Anchor for practical surrogate transfer, roughness features, and engineering drag prediction.
- Priority: High

---

## 2. Kai Fukami — Tohoku University

Focus for this repository: fluid-flow super-resolution, sparse-sensor reconstruction, reduced-order surrogates, nonlinear decomposition, and data-driven fluid mechanics workflows.

### Representative papers

#### Assessment of supervised machine learning methods for fluid flows

- Link: https://arxiv.org/abs/2001.09618
- Type: Paper / assessment
- Keywords: supervised learning, fluid flows, CNN, reconstruction, prediction
- Why it matters: A practical benchmark-style reference for what supervised ML can and cannot do across fluid-flow tasks.
- VA-use: Use as a baseline reading item before claiming a new architecture is useful for CFD.
- Priority: High

#### Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning

- Link: https://arxiv.org/abs/2101.00554
- Type: Paper
- Keywords: sparse sensors, field reconstruction, Voronoi tessellation, deep learning
- Why it matters: Directly targets the sensor-to-field reconstruction problem that appears in experimental fluids, thermal monitoring, and digital twins.
- VA-use: Anchor for sparse-observation reconstruction and sensor-placement discussions.
- Priority: High

#### Probabilistic neural networks for fluid flow surrogate modeling and data recovery

- Link: https://arxiv.org/abs/2005.04271
- Type: Paper
- Keywords: probabilistic neural network, surrogate modeling, uncertainty, data recovery
- Why it matters: Adds uncertainty/probabilistic framing to flow surrogate and recovery tasks, not just deterministic field prediction.
- VA-use: Cite for uncertainty-aware surrogate and data-recovery workflows.
- Priority: High

#### Convolutional neural network based hierarchical autoencoder for nonlinear mode decomposition of fluid field data

- Link: https://arxiv.org/abs/2006.06977
- Type: Paper
- Keywords: autoencoder, nonlinear mode decomposition, fluid fields, ROM
- Why it matters: Bridges classical modal decomposition intuition and nonlinear representation learning for flow fields.
- VA-use: Compare against POD, autoencoder-ROM, and latent dynamics methods.
- Priority: Medium

#### Sparse identification of nonlinear dynamics with low-dimensionalized flow representations

- Link: https://arxiv.org/abs/2010.12177
- Type: Paper
- Keywords: SINDy, sparse identification, reduced-order flow representation, nonlinear dynamics
- Why it matters: Connects sparse governing-equation discovery with compressed flow representations.
- VA-use: Useful bridge between Fukami-style flow ML and Brunton/SINDy-style interpretable dynamics.
- Priority: High

---

## 3. Romit Maulik — Purdue University

Focus for this repository: SciML for fluids, differentiable turbulence, OpenFOAM + deep learning deployment, probabilistic surrogates, model reduction, and solver-aware ML.

### Representative papers

#### Probabilistic neural networks for fluid flow surrogate modeling and data recovery

- Link: https://arxiv.org/abs/2005.04271
- Type: Paper
- Keywords: probabilistic neural networks, fluid surrogates, data recovery, uncertainty
- Why it matters: Shared with Kai Fukami's lineage; important because it frames fluid surrogates as uncertain recovery/prediction systems.
- VA-use: Cite for uncertainty-aware CFD surrogate modeling.
- Priority: High

#### Differentiable Turbulence: Closure as a partial differential equation constrained optimization

- Link: https://arxiv.org/abs/2307.03683
- Type: Paper
- Keywords: differentiable turbulence, closure modeling, PDE-constrained optimization, SciML
- Why it matters: Treats turbulence closure through differentiable/PDE-constrained optimization rather than pure offline regression.
- VA-use: Anchor for validation-gated and solver-aware turbulence closure research.
- Priority: High

#### Deploying deep learning in OpenFOAM with TensorFlow

- Link: https://arxiv.org/abs/2012.00900
- Type: Paper / workflow
- Keywords: OpenFOAM, TensorFlow, deployment, CFD solver integration
- Why it matters: Practical reference for putting trained deep-learning models inside a CFD workflow, which is where many surrogate papers stop being demos.
- VA-use: Use for OpenFOAM integration notes and solver-in-the-loop deployment planning.
- Priority: High

#### Sub-grid scale model classification and blending through deep learning

- Link: https://arxiv.org/abs/1812.11949
- Type: Paper
- Keywords: sub-grid scale model, LES, classification, model blending, deep learning
- Why it matters: Early applied example of ML for turbulence-model selection/blending rather than standalone field prediction.
- VA-use: Cite in learned-closure and LES-model-selection discussions.
- Priority: Medium

#### Machine-Learning for Nonintrusive Model Order Reduction of the Parametric Inviscid Transonic Flow past an airfoil

- Link: https://arxiv.org/abs/1911.07943
- Type: Paper
- Keywords: nonintrusive ROM, transonic airfoil, parametric flow, machine learning
- Why it matters: Useful engineering benchmark direction because airfoil parametric flow tests geometry/condition variation more than toy PDEs.
- VA-use: Compare with neural operators and geometry-family split benchmarks.
- Priority: Medium

---

## 4. Steven L. Brunton — University of Washington

Focus for this repository: sparse identification, dynamical systems, control, Koopman/operator thinking, reduced-order modeling, and machine learning for fluid mechanics.

### Representative papers

#### Machine Learning for Fluid Mechanics

- Link: https://arxiv.org/abs/1905.11075
- Type: Paper / review
- Keywords: machine learning, fluid mechanics, ROM, turbulence, control
- Why it matters: One of the cleanest overview references connecting fluid mechanics, ML, reduced-order models, and control.
- VA-use: Default citation for framing CFD-AI as more than black-box regression.
- Priority: High

#### PySINDy: A Python package for the Sparse Identification of Nonlinear Dynamics from Data

- Link: https://arxiv.org/abs/2004.08424
- Type: Code / paper
- Keywords: SINDy, sparse identification, dynamical systems, Python
- Why it matters: Turns sparse governing-equation discovery into usable software, making SINDy-style baselines easier to test.
- VA-use: Use as implementation anchor for interpretable surrogate/dynamics experiments.
- Priority: High

#### PySINDy: A comprehensive Python package for robust sparse system identification

- Link: https://arxiv.org/abs/2111.08481
- Type: Code / paper
- Keywords: PySINDy, robust sparse identification, dynamical systems
- Why it matters: More complete PySINDy reference with robust sparse system identification workflows.
- VA-use: Use when documenting reproducible sparse-model baselines.
- Priority: High

#### Discovery of Physics from Data: Universal Laws and Discrepancies

- Link: https://arxiv.org/abs/1906.07906
- Type: Paper
- Keywords: physics discovery, model discrepancy, data-driven laws, SINDy
- Why it matters: Important because real engineering systems often need discovery of missing physics or discrepancy terms, not full replacement of the simulator.
- VA-use: Anchor for hybrid modeling and discrepancy-learning arguments.
- Priority: High

#### Learning dominant physical processes with data-driven balance models

- Link: https://arxiv.org/abs/2001.10019
- Type: Paper
- Keywords: balance models, dominant processes, data-driven modeling, physics discovery
- Why it matters: Provides a route to identify which physical processes dominate a system from data.
- VA-use: Useful for interpretable model-reduction and physics-discovery discussions.
- Priority: Medium

---

## Cross-lineage patterns to watch

- **Wake/flow-field learning:** Sangseung Lee gives canonical deep-learning CFD field-prediction anchors.
- **Sparse sensors and reconstruction:** Kai Fukami provides the strongest bridge from flow ML to sparse experimental/digital-twin sensing.
- **Solver-aware SciML:** Romit Maulik anchors deployment, differentiable turbulence, and OpenFOAM integration.
- **Interpretable dynamics:** Steven L. Brunton anchors SINDy, Koopman-style thinking, control, and dynamical-system interpretability.
- **VA synthesis target:** combine these into validation-gated, interpretable, solver-aware CFD surrogates that survive geometry/family shift and produce auditable engineering decisions.
