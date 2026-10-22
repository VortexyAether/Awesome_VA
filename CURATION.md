# Curation Guide for Awesome_VA

This repository is a CFD-AI / SciML research radar, not a general archive.

## Daily curation mission

Collect, filter, summarize, and organize high-quality resources related to:

1. CFD-AI and Scientific Machine Learning
2. Turbulence prediction, surrogate modeling, super-resolution, autoregressive flow prediction, and generative modeling for physical fields
3. Neural operators, Fourier neural operators, operator learning, tensor methods, QTT, AMR, and adaptive discretization
4. Differentiable CFD solvers, JAX-based PDE solvers, and OpenFOAM-related AI workflows
5. AI-assisted research workflows for graduate students: paper writing, literature review, coding, experiment automation, and productivity

## Sources to scan

Use `sources.md` as the operational query set. Primary sources include:

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

## Source authority tiers

This tiering applies going forward to ALL curation — daily picks, resource pages, and `best/README.md` anchors — not only the cleanup pass that introduced it.

**Tier A — default-trust. Actively seek these for "Best Find" / `best/README.md` anchors.**
Peer-reviewed prestigious venues: Journal of Fluid Mechanics (JFM) and JFM Rapids, Physical Review Fluids, Physical Review Letters, Physical Review X, Journal of Computational Physics, AIAA Journal, Journal of Aircraft, Progress in Aerospace Sciences, Annual Review of Fluid Mechanics, Computer Methods in Applied Mechanics and Engineering (CMAME), International Journal for Numerical Methods in Fluids/Engineering, Nature / Nature Physics / Nature Machine Intelligence / Nature Communications, Science, PNAS, and top peer-reviewed ML venues (NeurIPS/ICML/ICLR/JMLR main-track, not workshop-only) when the paper is CFD-AI/SciML relevant.

**Tier B — keep only with strong signal.**
arXiv/preprint-only work is acceptable only if it has at least one of:
- an explicit "accepted at <Tier-A-like venue>" notice,
- a public code repo with real traction (meaningful stars AND a real license, not ★0/no-SPDX),
- authorship from a well-known lab/group with a track record,
- a widely-cited survey/review.

**Tier C — reject by default / remove on sight.**
- arXiv-only preprints with no accepted venue AND (no public code OR a ★0 unlicensed throwaway repo) AND no exceptional, independently-verifiable validation,
- vague or narrow single-result papers with no broader significance,
- SEO/blog-spam,
- anything already a near-duplicate of an existing entry.

When adding or re-evaluating any entry, state the tier (or cite the venue/signal that justifies Tier B) so later passes don't need to re-derive it from scratch.

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
- VA-use: Read / Implement / Benchmark / Cite / Watch / Ignore
- Risk / Caveat: Dataset limitation, code absence, toy-only validation, unclear reproducibility, or other caveat.
- Related threads: validation, CAD, surrogate, digital twin, MCP, sparse sensors, etc.
- Maturity: paper-only / prototype / maintained library / production-ready / watchlist
- Priority: High / Medium / Low
```

Avoid vague phrases such as “this is interesting” or “this is useful.” Explain specifically why it matters.

## Placement rules

Place each resource in the most relevant file under `resources/`.

Preferred files include:

- `resources/differentiable-python-pde-solvers.md`
- `resources/neural-operators-tensor-methods.md`
- `resources/turbulence-generative-flow-models.md`
- `resources/openfoam-ai-workflows.md`
- `resources/datasets-benchmarks.md`
- `resources/paper-writing-tools.md`

If a resource fits multiple categories, choose one primary location and add cross-reference tags in `Keywords` or `Possible use`.

## Daily digest

Create or update `daily/YYYY-MM-DD.md` with:

```markdown
# Daily sciML / Engineering Radar — YYYY-MM-DD

## Top Signals

3–5 concise signals. Each signal should say what changed technically, not only what was published.

## New Papers / Tools

### Item title

- Link: URL
- Type: Paper / Code / Dataset / Tool / Blog / Benchmark / Workflow
- Why it matters: Specific engineering/SciML consequence.
- VA relevance: How this connects to VA's research, writing, experiments, or workflow.
- Action: Read / Save / Test / Cite / Watch / Ignore

## Best Find of the Day

One item only. Explain why it beats the rest.

## Engineering-AI Pattern

Reusable pattern seen today, e.g. validation-gated surrogate, geometry-family generalization, sparse-sensor correction, CAD-native representation, or agent-callable engineering workflow.

## Possible VA Actions

- Read:
- Test:
- Save to resource file:
- LinkedIn/blog candidate:
```

Research ideas should be practical and connected to VA's interests, such as:

- deterministic diffusion/generative modeling for flow prediction
- turbulence surrogate modeling
- spectral energy consistency metrics
- sparse-sensor field reconstruction
- geometry-family split benchmarks
- validation-gated neural operators and fallback contracts
- CAD/BRep-native engineering AI
- CFD workflow automation

## Weekly synthesis

Create `weekly/YYYY-Www.md` when enough daily signals accumulate, especially before a LinkedIn/blog draft. Weekly notes should answer:

- What is the main technical thesis this week?
- What changed compared with previous weeks?
- What should VA read, test, cite, or write next?
- Which `themes/` or `experiments/` pages should be updated?

## Best anchors

Keep durable people/paper lineages in `best/README.md`. This page is for recurring high-value anchors, not daily news.

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
