# 150 Evidence — GH-300 학습·실습 증거

## 목적

자격증 합격 여부뿐 아니라 **Copilot을 어떤 Context와 제약으로 사용했고, AI Output을 어떻게 검증했는지** 재현 가능하게 남깁니다.

## Evidence 맵 (Evidence Map, EM)

| 코드 | 증빙 (Evidence, EVD) | 예시 |
|---:|---|---|
| 010 | Prompt / Context | Goal·Context·Constraints·Verification |
| 020 | Feature Selection | Suggestion / Chat / Edits / Agent / CLI 선택 근거 |
| 030 | Agent / MCP | Tool Scope / Trust Boundary / Agent Task |
| 040 | Generation / Review | Accept / Modify / Reject |
| 050 | Testing | Unit / Integration / Edge / Assertion |
| 060 | Debug / Refactor | 실패 → Root Cause → Fix → Behavior 보존 |
| 070 | Code Review / Organization | AI Review / Human Review / Policy Scenario |
| 080 | Responsible AI / Privacy | Risk / Exclusion / Safeguard / Secret 관리 |
| 090 | Scores / Exam / Reflection | QBank / Mock / GH-300 결과 / 회고 |

## 핵심 Template

- [`010-prompt-evidence-template.md`](./010-prompt-evidence-template.md)
- [`020-lab-evidence-template.md`](./020-lab-evidence-template.md)
- [`030-exam-evidence-template.md`](./030-exam-evidence-template.md)
- [`040-reflection-template.md`](./040-reflection-template.md)
- [`090-content-verification.md`](./090-content-verification.md)

## Prompt Evidence 최소 항목

```text
Date:
Task:
Selected Copilot feature:
Goal:
Context provided:
Context intentionally excluded:
Constraints:
Expected output:
Verification criteria:
Copilot output summary:
Decision: ACCEPT / MODIFY / REJECT
Reason:
Tests / checks:
Privacy / Security notes:
```

## 에이전트 / MCP Evidence (Agent / MCP Evidence, AMCPE)

실제 Agent/MCP 환경을 사용하는 경우 **Secret 값이나 Credential 자체는 기록하지 않습니다.**

```text
Agent goal:
Allowed files:
Allowed tools:
MCP server purpose:
Read scope:
Write scope:
Credential type: <name only, no value>
Human approval point:
Test / verification:
Unexpected behavior:
```

## 코드 리뷰 Evidence (Code Review Evidence, CRE)

```text
PR / sample diff:
Copilot finding:
Human finding:
Accepted AI findings:
Rejected AI findings:
Reason:
Final decision:
```

## 보안·개인정보 원칙

- 실제 Secret, Token, Password, API Key를 기록하지 않습니다.
- 민감 개인정보를 Prompt/Evidence에 포함하지 않습니다.
- Production Credential의 Screenshot을 저장하지 않습니다.
- Agent Tool 권한은 가능한 최소 범위로 설계합니다.
- AI 생성 코드가 정확하다고 가정하지 않습니다.
- Public Repository Evidence에 내부 기밀 내용을 올리지 않습니다.

## PASSED 비교 CLEAR (PASSED vs CLEAR, PASSEDCLEAR)

### PASSED

- GH-300 시험 합격

### CLEAR

- [ ] GH-300 PASS
- [ ] 핵심 Lab 80% 이상 완료
- [ ] Lab 110–130 수행 또는 상세 설계 Evidence
- [ ] AI-Assisted Development Project 90점 이상 권장
- [ ] Accept / Modify / Reject Evidence
- [ ] Testing / Debugging Evidence
- [ ] Responsible AI / Privacy Evidence
- [ ] QBank / Mock 기록
- [ ] 최종 Reflection

## 다음 과정으로 전달할 지식

```text
Copilot Feature / Policy 기초
      ↓
004 GitHub Administration

Privacy / Security / Review
      ↓
005 GitHub Advanced Security

Agent Mode / MCP / Sub-Agent
      ↓
006 GitHub Agentic AI Developer
```

---
[← 140 Resources](../140-resources/README.md) · [Copilot 홈](../README.md)
