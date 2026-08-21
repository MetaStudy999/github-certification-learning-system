# 004 GitHub Administration

> **GitHub Administration · GH-100**  
> GitHub Enterprise 환경의 **Identity, Governance, Secure Software Development, Actions, Usage/Cost**를 관리하는 중급 과정입니다.

## Quick Start

1. [`010-overview/`](./010-overview/)에서 **2026년 7월 크게 개정된 GH-100 시험 범위**를 확인합니다.
2. [`020-terms/`](./020-terms/)에서 GHEC, GHES, EMU, SAML SSO, SCIM, IdP 등 핵심 용어를 학습합니다.
3. [`030-concepts/`](./030-concepts/)에서 Enterprise → Organization → Team → Repository → User와 인증·권한 구조를 연결합니다.
4. [`040-official-docs/`](./040-official-docs/)의 Microsoft Learn GH-100 Study Guide를 시험 범위의 1차 기준으로 사용합니다.
5. [`060-labs/`](./060-labs/)에서 Identity, Deployment, Security, Apps, Actions, Runner, Audit, Cost를 Scenario 기반으로 실습합니다.
6. [`070-exercises/`](./070-exercises/)와 [`080-question-bank/`](./080-question-bank/)로 Enterprise 판단력을 강화합니다.
7. [`110-mock-exams/`](./110-mock-exams/)과 [`120-wrong-answers/`](./120-wrong-answers/)로 시험 준비도를 검증합니다.
8. [`130-progress/`](./130-progress/)와 [`150-evidence/`](./150-evidence/)에서 학습 결과를 관리합니다.

## Status

| 구분 | 상태 | 의미 |
|---|---|---|
| Content Status | **CONTENT-READY** | 최신 범위 기반 1차 학습·실습·문제·Mock 체계 구축 완료 |
| Learning Status | **PLANNED** | 실제 학습 시작 전 |

## Exam Snapshot

| 항목 | 내용 |
|---|---|
| 자격증 | GitHub Administration |
| 시험 | GH-100 |
| 수준 | Intermediate (중급) |
| 시험 시간 | 100분 |
| 현재 Microsoft Learn 표시 언어 | English |
| 기준 응시료 | USD 99 (지역별 가격이 다를 수 있음) |
| 현재 학습 기준 | **Skills measured as of July 2026** |

> 언어 표시는 GitHub Learn과 Microsoft Learn 사이에 차이가 생길 수 있습니다. 실제 응시 가능 언어는 **시험 예약 시점의 Pearson VUE / Microsoft Learn 화면을 최종 기준**으로 확인합니다.

## Current Skills Measured — July 2026

| # | Skill Area | 시험 비중 |
|---:|---|---:|
| 1 | Manage GitHub identities and access | 15–20% |
| 2 | Administer GitHub Enterprise environment | 10–15% |
| 3 | Implement secure software development and compliance | 25–30% |
| 4 | Manage GitHub Actions | 20–25% |
| 5 | Monitor and optimize GitHub usage | 10–15% |

> **중요:** 공식 Study Guide는 2026년 7월에 시험이 크게 변경되었다고 명시합니다. 오래된 GH-100 자료의 Domain 구성을 그대로 사용하지 않습니다.

## 핵심 Architecture

```text
GitHub Enterprise
│
├── Identity / Authentication
│   ├── Personal accounts
│   ├── Enterprise Managed Users (EMU)
│   ├── SAML SSO / 2FA
│   ├── SCIM / Team Synchronization
│   └── Identity Provider (IdP)
│
├── Governance
│   ├── Organizations
│   ├── Enterprise Teams
│   ├── Roles / Permissions
│   ├── Policies
│   └── Rulesets
│
├── Secure Software Development
│   ├── Vulnerability Alerts
│   ├── Secret Scanning
│   ├── CodeQL
│   ├── Dependabot
│   ├── Security Advisories
│   ├── PAT / GitHub Apps / OAuth Apps
│   └── Security Response Plan
│
├── GitHub Actions
│   ├── Reusable Actions / Workflows
│   ├── Enterprise / Org Policies
│   ├── Runner Groups
│   ├── GitHub-hosted / Self-hosted
│   ├── Networking / IP Allow Lists
│   └── Secrets / Third-party Vaults
│
└── Operations
    ├── Audit Log / API Usage
    ├── Support Bundles / Diagnostics
    ├── Adoption / Activity
    ├── Metered Usage
    └── License / Resource Optimization
```

