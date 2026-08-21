# 130 Progress — GH-300 진행률 Dashboard

## 상태 (Status, S)

- 콘텐츠 상태 (Content Status, CS): **CONTENT-READY**
- 학습 상태 (Learning Status, LS): **PLANNED**

> 콘텐츠 구축 상태와 실제 학습 상태를 분리합니다. 문서가 완성되어도 실제로 공부하지 않았다면 Learning Status는 `PLANNED` 또는 `READY`입니다.

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

## Skill 영역 Progress — 2026-08-07 (Skill Area Progress — 2026-08-07, SAP)

| Skill Area | Weight | Theory | Lab | QBank | Review | Status |
|---|---:|---|---|---|---|---|
| Use GitHub Copilot responsibly | 15–20% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Use GitHub Copilot features | 25–30% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Understand data and architecture | 10–15% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Apply prompt engineering and context crafting | 10–15% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Improve developer productivity | 10–15% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| Configure privacy, exclusions, safeguards | 10–15% | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |

## 7일 단기 집중 과정 (7-Day Fast Track, 7DFT)

| Day | 목표 | 완료 | 점수/메모 |
|---:|---|---|---|
| 1 | Responsible AI + IDE / Chat / CLI | ⬜ | |
| 2 | Edits / Agent / MCP / Code Review / Spaces / Spark | ⬜ | |
| 3 | Data Flow / Architecture / LLM Limits | ⬜ | |
| 4 | Prompt Engineering / Context / Instructions | ⬜ | |
| 5 | Productivity / Testing / Privacy / Safeguards | ⬜ | |
| 6 | Exercises + QBank 100 + Mock 01 | ⬜ | |
| 7 | Mock 02 + Final Mock + Final Review | ⬜ | |

상세 기록: [`010-daily-tracker.md`](./010-daily-tracker.md)

## 시험 Readiness Metrics (Exam Readiness Metrics, ERM)

| 지표 | 목표 | 현재 |
|---|---:|---:|
| 최신 Study Guide 확인 | 100% | ⬜ |
| 핵심 용어 설명 | 90%+ | - |
| 실습 (Labs, LAB) | 80%+ | - |
| 연습문제 (Exercises, EXR) | 80%+ | - |
| QBank 1회차 | 80%+ | - |
| QBank 2회차 | 85%+ | - |
| 최근 Mock 2회 | 85%+ | - |
| 최종 모의고사 (Final Mock, FM) | 90%+ 권장 | - |
| 오답 재시험 | 90%+ | - |

상세 Gate: [`020-readiness-gate.md`](./020-readiness-gate.md)

점수 기록: [`030-score-log.md`](./030-score-log.md)

## 콘텐츠 Gate 비교 시험 Gate (Content Gate vs Exam Gate, CGEG)

```text
CONTENT-READY
= 학습 자료가 준비됨

EXAM-READY
= 사용자가 실제로 학습·실습·문제풀이 기준을 통과함
```

두 상태를 절대 같은 의미로 사용하지 않습니다.

## PASSED 비교 CLEAR (PASSED vs CLEAR, PASSEDCLEAR)

`PASSED`:

- GH-300 자격시험 합격

`CLEAR`:

- [ ] GH-300 PASS
- [ ] 핵심 Lab 완료
- [ ] AI-Assisted Development Project 완료
- [ ] Evidence 정리
- [ ] Agent / MCP / Privacy를 포함한 핵심 개념 설명 가능
- [ ] 최종 Reflection 완료

---
[← 120 Wrong Answers](../120-wrong-answers/README.md) · [다음: 140 Resources →](../140-resources/README.md)
