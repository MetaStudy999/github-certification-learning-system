# 실습 (Lab, LAB) 080 — 오류 분석과 조정 (Error Analysis & Tuning, EAT)

## 목표 (Objective, OBJ)

Agent 실패를 유형화하고 원인에 맞는 개선 방법을 선택합니다.

## 실패 분류체계 (Failure Taxonomy, FT)

| Error type | 예시 | 개선 후보 |
|---|---|---|
| Input | 요구사항 모호 | 입력 형식 / 질문 개선 |
| Context | 필요한 정보 부족 | Context 선정 개선 |
| Planning | 단계 누락 | Plan Template / Validation |
| Tool | 잘못된 Tool 선택 | Tool Routing / Scope 개선 |
| State | 진행 상태 불일치 | Checkpoint / State 관리 |
| Evaluation | 잘못된 성공 판정 | Metric / Threshold 개선 |
| Governance | 승인 조건 누락 | Guardrail / Review 강화 |

## 실습 (Practice, PRAC)

실패 Scenario 5개를 선택해 `증상 → 원인 → 수정 → 재평가`를 기록합니다.

## 검증 (Verify, VER)

- [ ] 결과가 나쁘다고 무조건 Prompt만 수정하지 않음
- [ ] 원인 유형별 개선 방법을 선택
- [ ] 변경 전후 동일 평가 기준으로 비교

[← 이전](../070-evaluation-design/README.md) · [다음 →](../090-multi-agent-coordination/README.md)
