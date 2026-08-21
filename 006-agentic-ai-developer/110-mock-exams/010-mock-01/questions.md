# GH-600 Mock 시험 01 — 질문 (GH-600 Mock Exam 01 — Questions, GH-600MEQ)

> 자체 제작 40문항. 실제 시험문제를 복제하지 않습니다.

1. Agent 설계에서 가장 먼저 명확히 해야 할 것은? A Tool 수 B Goal/Input/Success Criteria C Memory 크기 D UI
2. Planning과 Execution을 분리하는 주된 이유는? A 계획 검토와 승인 가능 B Tool 제거 C Memory 삭제 D 비용 제거
3. Structured Plan에 가장 적절한 내용은? A 비밀번호 B 단계·위험·예상 산출물·성공 기준 C 무관 로그 D 임의 Token
4. Agent 자율성 수준을 결정할 핵심 기준은? A Risk와 Reversibility B 이름 길이 C Star 수 D README 길이
5. Human Review가 가장 필요한 상황은? A 영향이 크고 되돌리기 어려운 결정 B 용어 정의 읽기 C 문서 제목 확인 D 낮은 위험 요약
6. Agent Anti-pattern에 가까운 것은? A 명확한 Stop Condition B 성공 기준 없는 무제한 실행 C 제한된 Scope D Evaluation
7. Inspectable Artifact의 장점은? A 검토·재현·감사 가능 B 모든 오류 제거 C 권한 자동 확대 D 사람 제거
8. Tool 선택 시 가장 먼저 물어야 할 질문은? A 가장 강한 Tool인가 B 목표에 실제 필요한가 C 가장 최신 Tool인가 D 가장 많은 권한인가
9. Least Privilege의 의미는? A 필요한 최소 범위만 허용 B 모든 권한 허용 C 관리자 기본 D 감사 제거
10. MCP의 핵심 역할은? A Agent와 외부 도구·Context 연결 표준 B Memory 구조 C 평가 점수 D Branch 정책
11. MCP Registry의 개념적 역할은? A 자원 발견·관리 B Secret 저장 C Test 작성 D State 삭제
12. Allow List를 사용하는 이유는? A 허용된 연결을 제한 B 모든 연결 허용 C 로그 제거 D Memory 확장
13. Read-only Scope로 충분한 작업에 더 높은 권한을 주면? A 위험 증가 B 항상 성능 향상 C 평가 향상 D Memory 증가
14. Tool 결과가 예상과 다르면? A 무조건 계속 B 검증 후 Stop/Replan/Escalate 판단 C 권한 확대 D 로그 삭제
15. Repository Scope와 Branch Scope의 차이는? A 전체 저장소 범위 vs 특정 Branch 제한 B 동일 C Tool vs MCP D State vs Memory
16. 환경 제약이 충족되지 않을 때 적절한 동작은? A 안전한 중단 또는 Escalation B 무조건 실행 C 권한 확대 D 평가 삭제
17. CI Context에서 중요한 것은? A 결과와 검증 Artifact B 실제 비밀번호 C 임의 Token D UI 색상
18. Scope를 좁히는 주된 이유는? A Blast Radius와 불필요 접근 감소 B Memory 삭제 C Tool 수 증가 D 사람 제거
19. Memory와 State의 차이는? A 재사용 정보 vs 현재 실행 상황 B 동일 C Tool vs MCP D Plan vs Eval
20. Checkpoint의 목적은? A 상태 저장과 복구 지점 B 권한 확대 C Tool 추가 D 평가 제거
21. Retry와 Resume의 차이는? A 다시 시도 vs 저장 상태에서 이어가기 B 동일 C Memory vs Tool D Eval vs State
22. Idempotency가 중요한 이유는? A 재시도 중복 부작용 감소 B Memory 증가 C Tool 확대 D 로그 제거
23. State 불일치를 발견했다. 가장 적절한 것은? A 계속 실행 B 중단하고 검증 C 권한 확대 D 평가 제거
24. Evaluation의 목적은? A 결과 품질·안전·성공 판단 B Tool 수 증가 C Memory 삭제 D 권한 확대
25. Task Success 하나만 보면 부족한 이유는? A Correctness/Safety/Efficiency도 필요 B 항상 100%라서 C Tool과 동일 D State와 동일
26. 실패 Scenario를 평가 Dataset에 넣는 이유는? A 예외 상황 안정성 확인 B 점수 낮추기 C 로그 제거 D Tool 증가
27. False Success는? A 실패했는데 성공으로 판정 B Tool 실패 C Memory 만료 D Branch 삭제
28. Error Analysis의 첫 단계는? A 원인 유형 분류 B 권한 확대 C Tool 무조건 추가 D 평가 삭제
29. 결과가 나쁘다고 Prompt만 수정하면 부족한 이유는? A 원인이 Tool/State/Eval일 수 있음 B Prompt는 항상 완벽 C Tool이 없음 D Agent가 없음
30. Tuning의 올바른 흐름은? A Error Analysis→Change→Re-evaluate B Change만 반복 C 권한 확대 D 로그 삭제
31. Multi-Agent가 유리한 경우는? A 서로 다른 역할과 독립 검증의 가치가 클 때 B 모든 작업 C 단순 요약 D 역할이 하나일 때
32. Delegation과 Handoff의 차이는? A 작업 일부 위임 vs 책임/Context 전달 B 동일 C Tool vs MCP D Eval vs State
33. Agent 간 결과가 충돌하면? A 둘 다 실행 B 사전 정의 Rule 또는 Human Review C 로그 삭제 D 권한 확대
34. Shared Context를 최소화하는 이유는? A 불필요 노출·혼선·비용 감소 B Tool 삭제 C Eval 제거 D Memory 증가
35. Failure Boundary의 목적은? A 한 Agent 실패의 불필요한 확산 제한 B 모든 Agent 중단 C 로그 제거 D 권한 증가
36. Guardrail의 목적은? A 행동 제한·검증으로 위험 감소 B Tool 수 증가 C 사람 제거 D Memory 삭제
37. HITL은? A 중요한 실행 단계에서 사람이 승인·판단 B 사람 완전 제거 C Memory D MCP
38. HOTL은? A Agent 실행을 감독하고 필요 시 개입 B 모든 단계 수동 승인 C Tool 삭제 D State 삭제
39. Accountability에 필요한 것은? A 입력·계획·도구·결과·검토 기록 B Agent 이름만 C 결과만 D Tool 이름만
40. GH-600의 핵심 사고방식은? A 자율성만 최대화 B 자율성+검증+통제+책임성을 함께 설계 C Tool 수 최대화 D Human Review 제거
