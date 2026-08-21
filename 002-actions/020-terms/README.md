# 020 Terms — GitHub 액션 (GitHub Actions, GHACT / GH-200) 핵심 용어

## 빠른 시작 (Quick Start, QS)

용어는 영어 원문 + 한국어 뜻 + 한 문장 역할로 익힙니다.

| Term | 한국어 | 핵심 역할 |
|---|---|---|
| Workflow | 워크플로 | 하나 이상의 Job을 정의한 자동화 절차 |
| Event | 이벤트 | Workflow 실행을 유발하는 사건 |
| Trigger | 트리거 | 실행 조건 |
| Job | 작업 단위 | 동일 Runner에서 실행되는 Step 묶음 |
| Step | 단계 | Job 내부의 개별 실행 단계 |
| Action | 액션 | 재사용 가능한 자동화 구성요소 |
| Runner | 실행기 | Job을 실제 실행하는 머신/환경 |
| Context | 컨텍스트 | Workflow 실행 중 접근 가능한 메타데이터 |
| Expression | 표현식 | `${{ }}` 형태로 조건·값을 평가 |
| Secret | 비밀값 | 민감한 설정값 저장 |
| Variable | 변수 | 일반 설정값 저장 |
| Environment | 환경 | 배포 대상과 보호 규칙을 묶는 단위 |
| Matrix | 매트릭스 | 여러 OS·버전 조합으로 Job 확장 |
| Artifact | 아티팩트 | Workflow 결과 파일 저장·전달 |
| Cache | 캐시 | 의존성 등 재사용으로 실행시간 단축 |
| Reusable Workflow | 재사용 워크플로 | `workflow_call`로 다른 Workflow에서 호출 |
| Composite Action | 복합 액션 | 여러 Step을 하나의 Action으로 재사용 |
| Self-hosted Runner | 자체 호스팅 Runner | 사용자가 직접 관리하는 Runner |
| GITHUB_TOKEN | GitHub 토큰 | Workflow 실행에 자동 제공되는 저장소 범위 토큰 |
| OIDC | OpenID Connect | 장기 Cloud Secret 없이 단기 자격 증명 연계 |
| Attestation | 증명 | Artifact 출처·빌드 Provenance 확인 |

## 반드시 구분

- Workflow vs Action
- Job vs Step
- Variable vs Secret
- Cache vs Artifact
- Reusable Workflow vs Composite Action
- GitHub-hosted vs Self-hosted Runner
- `GITHUB_TOKEN` vs 별도 PAT

## 완료 기준

위 핵심 용어를 자료 없이 1문장씩 설명할 수 있어야 합니다.
