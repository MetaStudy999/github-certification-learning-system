# 005 GitHub Advanced Security

> **GitHub Advanced Security · GH-500**  
> GitHub Security Suites를 활용해 코드·자격증명·의존성 위험을 **예방 → 탐지 → 우선순위화 → 수정 → Governance**까지 관리하는 중급 보안 과정입니다.

## Quick Start

1. [`010-overview/`](./010-overview/)에서 **2026년 7월 크게 개정된 GH-500 시험 범위**를 확인합니다.
2. [`020-terms/`](./020-terms/)에서 Code Security, Secret Protection, Supply Chain Security, CodeQL, SARIF, SBOM 등 핵심 용어를 학습합니다.
3. [`030-concepts/`](./030-concepts/)에서 Secure SDLC와 GitHub Security Suites의 관계를 연결합니다.
4. [`040-official-docs/`](./040-official-docs/)의 Microsoft Learn GH-500 Study Guide를 시험 범위의 1차 기준으로 사용합니다.
5. [`060-labs/`](./060-labs/)에서 Secret Protection, Supply Chain, CodeQL, Security Operations, Administration을 실습합니다.
6. [`070-exercises/`](./070-exercises/) 50개 수행형 과제를 해결합니다.
7. [`080-question-bank/`](./080-question-bank/) Q001–Q100을 2회 풉니다.
8. [`110-mock-exams/`](./110-mock-exams/) 3회와 [`120-wrong-answers/`](./120-wrong-answers/) 재시험으로 준비도를 검증합니다.
9. [`130-progress/`](./130-progress/)와 [`150-evidence/`](./150-evidence/)에 실제 학습 결과를 기록합니다.

## Status

| 구분 | 상태 | 의미 |
|---|---|---|
| Content Status | **CONTENT-READY** | July 2026 범위 기반 학습·실습·평가 체계 구축 완료 |
| Learning Status | **PLANNED** | 실제 개인 학습 시작 전 |

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

> 2026년 7월에 시험 목표가 크게 개정되었으므로 오래된 `secret scanning / Dependabot / code scanning` 중심 자료만 사용하지 않습니다.

## Learning Architecture

```text
Secure SDLC
   ↓
Security Suites / Ecosystem
   ↓
Secret Protection
   ↓
Supply Chain Security
   ↓
Code Security / CodeQL
   ↓
Security Operations
   ↓
Administration / Governance
   ↓
Project + Mock + Evidence
```

## Directory Map

```text
005-advanced-security/
├── 010-overview/
├── 020-terms/
├── 030-concepts/
├── 040-official-docs/
├── 050-guides/
├── 060-labs/               # 12 Labs
├── 070-exercises/          # 50 tasks
├── 080-question-bank/      # Q001–Q100
├── 090-final-review/
├── 100-projects/
├── 110-mock-exams/         # 3 × 40 = 120
├── 120-wrong-answers/
├── 130-progress/
├── 140-resources/
└── 150-evidence/
```

## Assessment Volume

```text
Exercises       50
Question Bank  100
Mock Exams     120
-----------------
Exam-style self-authored questions: 220
```

## 7-Day Fast Track

| Day | 핵심 목표 |
|---:|---|
| 1 | Security Suites / Secure SDLC / Security Overview |
| 2 | Secret Protection / Push Protection / Custom Patterns |
| 3 | Supply Chain / Dependency Graph / Dependabot / SBOM |
| 4 | Code Security / CodeQL / SARIF / Default vs Advanced Setup |
| 5 | Security Operations / Campaigns / Prioritization / Remediation |
| 6 | Administration / Policies / Roles + QBank + Mock 01 |
| 7 | Mock 02 + Final Mock + Final Review + Exam Gate |

## 대표 프로젝트

**Secure SDLC Integration Project**

```text
Repository
→ Secret Prevention / Detection
→ Dependency / Supply Chain Security
→ CodeQL / Code Security
→ Pull Request Security Checks
→ Security Overview / Campaign
→ Triage / Remediation
→ Enterprise Policy / Evidence
```

## Exam Readiness Gate

- [ ] 최신 GH-500 Study Guide 확인
- [ ] 6개 Domain과 비중 설명 가능
- [ ] 핵심 Labs 80% 이상
- [ ] Exercises 80% 이상
- [ ] Question Bank 2회차 85% 이상
- [ ] 최근 Mock 2회 연속 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 최근 오답 재시험 90% 이상
- [ ] Secure SDLC Project 80점 이상 권장

## Official Baseline

- Microsoft Learn — Study guide for Exam GH-500  
  https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500
- Microsoft Learn — GitHub Advanced Security Certification  
  https://learn.microsoft.com/en-us/credentials/certifications/github-advanced-security/
- GitHub Learn — GitHub Advanced Security Certification  
  https://learn.github.com/certification/GHAS
- GitHub Docs — Security  
  https://docs.github.com/en/code-security

## Content Verification

[`150-evidence/090-content-verification.md`](./150-evidence/090-content-verification.md)에 구조·문항 수·범위 기준을 기록했습니다.

---

[← 004 GitHub Administration](../004-administration/README.md) · [다음: 006 Agentic AI Developer →](../006-agentic-ai-developer/README.md) · [통합 학습 시스템](../README.md)
