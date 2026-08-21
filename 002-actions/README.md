# 002 GitHub Actions

> **GitHub Actions · GH-200**  
> GitHub 자격증 학습 시스템의 두 번째 과정이며, Repository 이벤트를 **자동화 Workflow**로 연결하는 과정입니다.

## Quick Start

1. `010-overview/`에서 GH-200의 5개 Domain을 확인합니다.
2. `020-terms/`에서 Workflow, Event, Job, Step, Runner 등 핵심 용어를 익힙니다.
3. `030-concepts/`에서 Event → Workflow → Job → Step 구조를 연결합니다.
4. `040-official-docs/`의 공식 Study Guide와 GitHub Docs를 기준 자료로 사용합니다.
5. `060-labs/`에서 실제 YAML Workflow를 작성하고 실행합니다.
6. `070-exercises/`와 `080-question-bank/`로 Scenario 판단력을 강화합니다.
7. `110-mock-exams/`과 `120-wrong-answers/`로 시험 준비도를 검증합니다.
8. `130-progress/`와 `150-evidence/`에 실제 학습·실습 결과를 기록합니다.

## Status

| 구분 | 상태 | 의미 |
|---|---|---|
| Content Status | **CONTENT-READY** | 이론·실습·문제·Mock·Evidence 구조 구축 완료 |
| Learning Status | **PLANNED** | 실제 학습 시작 전 |

> `CONTENT-READY`와 실제 시험 준비 상태는 다릅니다. 실제 상태는 `130-progress/020-readiness-gate.md` 기준으로 판단합니다.

## Exam Snapshot

| 항목 | 내용 |
|---|---|
| 자격증 | GitHub Actions |
| 시험 | GH-200 |
| 수준 | Intermediate (중급) |
| 시험 시간 | 100분 |
| 응시 언어 | English, Spanish, Portuguese (Brazil), Korean, Japanese |
| 기준 응시료 | USD 99 (지역에 따라 달라질 수 있음) |
| 자격 유효기간 | 24개월 |
| 현재 학습 기준 | 2026-08-21 |

## Current Exam Domains

| Domain | 시험 비중 |
|---|---:|
| 1. Author and Manage Workflows | 20–25% |
| 2. Consume and Troubleshoot Workflows | 15–20% |
| 3. Author and Maintain Actions | 15–20% |
| 4. Manage GitHub Actions for the Enterprise | 20–25% |
| 5. Secure and Optimize Automation | 10–15% |

> 시험 범위는 변경될 수 있으므로 응시 직전 최신 공식 Study Guide를 다시 확인합니다.

## 핵심 구조

```text
Event / Trigger
      ↓
Workflow
      ↓
Job
      ↓
Runner
      ↓
Step
      ↓
Action / run command
      ↓
Artifact / Deployment / Result
```

## Content Inventory

| 구성 | 현재 콘텐츠 |
|---|---:|
| Labs | 10개 — 010~100 |
| Exercise | 6개 영역 / 60개 수행형 과제 |
| Question Bank | Q001–Q100 |
| Mock Exam | 3회 × 40문항 = 120문항 |
| 자체 문제 총량 | **220문항** |
| Final Review | Checklist / Confusion Matrix / Exam Strategy |
| Project | CI/CD Automation Integration Project |
| Wrong Answers | Error Log + Retry Queue |
| Progress | Daily Tracker + Readiness Gate + Score Log |
| Evidence | Environment / Workflow / Troubleshooting / Exam Reflection |

## 핵심 학습 영역

- Workflow YAML 구조
- Event / Trigger / `workflow_dispatch` / `workflow_call`
- Job / Step / Dependency / Conditional
- Context / Expression / Environment Variable
- Matrix / Service Container
- Cache / Artifact / Retention
- Reusable Workflow / Composite Action
- JavaScript Action / Docker Container Action
- GitHub-hosted Runner / Self-hosted Runner
- Secrets / Variables / Environments
- `GITHUB_TOKEN` / Permissions
- OIDC (OpenID Connect)
- Action version pinning / Full commit SHA
- Enterprise 정책 / Runner 관리
- Artifact Attestation / Provenance
- Workflow Troubleshooting / Logs

## Directory Map

```text
002-actions/
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
| 1 | Workflow / Event / Job / Step / Runner |
| 2 | Context / Expression / Variables / Secrets |
| 3 | Matrix / Service Containers / Cache / Artifact |
| 4 | Reusable Workflow / Composite·JS·Docker Actions |
| 5 | Enterprise Runner / Policy / Security / OIDC |
| 6 | Troubleshooting + Question Bank + Mock 01 |
| 7 | Mock 02 + Final Review + Exam Gate |

## Exam Readiness Gate

- [ ] 공식 Study Guide 최신 확인
- [ ] Lab 핵심 80% 이상 완료
- [ ] Exercise 6개 영역 80% 이상 설명
- [ ] Question Bank 1회차 80% 이상
- [ ] Question Bank 2회차 85% 이상
- [ ] Mock 최근 2회 연속 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 최근 오답 재시험 90% 이상
- [ ] CI/CD Project 80점 이상

## 대표 프로젝트

**GitHub Actions CI/CD Automation Project**

```text
Push / Pull Request
      ↓
CI Workflow
      ↓
Lint / Test
      ↓
Matrix
      ↓
Artifact
      ↓
Reusable Automation
      ↓
Security Controls
      ↓
Deployment Gate
```

Python 애플리케이션을 대상으로 Build → Test → Artifact → 선택적 Deploy 흐름을 구성하고, 보안·권한·재사용성·Troubleshooting까지 확인합니다.

## Official Baseline

- Microsoft Learn — GitHub Actions Certification  
  https://learn.microsoft.com/en-us/credentials/certifications/github-actions/
- Microsoft Learn — Study guide for Exam GH-200  
  https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200
- GitHub Learn — GitHub Actions Certification  
  https://learn.github.com/certification/ACTIONS
- GitHub Docs — GitHub Actions  
  https://docs.github.com/en/actions

---

[← 001 GitHub Foundations](../001-foundations/README.md) · [통합 학습 시스템](../README.md)
