# GitHub Certification Learning System

GitHub 공식 자격증 6종을 **기초 → 자동화 → AI 활용 → 운영 → 보안 → Agentic AI** 흐름으로 학습하고, 시험 준비·실습·점수·자격증·포트폴리오를 하나의 Repository에서 관리하는 통합 학습 시스템입니다.

## Quick Start

1. [`000-start-here/`](./000-start-here/)에서 전체 학습 방법과 6주 Fast Track을 확인합니다.
2. [`950-progress/`](./950-progress/)에서 Master Learning Dashboard를 확인합니다.
3. 장기 학습은 `001 → 002 → 003 → 004 → 005 → 006` 순으로 진행합니다.
4. 단기 취득 시에는 `001 → 003 → 002 → 004 → 005 → 006` Fast Track을 적용할 수 있습니다.
5. 각 과정에서 **용어 → 개념 → 공식 문서 → 실습 → 문제풀이 → 오답 → 모의고사 → Evidence** 순으로 진행합니다.
6. `CONTENT-READY`와 실제 `EXAM-READY`를 구분합니다.

## Certification Roadmap

| 코드 | 자격증 | 시험 코드 | Content Status | Learning Status |
|---:|---|---|---|---|
| 001 | [GitHub Foundations](./001-foundations/) | GH-900 | **CONTENT-READY** | READY |
| 002 | [GitHub Actions](./002-actions/) | GH-200 | **CONTENT-READY** | PLANNED |
| 003 | [GitHub Copilot](./003-copilot/) | GH-300 | **CONTENT-READY** | PLANNED |
| 004 | [GitHub Administration](./004-administration/) | GH-100 | **CONTENT-READY** | PLANNED |
| 005 | [GitHub Advanced Security](./005-advanced-security/) | GH-500 | **CONTENT-READY** | PLANNED |
| 006 | [GitHub Agentic AI Developer](./006-agentic-ai-developer/) | GH-600 | **CONTENT-READY** | PLANNED |

> 장기 역량 순서: **Foundations → Actions → Copilot → Administration → Advanced Security → Agentic AI Developer**

> 6주 Fast Track: **Foundations → Copilot → Actions → Administration → Advanced Security → Agentic AI Developer**

## System Control Tower

| 코드 | 공통 시스템 | 역할 |
|---:|---|---|
| 900 | [Glossary](./900-glossary/) | 6개 과정 통합 용어·약어·교차 개념 |
| 910 | [Question Bank](./910-question-bank/) | 600문항 통합 문제은행 Index |
| 920 | [Wrong Answers](./920-wrong-answers/) | Error Code·Retry 통합 관리 |
| 930 | [Mock Exams](./930-mock-exams/) | 720문항 Mock·Exam Gate |
| 940 | [Labs](./940-labs/) | 과정별 Lab·Verify 표준 |
| 950 | [Progress](./950-progress/) | Master Dashboard·Fast Track·시험 계획 |
| 960 | [Resources](./960-resources/) | 공식 자료·최신성 검증 |
| 970 | [Certificates](./970-certificates/) | 실제 자격 취득·Credential 기록 |
| 980 | [Portfolio](./980-portfolio/) | 6개 과정 누적 프로젝트·Capstone |

## Current Learning Content Scale

| 유형 | 현재 규모 |
|---|---:|
| Certification Courses | 6 |
| Question Bank | **600문항** |
| Mock Exams | **18회** |
| Mock Questions | **720문항** |
| 자체 시험형 콘텐츠 | **1,320문항** |
| Course Projects | 6 + Final Capstone |

> 문제는 모두 학습용 자체 제작이며 실제 시험 유출문제·복원문제·Brain Dump를 사용하지 않습니다.

## Content Status vs Learning Status

### Content Status

```text
BOOTSTRAPPED
→ BUILDING
→ CONTENT-READY
→ MAINTENANCE
```

### Learning Status

```text
PLANNED
→ READY
→ LEARNING
→ PRACTICING
→ REVIEWING
→ EXAM-READY
→ PASSED
→ CLEAR
```

