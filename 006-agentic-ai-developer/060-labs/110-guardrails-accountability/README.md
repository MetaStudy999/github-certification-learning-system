# 실습 (Lab, LAB) 110 — 가드레일과 책임성 (Guardrails & Accountability, GA)

## 목표 (Objective, OBJ)

Agent의 자율성을 제한·검증하고 사람이 책임 있게 감독할 수 있는 구조를 설계합니다.

## 가드레일 계층 (Guardrail Layers, GL)

```text
Input constraints
→ Planning validation
→ Tool / Scope restrictions
→ Execution checks
→ Evaluation thresholds
→ Human oversight
→ Audit / Evidence
```

## 실습 (Practice, PRAC)

다음 Scenario에 필요한 Guardrail을 정의합니다.

1. 읽기 전용 Repository 분석
2. 변경 제안서 생성
3. CI 결과 요약
4. 다중 Agent 검토
5. 평가 기준 미달 결과

## 책임성 점검표 (Accountability Checklist, AC)

- [ ] 누가 Agent를 호출했는가?
- [ ] 어떤 입력과 정책이 적용되었는가?
- [ ] 어떤 도구 범주가 허용되었는가?
- [ ] 어떤 Artifact가 생성되었는가?
- [ ] 누가 검토·승인했는가?
- [ ] 실패·예외가 기록되었는가?

[← 이전](../100-failure-conflict-handling/README.md) · [다음 →](../120-end-to-end-agentic-sdlc/README.md)
