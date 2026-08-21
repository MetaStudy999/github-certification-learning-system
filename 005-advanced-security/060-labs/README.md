# 060 Labs — GitHub Advanced Security 단계별 실습

## Lab Roadmap

| Level | Lab | 핵심 기술 |
|---:|---|---|
| 010 | Security Suites Overview | Security Overview / Suite 구조 |
| 020 | Secret Protection Basics | Secret Alert / Validity |
| 030 | Push Protection & Patterns | Push Protection / Custom Pattern |
| 040 | Dependency Graph & Alerts | Dependency Graph / Dependabot Alert |
| 050 | Dependency Review & SBOM | PR Review / SBOM |
| 060 | CodeQL Default Setup | Code Security / Default Setup |
| 070 | CodeQL Advanced & SARIF | Advanced Setup / SARIF |
| 080 | Alert Triage & Autofix | Triage / Dismissal / Autofix |
| 090 | Security Campaigns | Campaign / Prioritization |
| 100 | Security Policies & Roles | Policy / Role / Bypass |
| 110 | Enterprise Rollout | Default Config / Scale / API |
| 120 | Secure SDLC Integration | End-to-End 통합 프로젝트 |

## 공통 Lab 구조

```text
Objective
→ Threat / Risk
→ Concept
→ Safe Practice
→ Challenge
→ Verify
→ Evidence
```

## 안전 원칙

- 실제 유효 Secret을 Commit하지 않습니다.
- 의도적 취약 코드는 학습용 격리 Repository에서만 사용합니다.
- Production 보안 기능을 약화시키지 않습니다.
- Alert Dismissal 실습은 이유·Scope·Audit 관점을 포함합니다.

---
[← 050 Guides](../050-guides/README.md) · [Lab 010 시작 →](./010-security-suites-overview/README.md)
