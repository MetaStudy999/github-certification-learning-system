# 010 프로젝트 Rubric — CI/CD 자동화 프로젝트 (010 Project Rubric — CI/CD Automation Project, PRCICDAP)

| 영역 | 평가 항목 | 배점 |
|---|---|---:|
| Workflow | Event, Job, Dependency 구조가 명확함 | 15 |
| Test | Lint/Test가 재현 가능하게 실행됨 | 15 |
| Matrix | 버전 또는 OS Matrix를 목적에 맞게 사용 | 10 |
| Artifact/Cache | 두 기능을 목적에 맞게 구분 | 10 |
| Reuse | Reusable Workflow 또는 Composite Action 활용 | 10 |
| Runner | Runner 선택 이유를 설명 | 10 |
| Security | 최소 권한, Secret, Pinning, OIDC 설계 | 15 |
| Troubleshooting | 실패 재현 → Log 분석 → 수정 Evidence | 10 |
| Documentation | README에 구조와 검증 방법 기록 | 5 |
| **합계** |  | **100** |

## 판정

- 90–100: CLEAR 후보
- 80–89: PASS
- 70–79: 보완 후 재평가
- <70: 핵심 Lab 재수행

## 필수 실패 조건

다음 중 하나라도 있으면 점수와 무관하게 보완합니다.

- Secret을 Repository 코드에 평문 저장
- `GITHUB_TOKEN`에 불필요한 광범위 권한 부여
- 외부 Action 신뢰/버전 정책을 전혀 설명하지 못함
- Workflow 성공 여부를 검증하지 않음
