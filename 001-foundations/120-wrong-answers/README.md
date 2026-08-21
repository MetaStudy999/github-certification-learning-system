# 120 Wrong Answers — 오답 시스템

## 목적

오답을 정답 암기로 끝내지 않고 **왜 틀렸는지 → 어떤 개념을 다시 배워야 하는지 → 어떤 실습으로 확인할지 → 언제 다시 풀지**까지 연결합니다.

## Quick Start

1. [`010-error-log-template.md`](./010-error-log-template.md)로 오답을 기록합니다.
2. [`020-retry-queue.md`](./020-retry-queue.md)에 재시험 일정을 등록합니다.
3. 관련 Terms / Concepts / Lab을 다시 확인합니다.
4. +1일, +7일 재시험을 진행합니다.
5. 최근 오답 재시험 90% 이상이면 Exam Gate 조건을 충족합니다.

## 오답 원인 코드

| 코드 | 의미 | 예시 |
|---|---|---|
| CONCEPT | 개념 부족 | Fork 목적을 몰랐다 |
| COMPARE | 유사 개념 혼동 | Fetch와 Pull을 혼동 |
| READING | 조건 해석 실패 | `FIRST` 조건을 놓침 |
| MEMORY | 기억 실패 | SECURITY 파일 목적을 잊음 |
| PRACTICE | 실습 부족 | Branch 흐름을 화면에서 못 찾음 |
| SCOPE | 시험 범위 연결 실패 | Actions를 너무 깊게 공부하고 기본 목적을 놓침 |

## 오답 복습 Cycle

```text
오답 발생
 ↓
원인 코드 지정
 ↓
개념 1문장 재정의
 ↓
공식문서 확인
 ↓
관련 Lab 1회 수행
 ↓
+1일 재시험
 ↓
+7일 재시험
 ↓
90%+ 유지
 ↓
CLOSED
```

## 우선순위

1. 같은 개념을 2회 이상 틀림
2. Mock 02 / Final Mock 오류
3. Git/GitHub Basics 고비중 영역
4. Compare 유형 반복 오류
5. Scenario 조건 해석 오류
6. 단순 Memory 오류

## Compare 오류 특별 처리

`COMPARE` 오류가 발생하면 [`../090-final-review/020-confusion-matrix.md`](../090-final-review/020-confusion-matrix.md)에 해당 비교 항목이 있는지 확인합니다.

없으면 새로운 비교 항목을 추가합니다.

## Exam Gate 연결

시험 전 다음을 목표로 합니다.

- [ ] HIGH Priority OPEN 항목 0개
- [ ] 최근 오답 재시험 90% 이상
- [ ] 같은 개념 2회 연속 정답
- [ ] Mock 최근 2회 연속 85% 이상

---

[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
