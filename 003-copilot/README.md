# 003 GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300)

> **GitHub Copilot · GH-300**  
> GitHub 자격증 학습 시스템의 세 번째 과정이며, AI 개발 지원 기능을 **책임감 있게 이해하고 실제 개발 Workflow에 적용**하는 과정입니다.

## 빠른 시작 (Quick Start, QS)

1. [`010-overview/`](./010-overview/)에서 **2026-08-07 적용 시험 범위**를 먼저 확인합니다.
2. [`020-terms/`](./020-terms/)에서 Generative AI, LLM, Prompt, Context, Agent Mode, MCP, CLI 등 핵심 용어를 학습합니다.
3. [`030-concepts/`](./030-concepts/)에서 Copilot의 데이터 흐름, Prompt/Context, Human Review 구조를 연결합니다.
4. [`040-official-docs/`](./040-official-docs/)의 Microsoft Learn Study Guide를 시험 범위의 1차 기준으로 사용합니다.
5. [`060-labs/`](./060-labs/)에서 IDE, CLI, Agent Mode, MCP, Testing, Code Review, Privacy를 직접 실습합니다.
6. [`070-exercises/`](./070-exercises/)와 [`080-question-bank/`](./080-question-bank/)로 Scenario 판단력을 강화합니다.
7. [`110-mock-exams/`](./110-mock-exams/)과 [`120-wrong-answers/`](./120-wrong-answers/)로 시험 준비도를 검증합니다.
8. [`130-progress/`](./130-progress/)와 [`150-evidence/`](./150-evidence/)에서 실제 학습 결과를 별도로 관리합니다.

## 상태 (Status, S)

| 구분 | 상태 | 의미 |
|---|---|---|
| 콘텐츠 상태 (Content Status, CS) | **CONTENT-READY** | 2026-08 개정 범위·Lab·100문제·Mock·Evidence 구축 완료 |
| 학습 상태 (Learning Status, LS) | **PLANNED** | 실제 학습 시작 전 |

콘텐츠 구축 검증: [`150-evidence/090-content-verification.md`](./150-evidence/090-content-verification.md)

## 시험 개요 (Exam Snapshot, ES)

| 항목 | 내용 |
|---|---|
| 자격증 | GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) |
| 시험 | GH-300 |
| 수준 | Intermediate (중급) |
| 시험 시간 | 100분 |
| 응시 언어 | English, Portuguese, Spanish, Korean, Japanese |
| 기준 응시료 | USD 99 (지역별 가격이 다를 수 있음) |
| 자격 유효기간 | 24개월 |
| 현재 학습 기준 | **Skills measured as of 2026-08-07** |

## 현재 Skills Measured — 2026-08-07 (Current Skills Measured — 2026-08-07, CSM)

Microsoft Learn의 현재 GH-300 Study Guide 기준입니다.

| Skill Area | 시험 비중 |
|---|---:|
| 1. Use GitHub Copilot responsibly | 15–20% |
| 2. Use GitHub Copilot features | 25–30% |
| 3. Understand GitHub Copilot data and architecture | 10–15% |
| 4. Apply prompt engineering and context crafting | 10–15% |
| 5. Improve developer productivity with GitHub Copilot | 10–15% |
| 6. Configure privacy, content exclusions, and safeguards | 10–15% |

> **중요:** GitHub Learn의 자격증 페이지가 이전 7개 Domain 비중을 표시하는 시점이 있을 수 있습니다. 이 Repository에서는 **Microsoft Learn의 최신 GH-300 Study Guide(2026-08-07 적용)**를 시험 범위 기준으로 사용하고, GitHub Learn은 보조 자료로 교차 확인합니다.

## 2026 개정에서 반드시 포함할 기능

