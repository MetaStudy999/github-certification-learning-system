# 090 Final Review — GH-100 시험 직전 복습

## 핵심 비교

| A | B | 핵심 차이 |
|---|---|---|
| Authentication | Authorization | 신원 확인 vs 허용 행동 |
| SAML | SCIM | SSO 인증 vs 계정 Lifecycle |
| EMU | Personal Account | Enterprise 관리 Identity vs 개인 Identity |
| Enterprise | Organization | 최상위 Governance vs 협업·Repository 관리 단위 |
| Role | Permission | 역할 묶음 vs 실제 허용 작업 |
| Ruleset | Branch Protection | 중앙·유연한 규칙 체계 vs 기존 Branch 보호 방식 |
| GitHub App | OAuth App | 설치·세분화 권한 중심 vs 사용자 위임 중심 |
| GitHub-hosted Runner | Self-hosted Runner | GitHub 운영 vs 고객 운영 |
| Secret | OIDC | 장기/저장 Credential 가능 vs 단기 Federated Credential |
| Audit Log | Usage Report | 변경·행위 추적 vs 사용량·비용 분석 |
| GHEC | GHES | Cloud SaaS vs 고객 운영 Server |

## 5개 Skill Area 압축

1. **Identity & Access** — EMU, SAML, SCIM, Team, Role, Least Privilege
2. **Enterprise Environment** — GHEC/GHES, Data Residency, Deployment, Licensing, Support
3. **Security & Compliance** — Ruleset, GHAS, Secret/Code/Dependency Security, App/PAT Governance
4. **GitHub Actions Administration** — Policy, Runner Group, Network, OIDC, Vault, Cost
5. **Monitoring & Optimization** — Audit, API/Usage, License, Metered Product, Health, Cost

## 시험 Gate (Exam Gate, EG)

- [ ] 5개 Skill Area와 비중 설명 가능
- [ ] Enterprise / Organization / Repository Scope 구분 가능
- [ ] SAML / SCIM / EMU 설명 가능
- [ ] GHEC / GHES / Data Residency 구분 가능
- [ ] Ruleset / GHAS / App / PAT Governance 설명 가능
- [ ] Actions 정책 / Runner / OIDC / Vault 설명 가능
- [ ] Audit / Usage / Cost 분석 흐름 설명 가능
- [ ] Question Bank 2회차 85% 이상
- [ ] 최근 Mock 2회 연속 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 오답 재시험 90% 이상

## 시험 판단 순서

```text
Scope는 어디인가?
→ Identity / Security / Actions / Operations 중 어떤 영역인가?
→ 상위 Policy가 있는가?
→ 최소 권한인가?
→ 운영·감사 Evidence를 남길 수 있는가?
```

---
[← 080 Question Bank](../080-question-bank/README.md) · [다음: 100 Projects →](../100-projects/README.md)
