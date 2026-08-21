# Final Mock — 질문 (Final Mock — Questions, FMQ)

> 자체 제작 40문항입니다. 목표는 90% 이상입니다.

1. `workflow_dispatch`와 가장 직접적으로 연결되는 것은? A 수동 실행 B Reusable Workflow 호출 C Runner Group D Artifact
2. Reusable Workflow 호출 Event는? A workflow_call B schedule C release D check_run
3. Job Dependency는? A needs B uses C with D env
4. Step에서 Action 호출은? A uses B run C needs D permissions
5. 동일 Group의 이전 실행을 취소하려면? A concurrency B artifact C matrix D secrets
6. PR에서는 Test, main Push에서는 Deploy를 하려면? A Event/Branch 조건과 if B 모든 Event Deploy C Workflow 삭제 D Secret 제거
7. 앞선 Job Output 참조는? A needs B steps C vars D runner
8. Matrix 조합 제거는? A exclude B include C restore-keys D outputs
9. Matrix 조합 추가는? A include B exclude C concurrency D permissions
10. Database Integration Test 보조 서비스는? A Service Container B Artifact C Cache D Runner Group
11. Workflow가 실행되지 않을 때 FIRST? A Trigger/Filter B Artifact C Cache D Secret
12. Step이 Skipped일 때 FIRST? A if/Context B Runner Group C README D Milestone
13. API 권한 오류에서 FIRST? A permissions B matrix C cache D artifact
14. Runner Queue 문제에서 FIRST? A Online/Label/Access B README C Secret 출력 D Workflow 삭제
15. Cache Miss 반복에서 FIRST? A Key/Path B Project View C License D Issue
16. Artifact 파일 없음 오류에서 FIRST? A 실제 생성 경로 B Enterprise 이름 C Star D Branch 보호
17. Step 묶음 재사용은? A Composite Action B Reusable Workflow C Runner Group D Environment
18. Job/Workflow 구조 재사용은? A Reusable Workflow B Composite Action C Cache D Artifact
19. Custom Action Metadata는? A action.yml B runner.ini C workflow.json D project.yml
20. Container Runtime을 고정하는 Custom Action은? A Docker Action B JavaScript Action C Composite D Reusable Workflow
21. Node 기반 Custom Action은? A JavaScript Action B Docker Action C Service Container D Matrix
22. Action Input의 목적은? A 호출자가 동작 구성 B Runner 생성 C Secret 공개 D Cache 삭제
23. Action Output의 목적은? A 결과값 전달 B Repo Visibility C Billing D Issue 관리
24. Third-party Action 신뢰 강화를 위한 가장 강한 참조 방식은? A Full Commit SHA B latest C main D 임의 Tag
25. 내부망 서비스 접근 요구가 크다면 고려할 Runner는? A Self-hosted B GitHub-hosted만 가능 C Runner 불필요 D Gist Runner
26. Self-hosted Runner 운영 책임은? A 패치/보안/모니터링 B GitHub가 전부 담당 C README D Issue
27. 특정 Capability Runner 선택은? A Label B Artifact C Cache D Secret
28. Runner 접근 범위 중앙 관리는? A Runner Group B Project C Wiki D Discussion
29. Ephemeral Runner의 장점은? A 상태 잔존 위험 감소 B Secret 불필요 C 무료 보장 D Workflow 불필요
30. Enterprise Actions Policy의 목적은? A 중앙 Governance B Git 대체 C PR 대체 D Cache 생성
31. 중앙 Reusable Workflow의 운영 핵심은? A 버전/호환성/변경 영향 관리 B 무조건 latest C 테스트 생략 D Secret 평문
32. Organization Secret/Variable의 장점은? A 공통 설정 중앙화 B 공개 강제 C Runner 생성 D Artifact 대체
33. `GITHUB_TOKEN` 권한 원칙은? A 최소 권한 B write-all C Admin 고정 D PAT 필수
34. 장기 Cloud Key 의존 감소 방식은? A OIDC B Cache C Artifact D Matrix
35. Fork PR에 Secret 제공 시 가장 중요한 것은? A 신뢰 경계 B Cache Key C Matrix 크기 D Project View
36. Action Full SHA Pinning의 목적은? A 참조 코드 변경 위험 감소 B Runner 가속 C Artifact 압축 D Secret Rotation
37. Cache와 Artifact 구분은? A 실행 가속 vs 결과 보존/전달 B 둘 다 Secret C 둘 다 Runner D 동일
38. 느린 Workflow 최적화에서 올바른 접근은? A 병목 측정 후 Cache/Matrix/Concurrency/Dependency 개선 B 모든 Job 하나로 C Log 삭제 D Self-hosted 강제
39. Reusable Workflow와 Composite Action 구분 기준은? A Job/Workflow vs Step 묶음 B OS 종류 C Repo Visibility D Issue 수
40. GH-200 최종 준비에서 가장 적절한 것은? A Domain-Lab-Question-Mock-오답 반복 B Brain Dump 암기 C YAML만 암기 D 실습 생략
