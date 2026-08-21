# 130 Progress — 진행률 Dashboard

> 이 디렉터리는 **콘텐츠 구축 상태(Content Status)** 와 **실제 학습 상태(Learning Status)** 를 분리해서 관리합니다.

## 빠른 시작 (Quick Start, QS)

1. [`010-daily-tracker.md`](./010-daily-tracker.md)에서 매일 학습량을 기록합니다.
2. [`020-readiness-gate.md`](./020-readiness-gate.md)에서 시험 응시 조건을 확인합니다.
3. [`030-score-log.md`](./030-score-log.md)에 문제은행과 Mock 점수를 누적합니다.
4. 실제 학습을 시작하기 전 상태는 `READY`로 유지합니다.

## 상태 (Status, S)

### 콘텐츠 상태 (Content Status, CS)

**CONTENT-READY** — Foundations 학습 콘텐츠의 1차 구축이 완료된 상태입니다.

### 학습 상태 (Learning Status, LS)

현재 실제 학습 상태: **READY**

```text
READY
→ LEARNING
→ PRACTICING
→ REVIEWING
→ EXAM-READY
→ PASSED
→ CLEAR
```

## 영역 Progress (Domain Progress, DP)

| Domain | Theory | Lab | Questions | Review | Status |
|---|---|---|---|---|---|
| 1. Git and GitHub basics | ⬜ | ⬜ | ⬜ | ⬜ | READY |
| 2. Repositories | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 3. Collaboration | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 4. Modern development | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 5. Projects | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 6. Privacy/Security/Admin | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |
| 7. Community | ⬜ | ⬜ | ⬜ | ⬜ | PLANNED |

## 7-일차 Fast Track 추적 (7-Day Fast Track Tracker, DFTT)

| Day | 목표 | 완료 | 점수/메모 |
|---:|---|---|---|
| 1 | Domain 1 + Git Basics Lab | ⬜ | |
| 2 | Repository + Remote/Branch Lab | ⬜ | |
| 3 | Collaboration + GitHub Flow | ⬜ | |
| 4 | Modern Development + Projects | ⬜ | |
| 5 | Security/Admin + Community | ⬜ | |
| 6 | Question Bank + Mock 1 | ⬜ | |
| 7 | Mock 2 + Final Review | ⬜ | |

## 시험 Readiness Metrics (Exam Readiness Metrics, ERM)

| 지표 | 목표 | 현재 |
|---|---:|---:|
| 공식 학습자료 | 100% | 0% |
| 필수 용어 | 90%+ | 0% |
| 핵심 Lab | 80%+ | 0% |
| 문제은행 Q001–Q100 | 80%+ | - |
| Mock 최근 2회 | 85%+ | - |
| 최종 모의고사 (Final Mock, FM) | 90%+ 권장 | - |
| 오답 재시험 | 90%+ | - |

> 위의 `0%`와 `-`는 **콘텐츠가 없다는 뜻이 아니라 아직 실제 학습 결과를 입력하지 않았다는 뜻**입니다.

## CLEAR 기준

`PASSED`는 GH-900 시험 합격 상태입니다. `CLEAR`는 다음을 모두 만족할 때 사용합니다.

- [ ] GH-900 합격
- [ ] 핵심 Lab 완료
- [ ] Foundations 통합 Project 80점 이상
- [ ] Evidence 정리
- [ ] 문제은행 및 Mock 기록 보존
- [ ] 핵심 개념을 다른 사람에게 설명 가능
- [ ] 다음 과정(002 Actions)으로 전달할 선수지식 정리

---

[← 120 Wrong Answers](../120-wrong-answers/README.md) · [Daily Tracker →](./010-daily-tracker.md) · [다음: 140 Resources →](../140-resources/README.md)