`CONTENT-READY`는 학습 자료 구축 완료를 의미하고, `EXAM-READY`는 실제 학습자가 점수와 실습 Gate를 통과했다는 의미입니다.

## Learning Cycle

```text
시험 범위 확인
   ↓
필수 용어 / 개념
   ↓
공식 문서
   ↓
Labs / Exercises
   ↓
Question Bank
   ↓
Wrong Answer / Retry
   ↓
Mock Exams
   ↓
Exam Readiness Gate
   ↓
시험
   ↓
Project / Evidence
   ↓
PASSED → CLEAR
```

## Repository Structure

```text
github-certification-learning-system/
├── 000-start-here/
├── 001-foundations/
├── 002-actions/
├── 003-copilot/
├── 004-administration/
├── 005-advanced-security/
├── 006-agentic-ai-developer/
├── 900-glossary/
├── 910-question-bank/
├── 920-wrong-answers/
├── 930-mock-exams/
├── 940-labs/
├── 950-progress/
├── 960-resources/
├── 970-certificates/
├── 980-portfolio/
└── 990-archive/
```

## Standard Internal Course Structure

```text
010 Overview
020 Terms
030 Concepts
040 Official Docs
050 Guides
060 Labs
070 Exercises
080 Question Bank
090 Final Review
100 Projects
110 Mock Exams
120 Wrong Answers
130 Progress
140 Resources
150 Evidence
```

## Exam Readiness Gate

각 과정의 세부 기준이 우선이며 통합 기준은 다음과 같습니다.

- 공식 Study Guide 최신 범위 확인: 100%
- 핵심 용어 설명: 90% 이상
- 핵심 실습: 80% 이상
- Question Bank 2회차: 85% 이상
- 최근 오답 Retry: 90% 이상
- Minimum Mock Gate: 최근 2회 연속 85% 이상
- **Conservative Gate 권장:** Mock 01·Mock 02·Final Mock 모두 85% 이상 + Final Mock 90% 이상
- 대표 프로젝트: 80점 이상 권장

상세 정책: [`930-mock-exams/090-exam-readiness-policy.md`](./930-mock-exams/090-exam-readiness-policy.md)

## 6-Week Fast Track

| 주차 | 목표 자격증 |
|---:|---|
| Week 1 | GitHub Foundations |
| Week 2 | GitHub Copilot |
| Week 3 | GitHub Actions |
| Week 4 | GitHub Administration |
| Week 5 | GitHub Advanced Security |
| Week 6 | GitHub Agentic AI Developer |

통합 추적: [`950-progress/020-fast-track-dashboard.md`](./950-progress/020-fast-track-dashboard.md)

## 운영 원칙

- 모든 주요 디렉터리와 문서는 3자리 번호 체계를 사용합니다.
- 핵심 기술 용어는 영어 원문과 한국어 뜻을 함께 표기합니다.
- 공식 문서는 복제하지 않고 링크·핵심 요약·시험 포인트·연결 실습을 기록합니다.
- 실제 시험 유출문제나 Brain Dump를 사용하지 않습니다.
- 시험 합격(`PASSED`)과 실제 학습 완료(`CLEAR`)를 구분합니다.
- 실습 증거와 프로젝트 산출물은 재현 가능하도록 기록합니다.
- 빠르게 바뀌는 GitHub 기능은 학습 시작·시험 예약·응시 직전에 공식 Study Guide를 다시 검증합니다.

## Verification

- 6개 과정 콘텐츠 검증: [`000-start-here/090-system-verification.md`](./000-start-here/090-system-verification.md)
- 통합 Control Tower 검증: [`000-start-here/095-control-tower-verification.md`](./000-start-here/095-control-tower-verification.md)

## Current Phase

```text
001–006 Certification Content   COMPLETE
900–980 Shared Control Tower    COMPLETE
Repository System Verification PASS

NEXT
→ 001 Foundations 실제 학습 시작
→ Progress / Score / Evidence 누적
→ GH-900 Exam Readiness Gate
```

**Repository Content & Control Tower Phase: COMPLETE**
