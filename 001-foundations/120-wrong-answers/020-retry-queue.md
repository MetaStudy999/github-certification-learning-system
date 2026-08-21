# 020 Retry Queue — 오답 재시험 대기열

오답을 다시 풀 시점을 관리합니다.

## Queue

| Priority | Question ID | Domain | Error Code | +1 Day | +7 Days | Status |
|---|---|---|---|---|---|---|
| HIGH |  |  |  |  |  | OPEN |
| MEDIUM |  |  |  |  |  | OPEN |
| LOW |  |  |  |  |  | OPEN |

## Priority 규칙

### HIGH
- 같은 개념을 2회 이상 틀림
- Git/GitHub Basics 고비중 영역 반복 오류
- Mock 02 또는 Final Mock에서 틀림

### MEDIUM
- Compare 또는 Scenario 유형 1회 오류
- 실습을 다시 하면 해결 가능한 오류

### LOW
- 단순 기억 실수
- 바로 수정되고 재발하지 않은 오류

## Retry Gate

```text
오답 등록
  ↓
+1 Day 재시험
  ↓
틀림? ── YES → 관련 개념 + Lab 재학습 → HIGH
  │
  NO
  ↓
+7 Days 재시험
  ↓
90%+ 유지
  ↓
CLOSED
```

시험 직전에는 `OPEN` 상태의 HIGH 항목이 남아 있지 않는 것을 목표로 합니다.
