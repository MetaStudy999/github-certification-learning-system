# GH-600 Final Mock — 질문 (GH-600 Final Mock — Questions, GH-600FMQ)

> 자체 제작 40문항. 목표 점수 **90%+**.

1. Agent가 실행 전에 단계와 위험을 구조화해 출력한다. 이는? A State B Structured Plan C Memory D Eval
2. 계획이 승인되기 전 외부 변화가 일어나지 않게 하는 설계는? A Tool 확대 B Planning/Execution 분리 C Memory 공유 D Multi-Agent
3. Agent Goal이 모호할 때 가장 먼저 할 일은? A 권한 확대 B 성공 기준과 입력을 명확화 C Tool 추가 D 무한 Retry
4. 되돌리기 어려운 고위험 작업의 자율성은? A 더 강한 Review/Gate 필요 B 항상 최대 C 사람 제거 D Eval 제거
5. 실행 중 생성된 Plan/Result Artifact가 중요한 이유는? A Audit/Review/Observability B 권한 확대 C Tool 수 증가 D Memory 삭제
6. Agent가 필요한 기능보다 넓은 권한을 가진다. 가장 관련된 원칙은? A Least Privilege 위반 B Evaluation C Checkpoint D Handoff
7. MCP의 역할은? A Memory 저장 B 도구·Context 연결 표준 C 평가 Metric D Human Review
8. MCP Allow List가 필요한 이유는? A 허용 연결 범위 제한 B 모든 연결 확대 C State 삭제 D Tool 자동 생성
9. Tool 결과가 검증되지 않았는데 다음 단계로 진행한다. 가장 큰 문제는? A 검증 Gate 부족 B Memory 과다 C Agent 수 부족 D UI 문제
10. 특정 Branch 안에서만 Agent가 작업하도록 제한한다. 관련 개념은? A Scope B Memory C Evaluation D Campaign
11. CI 환경에서 Agent의 성공 증거로 적절한 것은? A 검증 결과 Artifact B 실제 비밀번호 C 임의 Token D 무관 로그 전체
12. Agent가 환경 전제가 깨졌는데 기존 계획을 계속 사용한다. 개선은? A Replan/Review B 권한 확대 C Tool 추가 D State 삭제
13. Memory와 State의 올바른 비교는? A 장기 재사용 정보 vs 현재 실행 상황 B 동일 C Tool vs MCP D Plan vs Eval
14. 작업 중단 후 저장 상태에서 이어가는 것은? A Retry B Resume C Restart always D Delegation
15. 같은 작업 재시도 시 중복 부작용 방지와 관련된 것은? A Idempotency B Few-shot C Registry D Artifact retention
16. State가 예상과 다르다. 가장 안전한 동작은? A 검증 없이 계속 B 중단하고 State 확인 C 권한 확대 D 로그 삭제
17. Evaluation의 핵심 요소는? A Metric/Dataset/Threshold/Evidence B Tool 수 C Agent 수 D Memory 길이
18. Agent가 틀린 결과를 냈지만 성공 판정되었다. 이것은? A False Success B Handoff C Checkpoint D Registry
19. Error Analysis에서 가장 먼저 할 것은? A 실패 원인 유형화 B Prompt 무조건 변경 C Tool 무조건 추가 D 권한 확대
20. Context 부족이 원인이라면 가장 적절한 Tuning은? A Context 선정 개선 B Human Review 제거 C 모든 Tool 허용 D State 삭제
21. 동일 개선 전후를 비교할 때 필요한 것은? A 통제된 동일 평가 기준 B 매번 다른 평가 C 점수 숨김 D 로그 삭제
22. Multi-Agent가 유리한 상황은? A 전문 역할 분리와 독립 검증의 가치가 복잡성보다 큼 B 모든 간단 작업 C 역할이 하나 D 조정이 전혀 필요 없음
23. Delegation은? A 작업 일부 위임 B 책임/Context 전체 전달만 C Tool Protocol D State 저장
24. Handoff Artifact의 핵심 내용은? A 현재 상태·완료 결과·남은 작업·Context B 실제 Secret C 관리자 권한 D 무관 로그
25. 두 Agent가 상반된 결론을 낸다. 가장 적절한 것은? A 둘 다 자동 반영 B Conflict Rule/Human Review C 로그 제거 D 권한 확대
26. Shared Context를 최소화하는 장점은? A 불필요 노출·혼선·비용 감소 B Agent 수 증가 C Tool 권한 증가 D Eval 제거
27. 한 Agent 오류가 전체 실행으로 번지는 것을 제한하는 설계는? A Failure Boundary B Long-term Memory C Registry D Prompt File
28. Guardrail의 주된 목적은? A 행동 제한·검증 B Agent 수 증가 C 권한 확대 D 사람 제거
29. HITL은? A 중요 단계에 사람이 승인·판단 B 모든 실행 자동 C Tool Protocol D Memory
30. HOTL은? A 사람이 감독하고 필요 시 개입 B 모든 단계 직접 실행 C State 삭제 D Eval 제거
31. 높은 위험에서 Human Review를 더 강하게 두는 기준은? A Risk/Reversibility B Agent 이름 C Star 수 D Tool 수
32. Accountability에 필요한 것은? A 입력·Plan·Tool·결과·검토 추적 B 결과만 C Tool 이름만 D Agent 이름만
33. Guardrail이 과도하면 발생할 수 있는 것은? A Delivery 지연/Review 부담 B 위험 0 보장 C Memory 삭제 D Tool 증가
34. Policy 위반 가능성이 탐지되었다. 적절한 동작은? A Stop/Review/Escalate B 무조건 계속 C 권한 확대 D 기록 삭제
35. Agent 자율성과 안전을 함께 높이려면? A 평가·가드레일·관찰가능성을 함께 설계 B 사람 제거 C Tool 수 최대화 D Scope 확대
36. GitHub를 Agentic SDLC의 Control Plane으로 보는 관점은? A 개발 Workflow·Artifact·Review와 Agent 활동을 연결해 관리 B GitHub가 LLM 자체 C GitHub가 Memory만 제공 D GitHub가 모든 책임 대체
37. `CONTENT-READY`의 의미는? A Repository 학습 콘텐츠 준비 완료 B 시험 합격 C 실제 학습 완료 D EXAM-READY와 동일
38. `EXAM-READY`에 가까운 상태는? A 실제 Gate 기준 통과 B 문서 생성 완료 C 시험 날짜 도래 D Tool 설치
39. GH-600 학습에서 피해야 할 접근은? A 자율성만 최대화하고 평가·Guardrail 생략 B 성공 기준 정의 C Sandbox 사용 D Human Review 설계
40. 시험 직전 최종 판단은? A 최신 공식 범위와 최근 Mock/오답 Gate 확인 B 무조건 응시 C 실습 생략 D 비공식 복원문제만 암기
