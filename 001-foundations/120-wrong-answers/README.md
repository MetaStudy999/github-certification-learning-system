# 120 Wrong Answers — 오답 시스템

## 목적

오답을 정답 암기로 끝내지 않고 **왜 틀렸는지 → 어떤 개념을 다시 배워야 하는지 → 어떤 실습으로 확인할지** 연결합니다.

## 오답 원인 코드

| 코드 | 의미 | 예시 |
|---|---|---|
| CONCEPT | 개념 부족 | Fork 목적을 몰랐다 |
| COMPARE | 유사 개념 혼동 | Fetch와 Pull을 혼동 |
| READING | 조건 해석 실패 | `FIRST` 조건을 놓침 |
| MEMORY | 기억 실패 | SECURITY 파일 목적을 잊음 |
| PRACTICE | 실습 부족 | Branch 흐름을 화면에서 못 찾음 |
| SCOPE | 시험 범위 연결 실패 | Actions를 너무 깊게 공부하고 기본 목적을 놓침 |

## 한 문제 처리 Template

```text
ID:
Domain:
Question summary:
My answer:
Correct answer:
Error code:
Why I was wrong:
Correct concept in one sentence:
Why alternatives are wrong:
Official source:
Related lab:
Retry date:
Retry result:
```

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
24시간 뒤 재문제
 ↓
7일 뒤 다시 확인
```

## 우선순위

다음 순서로 먼저 고칩니다.

1. 같은 개념을 2회 이상 틀림
2. Domain 1 고비중 영역
3. Compare 유형 반복 오류
4. Scenario 문제의 조건 해석 오류
5. 단순 Memory 오류

## Exam Gate 연결

시험 전 최근 오답 재시험에서 **90% 이상**을 목표로 합니다.

---

[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
