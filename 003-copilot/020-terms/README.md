# 020 Terms — GitHub Copilot 핵심 용어

## Quick Start

용어는 정의만 외우지 않습니다. 각 용어를 다음 세 문장으로 설명할 수 있어야 합니다.

1. **무엇인가?**
2. **언제 사용하는가?**
3. **무엇과 혼동하기 쉬운가?**

## AI / Prompt 기본 용어

| English | 약어 | 한국어 / 핵심 의미 |
|---|---|---|
| Artificial Intelligence | AI | 인공지능 |
| Generative AI | GenAI | 새로운 텍스트·코드 등을 생성하는 인공지능 |
| Large Language Model | LLM | 대규모 언어 모델 |
| Prompt | - | 모델에 제공하는 지시·질문 |
| Context | - | 응답 생성에 참고되는 주변 정보 |
| Token | - | 모델이 처리하는 텍스트 단위 |
| Context Window | - | 한 번에 참고 가능한 Context 범위 |
| Prompt Crafting | - | 개별 Prompt를 명확하게 작성하는 활동 |
| Prompt Engineering | - | 반복 가능하고 성능이 좋은 Prompt 전략을 설계하는 활동 |
| Zero-shot Prompting | - | 예시 없이 지시하는 방식 |
| Few-shot Prompting | - | 소수의 예시를 제공하는 방식 |
| Hallucination | - | 사실·코드·설정을 잘못 생성하는 현상 |
| Responsible AI | RAI | 책임 있는 AI 사용 원칙 |
| Human Review | - | 사람이 AI Output을 검토·승인하는 과정 |

## Copilot 사용 방식

| English | 한국어 / 핵심 의미 |
|---|---|
| Inline Suggestion | 코드 작성 위치에서 나타나는 자동 제안 |
| Code Completion | 작성 중인 코드의 이어질 내용을 제안 |
| Copilot Chat | 대화형 개발 지원 인터페이스 |
| Inline Chat | 현재 코드 위치·선택 영역과 밀접하게 상호작용하는 Chat |
| Copilot Edits | 여러 변경을 제안·적용하는 편집 중심 기능 |
| Agent Mode | 목표를 받아 여러 단계의 개발 작업을 도구와 함께 수행하는 모드 |
| Agent Session | Agent가 작업 목표와 상태를 유지하며 수행하는 세션 |
| Sub-Agent | 상위 Agent가 특정 하위 작업을 위임하는 Agent |
| GitHub Copilot CLI | CLI 환경에서 Copilot을 사용하는 인터페이스 |
| Copilot Code Review | 코드 변경을 AI가 검토하도록 지원하는 기능 |
| Pull Request Summary | PR 변경내용을 요약하는 기능 |

## Agent / Context 확장 용어

| English | 약어 | 한국어 / 핵심 의미 |
|---|---|---|
| Model Context Protocol | MCP | 모델/Agent가 외부 도구·데이터와 표준 방식으로 연결되도록 하는 프로토콜 |
| Tool | - | Agent가 실제 작업에 호출하는 기능 |
| Instruction File | - | Repository/환경에서 Copilot의 동작 지침을 지속적으로 제공하는 파일 |
| Prompt File | - | 반복 사용할 Prompt를 파일로 저장해 재사용하는 방식 |
| Space | - | Copilot에 관련 지식·Context를 묶어 제공하는 협업/지식 공간 |
| GitHub Spark | - | 자연어 중심으로 애플리케이션을 만들고 발전시키는 GitHub 기능 |

## Data / Architecture 용어

| English | 한국어 / 핵심 의미 |
|---|---|
| Data Flow | 입력부터 Output까지 데이터가 이동하는 흐름 |
| Prompt Building | 사용자 입력과 Context를 조합해 모델 Prompt를 만드는 과정 |
| Proxy Service | Prompt/Response 처리 과정에서 필터링·중계 역할을 하는 서비스 |
| Filtering | 정책·안전·공개 코드 일치 등 기준에 따라 입력/출력을 처리하는 과정 |
| Post-processing | 모델 응답 후 추가 검사·가공하는 과정 |
| Public Code Matching | 제안이 공개 코드와 일치하는지 판단하는 기능/정책 영역 |

## Developer Workflow 용어

| English | 한국어 / 핵심 의미 |
|---|---|
| Code Generation | 새 코드 생성 |
| Refactoring | 동작을 유지하며 코드 구조 개선 |
| Documentation | README, Docstring, 설명 문서 작성 |
| Debugging | 오류 원인 분석과 수정 |
| Unit Test | 작은 코드 단위 검증 |
| Integration Test | 여러 구성요소의 결합 동작 검증 |
| Edge Case | 일반적이지 않지만 처리해야 하는 경계·예외 상황 |
| Assertion | 기대 결과를 코드로 검증하는 조건 |
| Code Review | 코드 품질·정확성·보안 등을 검토하는 과정 |

## Privacy / Safeguard 용어

| English | 한국어 / 핵심 의미 |
|---|---|
| Privacy | 개인정보·사용 데이터 보호 원칙 |
| Content Exclusion | 특정 파일/콘텐츠가 Copilot Context로 사용되지 않도록 구성하는 기능 |
| Safeguard | AI 사용 위험을 줄이기 위한 보호장치 |
| Suggestion Matching Public Code Filter | 공개 코드와 일치하는 제안을 필터링하는 설정 |
| Output Ownership | 생성된 Output의 소유·사용 책임과 관련된 개념 |
| Policy | 조직에서 Copilot 기능 사용 여부와 범위를 관리하는 규칙 |
| Audit Log | 조직의 관리·사용 관련 이벤트를 추적하는 기록 |

## 반드시 비교할 용어

```text
Prompt            ↔ Context
Prompt Crafting   ↔ Prompt Engineering
Inline Suggestion ↔ Chat
Chat              ↔ Edits
Edits             ↔ Agent Mode
Agent Mode        ↔ CLI
Instruction File  ↔ Prompt File
Content Exclusion ↔ 원본 파일 삭제
AI Suggestion     ↔ 검증된 정답
Privacy           ↔ Security
```

## 학습 완료 기준

- [ ] 핵심 용어를 한글·영어로 연결할 수 있다.
- [ ] 약어 `AI`, `GenAI`, `LLM`, `MCP`, `RAI`를 풀어 말할 수 있다.
- [ ] Agent Mode / MCP / Sub-Agent의 관계를 설명할 수 있다.
- [ ] Prompt / Context / Instruction / Prompt File을 구분할 수 있다.
- [ ] Content Exclusion의 목적과 한계를 설명할 수 있다.

---
[← 010 Overview](../010-overview/README.md) · [다음: 030 Concepts →](../030-concepts/README.md)
