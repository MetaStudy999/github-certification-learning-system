# Mock Exam 01 — Questions

> 자체 제작 40문항입니다. 정답은 `answers.md`에서 확인합니다.

1. Workflow 전체 자동화 흐름을 구성하는 기본 단위는? A Step B Workflow C Runner D Artifact
2. `build` 후 `test` Job을 실행할 때 필요한 것은? A needs B uses C env D permissions
3. 수동 실행을 위한 Event는? A workflow_dispatch B workflow_call C schedule D release
4. 다른 Workflow에서 호출 가능한 Reusable Workflow를 만들 때 사용하는 Event는? A workflow_call B push C pull_request D workflow_run
5. Job 내부 Shell 명령 실행 키워드는? A run B uses C with D needs
6. 외부 Action 호출 키워드는? A uses B run C env D on
7. Ubuntu/Windows × Python 3.11/3.12 Matrix의 기본 조합 수는? A2 B3 C4 D6
8. Matrix 특정 조합을 제외하는 기능은? A exclude B include C needs D concurrency
9. Integration Test용 PostgreSQL을 Job 옆에서 실행할 때 적합한 것은? A Service Container B Artifact C Cache D Runner Group
10. 중복 Workflow 실행을 줄이기 위한 기능은? A concurrency B secrets C outputs D vars
11. Workflow가 시작되지 않을 때 FIRST 확인할 것은? A Trigger/Filter B Artifact C Cache D README
12. Step이 Skipped 됐을 때 가장 먼저 볼 것은? A if와 Context B Runner Group C Artifact D Issue
13. Permission 관련 API 오류가 발생하면 우선 확인할 것은? A Token permissions B Matrix C Cache D Milestone
14. Self-hosted Runner Job이 Queue 상태일 때 확인할 것은? A Online/Label/Access B README C Project D Artifact Name
15. Windows Matrix에서만 실패할 때 가장 좋은 진단은? A OS별 Shell/Path Log 비교 B Matrix 삭제 C Secret 공개 D Workflow 삭제
16. Cache Miss가 반복될 때 확인할 것은? A Key/Path B Issue Label C Runner Group D PR Title
17. Artifact Upload 실패 시 우선 확인할 것은? A 생성 경로 B Enterprise Name C Star D License
18. Reusable Workflow Input Type 오류 시 확인할 것은? A 호출부와 workflow_call inputs B Cache C Artifact D Runner Label
19. 반복되는 Step 묶음을 재사용하려면? A Composite Action B Runner Group C Artifact D Matrix
20. 여러 Repository에서 동일 CI Job 구조를 공유하려면? A Reusable Workflow B Cache C Gist D Project
21. Action Metadata 파일은? A action.yml B workflow.ini C runner.json D project.yml
22. Node 기반 Custom Action 유형은? A JavaScript Action B Docker Action C Service Container D Reusable Workflow
23. 고정 Runtime을 Container로 묶는 Action은? A Docker Action B Composite C Matrix D Cache
24. Action Output의 목적은? A 후속 로직에 결과 전달 B Runner 생성 C Secret 공개 D Branch 보호
25. 외부 Action을 Full SHA로 고정하는 이유는? A 코드 참조 변경 위험 감소 B Job 수 증가 C Cache 증가 D Artifact 압축
26. GitHub-hosted Runner 특징은? A GitHub가 환경 관리 B 사용자가 항상 OS 패치 C 내부망 자동접근 D Runner Group 필수
27. 내부망 DB 접근에 적합할 수 있는 Runner는? A Self-hosted B GitHub-hosted가 항상 정답 C Runner 불필요 D Gist
28. Self-hosted Runner의 운영 책임에 포함되는 것은? A OS 패치/보안 B README C Issue D Star
29. GPU Runner 선택에 유용한 것은? A Runner Label B Artifact C Cache D Milestone
30. Runner 접근 범위 중앙 관리에 유용한 것은? A Runner Group B Wiki C Discussion D Gist
31. Enterprise에서 허용 Action을 제한하는 이유는? A 공급망 위험 감소 B Commit 금지 C PR 삭제 D Issue 정리
32. 중앙 Reusable Workflow의 장점은? A 공통 정책 일관성 B Git 불필요 C Secret 공개 D Runner 제거
33. Organization 공통 Secret/Variable의 장점은? A 여러 Repo 중앙 관리 B 모든 값 공개 C Runner 삭제 D Cache 대체
34. Enterprise Governance에서 최소 권한 대상은? A Token/Runner/Secret/Workflow B README C Star D Wiki
35. Self-hosted Runner 공유 시 중요한 통제는? A 신뢰 경계/접근 범위 B Star C Label Color D Issue Template
36. GITHUB_TOKEN 권한 설계 원칙은? A 최소 권한 B 항상 write-all C Admin 고정 D Token 금지
37. 장기 Cloud Secret 의존을 줄이는 방식은? A OIDC B Cache C Artifact D Matrix
38. Fork PR에 Secret을 무조건 제공하면 위험한 이유는? A 외부 코드가 탈취 가능 B Matrix 느림 C Artifact 없음 D Git 손상
39. Cache와 Artifact 차이는? A 실행 가속 vs 결과 보존 B 둘 다 Secret C 둘 다 Runner D 차이 없음
40. Workflow 최적화에 적절한 조합은? A Cache/Matrix/Concurrency/Dependency 분석 B Log 삭제 C Secret 코드 저장 D 모든 Job 통합
