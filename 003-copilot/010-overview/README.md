# 010 Overview — GH-300

## Quick Start

GH-300은 제품 기능 암기 시험이 아니라 **AI를 책임감 있게 사용하고, Copilot 기능을 상황에 맞게 선택하며, 결과를 검증할 수 있는지**를 확인하는 시험으로 접근합니다.

```text
시험 범위 확인
→ 기능 지도 작성
→ Data/Architecture 이해
→ Prompt/Context 실습
→ Developer Use Case 실습
→ Privacy/Safeguard 확인
→ 문제풀이
→ Mock
```

## Skills Measured — 적용일 2026-08-07

| # | Skill Area | 비중 |
|---:|---|---:|
| 1 | Use GitHub Copilot responsibly | 15–20% |
| 2 | Use GitHub Copilot features | 25–30% |
| 3 | Understand GitHub Copilot data and architecture | 10–15% |
| 4 | Apply prompt engineering and context crafting | 10–15% |
| 5 | Improve developer productivity with GitHub Copilot | 10–15% |
| 6 | Configure privacy, content exclusions, and safeguards | 10–15% |

## 1. Responsible AI

반드시 설명할 수 있어야 합니다.

- Generative AI의 위험과 한계
- Bias, Fairness, Privacy, Transparency, Secure Code 위험
- AI Output을 검증해야 하는 이유
- Potential Harm 완화 전략
- Human Review의 책임

## 2. Copilot Features — 가장 큰 비중

현재 시험에서는 다음 기능을 폭넓게 봅니다.

```text
IDE
├── Inline Suggestions
├── Chat
├── Edits
└── Agent Mode

CLI
├── Interactive use
├── Sessions
├── Script generation
└── File management

Advanced
├── MCP
├── Agent Sessions / Sub-Agents
├── Code Review
├── PR Summaries
├── Spaces
├── Spark
├── Instructions files
└── Prompt files

Organization
├── Policies
├── Audit Log
└── Subscription Management / REST API
```

## 3. Data and Architecture

다음 흐름을 설명할 수 있어야 합니다.

```text
Developer input / editor context
        ↓
Context gathering
        ↓
Prompt building
        ↓
Proxy / filtering
        ↓
LLM
        ↓
Response
        ↓
Post-processing / matching checks
        ↓
Suggestion to developer
```

## 4. Prompt Engineering and Context Crafting

- Goal / Context / Constraints / Output / Verification
- Zero-shot / Few-shot
- Chat History
- Relevant Context 선택
- Prompt Process Flow

## 5. Developer Productivity

- Code generation
- Refactoring
- Documentation
- Learning new languages/frameworks
- Sample data
- Legacy modernization
- Debugging
- Unit / Integration Test
- Edge Case / Assertion
- Security improvement
- Performance optimization

## 6. Privacy / Exclusion / Safeguard

- Content Exclusion 구성과 한계
- Editor Settings
- Output Ownership
- Suggestions matching public code filtering
- Suggestion / Exclusion Troubleshooting

## 7-Day Fast Track

| Day | 핵심 목표 | 결과물 |
|---:|---|---|
| 1 | Responsible AI + IDE/Chat/CLI | 기능 비교표 |
| 2 | Agent Mode / Edits / MCP / Code Review | 기능 선택 시나리오 |
| 3 | Data Flow / Architecture / LLM Limits | 데이터 흐름 그림 |
| 4 | Prompt + Context + Instructions | Prompt 개선 기록 |
| 5 | Productivity + Testing + Privacy | 검증 Checklist |
| 6 | Exercises + QBank + Mock 01 | 약점 목록 |
| 7 | Mock 02 + Final Review | Exam Gate 판정 |

## 핵심 질문

1. Copilot Output이 그럴듯해 보여도 왜 반드시 검증해야 하는가?
2. Inline Suggestion, Chat, Edits, Agent Mode, CLI는 언제 각각 적합한가?
3. MCP는 Agentic Workflow에서 어떤 역할을 하는가?
4. Copilot은 어떤 Context를 수집하고 Prompt를 어떻게 구성하는가?
5. Zero-shot과 Few-shot은 언제 사용하는가?
6. Testing에서 Copilot이 도울 수 있는 것과 사람이 책임져야 하는 것은 무엇인가?
7. Content Exclusion은 무엇을 보장하고 무엇을 보장하지 않는가?

## Version Rule

이 과정은 **Microsoft Learn GH-300 Study Guide의 2026-08-07 적용 범위**를 기준으로 합니다. 시험 전날 최신 Study Guide의 `Skills measured`와 `Change log`를 다시 확인합니다.

---
[← Copilot 홈](../README.md) · [다음: 020 Terms →](../020-terms/README.md)
