# 150 Evidence — GH-600 학습·실습 증거

## Evidence Areas

| 코드 | Evidence | 예시 |
|---:|---|---|
| 010 | Architecture | Goal / Input / Output / Success Criteria |
| 020 | Planning | Structured Plan / Review Gate |
| 030 | Tool / MCP | Tool Matrix / Scope / Governance |
| 040 | State | Memory / State / Checkpoint |
| 050 | Evaluation | Metric / Rubric / Error Analysis |
| 060 | Multi-Agent | Role / Delegation / Handoff |
| 070 | Guardrails | Policy / Human Oversight / Auditability |
| 080 | Scores | QBank / Mock / Retry |
| 090 | Project / Exam | Project / Credential / Reflection |

## Templates

- [`010-design-evidence-template.md`](./010-design-evidence-template.md) — Agent Architecture / Tool / State / Guardrail 설계 기록
- [`020-evaluation-evidence-template.md`](./020-evaluation-evidence-template.md) — Evaluation / Error Analysis 기록
- [`030-exam-evidence-template.md`](./030-exam-evidence-template.md) — 시험 결과와 학습 지표 기록
- [`040-reflection-template.md`](./040-reflection-template.md) — 최종 학습 회고
- [`090-content-verification.md`](./090-content-verification.md) — Repository 콘텐츠 구축 검증

## General Evidence Template

```text
Date:
Lab / Project:
Domain:
Goal:
Design decision:
Why:
Alternative considered:
Evaluation:
Guardrail / human review:
Evidence reference:
What I learned:
```

## Safety Rule

- 실제 운영 권한 확대를 Evidence 과제로 사용하지 않습니다.
- 실제 Secret·Token·Password를 기록하지 않습니다.
- 공개 저장소에 비공개 조직 정보나 민감한 운영 정보를 기록하지 않습니다.
- 실제 시험문항이나 복원 문제를 기록하지 않습니다.

## CLEAR 기준

- [ ] GH-600 PASS
- [ ] 핵심 Labs 완료
- [ ] Agentic SDLC Design Project 80점 이상
- [ ] 6개 Domain Evidence
- [ ] QBank / Mock / Retry 기록
- [ ] 최종 Reflection

## 상태 구분

```text
CONTENT-READY
= 학습 자료 구축 완료

EXAM-READY
= 실제 학습자가 Exam Readiness Gate 통과

PASSED
= GH-600 시험 합격

CLEAR
= 자격시험 + 실습 + 프로젝트 + Evidence 완료
```

---
[← 140 Resources](../140-resources/README.md) · [GH-600 홈](../README.md)
