# 010 개요 (Overview, OVW) — GH-300

## 빠른 시작 (Quick Start, QS)

GH-300은 제품 기능 암기 시험이 아니라 **AI를 책임감 있게 사용하고, Copilot 기능을 상황에 맞게 선택하며, 결과를 검증할 수 있는지**를 확인하는 시험으로 접근합니다.

```text
시험 범위 확인
→ 기능 지도 작성
→ 데이터·아키텍처 (Data / Architecture, DA) 이해
→ 프롬프트·컨텍스트 (Prompt / Context, PC) 실습
→ 개발자 활용 사례 (Developer Use Case, DUC) 실습
→ 개인정보 보호·안전장치 (Privacy / Safeguard, PS) 확인
→ 문제풀이
→ 모의고사 (Mock, ME)
```

## 측정 기술 (Skills Measured, SM) — 적용일 2026-08-07

| # | 기술 영역 (Skill Area, SA) | 비중 |
|---:|---|---:|
| 1 | GitHub Copilot 책임 있게 사용 (Use GitHub Copilot responsibly, RAI) | 15–20% |
| 2 | GitHub Copilot 기능 사용 (Use GitHub Copilot features, CF) | 25–30% |
| 3 | GitHub Copilot 데이터 및 아키텍처 이해 (Understand GitHub Copilot data and architecture, DA) | 10–15% |
| 4 | 프롬프트 엔지니어링 및 컨텍스트 구성 적용 (Apply prompt engineering and context crafting, PECC) | 10–15% |
| 5 | GitHub Copilot으로 개발자 생산성 향상 (Improve developer productivity with GitHub Copilot, DP) | 10–15% |
| 6 | 개인정보 보호·콘텐츠 제외·안전장치 구성 (Configure privacy, content exclusions, and safeguards, PES) | 10–15% |

## 1. 책임 있는 AI (Responsible AI, RAI)

반드시 설명할 수 있어야 합니다.

- 생성형 AI (Generative AI, GenAI)의 위험과 한계
- 편향 (Bias), 공정성 (Fairness), 개인정보 보호 (Privacy), 투명성 (Transparency), 보안 코드 (Secure Code) 위험
- AI 출력 (AI Output, AIO)을 검증해야 하는 이유
- 잠재적 위해 (Potential Harm, PH) 완화 전략
- 사람 검토 (Human Review, HR)의 책임

## 2. Copilot 기능 (Copilot Features, CF) — 가장 큰 비중

현재 시험에서는 다음 기능을 폭넓게 봅니다.

```text
통합 개발 환경 (Integrated Development Environment, IDE)
├── 인라인 제안 (Inline Suggestions, IS)
├── 채팅 (Chat, CH)
├── 편집 (Edits, ED)
└── 에이전트 모드 (Agent Mode, AM)

명령줄 인터페이스 (Command-Line Interface, CLI)
├── 대화형 사용 (Interactive Use, IU)
├── 세션 (Sessions, SES)
├── 스크립트 생성 (Script Generation, SG)
└── 파일 관리 (File Management, FM)

고급 기능 (Advanced Features, AF)
├── 모델 컨텍스트 프로토콜 (Model Context Protocol, MCP)
├── 에이전트 세션 / 하위 에이전트 (Agent Sessions / Sub-Agents, ASA)
├── 코드 리뷰 (Code Review, CR)
├── PR 요약 (PR Summaries, PRS)
├── Spaces
├── Spark
├── 지침 파일 (Instructions Files, IF)
└── 프롬프트 파일 (Prompt Files, PF)

조직 (Organization, ORG)
├── 정책 (Policies, POL)
├── 감사 로그 (Audit Log, AL)
└── 구독 관리 / REST API (Subscription Management / REST API, SMRA)
```

## 3. 데이터와 아키텍처 (Data and Architecture, DA)

다음 흐름을 설명할 수 있어야 합니다.

```text
개발자 입력 / 편집기 컨텍스트 (Developer Input / Editor Context, DIEC)
        ↓
컨텍스트 수집 (Context Gathering, CG)
        ↓
프롬프트 구성 (Prompt Building, PB)
        ↓
프록시 / 필터링 (Proxy / Filtering, PF)
        ↓
대규모 언어 모델 (Large Language Model, LLM)
        ↓
응답 (Response, RSP)
        ↓
후처리 / 일치 검사 (Post-processing / Matching Checks, PMC)
        ↓
개발자 제안 (Suggestion to Developer, SD)
```

