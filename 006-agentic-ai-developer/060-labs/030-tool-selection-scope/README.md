# Lab 030 — Tool Selection & Scope

## Objective

Agent가 사용하는 Tool을 목적에 맞게 선택하고 접근 범위를 최소화하는 설계 원칙을 익힙니다.

## Practice

아래 표를 작성합니다.

| Need | Tool category | Required scope | Not required | Verification |
|---|---|---|---|---|
| Repository 정보 읽기 | | | | |
| 테스트 결과 확인 | | | | |
| 문서 초안 생성 | | | | |

## 핵심 질문

1. 이 Tool이 없으면 목표를 달성할 수 없는가?
2. Read-only로 충분한가?
3. Repository 전체가 필요한가, 제한된 범위면 되는가?
4. Tool 결과를 어떻게 검증할 것인가?
5. 실패 시 Agent가 중단해야 하는 조건은 무엇인가?

## Verify

- [ ] Tool 필요성 설명
- [ ] 최소 Scope 설명
- [ ] 불필요 권한 제거 근거 설명
- [ ] Tool 실패 시 안전한 중단 조건 정의

[← 이전](../020-planning-execution/README.md) · [다음 →](../040-mcp-governance/README.md)
