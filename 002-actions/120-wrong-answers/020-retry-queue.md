# 020 Retry Queue — GH-200

## Active Queue

| ID | Domain | Error Code | +1 Day | +7 Day | Status |
|---|---|---|---|---|---|
|  |  |  |  |  | OPEN |

## Priority 규칙 (Priority Rule, PR)

1. 같은 개념을 2회 이상 틀린 문제
2. Workflow / Enterprise 고비중 Domain
3. Security / Runner 오답
4. Troubleshooting `FIRST` 판단 오류
5. 단순 Memory/YAML 실수

## Retry Result

| 상태 | 의미 |
|---|---|
| OPEN | 아직 교정 중 |
| RETRY-1 | +1일 재시험 완료 |
| RETRY-7 | +7일 재시험 완료 |
| FIXED | 두 재시험 통과 |

## 시험 Gate (Exam Gate, EG)

시험 전 `OPEN` 상태의 고위험 오답을 남기지 않습니다.

- 최근 오답 재시험: **90% 이상**
- `SECURITY`, `RUNNER`, `REUSE` 반복 오류: 관련 Lab 재수행 필수
