# Curation Guide for Awesome_VA

This repository is a CFD-AI / SciML research radar, not a general archive.

## Daily curation mission

Collect, filter, summarize, and organize high-quality resources related to:

1. CFD-AI and Scientific Machine Learning
2. Turbulence prediction, surrogate modeling, super-resolution, and autoregressive flow prediction
3. Neural operators, Fourier neural operators, operator learning, tensor methods, QTT, AMR, and adaptive discretization
4. Differentiable CFD solvers, JAX-based PDE solvers, and OpenFOAM-related AI workflows
5. Diffusion models, deterministic generative models, and frequency/spectral methods for physical fields
6. AI-assisted research workflows for graduate students: paper writing, literature review, coding, experiment automation, and productivity

## Sources to scan

- arXiv
- Papers with Code
- GitHub trending and GitHub search
- Semantic Scholar when accessible
- Google Scholar when accessible
- Hugging Face papers and models
- University/lab research blogs
- Major conference proceedings when relevant
- Useful open-source tools, not only papers

## Selection criteria

Judge each candidate by:

- relevance to CFD-AI / SciML / engineering AI
- technical depth
- practical usefulness
- novelty
- code availability
- reproducibility
- connection to VA's research interests
- usefulness for future papers, experiments, proposals, or thesis writing

Only add resources that are genuinely worth saving. It is better to add 3 good resources than 20 mediocre ones.

## Reject by default

Do not add:

- low-quality AI-generated content
- SEO blog spam
- vague LinkedIn/social posts
- shallow Medium posts without technical substance
- resources with unclear relevance to CFD-AI, SciML, engineering AI, or graduate research workflows

## Required entry format

```markdown
## Title of the resource

- Link: URL
- Type: Paper / Code / Dataset / Tool / Blog / Lecture / Benchmark / Workflow
- Keywords: keyword1, keyword2, keyword3
- One-line summary: A concise explanation of what this is.
- Why it matters: Explain why this resource is important from a CFD-AI / SciML research perspective.
- Possible use: Explain how VA might use this resource in research, writing, experiments, or workflow automation.
- Maturity: paper-only / prototype / maintained library / production-ready / watchlist
- Priority: High / Medium / Low
```

Avoid vague phrases such as “this is interesting” or “this is useful.” Explain specifically why it matters.

## Placement rules

Place each resource in the most relevant file under `resources/`.

Preferred files include:

- `resources/differentiable-cfd-amr.md`
- `resources/neural-operators-tensor-methods.md`
- `resources/turbulence-surrogate-models.md`
- `resources/diffusion-generative-physics.md`
- `resources/jax-pde-solvers.md`
- `resources/openfoam-ai-workflows.md`
- `resources/research-productivity-agents.md`
- `resources/datasets-benchmarks.md`
- `resources/paper-writing-tools.md`
- `resources/weekly-digest.md`

If a resource fits multiple categories, choose one primary location and add cross-reference tags in `Keywords` or `Possible use`.

## Daily digest

Create or update `daily/YYYY-MM-DD.md` with:

```markdown
# Daily Research Radar — YYYY-MM-DD

## Highlights

- ...

## Added Resources

### Category

- [Resource title](URL) — short note.

## Best Find of the Day

Resource title and why it was the most valuable.

## Possible Research Ideas

1. ...
```

Research ideas should be practical and connected to VA's interests, such as:

- deterministic diffusion/generative modeling for flow prediction
- turbulence surrogate modeling
- spectral energy consistency metrics
- wafer-scale prediction with physics-inspired priors
- neural operator comparison
- CFD workflow automation

## Quality checks before commit

1. Read at least the abstract, README, or project description for every added resource.
2. Do not hallucinate details.
3. If there is no code, say so honestly.
4. If code is abandoned or poorly documented, mark it as `prototype` or `watchlist`.
5. Avoid duplicate entries.
6. Check that links are valid.
7. Run a markdown formatting check when possible.
8. Commit and push with a clean message.

## Commit style

Use messages such as:

- `daily-radar: add YYYY-MM-DD research updates`
- `resources: add differentiable CFD and neural operator papers`
- `docs: refine research radar structure`
