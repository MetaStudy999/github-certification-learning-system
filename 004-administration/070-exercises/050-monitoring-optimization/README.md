# 050 Monitoring & Optimization — 수행형 연습

> GH-100의 **Monitor and optimize GitHub usage** 영역을 운영·감사·비용 관점에서 연습합니다.

## 연습문제 (Exercises, EXR)

1. Audit Log에서 SSO 설정 변경과 Team 권한 변경을 추적하는 조사 절차를 작성하세요.
2. Enterprise 사용량 보고에서 Actions, Packages, Codespaces 등 Metered Product 비용을 분리해서 분석하는 방법을 설명하세요.
3. 특정 Organization의 Actions 비용이 급증했습니다. 실행 횟수, Runner, Artifact, Cache, 실패 재실행 관점에서 원인을 분해하세요.
4. API Rate Limit 또는 자동화 과다 호출 문제가 의심됩니다. Usage와 Audit Evidence를 어떻게 확인할지 설명하세요.
5. Enterprise 운영 KPI를 설계하세요. 예: Active Users, License Utilization, Failed Workflows, Security Alerts, Cost Trend.
6. 사용하지 않는 License와 비활성 Account를 식별하고 정리하는 Lifecycle 절차를 설계하세요.
7. Support 요청 전 수집해야 할 Diagnostic Evidence를 나열하고 민감정보가 포함되지 않도록 하는 방법을 설명하세요.
8. 정책 변경 후 예상치 못한 Workflow 실패가 증가했습니다. 변경 시점과 Audit Log를 연결해 Rollback 판단 절차를 작성하세요.
9. Organization별 Repository 수와 사용량이 증가하고 있습니다. 표준화·Archive·Ownership 정책으로 관리 복잡도를 줄이는 방안을 작성하세요.
10. 월간 Enterprise Health Review 문서를 설계하세요. Security, Actions, Identity, Cost, Support 항목을 포함합니다.

## 답안 기준

```text
Signal
→ Data Source
→ Scope
→ Baseline / Trend
→ Root Cause Hypothesis
→ Corrective Action
→ Verification
```

## 완료 기준

- [ ] 10개 Scenario 수행
- [ ] Audit / Usage / Cost 데이터를 구분 가능
- [ ] 운영 지표와 실제 조치 연결 가능
- [ ] 민감정보를 진단자료에 노출하지 않음

---
[← 040 Actions Administration](../040-actions-administration/README.md) · [다음: 080 Question Bank →](../../080-question-bank/README.md)
