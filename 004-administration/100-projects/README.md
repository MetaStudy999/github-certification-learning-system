# 100 Projects — GitHub 관리 (GitHub Administration, GHADM / GH-100) 통합 프로젝트

## Project 001 — Enterprise Administration Blueprint

### 목표

가상의 기업 `AI-COMPANY`를 기준으로 GitHub Enterprise 운영 구조를 설계합니다.

```text
Business Requirements
      ↓
Identity Model
      ↓
Enterprise / Organization Structure
      ↓
Team / Role / Repository Access
      ↓
Security & Compliance Policies
      ↓
Actions Governance / Runners / Network
      ↓
Audit / Usage / Cost Monitoring
      ↓
Incident / Support / Change Management
      ↓
Evidence + Review
```

## Phase 1 — Identity & Access

- [ ] EMU 또는 Personal Account 기반 모델 선택 이유
- [ ] SAML SSO 설계
- [ ] SCIM Provisioning/Deprovisioning 설계
- [ ] Team / Role / Least Privilege Matrix
- [ ] 외부 협력사 접근 모델

## Phase 2 — Enterprise Environment

- [ ] GHEC / GHES / Hybrid 선택 이유
- [ ] Data Residency 요구사항
- [ ] Organization 구조
- [ ] License / Support / Upgrade 정책
- [ ] Backup / Recovery 또는 SaaS 책임 경계

## Phase 3 — Security & Compliance

- [ ] Repository Ruleset 정책
- [ ] GHAS 활성화 Scope
- [ ] Secret / Code / Dependency Security
- [ ] GitHub App / OAuth App / PAT Governance
- [ ] Break-glass / Exception Policy

## Phase 4 — GitHub 액션 (GitHub Actions, GHACT / GH-200) Administration

- [ ] Allowed Actions 정책
- [ ] Runner Group 설계
- [ ] Self-hosted Runner Hardening 책임
- [ ] Private Network 접근 구조
- [ ] OIDC / Vault / Secret 전략
- [ ] Usage / Cost Control

## Phase 5 — Monitoring & Operations

- [ ] Audit Log Review
- [ ] License Utilization
- [ ] Metered Product Usage
- [ ] Monthly Health Review
- [ ] Incident / Support Escalation
- [ ] Change Management

## 필수 산출물

```text
010-enterprise-architecture.md
020-identity-access-matrix.md
030-security-policy.md
040-actions-governance.md
050-monitoring-cost.md
060-incident-support.md
070-final-review.md
```

## 평가 기준

| 영역 | 배점 |
|---|---:|
| Identity & Access | 20 |
| Enterprise Environment | 15 |
| Security & Compliance | 25 |
| Actions Administration | 20 |
| Monitoring / Cost / Audit | 10 |
| Evidence / Explainability | 10 |
| **합계** | **100** |

**80점 이상:** PASS  
**90점 이상 + 재현 가능한 Evidence:** CLEAR 후보

---
[← 090 Final Review](../090-final-review/README.md) · [다음: 110 Mock Exams →](../110-mock-exams/README.md)
