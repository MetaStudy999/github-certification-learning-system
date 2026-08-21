# 040 Actions Administration — 수행형 연습

> GitHub Actions를 Enterprise 관리자 관점에서 **정책·Runner·Network·Credential·Cost**로 관리하는 연습입니다.

## Exercises

1. Enterprise 전체에서 허용할 Action Source 정책을 설계하세요. GitHub 작성 Action, Marketplace, 내부 Action을 어떻게 구분할지 설명합니다.
2. 외부 Action을 태그가 아니라 Full Commit SHA로 고정하는 이유와 운영 부담을 설명하세요.
3. Organization A와 B가 서로 다른 Self-hosted Runner Group을 사용해야 합니다. 접근 Scope를 설계하세요.
4. 내부망 Resource에 접근해야 하는 Workflow를 위해 Self-hosted Runner를 사용할 때 네트워크와 보안 책임을 정리하세요.
5. Cloud 배포용 장기 Secret 대신 OIDC를 사용할 수 있는 구조를 설명하세요.
6. Third-party Vault를 GitHub Actions와 연동할 때 Secret 값이 Repository에 장기 저장되지 않도록 설계하세요.
7. Workflow가 지나치게 많은 권한을 가진 `GITHUB_TOKEN`을 사용합니다. 최소 권한으로 수정하는 절차를 설명하세요.
8. Actions 사용량이 급증했습니다. Runner, Artifact, Cache, Workflow 실행 빈도 관점에서 비용 원인을 분해하세요.
9. Enterprise에서 Actions를 일부 Organization에만 허용해야 합니다. 상위 정책과 하위 예외를 어떻게 설계할지 설명하세요.
10. Self-hosted Runner 장애가 반복됩니다. Health, Queue, Label, Network, Capacity 순으로 Troubleshooting 절차를 작성하세요.

## 답안 기준

```text
Requirement
→ Enterprise Policy
→ Organization / Repository Scope
→ Runner / Network / Credential
→ Security Risk
→ Cost / Operations
→ Audit / Verification
```

## 완료 기준

- [ ] 10개 Scenario 수행
- [ ] Hosted vs Self-hosted Runner 설명 가능
- [ ] OIDC / Secret / Vault 차이 설명 가능
- [ ] Actions 정책 상속과 예외 처리 설명 가능

---
[← 030 Security & Compliance](../030-security-compliance/README.md) · [다음: 050 Monitoring & Optimization →](../050-monitoring-optimization/README.md)
