# 040 Evaluation / Error Analysis / Tuning — 연습문제 (Exercises, EXR)

1. Agent Task Success를 측정할 Metric 5개를 설계하세요.
2. Correctness와 Safety를 별도 Metric으로 관리해야 하는 이유를 설명하세요.
3. 정상 입력뿐 아니라 모호한 입력·Tool 실패를 평가 Dataset에 포함해야 하는 이유를 설명하세요.
4. Agent 실패를 Input, Context, Planning, Tool, State, Evaluation 오류로 분류하세요.
5. 결과가 나쁠 때 Prompt만 수정하는 접근의 한계를 설명하세요.
6. Error Analysis 결과를 Tuning 우선순위로 연결하는 방법을 설명하세요.
7. 변경 전후 성능을 공정하게 비교하려면 무엇을 고정해야 하는지 설명하세요.
8. 정량 Metric과 Human Evaluation을 함께 써야 하는 Scenario를 설명하세요.
9. False Success, 즉 실패했는데 성공으로 판정하는 문제의 위험을 설명하세요.
10. Evaluation Threshold 미달 시 Retry, Stop, Escalate 중 무엇을 선택할지 판단 기준을 작성하세요.

## 완료 기준

- [ ] Metric / Dataset / Threshold 설명
- [ ] Failure Taxonomy 사용
- [ ] 개선 전후 동일 기준 비교

[← 이전](../030-memory-state-execution/README.md) · [다음 →](../050-multi-agent-coordination/README.md)
