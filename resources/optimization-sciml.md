# Optimization for Scientific Machine Learning

## SpecMuon: Muon with Spectral Guidance

- Link: https://arxiv.org/abs/2602.16167
- Type: Optimizer for Scientific ML
- Summary:
  - Adapts the Muon optimizer idea for scientific computing / physics-informed learning.
  - Introduces spectral-aware guidance to handle ill-conditioned gradients, multi-scale spectral behavior, and stiffness.
- Why it matters:
  - PINNs and neural operators often fail because optimization is poorly conditioned, not because the architecture is impossible.
  - CFD applications frequently involve stiffness, multi-scale spectra, and hard physical constraints.
  - Since CFD-specific applications may still be sparse, this could be a good early exploration topic.
- Possible follow-up:
  - Test on PINN benchmarks, operator-learning problems, or differentiable CFD inverse problems.
  - Compare against AdamW, L-BFGS, Shampoo-like second-order-ish optimizers, and baseline Muon.

## Attention Residuals

- Link: https://github.com/MoonshotAI/Attention-Residuals/tree/master
- Type: Neural network architecture / residual connection method
- Summary:
  - Addresses information dilution in fixed residual connections.
  - Applies softmax attention over previous layer outputs to select and aggregate needed information data-dependently.
  - Introduces Block AttnRes to reduce memory overhead and support large models.
- Why it matters:
  - Potentially relevant to deep surrogate models, neural operators, and long-depth architectures where residual information routing matters.

## CLARA compartment-model generation for multiphase reactors

- Link: https://arxiv.org/abs/2604.26695
- Type: CFD-to-compartment-model reduction / control-oriented surrogate tooling
- Why it matters:
  - Automates reduced compartment-model generation from expensive multiphase CFD simulations.
  - Directly connects CFD, real-time control, design optimization, and interpretable surrogate modeling.
  - Strong candidate for lab discussion because it is closer to deployable engineering control than generic AI-for-PDE claims.

## Robust multi-jet active flow control

- Link: https://arxiv.org/abs/2604.26481
- Type: Active flow control / reinforcement-learning-inspired control framework
- Why it matters:
  - Addresses robustness of multi-jet actuation for airfoil flow control in weakly compressible flow.
  - Useful for connecting SciML/control papers to aerodynamic actuation and closed-loop CFD experiments.
  - Track as a control benchmark idea rather than only an architecture paper.