## 4. 프롬프트 엔지니어링과 컨텍스트 구성 (Prompt Engineering and Context Crafting, PECC)

- 목표 / 컨텍스트 / 제약 / 출력 / 검증 (Goal / Context / Constraints / Output / Verification, GCCOV)
- 제로샷 / 퓨샷 (Zero-shot / Few-shot, ZF)
- 채팅 기록 (Chat History, CH)
- 관련 컨텍스트 (Relevant Context, RC) 선택
- 프롬프트 처리 흐름 (Prompt Process Flow, PPF)

## 5. 개발자 생산성 (Developer Productivity, DP)

- 코드 생성 (Code Generation, CG)
- 리팩터링 (Refactoring, RF)
- 문서화 (Documentation, DOC)
- 새 언어·프레임워크 학습 (Learning New Languages / Frameworks, LNF)
- 샘플 데이터 (Sample Data, SD)
- 레거시 현대화 (Legacy Modernization, LM)
- 디버깅 (Debugging, DBG)
- 단위 / 통합 테스트 (Unit / Integration Test, UIT)
- 엣지 케이스 / 단언문 (Edge Case / Assertion, ECA)
- 보안 개선 (Security Improvement, SI)
- 성능 최적화 (Performance Optimization, PO)

## 6. 개인정보 보호 / 제외 / 안전장치 (Privacy / Exclusion / Safeguard, PES)

- 콘텐츠 제외 (Content Exclusion, CE) 구성과 한계
- 편집기 설정 (Editor Settings, ES)
- 출력물 소유권 (Output Ownership, OO)
- 공개 코드 일치 제안 필터링 (Suggestions Matching Public Code Filtering, SMPCF)
- 제안 / 제외 문제 해결 (Suggestion / Exclusion Troubleshooting, SET)

## 7일 단기 집중 과정 (7-Day Fast Track, 7DFT)

| 일차 (Day, D) | 핵심 목표 | 결과물 |
|---:|---|---|
| 1 | 책임 있는 AI + IDE / Chat / CLI (Responsible AI + IDE / Chat / CLI, RAIC) | 기능 비교표 |
| 2 | 에이전트 모드 / Edits / MCP / 코드 리뷰 (Agent Mode / Edits / MCP / Code Review, AEMC) | 기능 선택 시나리오 |
| 3 | 데이터 흐름 / 아키텍처 / LLM 한계 (Data Flow / Architecture / LLM Limits, DALL) | 데이터 흐름 그림 |
| 4 | 프롬프트 + 컨텍스트 + 지침 (Prompt + Context + Instructions, PCI) | Prompt 개선 기록 |
| 5 | 생산성 + 테스트 + 개인정보 보호 (Productivity + Testing + Privacy, PTP) | 검증 Checklist |
| 6 | 연습문제 + 문제은행 + 모의고사 01 (Exercises + QBank + Mock 01, EQM) | 약점 목록 |
| 7 | 모의고사 02 + 최종 복습 (Mock 02 + Final Review, MFR) | 시험 통과 기준 판정 |

## 핵심 질문

1. Copilot 출력 (Copilot Output, CO)이 그럴듯해 보여도 왜 반드시 검증해야 하는가?
2. 인라인 제안 (Inline Suggestion, IS), 채팅 (Chat, CH), 편집 (Edits, ED), 에이전트 모드 (Agent Mode, AM), CLI는 언제 각각 적합한가?
3. MCP는 에이전틱 워크플로 (Agentic Workflow, AW)에서 어떤 역할을 하는가?
4. Copilot은 어떤 컨텍스트 (Context, CTX)를 수집하고 프롬프트 (Prompt, PRM)를 어떻게 구성하는가?
5. 제로샷 (Zero-shot, ZS)과 퓨샷 (Few-shot, FS)은 언제 사용하는가?
6. 테스트 (Testing, TST)에서 Copilot이 도울 수 있는 것과 사람이 책임져야 하는 것은 무엇인가?
7. 콘텐츠 제외 (Content Exclusion, CE)는 무엇을 보장하고 무엇을 보장하지 않는가?

## 버전 규칙 (Version Rule, VR)

이 과정은 **Microsoft Learn GH-300 학습 가이드 (Study Guide, SG)의 2026-08-07 적용 범위**를 기준으로 합니다. 시험 전날 최신 Study Guide의 `Skills measured`와 `Change log`를 다시 확인합니다.

---
[← Copilot 홈](../README.md) · [다음: 020 용어 (Terms, TRM) →](../020-terms/README.md)
