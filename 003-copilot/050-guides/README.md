# 050 Guides — GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) 입문자 가이드

## 빠른 시작 (Quick Start, QS)

Copilot을 처음 배울 때는 기능 이름부터 외우기보다 다음 순서로 이해합니다.

```text
왜 필요한가?
→ 어떤 인터페이스가 있는가?
→ Prompt와 Context는 무엇인가?
→ Agent는 무엇이 다른가?
→ 결과를 어떻게 검증하는가?
→ Privacy와 Responsible AI를 어떻게 지키는가?
```

## 1. 기능 선택을 쉽게 이해하기

```text
코드 작성 중 다음 줄이 필요하다
→ Inline Suggestion

질문·설명·디버깅 대화가 필요하다
→ Chat

여러 파일을 편집하고 싶다
→ Edits

목표를 주고 여러 단계를 수행하게 하고 싶다
→ Agent Mode

Terminal에서 작업하고 싶다
→ Copilot CLI
```

핵심은 `가장 강력한 기능`이 아니라 **현재 작업에 가장 적절한 기능**을 선택하는 것입니다.

## 2. Prompt 기본 구조

좋은 Prompt는 가능하면 다음 요소를 포함합니다.

1. **Goal** — 무엇을 원하는가
2. **Context** — 현재 코드·환경·문제
3. **Constraints** — 지켜야 할 조건
4. **Output** — 원하는 결과 형식
5. **Verification** — 성공 여부 확인 기준

예시:

```text
Goal: Python 함수의 입력 검증을 개선해 줘.
Context: 아래 함수는 문자열을 받아 날짜로 변환한다.
Constraints: 기존 API는 유지하고 표준 라이브러리만 사용한다.
Output: 수정 코드와 변경 이유를 설명한다.
Verification: 정상/비정상 입력 Unit Test도 작성한다.
```

## 3. Context를 많이 주면 항상 좋은가?

아닙니다.

```text
Relevant Context ↑
→ 유용한 응답 가능성 ↑

Irrelevant / Conflicting Context ↑
→ 혼동 가능성 ↑
```

필요한 파일·선택 영역·오류 메시지·요구사항을 중심으로 Context를 제공합니다.

## 4. Agent Mode를 이해하는 가장 쉬운 방법

Chat은 주로 **답변을 제안**합니다.

Agent Mode는 목표를 받아 **여러 단계 작업을 계획·실행**할 수 있습니다.

```text
Goal
→ Plan
→ Inspect files
→ Edit
→ Run tool / test
→ Observe result
→ Revise
→ Human review
```

Agent가 더 많이 행동할수록 사람의 검토가 덜 필요한 것이 아니라 **검토해야 할 범위가 더 넓어집니다.**

## 5. MCP는 왜 필요한가?

MCP(Model Context Protocol)는 Agent가 외부 도구나 데이터 소스와 연결될 때 사용할 수 있는 표준 인터페이스입니다.

```text
Copilot / Agent
      ↓
     MCP
      ↓
Tools / Data / Services
```

시험에서는 MCP를 특정 제품 하나로 외우기보다 **Agent의 Tool/Context 확장 구조**로 이해합니다.

## 6. Copilot Output 검증 순서

```text
AI Output
  ↓
Requirement Review
  ↓
Code Review
  ↓
Run / Build
  ↓
Test
  ↓
Security / Privacy Check
  ↓
Accept / Modify / Reject
```

`설명이 그럴듯하다`와 `코드가 올바르다`는 다릅니다.

## 7. Test 생성에서도 사람이 해야 할 일

Copilot이 Test 초안을 만들어도 다음을 직접 확인합니다.

- 정상 Case
- Boundary / Edge Case
- Error Case
- Assertion이 실제 요구사항을 검증하는지
- Test가 잘못된 구현을 그대로 승인하지 않는지

## 8. Privacy 기본 원칙

Prompt에 다음을 불필요하게 넣지 않습니다.

- Password
- API Key
- Access Token
- Secret
- 개인정보
- Production Credential
- 공개하면 안 되는 내부 데이터

Content Exclusion은 중요한 관리 기능이지만 **Secret Management를 대체하지 않습니다.**

## 9. Responsible AI Checklist

AI 결과를 사용할 때 묻습니다.

```text
정확한가?
안전한가?
편향되지는 않았는가?
개인정보를 노출하지 않는가?
라이선스·정책에 문제가 없는가?
누가 최종 책임을 지는가?
```

## 10. 시험 문제 접근법

Scenario 문제에서는 다음 순서로 읽습니다.

```text
Goal
→ Constraints
→ Required interface
→ Security / Privacy condition
→ BEST / FIRST / MOST appropriate
→ 기능 선택
```

기능 이름이 익숙하다는 이유만으로 선택하지 않습니다.

---
[← 040 Official Docs](../040-official-docs/README.md) · [다음: 060 Labs →](../060-labs/README.md)
