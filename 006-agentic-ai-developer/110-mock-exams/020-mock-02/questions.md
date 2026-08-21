# GH-600 Mock 시험 02 — 질문 (GH-600 Mock Exam 02 — Questions, GH-600MEQ)

> 자체 제작 Scenario 40문항.

1. Agent가 Issue를 처리하기 전 계획서를 출력하고 Reviewer 확인을 기다린다. 이 설계의 핵심 원칙은? A Planning/Execution 분리 B Memory 삭제 C Tool 확대 D Multi-Agent 강제
2. 성공 기준이 없는 Agent가 계속 추가 작업을 수행한다. 가장 먼저 보완할 것은? A Stop/Success Criteria B Tool 수 C Memory 길이 D Agent 이름
3. 실행 전 계획에 필요한 도구 범주와 예상 산출물을 기록한다. 주된 이점은? A 검토 가능성 B 권한 확대 C 평가 제거 D 로그 축소
4. 위험이 낮고 쉽게 되돌릴 수 있는 작업과 높은 위험 작업의 자율성은? A 동일 B Risk에 따라 다르게 설계 C 항상 최대 D 항상 0
5. Agent의 계획이 요구사항과 맞지 않는다. 가장 적절한 흐름은? A 실행 B Revise/Review 후 다시 검증 C 권한 확대 D Tool 추가만
6. Repository 내용을 읽기만 하면 되는 Agent에 필요한 것은? A 필요한 읽기 범위 중심 설계 B 관리자 권한 C 모든 Organization 권한 D 감사 제거
7. Tool 선택 기준으로 가장 부적절한 것은? A 목표 필요성 B 최소 Scope C 신뢰 경계 D 권한이 강할수록 좋음
8. MCP 연결 후보가 여러 개다. 우선 고려할 것은? A 출처·기능·허용 정책·Scope B 이름 길이 C UI 색상 D Star 수
9. 허용된 MCP 연결만 쓰도록 제한하는 개념은? A Allow List B Memory C Checkpoint D Eval
10. Tool 결과가 검증 기준을 만족하지 못한다. Agent는? A 무조건 계속 B Stop/Replan/Escalate 중 정책에 맞게 선택 C 권한 확대 D 로그 제거
11. Agent 실행을 특정 Branch 범위로 제한하는 목적은? A 불필요한 영향 범위 감소 B Memory 확장 C 평가 제거 D Tool 수 증가
12. Sandbox를 학습 환경으로 쓰는 이유는? A 실험 영향 제한 B 성능 무조건 증가 C Agent가 필수 요구 D Memory 제거
13. CI 결과 요약 Agent의 Evidence로 적절한 것은? A 실행 결과·검증 기준·요약 Artifact B 실제 비밀번호 C 무관한 로그 전체 D 익명 변경
14. 현재 작업의 완료 단계와 다음 단계를 추적하는 것은? A State B Long-term Memory C Guardrail D Registry
15. Checkpoint가 특히 유용한 경우는? A 장시간·다단계 작업 재개 B 한 문장 요약 C Tool 이름 변경 D UI 설정
16. Retry가 반복 부작용을 만들 수 있다. 관련 설계 개념은? A Idempotency B Few-shot C Branch Name D Markdown
17. 실행 상태가 예상과 불일치한다. 가장 안전한 대응은? A 계속 실행 B 중단·상태 검증 C Tool 권한 확대 D 평가 삭제
18. 과거 Memory가 오래되어 잘못된 판단을 유도한다. 개선은? A Memory 최신성/검증 정책 B Tool 추가 C Human Review 삭제 D State 삭제
19. Agent 결과가 정확하지만 정책 위반이다. 평가 결과는? A 성공 B 안전성 기준 때문에 실패 C 무조건 통과 D 평가 불가
20. Evaluation Dataset에 모호한 요구사항을 넣는 목적은? A 불확실성 대응 평가 B 점수 낮추기 C Tool 삭제 D Memory 제거
21. Agent가 실패했지만 Success Metric이 통과한다. 이것은? A False Success B Tool Failure C Checkpoint D Handoff
22. 결과 품질 저하 원인이 Context 부족으로 보인다. 적절한 Tuning은? A Context 선정 개선 B 권한 확대 C 모든 Tool 추가 D 평가 제거
23. Plan 단계가 반복적으로 누락된다. 개선 후보는? A Plan Template/Validation B Memory 삭제 C Tool 확대 D 로그 제거
24. 동일 수정 후 성능을 비교하려면? A 동일한 평가 기준/셋 사용 B 매번 다른 기준 C 점수 숨김 D 평가 생략
25. 서로 다른 두 Agent가 같은 작업을 중복 수행한다. 문제는? A 역할 경계 불명확 B Memory 부족 C MCP 없음 D Guardrail 과다
26. Reviewer Agent로 작업을 넘길 때 필요한 것은? A Handoff Artifact B 관리자 권한 C 모든 Memory D 실제 Secret
27. 두 Agent의 결론이 충돌한다. 적절한 것은? A 둘 다 자동 적용 B Conflict Rule/Human Review C 로그 제거 D 권한 확대
28. Multi-Agent를 쓰지 않아도 되는 단순 작업에 여러 Agent를 쓰면? A 조정 복잡성 증가 B 항상 품질 향상 C 비용 감소 보장 D State 불필요
29. 한 Agent 오류가 전체 실행을 망가뜨리는 것을 줄이는 것은? A Failure Boundary B Tool 확대 C Memory 삭제 D Eval 제거
30. Agent 역할 분리의 주된 장점은? A 전문화·독립 검증 가능 B 권한 최대화 C 로그 제거 D Human Review 삭제
31. 중요한 변경 전 사람 승인을 요구하는 구조는? A HITL B HOTL만 C Memory D MCP Registry
32. Agent가 실행하되 사람이 관찰하고 필요 시 중단할 수 있다. A HOTL B HITL only C SBOM D SARIF
33. Guardrail이 필요한 이유는? A 행동 경계·정책 준수·위험 제한 B Tool 수 증가 C Agent 속도만 증가 D 사람 제거
34. Guardrail이 지나치게 강하면? A Delivery 지연·Alert fatigue 가능 B 위험 0 보장 C Memory 삭제 D Tool 증가
35. Accountability Artifact에 포함할 항목은? A 입력·계획·Tool 범주·결과·검토 B Agent 이름만 C 결과만 D Tool 이름만
36. Policy 위반 가능성이 탐지되었다. 적절한 흐름은? A Stop/Review/Escalate B 계속 실행 C 권한 확대 D 기록 삭제
37. Human Reviewer가 모든 사소한 단계에 개입해 병목이 생긴다. 개선 원칙은? A Risk 기반 Review 위치 조정 B 사람 완전 제거 C Tool 최대화 D Eval 삭제
38. Agent 자율성과 안전의 균형을 판단하는 가장 좋은 기준은? A 위험·가역성·검증 가능성 B Agent 수 C Tool 수 D Memory 길이
39. GH-600에서 GitHub를 Control Plane으로 본다는 의미에 가까운 것은? A Agent 활동이 개발 Workflow·Artifact·Review와 연결되어 관리됨 B GitHub가 LLM 자체임 C GitHub가 Memory만 저장 D GitHub가 모든 판단 수행
40. 시험 준비 Gate로 가장 적절한 것은? A 공식 범위+Labs+QBank+Mock+오답 재검증 B 용어만 암기 C 실습 생략 D 유출문제 수집
