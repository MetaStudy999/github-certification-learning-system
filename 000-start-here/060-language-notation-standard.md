# 한글·영어·약어 표기 표준 (Korean-English-Abbreviation Notation Standard, KEA)

이 문서는 GitHub 자격증 통합 학습 시스템(GitHub Certification Learning System, GCLS)의 모든 Markdown 문서에 적용하는 공통 표기 기준입니다.

## 001 기본 원칙 (Basic Principles, BP)

문서에서 핵심 개념·학습 영역·상태·절차를 처음 소개할 때는 다음 순서를 사용합니다.

```text
한글 명칭 (English Full Name, ABBR)
```

예시:

```text
콘텐츠 상태 (Content Status, CS)
학습 상태 (Learning Status, LS)
문제은행 (Question Bank, QB)
모의고사 (Mock Exams, ME)
증빙 (Evidence, EVD)
```

같은 문서에서 두 번째 이후 등장할 때는 문맥이 명확하면 한글명 또는 약어만 사용할 수 있습니다.

## 002 공식 명칭 처리 (Official Name Handling, ONH)

GitHub 제품명·자격증명·시험 코드처럼 공식 영어 명칭이 중요한 경우에도 한국어 설명을 함께 제공합니다. 공식 명칭 자체를 임의로 변경한 것처럼 보이지 않도록 영어 원문을 보존합니다.

| 한글 설명 | 공식 영어 명칭 | GCLS 약어 | 시험 코드 |
|---|---|---|---|
| GitHub 기초 | GitHub Foundations | GHF | GH-900 |
| GitHub 액션 | GitHub Actions | GHACT | GH-200 |
| GitHub 코파일럿 | GitHub Copilot | GHCOP | GH-300 |
| GitHub 관리 | GitHub Administration | GHADM | GH-100 |
| GitHub 고급 보안 | GitHub Advanced Security | GHAS | GH-500 |
| GitHub 에이전틱 AI 개발자 | GitHub Agentic AI Developer | GHAI | GH-600 |

`GHF`, `GHACT`, `GHCOP`, `GHADM`, `GHAS`, `GHAI`는 GCLS 내부에서 사용하는 과정 식별 약어이며, `GH-900` 등의 시험 코드와 구분합니다.

문장이나 제목에서는 다음 형식을 사용합니다.

```text
GitHub 기초 (GitHub Foundations, GHF / GH-900)
```

## 003 표준 과정 영역 (Standard Course Areas, SCA)

| 번호 | 한글 | 영어 | GCLS 약어 |
|---:|---|---|---|
| 010 | 개요 | Overview | OVW |
| 020 | 용어 | Terms | TRM |
| 030 | 개념 | Concepts | CPT |
| 040 | 공식 문서 | Official Docs | ODC |
| 050 | 가이드 | Guides | GDE |
| 060 | 실습 | Labs | LAB |
| 070 | 연습문제 | Exercises | EXR |
| 080 | 문제은행 | Question Bank | QB |
| 090 | 최종 복습 | Final Review | FR |
| 100 | 프로젝트 | Projects | PRJ |
| 110 | 모의고사 | Mock Exams | ME |
| 120 | 오답 관리 | Wrong Answers | WA |
| 130 | 진행 현황 | Progress | PRG |
| 140 | 자료 | Resources | RES |
| 150 | 증빙 | Evidence | EVD |

위 약어 가운데 업계 표준 약어가 아닌 것은 **GCLS 내부 문서 탐색용 약어**입니다.

## 004 공통 운영 용어 (Common Operational Terms, COT)

| 한글 | 영어 | 약어 |
|---|---|---|
| 빠른 시작 | Quick Start | QS |
| 콘텐츠 상태 | Content Status | CS |
| 학습 상태 | Learning Status | LS |
| 자격증 로드맵 | Certification Roadmap | CR |
| 학습 아키텍처 | Learning Architecture | LA |
| 시험 준비도 통과 기준 | Exam Readiness Gate | ERG |
| 저장소 맵 | Repository Map | RM |
| 시스템 통합 관제 | System Control Tower | SCT |
| 검증 | Verification | VER |
| 최종 종합 프로젝트 | Final Capstone | FCAP |
| 학습 세션 | Study Session | SS |
| 점수 기록 | Score Log | SL |
| 일일 추적 | Daily Tracker | DT |
| 재도전 대기열 | Retry Queue | RQ |
| 오류 기록 | Error Log | EL |
| 포트폴리오 | Portfolio | PTF |

