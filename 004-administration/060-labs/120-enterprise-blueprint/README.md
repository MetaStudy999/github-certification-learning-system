# Lab 120 — Enterprise Administration Blueprint

## Objective

GH-100의 5개 Skill Area를 하나의 **Enterprise 운영 설계**로 통합합니다.

## Scenario

가상 회사 `ACME Digital`:

- 직원 800명
- 개발자 300명
- 여러 사업부 Organization 운영
- Cloud 우선
- 중앙 IdP 사용
- 일부 데이터에 지역 저장 요구
- 보안팀이 GHAS 정책 관리
- CI/CD가 사내 Network와 Cloud에 접근
- 외부 SaaS Integration 다수
- 비용·License 사용량을 분기별 최적화

## Phase 1 — Deployment

선택:

```text
GHEC + EMU
GHEC + Data Residency + EMU
GHEC + Personal Accounts
GHES
```

선택 근거:

- Identity
- Data Residency
- Operations
- Network
- Compliance
- Cost

## Phase 2 — Identity

```text
IdP:
SAML SSO:
2FA policy:
SCIM:
Team synchronization:
Joiner/Mover/Leaver:
```

## Phase 3 — Access / Governance

```text
Organizations:
Enterprise Teams:
Repository roles:
Privileged roles:
Access review:
Enterprise policies:
Rulesets:
```

## Phase 4 — Security

```text
Secret scanning:
CodeQL:
Dependabot:
Security advisories:
App approval:
PAT policy:
Security response plan:
Audit/reporting:
```

## Phase 5 — Actions

```text
Reusable workflows:
Allowed actions policy:
Runner groups:
GitHub-hosted runners:
Self-hosted runners:
Network boundaries:
Secrets:
Third-party vault:
```

## Phase 6 — Operations

```text
Admin triage:
GitHub Support escalation:
Diagnostics:
Audit log:
API monitoring:
Adoption metrics:
License usage:
Metered usage:
Cost optimization:
```

## Deliverables

- [ ] Deployment Decision Table
- [ ] Identity Lifecycle Diagram
- [ ] Role / Permission Matrix
- [ ] Security Governance Map
- [ ] Integration Approval Standard
- [ ] Actions / Runner Architecture
- [ ] Support / Incident Runbook
- [ ] Usage / Cost Dashboard Design

## Verify

5분 안에 다음을 설명합니다.

> “이 기업의 GitHub Enterprise를 왜 이 배포 모델로 선택했고, 사용자를 어떻게 인증·관리하며, Repository와 Actions를 어떻게 통제하고, 보안·운영·비용을 어떻게 지속적으로 관리하는가?”

---
[← Lab 110](../110-audit-usage-cost/README.md) · [Labs 홈](../README.md)
