# 020 Confusion Matrix — 헷갈리는 개념 비교

| A | B | 시험 판단 기준 |
|---|---|---|
| Workflow | Action | 전체 자동화 흐름 vs 재사용 기능 단위 |
| Job | Step | Runner 단위 vs Job 내부 단계 |
| `workflow_dispatch` | `workflow_call` | 수동 실행 vs 다른 Workflow 호출 |
| `run` | `uses` | Shell 실행 vs Action 호출 |
| `needs` | `if` | Job Dependency vs 실행 조건 |
| `github` Context | `runner` Context | Event/Repo 정보 vs Runner 정보 |
| `steps` Context | `needs` Context | 같은 Job Step Output vs 선행 Job Output |
| Matrix `include` | `exclude` | 조합 추가 vs 제거 |
| Cache | Artifact | 실행 가속 vs 결과 보존·전달 |
| Service Container | Container Job | 보조 서비스 vs Job 실행환경 |
| Reusable Workflow | Composite Action | Job/Workflow 재사용 vs Step 묶음 |
| JavaScript Action | Docker Action | Node 기반 실행 vs Container 기반 실행 |
| GitHub-hosted Runner | Self-hosted Runner | GitHub 관리 vs 사용자 관리 |
| Runner Label | Runner Group | 실행 대상 선택 vs 접근·정책 그룹화 |
| Variable | Secret | 일반 설정값 vs 민감정보 |
| `GITHUB_TOKEN` | PAT | Workflow 자동 Token vs 사용자/앱 범위 Token |
| OIDC | Access Key | 단기 연합 인증 vs 장기 Secret |
| Tag Pinning | Full SHA Pinning | 사람이 읽기 쉬움 vs 변경 불변성 강화 |
| `success()` | `always()` | 성공 시 vs 이전 상태와 무관한 실행 |
| Event Filter | Job `if` | Workflow/Trigger 범위 축소 vs Job 실행 판단 |

## 사용법

1. 왼쪽과 오른쪽을 각각 한 문장으로 정의합니다.
2. 상황 예시를 하나씩 만듭니다.
3. 실제 문제에서는 **기능 이름보다 요구사항의 목적**을 먼저 찾습니다.
