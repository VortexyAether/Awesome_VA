<div align="center">

# 🌊 Awosome_VA

### **SciML · CFD · AI-assisted research workflow** 큐레이션 저장소

[![SciML](https://img.shields.io/badge/SciML-CFD-2563eb?style=for-the-badge)](#-sciml--cfd)
[![Agents](https://img.shields.io/badge/AI%20Agents-생산성-7c3aed?style=for-the-badge)](#-ai-agent--생산성)
[![Graduate](https://img.shields.io/badge/대학원생-Workflow-16a34a?style=for-the-badge)](#-대학원생-연구-워크플로우)
[![English](https://img.shields.io/badge/README-English-dc2626?style=for-the-badge)](README.md)

*CFD-ML 연구와 대학원생 생산성에 유용한 논문, 도구, 저장소, 워크플로우, 기술 노트 모음.*

</div>

---

## 🧭 빠른 이동

| 🚀 대분류 | 포함되는 것 | 바로가기 |
|---|---|---|
| **SciML & CFD** | CFD solver, AMR, OpenFOAM, meshing, JAX prototype, neural operator, visualization | [이동](#-sciml--cfd) |
| **대학원생 연구 워크플로우** | 논문 작성, 연구 자동화, 발표/보고서 구조, 학술/산업 기회 | [이동](#-대학원생-연구-워크플로우) |
| **AI agent & 생산성** | Claude/Codex/OpenCode, local LLM, skill/harness, agent-friendly tooling | [이동](#-ai-agent--생산성) |
| **문서/행정/운영** | HWP 도구, 행사, cloud cost/security, 기타 유틸리티 | [이동](#-문서행정운영) |

---

## 🔬 SciML & CFD

| 분야 | 먼저 볼 문서 | 대표 자료 |
|---|---|---|
| 🧪 **Differentiable CFD / AMR** | [Differentiable CFD & AMR solvers](resources/differentiable-cfd-amr.md) | JAX-AMR, JANC, JAXFLUIDS, LEX v1.6.0 |
| 🧱 **Meshing / HPC CFD** | [Meshing & GPU workflows](resources/meshing-gpu-workflows.md) · [GPU OpenFOAM](resources/gpu-openfoam-hpc.md) | PhysicsNeMo-Mesh, meshio, SALOME/Gmsh/Pointwise, OpenFOAM GPU acceleration |
| 🌪️ **OpenFOAM 실무** | [OpenFOAM tips](resources/openfoam-tips.md) | solver reference, OpenFOAM-dev, square-cylinder notes, `startFrom latestTime` |
| ⚡ **JAX CFD 프로토타입** | [JAX-based CFD prototypes](resources/jax-cfd-prototypes.md) | google/jax-cfd, AeroJAX, IBM airfoil flap, GUI prototype |
| 🎞️ **시각화** | [Visualization & post-processing](resources/visualization-postprocessing.md) · [Weather/climate visualization](resources/weather-climate-visualization.md) | PyVista, Omniverse Q-criterion, Earth2Studio, black-hole simulation visualization |
| 🧩 **CAD / geometry AI** | [CAD, geometry & AI-assisted design](resources/cad-geometry-ai.md) | ForgeCAD, FreeCAD + Claude Code, Zero-to-CAD, FeatureFox, FreeCAD MCP |
| 🧠 **Neural operator / architecture** | [Neural operators & tensor methods](resources/neural-operators-tensor-methods.md) · [Optimization for SciML](resources/optimization-sciml.md) | PhysicsNeMo, neuraloperator, JetSCI, MENO, FNO-LBM, LESnets |
| 🎓 **Fluid/AI 교육** | [Fluid mechanics, turbulence & AI education](resources/education-fluid-ai.md) | VinuesaLab |
| ∑ **수학적 기반** | [Mathematical foundations](resources/math-foundations.md) | function representation notes |

---

## 🧑‍🎓 대학원생 연구 워크플로우

| 분야 | 먼저 볼 문서 | 대표 자료 |
|---|---|---|
| ✍️ **연구 자동화 / 글쓰기** | [Research automation & writing](resources/research-automation-writing.md) | MarkItDown, PaperOrchestra, PaperBanana, Feynman, Overleaf MCP |
| 🗂️ **발표 / 보고서 구조** | [Research presentation & report structure](resources/research-presentation-workflow.md) | scenario → metric → data → learning → analysis → application workflow |
| 📌 **행사 / 기회** | [Events & opportunities](resources/events-opportunities.md) | SEMICON, 산업계/커리어 신호 |

---

## 🤖 AI agent & 생산성

| 분야 | 먼저 볼 문서 | 대표 자료 |
|---|---|---|
| 🛠️ **Agent 도구** | [Agent tools & research workflow](resources/agent-tools-workflow.md) | Claude Code tips, Codex/OpenCode, Google Workspace CLI, MCP/CAD bridges, sim-cli |
| 🏫 **연구실 AI 도입** | [AI coding & lab adoption](resources/ai-coding-lab-adoption.md) | 공용 Claude/API 전략, 랩세미나 아이디어, Codex 지원 프로그램 |
| 💻 **Local AI workflow** | [Local AI research workflow](resources/local-ai-workflow.md) | Ollama, llama.cpp, whatcani.run, Gemma/local LLMs |

---

## 📄 문서/행정/운영

| 분야 | 먼저 볼 문서 | 대표 자료 |
|---|---|---|
| 📝 **문서/행정 도구** | [Miscellaneous tools](resources/misc-tools.md) | HOP Open HWP, image/video AI notes |
| 🔐 **보안 / 비용 / 운영** | [Security, cost & operations](resources/security-cost-ops.md) | AWS billing incident, secret/cost reminders |

---

## 🧹 큐레이션 원칙

- **SciML/CFD 연구**, **대학원생 연구 워크플로우**, **AI 생산성**, **연구실 운영**에 유용한 자료를 우선한다.
- 과제, 사적인 연구실 운영 대화, 일시적인 Slack 잡담은 재사용 가능한 자료가 있을 때만 포함한다.
- 각 entry는 짧게 유지한다: 링크, 왜 중요한지, 어디에 쓸 수 있는지.
- 자세한 내용은 `resources/*.md`에 두고, README는 한눈에 보는 대시보드로 유지한다.

---

<div align="center">

**VA_claw**가 🦞 집게로 관리합니다.

</div>
