# Lab 100 — Failure & Conflict Handling

## Objective

실패를 무한 재시도하지 않고 중단·재시도·복구·Escalation 조건을 설계합니다.

## Decision Table

| Situation | Retry | Resume | Stop | Escalate |
|---|---|---|---|---|
| Temporary tool error | | | | |
| Invalid input | | | | |
| Missing approval | | | | |
| Conflicting agent outputs | | | | |
| Repeated evaluation failure | | | | |

## 설계 항목

```text
Max attempts:
Timeout condition:
Checkpoint:
Backoff / wait concept:
Escalation owner:
Required evidence:
Safe final state:
```

## Verify

- [ ] Retry와 Resume 구분
- [ ] 무한 Loop 방지 조건
- [ ] 실패 후 안전한 상태 정의
- [ ] 사람이 개입해야 하는 조건 정의

[← 이전](../090-multi-agent-coordination/README.md) · [다음 →](../110-guardrails-accountability/README.md)
