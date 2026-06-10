# Experiment Ideas

Concrete VA-sized experiments derived from daily and weekly radar.

This directory is for turning papers into testable engineering artifacts.

Good experiment notes are small, executable, and skeptical.

Recommended initial experiment pages:

- `spectral-error-metric-for-flow-surrogates.md`
- `geometry-family-split-benchmark.md`
- `validation-gated-neural-operator.md`
- `sparse-sensor-to-field-reconstruction.md`
- `openfoam-model-in-the-loop-demo.md`

Template:

```markdown
# Experiment Title

## Question
What are we trying to test?

## Motivation
Which daily/weekly radar items caused this?

## Minimal setup
Dataset, baseline, model, metric, compute estimate.

## Baselines
Classical method, simple ML method, modern method.

## Metrics
Field error, spectral error, boundary/flux error, rollout stability, downstream objective error, latency.

## Expected failure modes
Where the method is likely to cheat or break.

## Success criterion
What result would make this worth continuing?
```
