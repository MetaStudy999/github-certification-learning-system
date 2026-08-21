# 090 콘텐츠 검증 (Content Verification, CV) — 003 GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300)

**검증일 (Verification Date, VD):** 2026-08-21  
**과정 (Course, CRS):** GH-300 GitHub Copilot

## 1. 공식 범위 기준선 (Official Scope Baseline, OSB)

- [x] Microsoft Learn GH-300 학습 가이드 (Study Guide, SG) 확인
- [x] `Skills measured as of 2026-08-07` 기준 반영
- [x] 현재 6개 기술 영역 (Skill Area, SA) 반영
- [x] 이전 7개 영역 (Domain, DOM) 비중을 현재 시험 기준으로 사용하지 않도록 수정
- [x] GitHub Learn과 Microsoft Learn의 표시 차이가 있을 경우 Microsoft Learn 최신 Study Guide 우선 원칙 기록

## 2. 표준 과정 구조 (Standard Course Structure, SCS)

- [x] 010 개요 (Overview, OVW)
- [x] 020 용어 (Terms, TRM)
- [x] 030 개념 (Concepts, CPT)
- [x] 040 공식 문서 (Official Docs, ODC)
- [x] 050 가이드 (Guides, GDE)
- [x] 060 실습 (Labs, LAB)
- [x] 070 연습문제 (Exercises, EXR)
- [x] 080 문제은행 (Question Bank, QB)
- [x] 090 최종 복습 (Final Review, FR)
- [x] 100 프로젝트 (Projects, PRJ)
- [x] 110 모의고사 (Mock Exams, ME)
- [x] 120 오답 관리 (Wrong Answers, WA)
- [x] 130 진행 현황 (Progress, PRG)
- [x] 140 자료 (Resources, RES)
- [x] 150 증빙 (Evidence, EVD)

## 3. 현재 기능 범위 (Current-Feature Coverage, CFC)

- [x] 통합 개발 환경 / 인라인 제안 / 채팅 (IDE / Inline Suggestion / Chat, ISC)
- [x] Copilot 편집 (Copilot Edits, CE)
- [x] Copilot 명령줄 인터페이스 (Copilot CLI, CCLI)
- [x] 에이전트 모드 (Agent Mode, AM)
- [x] 에이전트 세션 / 하위 에이전트 (Agent Sessions / Sub-Agents, ASA)
- [x] 모델 컨텍스트 프로토콜 (Model Context Protocol, MCP)
- [x] Copilot 코드 리뷰 / PR 요약 (Copilot Code Review / PR Summary, CRPS)
- [x] 지침 / 프롬프트 파일 (Instructions / Prompt Files, IPF)
- [x] Spaces
- [x] Spark
- [x] 조직 정책 / 감사 로그 / REST API (Organization Policy / Audit Log / REST API, OAR)
- [x] 데이터 흐름 / 프롬프트 구성 / 필터링 / 후처리 (Data Flow / Prompt Building / Filtering / Post-processing, DFPF)
- [x] 프롬프트 엔지니어링 / 컨텍스트 구성 (Prompt Engineering / Context Crafting, PECC)
- [x] 테스트 / 보안 / 성능 (Testing / Security / Performance, TSP)
- [x] 콘텐츠 제외 / 공개 코드 일치 안전장치 (Content Exclusion / Public Code Matching Safeguard, CEPS)

## 4. 실습 (Labs, LAB)

현재 실습 로드맵 (Lab Roadmap, LR):

```text
010–100  기존 핵심 Copilot 개발 워크플로 (Development Workflow, DW)
110      Copilot CLI / Agent Mode / MCP
120      Code Review / Organization Policy
130      Spaces / Spark / Instructions / Prompt Files
```

- [x] 총 13개 실습 (Lab, LAB) 디렉터리 구성
- [x] Agent/MCP 최소 권한 원칙 포함
- [x] Secret / PII 미노출 원칙 포함
- [x] 사람 검토 / 테스트 검증 (Human Review / Test Verification, HRTV) 포함

## 5. 연습문제 (Exercises, EXR)