- Copilot in the IDE / Inline Suggestions / Chat
- **GitHub Copilot CLI**
- **Agent Mode / Agent Sessions / Sub-Agents**
- **Copilot Edits**
- **MCP (Model Context Protocol)**
- Copilot Code Review / Pull Request Summaries
- Spaces / Spark
- Instructions files / Prompt files
- Organization-wide Policy / Audit Log / Subscription Management
- Data Flow / Prompt Building / Proxy Filtering / Post-processing
- Zero-shot / Few-shot / Context Crafting
- Code Generation / Refactoring / Documentation / Testing
- Security / Performance Suggestions
- Content Exclusions / Public Code Matching Filter / Troubleshooting

## 핵심 구조

```text
Developer Intent
      ↓
Prompt + Context + Instructions
      ↓
Copilot (IDE / CLI / Agent)
      ↓
Suggestion / Edit / Agent Action
      ↓
Human Review
      ↓
Code / Test / Refactor / Documentation
      ↓
Run / Test / Security / Privacy Verification
```

## Directory 맵 (Directory Map, DM)

```text
003-copilot/
├── 010-overview/
├── 020-terms/
├── 030-concepts/
├── 040-official-docs/
├── 050-guides/
├── 060-labs/
├── 070-exercises/
├── 080-question-bank/
├── 090-final-review/
├── 100-projects/
├── 110-mock-exams/
├── 120-wrong-answers/
├── 130-progress/
├── 140-resources/
└── 150-evidence/
```

## 콘텐츠 Snapshot (Content Snapshot, CS)

```text
Labs               13개
Exercises           60개
Question Bank       100문제
Mock Exams          3회 × 40 = 120문제
자체 문제 총계      220문제
Final Review        Checklist + Confusion Matrix + Exam Strategy
Project             AI-Assisted Development Project + Rubric + Evidence
```

## 7일 단기 집중 과정 (7-Day Fast Track, 7DFT)

| Day | 핵심 목표 |
|---:|---|
| 1 | Responsible AI + Copilot IDE/Chat/CLI 기본 |
| 2 | Agent Mode / Edits / MCP / Code Review / Spaces / Spark |
| 3 | Data Flow / Architecture / LLM Limitations |
| 4 | Prompt Engineering / Context Crafting / Instructions / Prompt Files |
| 5 | Productivity / Testing / Security / Privacy / Exclusions |
| 6 | Exercises + Question Bank + 약점 Lab + Mock 01 |
| 7 | Mock 02 + Final Mock + Final Review + Exam Readiness Gate |

## 대표 프로젝트

**AI-Assisted Development Project**

```text
Requirements
   ↓
Prompt / Context / Instructions
   ↓
Implementation or Agent Task
   ↓
Test Generation
   ↓
Debugging
   ↓
Refactoring
   ↓
Code Review / Documentation
   ↓
Human Review / Verification
   ↓
Privacy / Security Check
```

## 시험 준비도 통과 기준 (Exam Readiness Gate, ERG)

- [ ] 최신 Microsoft Learn GH-300 Study Guide 확인
- [ ] 6개 Skill Area를 비중과 함께 설명 가능
- [ ] IDE / CLI / Agent Mode / MCP의 역할을 구분 가능
- [ ] Prompt와 Context를 설계하고 결과를 검증 가능
- [ ] Data Flow와 LLM/Copilot 한계를 설명 가능
- [ ] Responsible AI / Privacy / Content Exclusion / Safeguard 설명 가능
- [ ] Question Bank 2회차 85% 이상
- [ ] Mock Exam 최근 2회 연속 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 최근 오답 재시험 90% 이상

## Official Baseline

- Microsoft Learn — Study guide for Exam GH-300  
  https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300
- Microsoft Learn — GitHub Copilot Certification  
  https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/
- GitHub Learn — GitHub Copilot Certification  
  https://learn.github.com/certification/COPILOT
- GitHub Docs — GitHub Copilot  
  https://docs.github.com/en/copilot

---

[← 002 GitHub Actions](../002-actions/README.md) · [통합 학습 시스템](../README.md)
