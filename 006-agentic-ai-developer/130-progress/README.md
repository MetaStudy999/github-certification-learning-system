# 130 Progress — GH-600 진행률 Dashboard

## 상태 (Status, S)

- 콘텐츠 상태 (Content Status, CS): **CONTENT-READY**
- 학습 상태 (Learning Status, LS): **PLANNED**

> 콘텐츠 구축 상태와 실제 개인 학습 상태를 분리합니다. Repository가 완성되어도 실제 학습을 시작하지 않았다면 Learning Status는 `PLANNED`입니다.

## 학습 상태 흐름 (Learning Status Flow, LSF)

```text
PLANNED
→ READY
→ LEARNING
→ PRACTICING
→ REVIEWING
→ EXAM-READY
→ PASSED
→ CLEAR
```

## 영역 Progress (Domain Progress, DP)

| Domain | Weight | Theory | Lab | QBank | Review | Status |
|---|---:|---|---|---|---|---|
| Agent Architecture / SDLC | 15–20% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Tool Use / Environment | 20–25% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Memory / State / Execution | 10–15% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Evaluation / Error Analysis | 15–20% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Multi-Agent Coordination | 15–20% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Guardrails / Accountability | 10–15% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |

## 7-일차 추적 (7-Day Tracker, DT)

| Day | 목표 | 완료 | Score / Notes |
|---:|---|---|---|
| 1 | Architecture / SDLC / Planning | ⬜ | |
| 2 | Tools / MCP / Environment | ⬜ | |
| 3 | Memory / State / Execution | ⬜ | |
| 4 | Evaluation / Error Analysis | ⬜ | |
| 5 | Multi-Agent Coordination | ⬜ | |
| 6 | Guardrails / Accountability + QBank | ⬜ | |
| 7 | Mock / Final Review | ⬜ | |

상세 기록:

- [`010-daily-tracker.md`](./010-daily-tracker.md)
- [`020-readiness-gate.md`](./020-readiness-gate.md)
- [`030-score-log.md`](./030-score-log.md)

## 시험 Readiness Metrics (Exam Readiness Metrics, ERM)

| 지표 | 목표 | 현재 |
|---|---:|---:|
| 최신 공식 Study Guide 확인 | 100% | ⬜ |
| 핵심 용어 설명 | 90%+ | - |
| 실습 (Labs, LAB) | 80%+ | - |
| 연습문제 (Exercises, EXR) | 80%+ | - |
| QBank 1회차 | 80%+ | - |
| QBank 2회차 | 85%+ | - |
| Mock 01 | 85%+ | - |
| Mock 02 | 85%+ | - |
| 최종 모의고사 (Final Mock, FM) | 90%+ 권장 | - |
| 최근 오답 재시험 | 90%+ | - |
| Agentic SDLC Project | 80점+ | - |

## 콘텐츠 Gate 비교 시험 Gate (Content Gate vs Exam Gate, CGEG)

```text
CONTENT-READY
= 학습 자료가 준비됨

EXAM-READY
= 실제 학습·실습·문제풀이 기준을 통과함
```

두 상태를 같은 의미로 사용하지 않습니다.

## PASSED 비교 CLEAR (PASSED vs CLEAR, PASSEDCLEAR)

`PASSED`: GH-600 자격시험 합격

`CLEAR`:

- [ ] GH-600 PASS
- [ ] 핵심 Labs 완료
- [ ] Agentic SDLC Design Project 80점 이상
- [ ] Architecture / Tool / State / Evaluation / Multi-Agent / Guardrail Evidence 정리
- [ ] QBank / Mock / Retry 기록
- [ ] 최종 Reflection 완료

---
[← 120 Wrong Answers](../120-wrong-answers/README.md) · [다음: 140 Resources →](../140-resources/README.md)
