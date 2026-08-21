# 005 GitHub Advanced Security

> **GitHub Advanced Security · GH-500**  
> GitHub Security Suites를 활용해 코드·Secret·Dependency 위험을 **예방 → 탐지 → 우선순위화 → 수정 → Governance**까지 관리하는 중급 보안 과정입니다.

## Quick Start

1. [`010-overview/`](./010-overview/)에서 **2026년 7월 크게 개정된 GH-500 시험 범위**를 확인합니다.
2. [`020-terms/`](./020-terms/)에서 Code Security, Secret Protection, Supply Chain Security, CodeQL, SARIF, SBOM 등 핵심 용어를 학습합니다.
3. [`030-concepts/`](./030-concepts/)에서 Secure SDLC와 GitHub Security Suites의 관계를 연결합니다.
4. [`040-official-docs/`](./040-official-docs/)의 Microsoft Learn GH-500 Study Guide를 시험 범위의 1차 기준으로 사용합니다.
5. [`060-labs/`](./060-labs/)에서 Secret Protection, Dependency Security, CodeQL, Security Operations, Administration을 실습합니다.
6. [`070-exercises/`](./070-exercises/)와 [`080-question-bank/`](./080-question-bank/)로 Scenario 판단력을 강화합니다.
7. [`110-mock-exams/`](./110-mock-exams/)과 [`120-wrong-answers/`](./120-wrong-answers/)로 시험 준비도를 검증합니다.
8. [`130-progress/`](./130-progress/)와 [`150-evidence/`](./150-evidence/)에서 실제 학습 결과를 관리합니다.

## Status

| 구분 | 상태 | 의미 |
|---|---|---|
| Content Status | **BUILDING** | July 2026 개정 범위 기반 콘텐츠 구축 중 |
| Learning Status | **PLANNED** | 실제 학습 시작 전 |

## Exam Snapshot

| 항목 | 내용 |
|---|---|
| 자격증 | GitHub Advanced Security |
| 시험 | GH-500 |
| 수준 | Intermediate (중급) |
| 시험 시간 | 100분 |
| 응시 언어 | English, Spanish, Portuguese (Brazil), Korean, Japanese |
| 기준 응시료 | USD 99 (지역에 따라 다를 수 있음) |
| 자격 유효기간 | 24개월 |
| 현재 학습 기준 | **Skills measured as of July 2026** |

## Current Skills Measured — July 2026

| # | Domain | 시험 비중 |
|---:|---|---:|
| 1 | Describe GitHub Security suites, features, and ecosystem | 15–20% |
| 2 | Configure and use Secret Protection | 15–20% |
| 3 | Configure and use Supply Chain Security | 15–20% |
| 4 | Configure and use Code Security | 10–15% |
| 5 | Security Operations: best practices, prioritization, and remediation | 15–20% |
| 6 | GitHub Security Suites Administration | 10–15% |

> **중요:** 2026년 7월에 시험 목표가 크게 개정되었습니다. 오래된 `secret scanning`, `Dependabot`, `code scanning` 중심 분류만 사용하지 않고, 최신 **Secret Protection / Supply Chain Security / Code Security / Security Operations / Administration** 구조를 기준으로 학습합니다.

## 핵심 Architecture

```text
Secure SDLC
   ↓
GitHub Security Suites
│
├── Secret Protection
│   ├── Secret Detection
│   ├── Push Protection
│   ├── Validity Checks
│   ├── Custom Patterns
│   └── Alert Lifecycle / Bypass
│
├── Supply Chain Security
│   ├── Dependency Graph
│   ├── Dependabot Alerts
│   ├── Dependency Review
│   ├── Dependency Updates
│   └── SBOM
│
├── Code Security
│   ├── CodeQL
│   ├── Code Scanning
│   ├── SARIF
│   ├── Default / Advanced Setup
│   └── Autofix / Triage
│
├── Security Operations
│   ├── Security Overview
│   ├── Alert Prioritization
│   ├── Security Campaigns
│   ├── Remediation
│   └── CVE / CWE / Advisory
│
└── Administration
    ├── Enterprise / Organization Policies
    ├── Roles / Permissions
    ├── Rulesets / Exceptions
    ├── Default Configurations
    └── API / Automation at Scale
```

## Directory Map

```text
005-advanced-security/
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

## 7-Day Fast Track

| Day | 핵심 목표 |
|---:|---|
| 1 | Security Suites / Secure SDLC / Security Overview |
| 2 | Secret Protection / Push Protection / Custom Patterns |
| 3 | Supply Chain / Dependency Graph / Dependabot / SBOM |
| 4 | Code Security / CodeQL / SARIF / Default vs Advanced Setup |
| 5 | Security Operations / Campaigns / Prioritization / Remediation |
| 6 | Administration / Policies / Roles / Automation + QBank + Mock 01 |
| 7 | Mock 02 + Final Mock + Final Review + Exam Gate |

## 대표 프로젝트

**Secure SDLC Integration Project**

```text
Repository
   ↓
Secret Protection
   ↓
Dependency / Supply Chain Security
   ↓
CodeQL / Code Security
   ↓
Pull Request Security Checks
   ↓
Security Overview / Campaign
   ↓
Triage / Remediation
   ↓
Enterprise Policy / Evidence
```

## Exam Readiness Gate

- [ ] 최신 GH-500 Study Guide 확인
- [ ] 6개 Domain과 비중 설명 가능
- [ ] Secret Protection / Push Protection / Custom Pattern 설명 가능
- [ ] Dependency Graph / Dependabot / Dependency Review / SBOM 구분 가능
- [ ] CodeQL / SARIF / Default Setup / Advanced Setup 설명 가능
- [ ] CVE / CWE / Advisory / Campaign / Alert Triage 설명 가능
- [ ] Enterprise/Org Security Policy와 Role/Permission 설명 가능
- [ ] Question Bank 2회차 85% 이상
- [ ] 최근 Mock 2회 연속 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 최근 오답 재시험 90% 이상

## Official Baseline

- Microsoft Learn — Study guide for Exam GH-500  
  https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500
- Microsoft Learn — GitHub Advanced Security Certification  
  https://learn.microsoft.com/en-us/credentials/certifications/github-advanced-security/
- GitHub Learn — GitHub Advanced Security Certification  
  https://learn.github.com/certification/GHAS
- GitHub Docs — Security  
  https://docs.github.com/en/code-security

---

[← 004 GitHub Administration](../004-administration/README.md) · [통합 학습 시스템](../README.md)
