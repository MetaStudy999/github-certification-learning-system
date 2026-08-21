# 120 Wrong Answers — GH-600 오답 시스템

## 오류 Codes (Error Codes, EC)

| 코드 | 의미 |
|---|---|
| ARCH | Agent Architecture / SDLC 설계 오류 |
| PLAN | Planning / Execution 경계 혼동 |
| TOOL | Tool / Scope 선택 오류 |
| MCP | MCP / Governance 개념 오류 |
| STATE | Memory / State / Execution 오류 |
| EVAL | Evaluation / Error Analysis 오류 |
| MULTI | Multi-Agent / Handoff 오류 |
| GUARD | Guardrail / Accountability 오류 |
| READING | Scenario 조건 해석 오류 |

## 재도전 주기 (Retry Cycle, RC)

```text
오답
→ Error Code
→ 실패 원인
→ 올바른 설계 원칙 1문장
→ 관련 공식문서
→ 관련 Lab
→ +1일 Retry
→ +7일 Retry
```

## 통과 기준 (Gate, GATE)

시험 전 최근 오답 재시험 **90% 이상**을 목표로 합니다.

[← 110 Mock Exams](../110-mock-exams/README.md) · [다음: 130 Progress →](../130-progress/README.md)
