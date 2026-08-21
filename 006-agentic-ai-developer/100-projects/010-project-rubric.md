# Agentic SDLC Design Project — Rubric

| 영역 | 배점 | 평가 기준 |
|---|---:|---|
| Architecture / Success Criteria | 15 | Goal/Input/Output/Success 명확 |
| Planning / Approval | 15 | Plan과 Execution 분리, Review Gate |
| Tool / MCP / Scope | 15 | 필요 Tool과 최소 범위·Trust 설명 |
| Memory / State / Execution | 10 | State/Checkpoint/Recovery 설계 |
| Evaluation / Error Analysis | 15 | Metric/Dataset/Failure 분석 |
| Multi-Agent Coordination | 10 | 필요 여부·역할·Handoff 근거 |
| Guardrails / Accountability | 15 | 정책·Human Oversight·Auditability |
| Evidence / Explainability | 5 | 재현 가능한 Artifact |
| **합계** | **100** | |

## 판정

- 0–79: 보완 필요
- 80–89: `PASS`
- 90–100 + Evidence: `CLEAR` 후보

## 감점 원칙

- 자율성만 높이고 Evaluation/Guardrail이 없음
- 필요 이상 Scope/Permission을 기본 선택
- 실패·중단·Escalation 조건이 없음
- Human Review 책임이 불명확
