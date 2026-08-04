# Thermal & Heat Transfer

Resources for heat-transfer modeling, thermal-fluid digital twins, thermal property prediction, and automation-ready validation workflows.

## PINO thermal ranking of low-cost wall materials

- Link: https://arxiv.org/abs/2607.25668
- Data: https://doi.org/10.5281/zenodo.21311299
- Type: Physics-informed neural operator + thermal decision-QoI study
- Keywords: PINO, FNO, building envelope, thermal ranking, ISO 13786, data-scarce physics loss, QoI
- One-line summary: Couples Crank–Nicolson FDM data generation with a PINO/FNO operator that maps wall-material parameters to temperature fields while preserving peak inner-surface temperature and ISO 13786 lag/decrement QoIs.
- Why it matters:
  - Engineering thermal surrogates should preserve decision rankings and regime boundaries, not only field RMSE.
  - Reports data-scarce physics-loss gains on QoI MAE and shows material rankings can reverse across climate regimes.
  - Transferable pattern for process/decision QoI evaluation under sparse labeled solves.
- Evidence: Issue Board harvest notes field rel.L2 ~5.14e-4, QoI MAE ~0.201 K, and scarce-data QoI improvements of roughly 18.8–27.5%.
- Caveat: 1D wall heat equation for housing materials rather than full-building or aerospace CFD.
- Possible use: Reuse the QoI-ranking + climate-regime sweep pattern when scoring thermal/CFD surrogates for design decisions.
- Maturity: paper + Zenodo data claim
- Priority: High

## Cepstral analysis for Green-Kubo thermal conductivity calculations of MOFs

- Link: https://arxiv.org/abs/2606.13588
- Type: Thermal-property simulation workflow / machine-learned potential + Green-Kubo acceleration
- Keywords: thermal conductivity, Green-Kubo, cepstral analysis, machine-learned potential, MOF, automation
- One-line summary: Combines machine-learned moment tensor potentials with cepstral analysis to make Green-Kubo thermal-conductivity estimates for MOFs more stable, faster-converging, and less dependent on ad hoc user parameters.
- Why it matters:
  - Heat-transfer prediction often fails operationally because workflows are noisy, parameter-sensitive, and hard to automate reproducibly.
  - The paper reports stable convergence over roughly 1–2 ns of sampling for MOF examples, compared with erratic direct Green-Kubo analysis.
  - Useful pattern for VA: prioritize thermal workflows with quantified convergence, uncertainty, and automation readiness rather than only model accuracy claims.
- Possible use: Track as a reference for automated thermal-property pipelines and for comparing MD/ML-potential heat-transfer estimates against experimental or high-fidelity baselines.
- Maturity: paper-only
- Priority: Medium

## Collective Bubble Nucleation

- Link: https://arxiv.org/abs/2606.14567
- Type: Boiling heat-transfer / two-phase flow physics paper
- Keywords: boiling, bubble nucleation, vapor removal, site stability, two-phase flow, cooling
- One-line summary: Studies how interactions between boiling bubbles govern nucleation-site stability and vapor removal through scale-separated hydrodynamic mechanisms.
- Why it matters:
  - Boiling/cooling surrogates that only predict averaged heat-transfer coefficients can miss site activation, deactivation, and vapor-removal failure modes.
  - The paper is a useful physics anchor for regime-aware thermal-fluid ML, especially around phase change and critical heat-transfer transitions.
  - Relevant to electronics cooling, liquid cooling, and thermal-management digital twins where operating-envelope boundaries matter.
- Possible use: When evaluating boiling ML/surrogate papers, add separate metrics or qualitative checks for site stability, vapor-removal dynamics, and transition/CHF-adjacent behavior.
- Maturity: paper-only
- Priority: Medium
