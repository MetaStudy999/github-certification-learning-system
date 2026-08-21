# Lab 050 — Environment & Execution Context

## Objective

Agent가 어떤 환경과 Scope에서 작동하는지 명시적으로 설계합니다.

## Practice

아래 3개 Context를 비교합니다.

| Context | Allowed scope | Expected artifacts | Human review | Failure behavior |
|---|---|---|---|---|
| Repository analysis | | | | |
| Branch-scoped change proposal | | | | |
| CI validation | | | | |

## 핵심 질문

- 작업 범위는 Repository 전체인가 제한된 영역인가?
- 읽기와 변경 제안 중 무엇이 필요한가?
- 결과를 어떤 Artifact로 남길 것인가?
- 환경별 제약이 다를 때 Agent는 어떻게 중단·Escalate해야 하는가?

## Verify

- [ ] Execution Context와 Tool Permission을 구분 가능
- [ ] Repository/Branch/CI Scope 차이 설명 가능
- [ ] 환경 제약을 성공 기준과 연결 가능

[← 이전](../040-mcp-governance/README.md) · [다음 →](../060-memory-state-checkpoint/README.md)
