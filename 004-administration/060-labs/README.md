# 060 Labs — GitHub Administration 단계별 실습

## Quick Start

Enterprise 기능 중에는 실제 Enterprise License, IdP, GHES 또는 관리자 권한이 필요한 항목이 있습니다. 그런 경우 **실제 운영환경을 임의 변경하지 않고 Scenario / Decision Table / Sandbox 중심**으로 학습합니다.

## Lab Roadmap

| Level | Lab | 핵심 기술 |
|---:|---|---|
| 010 | [Identity Models](./010-identity-models/) | EMU / Personal Accounts / AuthN / AuthZ |
| 020 | [SAML / SCIM / Team Sync](./020-saml-scim-team-sync/) | SSO / 2FA / Provisioning / IdP |
| 030 | [Roles / Teams / Permissions](./030-roles-teams-permissions/) | Org / Repo Roles / Enterprise Teams / Audit |
| 040 | [Deployment / Licensing](./040-deployment-licensing/) | GHEC / Data Residency / GHES / Billing |
| 050 | [Support / Standards / Diagnostics](./050-support-standards-diagnostics/) | Admin vs Support / Bundles / Process Standards |
| 060 | [Security Policies / Rulesets](./060-security-policies-rulesets/) | Enterprise Policy / Rulesets / Data Protection |
| 070 | [Security Features / Response](./070-security-features-response/) | CodeQL / Secret Scanning / Dependabot / Advisories |
| 080 | [PAT / Apps / Integrations](./080-pat-apps-integrations/) | PAT / GitHub Apps / OAuth / Rate Limits |
| 090 | [Actions Governance](./090-actions-governance/) | Reuse / Policies / Secrets |
| 100 | [Runners / Networking / Vaults](./100-runners-networking-vaults/) | Runner Groups / IP / Private Network / Vault |
| 110 | [Audit / Usage / Cost](./110-audit-usage-cost/) | Audit / API / Adoption / Metered Usage |
| 120 | [Enterprise Blueprint](./120-enterprise-blueprint/) | 전체 통합 설계 |

## 공통 구조

```text
Objective
→ Concept
→ Scenario / Practice
→ Decision
→ Verify
→ Evidence
```

## 안전 원칙

- 실제 Enterprise Policy를 학습 목적으로 약화시키지 않습니다.
- 실제 SSO/SCIM 연결을 임의 변경하지 않습니다.
- 실제 PAT, Client Secret, Private Key를 Repository에 저장하지 않습니다.
- Production Runner를 실험용 Workflow에 연결하지 않습니다.
- 실제 Secret 값을 Evidence에 남기지 않습니다.
- GHES Support Bundle에 민감 정보가 포함될 수 있으므로 공개 Repository에 올리지 않습니다.

## 핵심 완료 기준

- [ ] Identity / Deployment Model Decision Table 작성
- [ ] Role / Permission Matrix 작성
- [ ] Security Governance Map 작성
- [ ] App/PAT 선택 근거 설명
- [ ] Actions / Runner / Network / Secret Blueprint 작성
- [ ] Audit / Usage / Cost Optimization Scenario 수행
- [ ] Enterprise Administration Blueprint 완성

---
[← 050 Guides](../050-guides/README.md) · [Lab 010 시작 →](./010-identity-models/README.md)
