# 020 Retry Dashboard — 통합 재시험 관리

## 재도전 대기열 (Retry Queue, RQ)

| 날짜 | 과정 | 문제 ID | Error Code | +1일 | +7일 | 최근 결과 | 상태 |
|---|---|---|---|---|---|---:|---|
|  |  |  |  | ⬜ | ⬜ |  | OPEN |

## 상태 (Status, S)

```text
OPEN
→ REVIEWED
→ RETRY-1-PASS
→ RETRY-7-PASS
→ CLOSED
```

## 종료 통과 기준 (Close Gate, CG)

다음 조건을 모두 만족하면 오답을 `CLOSED`로 변경합니다.

- [ ] 정답을 맞혔다.
- [ ] 왜 정답인지 설명할 수 있다.
- [ ] 다른 선택지가 왜 덜 적절한지 설명할 수 있다.
- [ ] 관련 기능을 1문장으로 설명할 수 있다.
- [ ] 반복 오답이면 관련 Lab을 재수행했다.

## 통합 목표

시험 응시 전 최근 오답 Retry 정확도 **90% 이상**을 목표로 합니다.

---
[Wrong Answers Home](./README.md)