## Deployment Models to Distinguish

```text
GitHub Enterprise Cloud + EMU
GitHub Enterprise Cloud + Data Residency + EMU
GitHub Enterprise Cloud + Personal Accounts
GitHub Enterprise Server (GHES)
```

각 모델의 **Identity, Data Location, Administration, Support, Upgrade/Operations 책임** 차이를 비교합니다.

## Directory Map

```text
004-administration/
├── 010-overview/
├── 020-terms/
├── 030-concepts/
├── 040-official-docs/
├── 050-guides/
├── 060-labs/
├── 070-exercises/
├── 080-question-bank/
├── 090-final-review/
├── 100-projects/
├── 110-mock-exams/
├── 120-wrong-answers/
├── 130-progress/
├── 140-resources/
└── 150-evidence/
```

## Content Build Summary

| 항목 | 구축 상태 |
|---|---:|
| Labs | 12개 |
| Exercises | 50개 |
| Question Bank | 100문제 |
| Mock Exams | 3회 × 40문항 |
| 자체 문제 총계 | **220문항** |
| Final Review | 완료 |
| Enterprise Blueprint | 완료 |
| Wrong Answer / Retry | 완료 |
| Progress / Gate | 완료 |
| Evidence | 완료 |

## 7-Day Fast Track

| Day | 핵심 목표 |
|---:|---|
| 1 | Identity / Accounts / SAML SSO / 2FA / SCIM / IdP |
| 2 | Roles / Permissions / Enterprise Teams / Policies / Rulesets |
| 3 | Deployment / GHES / GHEC / EMU / Data Residency / Licensing / Support |
| 4 | Security / CodeQL / Secret Scanning / Dependabot / Apps / PAT |
| 5 | Actions / Runner Groups / Networking / Secrets / Vaults |
| 6 | Audit / Diagnostics / Usage / Cost + QBank + Mock 01 |
| 7 | Mock 02 + Final Mock + Final Review + Exam Gate |

## 대표 프로젝트

**Enterprise Administration Blueprint**

```text
Business / Compliance Requirements
        ↓
Deployment Model
        ↓
Identity / IdP / SSO / Provisioning
        ↓
Enterprise / Organization / Teams
        ↓
Roles / Permissions / Rulesets
        ↓
Security Policy / Apps / PAT
        ↓
Actions / Runners / Network / Secrets
        ↓
Audit / Support / Usage / Cost
        ↓
Operational Runbook
```

## Exam Readiness Gate

- [ ] 최신 GH-100 Study Guide 확인
- [ ] 5개 Skill Area와 비중 설명 가능
- [ ] EMU / Personal Account, SAML / SCIM / Team Sync 구분 가능
- [ ] GHEC / Data Residency / GHES Deployment 차이 설명 가능
- [ ] Security Policy / CodeQL / Secret Scanning / Dependabot 관리 설명 가능
- [ ] PAT / GitHub App / OAuth App 구분 가능
- [ ] Runner / Networking / Secrets / Vault 관리 설명 가능
- [ ] Audit / Support / Diagnostics / Usage / Cost 최적화 설명 가능
- [ ] Question Bank 2회차 85% 이상
- [ ] 최근 Mock 2회 연속 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 최근 오답 재시험 90% 이상

## Official Baseline

- Microsoft Learn — Study guide for Exam GH-100  
  https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100
- Microsoft Learn — GitHub Administration Certification  
  https://learn.microsoft.com/en-us/credentials/certifications/github-administration/
- GitHub Learn — GitHub Administration Certification  
  https://learn.github.com/credentials
- GitHub Docs — Enterprise Cloud  
  https://docs.github.com/en/enterprise-cloud@latest/admin
- GitHub Docs — Enterprise Server  
  https://docs.github.com/en/enterprise-server@latest/admin

---

[← 003 GitHub Copilot](../003-copilot/README.md) · [통합 학습 시스템](../README.md)
