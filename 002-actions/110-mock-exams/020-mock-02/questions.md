# Mock 시험 02 — 질문 (Mock Exam 02 — Questions, MEQ)

> 자체 제작 40문항입니다. 정답은 `answers.md`에서 확인합니다.

1. PR 생성 시에만 Workflow를 실행하려면? A pull_request B push C schedule D release
2. `main` Branch Push에서만 Deploy Job을 실행하려면 적절한 것은? A Branch/Event 조건과 Job if B 모든 Event Deploy C Secret 제거 D Runner 삭제
3. 같은 Job의 앞선 Step Output 참조 Context는? A steps B needs C matrix D vars
4. 선행 Job Output 참조 Context는? A needs B steps C github D runner
5. 실패한 경우에만 진단 Step을 실행하려면? A failure() B always() C success() D contains()
6. Cleanup을 이전 결과와 관계없이 실행하려면? A always() B success() C failure() D hashFiles()
7. Matrix 조합을 추가할 때? A include B exclude C needs D permissions
8. Cache 대체 Key 탐색에 사용하는 것은? A restore-keys B outputs C services D concurrency
9. Build 산출물을 다음 Job에 전달하려면? A Artifact B Cache C Secret D Variable
10. Dependency 설치 재사용으로 속도를 높이려면? A Cache B Artifact C Runner Group D Environment
11. `Resource not accessible by integration`가 발생했다. FIRST 조치는? A permissions 확인 B Artifact 삭제 C Cache 삭제 D Matrix 확대
12. Job이 Queue에 머문다. FIRST 조치는? A runs-on Label/Runner 상태 확인 B Secret 출력 C Workflow 삭제 D Issue 생성
13. Workflow는 실행되지만 Step이 건너뛰어졌다. FIRST 확인은? A if 조건 B Artifact C Project D README
14. `workflow_call` Input Type 오류가 난다. 무엇을 비교해야 하는가? A 호출값과 Input 정의 B Cache Key C Runner Group D License
15. Service Container가 연결되지 않는다. 무엇을 확인해야 하는가? A 서비스 설정/Port/Network 사용 방식 B README C Star D Milestone
16. 외부 Action 업데이트 후 실패가 시작됐다. 무엇을 확인할까? A Action 참조 버전 B Issue Label C Artifact Name D Organization Name
17. 여러 Step을 재사용 가능한 기능 단위로 만들려면? A Composite Action B Reusable Workflow만 가능 C Runner Group D Matrix
18. 여러 Job을 포함한 공통 CI를 재사용하려면? A Reusable Workflow B Composite Action C Cache D Secret
19. Reusable Workflow를 호출하는 위치로 가장 적절한 것은? A Job 수준 uses B Step run C Repository Settings D Issue
20. Custom Action의 입력값 정의는 주로 어디에? A action.yml B README C package cache D runner label
21. Node 기반 로직을 배포하는 Action은? A JavaScript Action B Docker Action C Service Container D Matrix
22. Container로 Runtime을 고정할 때? A Docker Action B Composite만 C Artifact D Environment
23. Composite Action에 적합한 사례는? A 반복 Shell Step 묶음 B Enterprise Policy C Runner OS 패치 D Secret Rotation
24. Action Output을 정의하는 이유는? A 후속 로직에 결과 제공 B Repo Visibility 변경 C Runner 생성 D Billing
25. Third-party Action 버전 안정성을 강화하려면? A Full SHA Pinning B latest C main Branch D 임의 Tag
26. GitHub-hosted Runner의 장점은? A 운영 부담 감소 B 내부망 자동 접근 C 모든 Tool 영구 고정 D 사용자 OS 패치 필요
27. Self-hosted Runner의 주요 장점은? A 네트워크/하드웨어 제어 B 보안 책임 없음 C 항상 무료 D GitHub가 OS 패치
28. Runner Label의 목적은? A 특정 Capability Runner 선택 B Secret 암호화 C Artifact 저장 D Branch 보호
29. Runner Group의 목적은? A 접근/정책 단위 관리 B Matrix 조합 C Cache Key D Workflow Trigger
30. Ephemeral Runner의 장점은? A 실행 후 상태 잔존 감소 B Secret 자동 생성 C Workflow 삭제 D Billing 제거
31. Enterprise Policy의 목적은? A Actions 사용 규칙 중앙 통제 B Git Commit 대체 C PR Review 대체 D Cache 생성
32. 중앙 Reusable Workflow 변경 시 중요한 것은? A 버전/호환성 관리 B 최신 main 무조건 강제 C 테스트 생략 D Secret 평문화
33. Org Secret/Variable의 목적은? A 여러 Repo 공통 설정 중앙화 B 모든 값 공개 C Runner 생성 D Artifact 암호화
34. Self-hosted Runner를 Public Repo에 무제한 제공하면 위험한 이유는? A 신뢰하지 않는 코드 실행 가능 B Git 사용 불가 C Matrix 불가 D Artifact 불가
35. Enterprise Governance에서 가장 적절한 접근은? A 최소 권한과 신뢰 경계 B 모든 권한 허용 C 모든 Log 제거 D Secret 하드코딩
36. Cloud 배포 장기 Key를 줄이는 방법은? A OIDC B Cache C Matrix D Artifact
37. `GITHUB_TOKEN` 기본 설계 원칙은? A 최소 권한 B Admin 고정 C write-all D PAT로 항상 교체
38. Fork PR Secret 노출 방지를 위해 중요한 것은? A 신뢰 경계와 Secret 제공 조건 B Cache 사용 C Artifact 이름 D Milestone
39. Full SHA Pinning의 목적은? A 참조 코드 변경 위험 감소 B 실행속도 향상 C Runner 수 증가 D Secret Rotation
40. 느린 Workflow를 개선하는 BEST 접근은? A 병목을 측정하고 Cache/Matrix/Concurrency/Dependency 최적화 B 모든 Job 삭제 C Secret 출력 D 모든 Runner Self-hosted
