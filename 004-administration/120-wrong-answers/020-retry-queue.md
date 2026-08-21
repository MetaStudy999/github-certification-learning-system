# GH-100 재도전 대기열 (Retry Queue, RQ)

| ID | Source | Skill Area | Error Code | +1 Day | +7 Day | Status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  | OPEN |

## 운영 규칙

1. 틀린 문제는 즉시 Queue에 넣습니다.
2. +1일에 다시 풀어 **이유까지 설명**합니다.
3. +7일에 무자료 재시험합니다.
4. 두 번 모두 맞고 관련 개념을 설명할 수 있을 때 `CLOSED`로 변경합니다.
5. 같은 Error Code가 3회 이상 반복되면 관련 Lab 전체를 재수행합니다.

## 반복 오류 Escalation

```text
1회 오류 → 개념 복습
2회 오류 → 관련 Lab
3회 오류 → Skill Area 전체 복습
4회 이상 → Mock 중단 후 기초 재학습
```

---
[← Wrong Answers](./README.md)
