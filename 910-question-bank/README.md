# 910 Question Bank — 통합 문제은행 Control Tower

6개 자격증의 자체 문제은행을 한 곳에서 탐색하고 점수 기준을 통일합니다. 실제 시험 문항·복원문제·Brain Dump는 사용하지 않습니다.

## Quick Start

1. [`010-question-bank-index.md`](./010-question-bank-index.md)에서 과정별 문제은행으로 이동합니다.
2. 각 과정의 100문제를 1회 풀고 80% 이상을 목표로 합니다.
3. 2회차에서 85% 이상을 확보합니다.
4. 틀린 문제는 [`../920-wrong-answers/`](../920-wrong-answers/)의 통합 오답 Cycle로 보냅니다.
5. 이후 [`../930-mock-exams/`](../930-mock-exams/)로 이동합니다.

## Current Scale

| 과정 | 시험 | Question Bank |
|---|---|---:|
| 001 Foundations | GH-900 | 100 |
| 002 Actions | GH-200 | 100 |
| 003 Copilot | GH-300 | 100 |
| 004 Administration | GH-100 | 100 |
| 005 Advanced Security | GH-500 | 100 |
| 006 Agentic AI Developer | GH-600 | 100 |
| **합계** |  | **600** |

## Standard Question Cycle

```text
Scenario / Question
→ My Answer
→ Correct Answer
→ Why Correct
→ Why Alternatives Are Less Appropriate
→ Domain / Keyword
→ Official Documentation
→ Related Lab
→ Wrong-Answer Classification
→ Retry
```

## Common Gate

| 단계 | 기준 |
|---|---:|
| QBank 1회차 | 80%+ |
| QBank 2회차 | 85%+ |
| 최근 오답 재시험 | 90%+ |

## 문항 작성 원칙

- 정의 암기보다 **Scenario 판단과 비교**를 우선합니다.
- `BEST`, `FIRST`, `MOST appropriate` 유형을 사용하되 실제 시험 문제를 모사하지 않습니다.
- 정답뿐 아니라 다른 선택지가 덜 적절한 이유를 남깁니다.
- 기능이 빠르게 변하는 항목은 공식 Study Guide와 Docs로 재검증합니다.
- 보안 설정 약화, 실제 Secret 사용, 운영 환경의 위험한 변경을 학습 정답으로 요구하지 않습니다.

## Supporting Docs

- [`010-question-bank-index.md`](./010-question-bank-index.md) — 6개 과정 문제은행 바로가기
- [`020-question-design-standard.md`](./020-question-design-standard.md) — 자체 문제 작성 표준
- [`090-study-cycle.md`](./090-study-cycle.md) — QBank → 오답 → Mock 전환 절차

---
[통합 README](../README.md)