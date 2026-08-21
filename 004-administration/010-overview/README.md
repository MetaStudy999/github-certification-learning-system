# 010 Overview — GH-100 GitHub 관리 (GitHub Administration, GHADM / GH-100)

## 빠른 시작 (Quick Start, QS)

2026년 7월 GH-100은 크게 개정되었습니다. 이 과정은 오래된 관리자 기능 목록이 아니라 **현재 5개 Skill Area**를 기준으로 학습합니다.

## 측정 기술 (Skills Measured, SM) — July 2026

| # | Skill Area | 비중 |
|---:|---|---:|
| 1 | Manage GitHub identities and access | 15–20% |
| 2 | Administer GitHub Enterprise environment | 10–15% |
| 3 | Implement secure software development and compliance | 25–30% |
| 4 | Manage GitHub Actions | 20–25% |
| 5 | Monitor and optimize GitHub usage | 10–15% |

## 1. 식별과 접근 (Identities and Access, IA)

반드시 이해할 내용:

- Managed Users vs Personal Accounts
- SAML SSO / 2FA
- SCIM / Team Synchronization
- Identity Provider (IdP)
- Authentication vs Authorization
- Organization / Repository Roles
- Enterprise Teams
- Access Audit
- Policies / Rulesets / Roles

## 2. 엔터프라이즈 환경 (Enterprise Environment, EE)

- Admin이 해결할 문제 vs GitHub Support가 필요한 문제
- Support Bundle / Diagnostics
- Workflow / Branch / Review / Release Standards
- GHEC + EMU
- GHEC + Data Residency + EMU
- GHEC + Personal Accounts
- GHES
- Licensing / Billing / Consumption

## 3. 보안 Software 개발 and Compliance (Secure Software Development and Compliance, SSDC)

현재 가장 높은 비중입니다.

- Enterprise / Organization Policies
- Rulesets
- Security Posture / Data Protection
- Audit Logging / Reporting
- Vulnerability Alerts
- Secret Scanning
- CodeQL
- Dependabot
- Security Advisories
- Security Response Plan
- Personal Access Token (PAT)
- GitHub Apps / OAuth Apps
- API Rate Limits
- App Approval Policy

## 4. GitHub 액션 (GitHub Actions, GHACT / GH-200)

- Reuse of Actions / Workflows
- Organization Policies
- Runner Groups
- GitHub-hosted vs Self-hosted Runner
- IP Allow Lists
- Azure Private Networking
- Runner Performance
- Organization / Repository Secrets
- Third-party Vaults

## 5. 모니터링과 최적화 (Monitor and Optimize, MO)

- Audit Logs
- API Usage
- Diagnostics
- Adoption / Activity / Underused Features
- Metered Product Usage Reports
- License Optimization
- Resource / Cost Optimization

## 엔터프라이즈 관리 Thinking 모델 (Enterprise Admin Thinking Model, EATM)

```text
Requirement
→ Deployment Model
→ Identity
→ Access
→ Governance
→ Security
→ Automation
→ Operations
→ Audit / Cost
```

시험에서는 특정 기능의 존재 여부보다 **어떤 관리 문제에 어떤 Enterprise 기능과 정책을 적용하는가**가 중요합니다.

## 7일 단기 집중 과정 (7-Day Fast Track, 7DFT)

| Day | 핵심 학습 | 결과물 |
|---:|---|---|
| 1 | Identity / SSO / SCIM / IdP | Identity 비교표 |
| 2 | Roles / Teams / Policies / Rulesets | Access Matrix |
| 3 | Deployment / Licensing / Support | Deployment Decision Table |
| 4 | Security / Apps / PAT | Security Governance Map |
| 5 | Actions / Runners / Network / Secrets | Actions Admin Blueprint |
| 6 | Audit / Usage / Cost + QBank | Weakness Report |
| 7 | Mock / Final Review | Exam Gate |

## 버전 규칙 (Version Rule, VR)

- 시험 시작 전 Microsoft Learn GH-100 Study Guide의 `Skills measured as of`를 확인합니다.
- 2026년 7월 이전 자료는 **현재 범위와 대조한 뒤** 사용합니다.
- Preview 기능은 공식 Study Guide에 포함될 수 있으므로 시험 직전 공식 Docs를 확인합니다.

---
[← Administration 홈](../README.md) · [다음: 020 Terms →](../020-terms/README.md)
