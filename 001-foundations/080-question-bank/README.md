# 080 Question Bank — 자체 문제은행

> 실제 시험 문항이나 Brain Dump를 복제하지 않습니다. 공식 GH-900 학습목표를 바탕으로 **자체 제작 문제**만 사용합니다.

## 빠른 시작 (Quick Start, QS)

문제 하나를 다음 구조로 학습합니다.

```text
문제
→ 내 답
→ 정답
→ 왜 정답인가
→ 왜 다른 선택지는 아닌가
→ 관련 개념 / Lab
→ 다시 풀기
```

## 100-질문 단계 (100-Question Phase, QP)

현재 문제은행은 **Q001–Q100**까지 구축되었습니다.

| 코드 | Set | 문제 | 핵심 영역 |
|---:|---|---:|---|
| 010 | [Basics](./010-basics/README.md) | Q001–Q010 | Git/GitHub 기본 |
| 020 | [Repositories & Compare](./020-repositories-compare/README.md) | Q011–Q020 | Repository, Clone/Fork, 문서 |
| 030 | [Collaboration & Scenario](./030-collaboration-scenario/README.md) | Q021–Q030 | Issue, PR, Review, GitHub Flow |
| 040 | [Modern Development & Projects](./040-modern-development-projects/README.md) | Q031–Q040 | Actions, Copilot, Codespaces, Projects |
| 050 | [Security, Admin & Community](./050-security-admin-community/README.md) | Q041–Q050 | 2FA, 권한, 보호, Open Source |
| 060 | [Git Workflow](./060-git-workflow/README.md) | Q051–Q060 | Git 명령·Branch·Remote |
| 070 | [Repository Governance](./070-repository-governance/README.md) | Q061–Q070 | 문서·권한·Ruleset·조직 |
| 080 | [Collaboration Scenarios](./080-collaboration-scenarios/README.md) | Q071–Q080 | Issue·PR·Review·Checks |
| 090 | [Products & Community](./090-products-community/README.md) | Q081–Q090 | Actions·Copilot·Codespaces·Community |
| 100 | [Mixed Gate](./100-mixed-gate/README.md) | Q091–Q100 | 전 범위 혼합 |

## 점수 기준

| 정답률 | 조치 |
|---:|---|
| 90–100% | Mock Exam 진행 |
| 80–89% | 오답만 재학습 후 Mock 진행 |
| 70–79% | 관련 Exercise + Lab 재수행 |
| 70% 미만 | Terms + Concepts부터 복습 |

### 100문제 Gate

- 1회차 목표: **80/100 이상**
- 2회차 목표: **85/100 이상**
- 최근 오답 재시험: **90% 이상**
- Compare 반복 오류: Confusion Matrix에 반영

## 문제 설계 원칙

- 정의 암기만 묻지 않습니다.
- 유사 기능의 차이를 비교합니다.
- 실제 협업 상황에서 어떤 기능을 선택할지 판단합니다.
- 보안 설정을 약화시키는 실습은 요구하지 않습니다.
- 실제 시험 문항을 수집하거나 재현하지 않습니다.

## Mock 연계

100문제 Gate를 통과하면 다음으로 이동합니다.

```text
Q001–Q100
  ↓
Mock 01 (40)
  ↓
Mock 02 (40)
  ↓
Final Mock (40)
  ↓
오답 재시험
  ↓
EXAM-READY
```

모의고사는 [`../110-mock-exams/`](../110-mock-exams/)에 구축되어 있습니다.

## 다음 확장

```text
100문제 [CURRENT]
  ↓
150문제
  ↓
200문제
```

단, 문제 수를 늘리기 전에 **100문제 + Mock 3회 + 오답 Cycle**을 먼저 수행합니다.

## 점수 기록

| 회차 | 정답 | 전체 | 정답률 | 약점 Domain | 다음 행동 |
|---:|---:|---:|---:|---|---|
| 1 |  | 100 |  |  |  |
| 2 |  | 100 |  |  |  |

---

[← 070 Exercises](../070-exercises/README.md) · [Q001 시작 →](./010-basics/README.md)
