# Lab 110 — Copilot CLI / Agent Mode / MCP

## Objective

GitHub Copilot의 **CLI**, **Agent Mode**, **MCP**를 서로 다른 목적의 기능으로 구분하고, Agentic Development Workflow를 안전하게 설계합니다.

## Concept

```text
CLI
→ Terminal 중심 Copilot 상호작용

Agent Mode
→ 목표를 받아 여러 단계 작업 수행

MCP
→ Agent와 외부 Tool / Data를 연결하는 표준 인터페이스
```

## Practice 1 — 기능 선택

다음 상황에서 가장 적합한 방식을 선택하고 이유를 기록합니다.

1. Terminal에서 명령 설명과 Script 초안을 받고 싶다.
2. 여러 파일을 조사하고 수정한 뒤 Test까지 반복하게 하고 싶다.
3. Agent가 외부 도구의 데이터를 읽도록 표준 방식으로 연결하고 싶다.

기록 형식:

```text
Scenario:
Selected feature:
Why:
Why alternatives are less appropriate:
Risk:
Verification:
```

## Practice 2 — Agent Task 설계

안전한 Sandbox Repository에서 다음과 같은 작은 목표를 작성합니다.

```text
Goal:
- 기존 Python 모듈의 중복 코드를 찾는다.
- 변경 전 Test를 확인한다.
- 최소 변경으로 Refactor한다.
- Test를 다시 실행한다.
- 변경 요약을 작성한다.

Constraints:
- 외부 네트워크 호출 금지
- Secret 접근 금지
- Public API 변경 금지
- Test 실패 시 추가 변경 전에 원인 설명
```

Agent가 실제로 사용할 수 없는 기능이 있는 환경이라면 **실행 대신 계획과 권한 경계를 설계**합니다.

## Practice 3 — MCP Trust Boundary

MCP Server를 연결한다고 가정하고 다음을 표로 작성합니다.

| 항목 | 질문 |
|---|---|
| Data | 어떤 데이터를 읽는가? |
| Tools | 어떤 동작을 수행할 수 있는가? |
| Write Access | 쓰기 권한이 필요한가? |
| Credential | 어떤 자격증명이 필요한가? |
| Scope | 최소 권한인가? |
| Logging | 어떤 행동을 추적할 수 있는가? |
| Failure | 잘못된 Tool 호출 시 영향은? |

## Challenge

`Chat만으로 충분한 작업`과 `Agent Mode가 더 적합한 작업`을 각각 3개 작성하세요.

그리고 Agent Mode가 항상 더 좋은 선택이 아닌 이유를 설명합니다.

## Verify

- [ ] CLI / Agent Mode / MCP를 각각 한 문장으로 설명 가능
- [ ] Agent Mode와 Chat의 차이를 설명 가능
- [ ] MCP를 단순한 데이터베이스나 특정 제품명으로 오해하지 않음
- [ ] Agent Tool 권한에 최소 권한 원칙을 적용함
- [ ] Agent 결과를 Test / Review로 검증하는 절차를 작성함

## 증빙 (Evidence, EVD)

```text
Date:
Environment:
Scenario comparison:
Agent goal:
Constraints:
MCP trust boundary:
Verification result:
What I learned:
```

---
[← Lab 100](../100-end-to-end-development/README.md) · [Lab 120 →](../120-code-review-org-policy/README.md)
