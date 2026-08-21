# GH-500 재도전 대기열 (Retry Queue, RQ)

| ID | Domain | Error Code | +1 Day | +7 Day | Final | Status |
|---|---|---|---|---|---|---|
| Example | Secret Protection | SECRET | ⬜ | ⬜ | ⬜ | OPEN |

## 상태 (Status, S)

- `OPEN` — 복습 전
- `REVIEWED` — 개념 복습 완료
- `RETRY-1` — +1일 재시험 완료
- `RETRY-7` — +7일 재시험 완료
- `CLOSED` — 재시험 기준 통과

## 통과 기준 (Gate, GATE)

시험 전 최근 오답 재시험 **90% 이상**을 유지합니다.
