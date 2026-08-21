# 006 GitHub Agentic AI Developer

> **GitHub Agentic AI Developer · GH-600**  
> GitHub 기반 SDLC에서 AI Agent의 아키텍처, 도구 상호작용, 상태 관리, 평가, 다중 Agent 조정, Guardrail과 Accountability를 학습하는 자격증 과정입니다.

> 이 Repository의 내용은 자격증 학습용 고수준 설계·판단 연습을 중심으로 하며 실제 운영 환경의 권한을 확대하거나 안전 통제를 우회하는 절차를 다루지 않습니다.

## Quick Start

1. `010-overview/`에서 6개 시험 Domain을 확인합니다.
2. `020-terms/`에서 Agent, Tool, MCP, Memory, State, Evaluation, Guardrail 등 핵심 용어를 익힙니다.
3. `030-concepts/`에서 Planning, Execution, Evaluation, Human Oversight의 관계를 이해합니다.
4. `040-official-docs/`의 Microsoft Learn GH-600 Study Guide와 GitHub Learn을 기준 자료로 사용합니다.
5. `060-labs/`에서는 안전한 Sandbox와 문서 기반 Scenario로 핵심 개념을 연습합니다.
6. Exercises → Question Bank → Mock → Wrong Answers → Evidence 순으로 준비합니다.

## Status

| 구분 | 상태 | 의미 |
|---|---|---|
| Content Status | **BUILDING** | 현재 GH-600 시험 범위 기반 콘텐츠 구축 중 |
| Learning Status | **PLANNED** | 실제 학습 시작 전 |

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

> GitHub Learn은 현재 자격증 이름에 `(beta)`를 표시하는 반면 Microsoft Learn 자격증 페이지는 `GitHub Certified: Agentic AI Developer`로 표시합니다. 실제 예약·점수 처리 상태는 시험 예약 화면을 최종 기준으로 확인합니다.

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

- 입력과 성공 기준
- 계획과 실행의 분리
- 필요한 도구와 최소 권한
- 상태와 실행 기록
- 평가 기준
- 다중 Agent가 필요한 조건
- Guardrail과 Human Review
- 실패 시 중단·복구·책임 추적 원칙

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