## 005 기술 용어 표기 (Technical Term Notation, TTN)

업계에서 널리 쓰는 공식 약어가 있으면 그 약어를 우선 사용합니다.

| 한글 | 영어 | 약어 |
|---|---|---|
| 지속적 통합 / 지속적 배포 | Continuous Integration / Continuous Delivery | CI/CD |
| 소프트웨어 개발 수명주기 | Software Development Life Cycle | SDLC |
| 모델 컨텍스트 프로토콜 | Model Context Protocol | MCP |
| 책임 있는 인공지능 | Responsible AI | RAI |
| 역할 기반 접근 제어 | Role-Based Access Control | RBAC |
| 싱글 사인온 | Single Sign-On | SSO |
| 오픈ID 연결 | OpenID Connect | OIDC |
| 소프트웨어 자재 명세서 | Software Bill of Materials | SBOM |
| 정적 분석 결과 교환 형식 | Static Analysis Results Interchange Format | SARIF |

## 006 번역하지 않는 항목 (Non-Translated Items, NTI)

다음 항목은 정확성과 재현성을 위해 원문을 유지합니다.

- 명령어와 소스 코드
- 파일·디렉터리 경로
- YAML / JSON 키
- API 이름과 파라미터
- URL
- GitHub 화면에서 실제로 클릭해야 하는 UI 라벨이 원문과 정확히 일치해야 하는 경우
- 공식 제품명·서비스명 자체
- `Q001`, `E010-01`, `GH-900`처럼 의미보다 식별 기능이 우선인 코드

이 경우 설명 문장에서 한국어 의미를 함께 제공하고, 코드 블록 내부는 원문을 보존합니다.

## 007 문서 작성 규칙 (Documentation Rules, DR)

새 문서를 만들거나 기존 문서를 수정할 때 다음 기준을 적용합니다.

1. 제목과 주요 섹션은 `한글 (English Full Name, ABBR)` 형식을 기본으로 사용합니다.
2. 약어는 첫 등장 시 반드시 영어 원문과 함께 설명합니다.
3. 공식 약어와 GCLS 내부 약어를 혼동하지 않습니다.
4. 명령어·코드·경로·URL을 임의 번역하지 않습니다.
5. 한국어만 읽어도 학습 흐름을 이해할 수 있어야 합니다.
6. 영어 원문을 함께 제공하여 공식 문서 검색이 가능해야 합니다.
7. 동일 용어는 Repository 전체에서 같은 번역과 약어를 사용합니다.
8. 표에 `한글 / 영어 / 약어` 열이 따로 있는 경우 각 열에는 해당 표현만 기록하여 중복 병기를 피합니다.

## 008 적용 범위 (Scope, SCP)

이 표준은 다음 영역 전체에 적용합니다.

```text
README.md
000-start-here/
001-foundations/
002-actions/
003-copilot/
004-administration/
005-advanced-security/
006-agentic-ai-developer/
900-glossary/
910-question-bank/
920-wrong-answers/
930-mock-exams/
940-labs/
950-progress/
960-resources/
970-certificates/
980-portfolio/
990-archive/
```

앞으로 생성되는 Markdown 문서도 동일한 기준을 사용합니다.

## 009 자동 점검 (Automated Audit, AA)

Repository는 다음 파일을 사용하여 표기 일관성을 유지합니다.

```text
scripts/normalize-language-notation.py
scripts/finalize-language-notation.py
.github/workflows/normalize-language-notation.yml
000-start-here/061-language-audit.md
```

자동 정규화는 문서 제목과 공통 학습 라벨을 중심으로 수행하며, 의미가 달라질 수 있는 코드·명령어·경로는 수정하지 않습니다.
