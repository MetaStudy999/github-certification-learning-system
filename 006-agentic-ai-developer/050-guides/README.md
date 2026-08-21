# 050 Guides — Agentic AI 입문자 가이드

## Agent를 이해하는 순서

```text
무엇을 달성해야 하는가?
→ 어떤 입력이 필요한가?
→ 성공 기준은 무엇인가?
→ 계획과 실행을 어떻게 분리할 것인가?
→ 어떤 도구가 필요한가?
→ 상태를 어떻게 추적할 것인가?
→ 결과를 어떻게 평가할 것인가?
→ 어디서 사람이 개입할 것인가?
```

## 에이전트 설계 카드 (Agent Design Card, ADC)

```text
Goal:
Inputs:
Expected outputs:
Success criteria:
Allowed tools:
Scope:
State to track:
Evaluation criteria:
Guardrails:
Human review points:
Stop / Escalation conditions:
```

## 자율성 설계 원칙

Agent의 자율성은 `높을수록 좋다`가 아닙니다.

```text
Risk가 낮고 검증이 쉬움
→ 더 많은 자동화 가능

Risk가 높거나 되돌리기 어려움
→ 더 강한 제한 / 승인 / 검증 필요
```

## 학습 안전 원칙

- Sandbox와 문서 기반 Scenario를 우선합니다.
- 실제 운영 시스템 권한 확대를 학습 과제로 사용하지 않습니다.
- Tool Permission은 최소 필요 범위를 기준으로 판단합니다.
- Agent 결과는 독립적인 Evaluation과 Human Review를 거칩니다.

[← 040 Official Docs](../040-official-docs/README.md) · [다음: 060 Labs →](../060-labs/README.md)
