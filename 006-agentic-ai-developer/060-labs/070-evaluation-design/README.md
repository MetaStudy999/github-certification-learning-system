# Lab 070 — Evaluation Design

## Objective

Agent 결과를 감으로 판단하지 않고 명시적인 Evaluation 기준으로 평가합니다.

## Practice

다음 평가표를 설계합니다.

| Metric | Definition | Pass threshold | 증빙 (Evidence, EVD) |
|---|---|---:|---|
| Task success | | | |
| Correctness | | | |
| Safety / policy compliance | | | |
| Efficiency | | | |
| Human review quality | | | |

## Test Set 설계

- 정상 Scenario
- 모호한 입력
- 불완전한 Context
- Tool 실패
- 충돌하는 요구사항
- 중단 또는 Escalation이 필요한 Scenario

## Verify

- [ ] 성공률 하나만으로 평가하지 않는 이유 설명
- [ ] 평가 Dataset과 실제 운영 Monitoring 차이 설명
- [ ] 정성 평가와 정량 평가를 함께 설계

[← 이전](../060-memory-state-checkpoint/README.md) · [다음 →](../080-error-analysis-tuning/README.md)