- [x] 책임 있는 AI (Responsible AI, RAI) — 10
- [x] Copilot 기능 (Copilot Features, CF) — 10
- [x] 데이터 / 아키텍처 (Data / Architecture, DA) — 10
- [x] 프롬프트 / 컨텍스트 (Prompt / Context, PC) — 10
- [x] 개발자 생산성 (Developer Productivity, DP) — 10
- [x] 개인정보 보호 / 안전장치 (Privacy / Safeguards, PS) — 10

**총 수행형 연습문제 (Exercise, EXR): 60개**

## 6. 문제은행 (Question Bank, QB)

- [x] Q001–Q010 책임 있는 AI (Responsible AI, RAI)
- [x] Q011–Q020 IDE / CLI
- [x] Q021–Q030 에이전트 / 고급 기능 (Agent / Advanced Features, AAF)
- [x] Q031–Q040 조직 / 거버넌스 (Organization / Governance, OG)
- [x] Q041–Q050 데이터 / 아키텍처 (Data / Architecture, DA)
- [x] Q051–Q060 프롬프트 / 컨텍스트 (Prompt / Context, PC)
- [x] Q061–Q070 개발자 생산성 (Developer Productivity, DP)
- [x] Q071–Q080 테스트 / 보안 / 성능 (Testing / Security / Performance, TSP)
- [x] Q081–Q090 개인정보 보호 / 안전장치 (Privacy / Safeguards, PS)
- [x] Q091–Q100 혼합 통과 기준 (Mixed Gate, MG)

**총 자체 문제은행 (Question Bank, QB): 100문제**

## 7. 모의고사 (Mock Exams, ME)

- [x] 모의고사 01 (Mock 01, M01) — 40문제 + 정답표 (Answer Key, AK)
- [x] 모의고사 02 (Mock 02, M02) — 40문제 + 정답표 (Answer Key, AK)
- [x] 최종 모의고사 (Final Mock, FM) — 40문제 + 정답표 (Answer Key, AK)

**총 모의고사 문항 (Mock Questions, MQ): 120문제**

```text
문제은행 (Question Bank, QB) 100
+ 모의고사 (Mock Exams, ME) 120
= 자체 학습 문제 총 220문제
```

## 8. 복습 / 프로젝트 / 증빙 (Review / Project / Evidence, RPE)

- [x] 최종 점검표 (Final Checklist, FC)
- [x] 혼동 개념 비교표 (Confusion Matrix, CM)
- [x] 시험 당일 전략 (Exam-Day Strategy, EDS)
- [x] AI 보조 개발 프로젝트 (AI-Assisted Development Project, AADP)
- [x] 프로젝트 평가 기준 (Project Rubric, PR)
- [x] 프로젝트 증빙 점검표 (Project Evidence Checklist, PEC)
- [x] 오답 오류 코드 (Wrong Answer Error Codes, WAEC)
- [x] +1 / +7 재도전 대기열 (Retry Queue, RQ)
- [x] 일일 추적 (Daily Tracker, DT)
- [x] 시험 준비도 통과 기준 (Exam Readiness Gate, ERG)
- [x] 점수 기록 (Score Log, SL)
- [x] 프롬프트 / 실습 / 시험 / 회고 증빙 템플릿 (Prompt / Lab / Exam / Reflection Evidence Templates, PLER)

## 9. 콘텐츠 상태 의사결정 (Content Status Decision, CSD)

```text
Course content structure: PASS
Current exam scope alignment: PASS
Labs: PASS
Exercises: PASS
Question Bank: PASS
Mock Exams: PASS
Wrong-answer system: PASS
Progress / Evidence: PASS
```

### 콘텐츠 상태 (Content Status, CS)

**CONTENT-READY**

### 학습 상태 (Learning Status, LS)

**PLANNED**

> `CONTENT-READY`는 학습 자료가 준비되었다는 뜻입니다. 사용자의 실제 GH-300 학습·실습·점수 Gate를 통과했다는 뜻이 아닙니다.

## 10. 유지관리 규칙 (Maintenance Rule, MR)

다음 경우 `MAINTENANCE` 또는 재검증으로 전환합니다.

- Microsoft Learn의 `Skills measured as of` 날짜 변경
- GH-300 Change Log 변경
- Agent / CLI / MCP / Copilot Feature 명칭·동작의 중대한 변경
- Privacy / Content Exclusion / Policy 변경
- 시험 언어·시간·가격·유효기간 변경
