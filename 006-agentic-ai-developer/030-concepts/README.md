# 030 Concepts — Agentic AI 핵심 개념

## 기본 구조

```text
Requirement
   ↓
Inputs / Success Criteria
   ↓
Planning
   ↓
Review / Approval
   ↓
Controlled Execution
   ↓
State / Checkpoint
   ↓
Evaluation
   ↓
Improve / Stop / Escalate
```

## 반드시 구분

| A | B | 핵심 차이 |
|---|---|---|
| Planning | Execution | 무엇을 할지 정리 vs 실제 행동 수행 |
| Reasoning | Action | 내부 판단 vs 외부 상태 변화 |
| Memory | State | 장기·재사용 정보 vs 현재 실행 상황 |
| Tool | MCP | 기능 인터페이스 vs 도구 연결 표준 |
| Evaluation | Monitoring | 결과 품질 평가 vs 실행 상태 관찰 |
| Retry | Resume | 다시 시도 vs 저장된 상태에서 이어가기 |
| Single Agent | Multi-Agent | 하나의 책임 범위 vs 역할 분산·조정 |
| Delegation | Handoff | 작업 일부 위임 vs 책임/Context 전달 |
| Guardrail | Human Review | 자동·정책 기반 제한 vs 사람의 판단 |
| HITL | HOTL | 실행 중 승인 참여 vs 감독하며 필요 시 개입 |

## 핵심 설계 원칙

1. 입력·출력·성공 기준을 명확히 합니다.
2. 계획과 실행을 분리합니다.
3. 도구 접근은 필요한 범위로 제한합니다.
4. 상태와 결과를 관찰 가능한 Artifact로 남깁니다.
5. 평가 기준 없이 자율성만 높이지 않습니다.
6. 중요한 위험 지점에는 Guardrail과 Human Oversight를 둡니다.
7. 실패 시 중단·재시도·복구·Escalation 조건을 정의합니다.

[← 020 Terms](../020-terms/README.md) · [다음: 040 Official Docs →](../040-official-docs/README.md)
