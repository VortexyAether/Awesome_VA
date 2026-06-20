#!/usr/bin/env python3
"""Generate static SVG dashboard assets for Awesome_VA.

No third-party dependencies. GitHub READMEs can safely render checked-in SVGs;
GitHub Actions can regenerate these from the current daily/resources notes.
"""
from __future__ import annotations

import html
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "daily"
RESOURCES = ROOT / "resources"
OUT = ROOT / "assets" / "trends"

CATEGORIES = {
    "CFD Surrogates": ["cfd-surrogate", "surrogate", "digital twin", "field rmse", "qoi", "readout"],
    "Neural Operators": ["neural-operator", "operator learning", "fno", "deeponet", "cno", "qtt"],
    "Validation / UQ": ["uncertainty", "uq", "validation", "conformal", "calibrated", "fallback", "trust"],
    "CAD / Geometry AI": ["cad", "brep", "geometry", "mesh", "meshing", "cadquery"],
    "CAE Agents": ["agent", "multi-agent", "llm", "workflow", "orchestrate", "mcp"],
    "Turbulence / Flow Gen": ["turbulence", "flow matching", "generative", "navier", "lagrangian"],
    "Thermal / Multiphysics": ["thermal", "heat", "multiphysics", "fea", "coupled"],
    "GPU / Deployment": ["gpu", "hpc", "deployment", "latency", "compact", "mlops"],
}

STACK_FILES = {
    "Data / Benchmarks": ["datasets-benchmarks.md"],
    "Solvers / CFD": ["differentiable-python-pde-solvers.md", "openfoam-ai-workflows.md", "openfoam-tips.md"],
    "Surrogates": ["cfd-ai-papers-surveys.md", "neural-operators-tensor-methods.md", "turbulence-generative-flow-models.md"],
    "Geometry / CAD": ["cad-geometry-ai.md", "meshing-gpu-workflows.md"],
    "Agents / Workflow": ["agent-tools-workflow.md", "research-automation-writing.md", "ai-coding-lab-adoption.md"],
    "Validation / Ops": ["optimization-sciml.md", "security-cost-ops.md"],
    "Visualization": ["visualization-postprocessing.md", "weather-climate-visualization.md"],
}


def read_recent_daily(limit: int = 30) -> str:
    files = sorted(DAILY.glob("20*.md"))[-limit:]
    return "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in files)


def count_categories(text: str) -> Counter[str]:
    lower = text.lower()
    counts: Counter[str] = Counter()
    for cat, needles in CATEGORIES.items():
        for needle in needles:
            counts[cat] += lower.count(needle.lower())
    for cat in CATEGORIES:
        counts.setdefault(cat, 0)
    return counts


def count_resource_entries() -> Counter[str]:
    counts: Counter[str] = Counter()
    for label, files in STACK_FILES.items():
        total = 0
        for name in files:
            path = RESOURCES / name
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            total += len(re.findall(r"^##\s+", text, flags=re.M))
            total += len(re.findall(r"^- \[", text, flags=re.M))
        counts[label] = total
    return counts


def svg_bar_chart(title: str, subtitle: str, values: Counter[str], path: Path, color: str) -> None:
    items = values.most_common()
    width = 920
    row_h = 34
    top = 86
    height = top + row_h * len(items) + 36
    max_v = max([v for _, v in items] or [1]) or 1
    left = 210
    bar_max = 560
    rows = []
    for i, (name, value) in enumerate(items):
        y = top + i * row_h
        w = int((value / max_v) * bar_max) if max_v else 0
        rows.append(f'<text x="24" y="{y+20}" font-size="15" fill="#d7dee8">{html.escape(name)}</text>')
        rows.append(f'<rect x="{left}" y="{y+5}" width="{max(w, 6)}" height="18" rx="5" fill="{color}" opacity="0.88"/>')
        rows.append(f'<text x="{left + max(w, 6) + 12}" y="{y+20}" font-size="14" fill="#9fb1c7">{value}</text>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" rx="18" fill="#0b0f14"/>
  <rect x="1" y="1" width="{width-2}" height="{height-2}" rx="17" fill="none" stroke="#263241"/>
  <text x="24" y="36" font-size="24" font-family="Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif" font-weight="700" fill="#f7fafc">{html.escape(title)}</text>
  <text x="24" y="62" font-size="14" font-family="Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif" fill="#91a4bb">{html.escape(subtitle)}</text>
  <g font-family="Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif">
    {''.join(rows)}
  </g>
</svg>
'''
    path.write_text(svg, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    momentum = count_categories(read_recent_daily())
    coverage = count_resource_entries()
    svg_bar_chart("Topic Momentum", "Keyword/tag signal count from recent daily radar notes", momentum, OUT / "topic-momentum.svg", "#38bdf8")
    svg_bar_chart("Engineering AI Stack Coverage", "Approximate curated-entry coverage across resource pages", coverage, OUT / "stack-coverage.svg", "#a78bfa")
    print(f"wrote {(OUT / 'topic-momentum.svg').relative_to(ROOT)}")
    print(f"wrote {(OUT / 'stack-coverage.svg').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
