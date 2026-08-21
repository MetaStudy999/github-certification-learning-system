# 020 Copilot 기능 (Copilot Features, CF) — 수행형 연습

## 목표

통합 개발 환경 (Integrated Development Environment, IDE), 명령줄 인터페이스 (Command-Line Interface, CLI), 에이전트 모드 (Agent Mode, AM), 모델 컨텍스트 프로토콜 (Model Context Protocol, MCP), 코드 리뷰 (Code Review, CR), Spaces, Spark, 지침 (Instructions, INS) 등 현재 GH-300 범위의 기능을 **상황에 맞게 선택**합니다.

## 연습문제 (Exercises, EXR)

### E020-01 — 인라인 제안과 채팅 비교 (Inline Suggestion vs Chat, ISC)
A. 현재 함수의 다음 3줄을 빠르게 작성하고 싶다.  
B. 이 함수가 왜 느린지 원인을 설명받고 싶다.

각각 어떤 기능이 더 적합한지 설명하세요.

### E020-02 — 채팅과 편집 비교 (Chat vs Edits, CE)
여러 파일의 동일한 API 호출 패턴을 새 방식으로 바꾸고 변경안을 검토하고 싶습니다. Chat과 Edits 중 어느 쪽을 우선 고려할지 이유를 적으세요.

### E020-03 — 편집과 에이전트 모드 비교 (Edits vs Agent Mode, EAM)
다음 두 작업을 분류하세요.

1. 여러 파일에 정해진 Rename을 적용한다.
2. 실패 Test 원인을 조사하고 관련 파일을 찾아 수정하고 Test를 다시 실행한다.

### E020-04 — Copilot 명령줄 인터페이스 (Copilot CLI, CCLI)
Terminal에서 반복되는 Git 명령을 설명받고 안전한 Shell Script 초안을 만들고 싶습니다. CLI가 적합한 이유와 실행 전 검증할 항목을 작성하세요.

### E020-05 — 에이전트 모드 (Agent Mode, AM)
Agent에게 `버그를 고쳐`라고만 지시하는 Prompt의 문제점을 찾고 Goal/Constraints/Verification을 추가해 개선하세요.

### E020-06 — 모델 컨텍스트 프로토콜 (Model Context Protocol, MCP)
Agent가 외부 Issue Tracker 정보를 읽어야 합니다. MCP를 사용할 때 확인해야 할 Data Scope, Tool Permission, Credential, Logging 항목을 작성하세요.

### E020-07 — 하위 에이전트 (Sub-Agent, SA)
큰 작업을 `Test 분석`, `보안 검토`, `문서화`로 분리한다고 가정합니다. Sub-Agent 위임의 장점과 위험을 각각 2개씩 적으세요.

### E020-08 — 코드 리뷰 (Code Review, CR)
Copilot Code Review가 PR에서 제안을 했습니다. 사람이 반드시 별도로 검토해야 할 항목을 5개 작성하세요.

### E020-09 — 지침 / 프롬프트 파일 (Instructions / Prompt Files, IPF)
다음을 분류하세요.

- 모든 Python 코드는 type hint를 사용한다.
- PR Review 시 Correctness → Security → Test → Docs 순서로 분석한다.

왜 하나는 지속 지침, 다른 하나는 반복 Task Prompt가 될 수 있는지 설명하세요.

### E020-10 — Spaces와 Spark 기능 비교 (Spaces / Spark, SS)
A. 팀의 설계 원칙과 API 규칙을 Copilot이 참고하도록 묶고 싶다.  
B. 자연어 요구사항으로 작은 Prototype 앱을 빠르게 만들고 싶다.

각 상황에 더 가까운 기능을 선택하고 한계를 적으세요.

## 자가 검증

- [ ] Inline Suggestion / Chat / Edits / Agent Mode를 구분한다.
- [ ] CLI의 사용 목적을 설명한다.
- [ ] MCP를 Tool/Context 연결 구조로 설명한다.
- [ ] Code Review를 Human Review 대체물로 오해하지 않는다.
- [ ] Instructions / Prompt Files / Spaces / Spark를 구분한다.

## 관련 실습 (Related Labs, RL)

- [`110-cli-agent-mcp`](../../060-labs/110-cli-agent-mcp/)
- [`120-code-review-org-policy`](../../060-labs/120-code-review-org-policy/)
- [`130-spaces-spark-instructions`](../../060-labs/130-spaces-spark-instructions/)

---
[← 010 책임 있는 AI (Responsible AI, RAI)](../010-responsible-ai/README.md) · [030 데이터와 아키텍처 (Data & Architecture, DA) →](../030-data-architecture/README.md)
