# Lab 110 — Audit / Usage / Cost Optimization

## Objective

Audit Log, API Usage, Adoption, Metered Usage, License Consumption을 분석해 **운영 가시성과 비용 최적화**로 연결합니다.

## Concept

```text
Audit / API / Usage Data
        ↓
Who / What / How Much
        ↓
Adoption / Activity / Underuse
        ↓
License / Metered Product Analysis
        ↓
Policy / Capacity / License Decision
        ↓
Cost / Performance Optimization
```

## Practice 1 — Audit Questions

다음 사건이 발생했다고 가정합니다.

> 중요한 Organization Policy가 예상치 않게 변경되었다.

Audit Log에서 찾을 질문:

```text
Who?
What action?
When?
Which scope?
Source / actor context?
Related changes?
```

## Practice 2 — API Usage

Integration의 API 사용량이 급증합니다.

분석:

- 어떤 App/PAT가 호출하는가?
- 정상 Business Growth인가?
- Polling이 과도한가?
- Rate Limit 위험은?
- Cache/Webhook/Backoff 개선이 가능한가?

## Practice 3 — Adoption

가상 Report:

| Feature | Licensed Users | Active Users | Observation |
|---|---:|---:|---|
| Product A | 100 | 93 | |
| Product B | 100 | 28 | |
| Product C | 50 | 3 | |

단순히 Active가 적다고 즉시 제거하지 않고 다음을 확인합니다.

- Business need
- Seasonal use
- Training gap
- Technical blocker
- License assignment

## Practice 4 — Cost Optimization

```text
Usage report
→ Unused / underused resource
→ Owner 확인
→ Business need 확인
→ Rightsize / Remove / Reassign
→ Measure again
```

## Challenge

`비용 최적화 = 라이선스 수를 최대한 줄이는 것`이라는 주장에 반박하세요.

## Verify

- [ ] Audit Log와 Diagnostics 차이 설명
- [ ] API Usage 분석 질문 작성
- [ ] Adoption / Activity / Underuse 구분
- [ ] Metered Usage와 License Consumption 구분
- [ ] Cost와 Performance를 함께 최적화하는 절차 설명

---
[← Lab 100](../100-runners-networking-vaults/README.md) · [Lab 120 →](../120-enterprise-blueprint/README.md)
