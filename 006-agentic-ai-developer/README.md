# 006 GitHub Agentic AI Developer

> **GitHub Agentic AI Developer · GH-600**  
> GitHub 기반 SDLC에서 AI Agent의 아키텍처, 도구 상호작용, 상태 관리, 평가, 다중 Agent 조정, Guardrail과 Accountability를 학습하는 자격증 과정입니다.

> 이 Repository의 내용은 자격증 학습용 고수준 설계·판단 연습을 중심으로 하며 실제 운영 환경의 권한을 확대하거나 안전 통제를 우회하는 절차를 다루지 않습니다.

## Quick Start

1. [`010-overview/`](./010-overview/)에서 6개 시험 Domain을 확인합니다.
2. [`020-terms/`](./020-terms/)에서 Agent, Tool, MCP, Memory, State, Evaluation, Guardrail 등 핵심 용어를 익힙니다.
3. [`030-concepts/`](./030-concepts/)에서 Planning, Execution, Evaluation, Human Oversight의 관계를 이해합니다.
4. [`040-official-docs/`](./040-official-docs/)의 Microsoft Learn GH-600 Study Guide와 GitHub Learn을 기준 자료로 사용합니다.
5. [`060-labs/`](./060-labs/)에서 안전한 Sandbox와 문서 기반 Scenario로 핵심 개념을 연습합니다.
6. [`070-exercises/`](./070-exercises/) → [`080-question-bank/`](./080-question-bank/) → [`110-mock-exams/`](./110-mock-exams/) → [`120-wrong-answers/`](./120-wrong-answers/) 순으로 시험 준비를 진행합니다.
7. [`130-progress/`](./130-progress/)의 Exam Readiness Gate를 통과한 뒤 실제 응시 상태를 `EXAM-READY`로 변경합니다.
8. [`150-evidence/`](./150-evidence/)에서 설계·평가·시험·회고 Evidence를 관리합니다.

## Status

| 구분 | 상태 | 의미 |
|---|---|---|
| Content Status | **CONTENT-READY** | GH-600 학습·실습·문제·Mock·Evidence 구축 완료 |
| Learning Status | **PLANNED** | 실제 학습 시작 전 |

> 콘텐츠 구축 검증: [`150-evidence/090-content-verification.md`](./150-evidence/090-content-verification.md)

## Exam Snapshot

| 항목 | 내용 |
|---|---|
| 자격증 | GitHub Certified: Agentic AI Developer |
| 시험 | GH-600 |
| 수준 | Intermediate (중급) |
| 시험 시간 | 120분 |
| 현재 표시 언어 | English |
| 현재 Microsoft Learn 기준 응시료 | USD 165 (지역별 차이 가능) |
| 자격 유효기간 | 24개월 |

> GitHub Learn은 자격증 이름이나 beta 상태 표기가 Microsoft Learn과 일시적으로 다를 수 있습니다. 실제 예약·점수 처리 상태는 시험 예약 시점의 공식 화면을 최종 기준으로 확인합니다.

## Current Exam Domains

| # | Domain | 비중 |
|---:|---|---:|
| 1 | Prepare agent architecture and SDLC processes | 15–20% |
| 2 | Implement Tool Use and Environment Interaction | 20–25% |
| 3 | Manage Memory, State, and Execution | 10–15% |
| 4 | Perform Evaluation, Error Analysis, and Tuning | 15–20% |
| 5 | Orchestrate Multi-Agent Coordination | 15–20% |
| 6 | Implement Guardrails and Accountability | 10–15% |

## Conceptual Learning Flow

```text
Requirement
→ Agent Architecture
→ Plan and Success Criteria
→ Human / Policy Review
→ Controlled Tool Interaction
→ State / Execution Tracking
→ Evaluation / Error Analysis
→ Multi-Agent Coordination when needed
→ Guardrails / Accountability
→ Human Review
```

## 핵심 학습 영역

- Agent Architecture / SDLC Integration
- Planning / Reasoning / Action의 경계
- Structured Plan / Success Criteria
- Tool Selection / Controlled Permission
- MCP (Model Context Protocol) 개념과 Governance
- Execution Context / Repository Scope / Branch Scope 개념
- Memory / State / Checkpoint / Resume
- Evaluation / Error Analysis / Tuning
- Multi-Agent Coordination / Delegation / Handoff
- Guardrails / Least Privilege / Accountability
- Human-in-the-loop / Human Oversight
- Inspectable Artifacts / Auditability

## Built Learning Assets

| 영역 | 구축 결과 |
|---|---:|
| Labs | 12개 |
| Exercises | 60개 |
| Question Bank | 100문제 |
| Mock Exams | 3회 × 40문제 = 120문제 |
| 자체 시험형 문제 | **총 220문제** |
| Final Review | 완료 |
| Agentic SDLC Design Project | 완료 |
| Wrong Answer / Retry | 완료 |
| Progress / Exam Gate | 완료 |
| Evidence Templates | 완료 |

## Directory Map

```text
006-agentic-ai-developer/
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

## 대표 프로젝트

**GitHub Agentic SDLC Design Project**

Agent가 개발 Workflow에 참여하는 상황을 가정해 다음을 문서 기반으로 설계합니다.

```text
Requirement / Issue
        ↓
Architecture / Success Criteria
        ↓
Structured Plan
        ↓
Review Gate
        ↓
Controlled Tool / MCP Design
        ↓
State / Checkpoint
        ↓
Evaluation / Error Analysis
        ↓
Optional Multi-Agent Coordination
        ↓
Guardrails / Accountability
        ↓
Human Review / Evidence
```

## Exam Readiness Gate

- [ ] 최신 공식 GH-600 Study Guide 확인
- [ ] 6개 Domain과 비중 설명 가능
- [ ] Planning / Execution / Tool / MCP / Scope를 구분 가능
- [ ] Memory / State / Checkpoint / Resume를 설명 가능
- [ ] Evaluation과 Error Analysis를 설계 가능
- [ ] Single Agent와 Multi-Agent 선택 근거 설명 가능
- [ ] Guardrail / Accountability / Human Oversight 설명 가능
- [ ] Labs 80% 이상
- [ ] Question Bank 2회차 85% 이상
- [ ] Mock 01 / Mock 02 각각 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 최근 오답 재시험 90% 이상
- [ ] Agentic SDLC Design Project 80점 이상

## Official Baseline

- Microsoft Learn — GitHub Certified: Agentic AI Developer  
  https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-developer/
- Microsoft Learn — Study guide for Exam GH-600  
  https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-600
- Microsoft Learn — GH-600T00 Developing in Agentic AI Systems  
  https://learn.microsoft.com/en-us/training/courses/gh-600t00
- GitHub Learn — GitHub Agentic AI Developer  
  https://learn.github.com/certification/AGENTIC

---

[← 005 GitHub Advanced Security](../005-advanced-security/README.md) · [통합 학습 시스템](../README.md)
