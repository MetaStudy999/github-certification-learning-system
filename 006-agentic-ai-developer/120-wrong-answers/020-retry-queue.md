# GH-600 Retry Queue

| ID | Domain | Error Code | +1 Day | +7 Day | Final | Status |
|---|---|---|---|---|---|---|
| Example | Tool Use | TOOL | ⬜ | ⬜ | ⬜ | OPEN |

## 상태 (Status, S)

- `OPEN` — 복습 전
- `REVIEWED` — 원리 재학습 완료
- `RETRY-1` — +1일 재시험
- `RETRY-7` — +7일 재시험
- `CLOSED` — 기준 통과

## Gate

시험 전 최근 오답 재시험 **90% 이상**을 유지합니다.
