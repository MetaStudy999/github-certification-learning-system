# Mock 시험 01 — 정답 (Mock Exam 01 — Answers, MEA)

| Q | Ans | 핵심 이유 |
|---:|:---:|---|
| 1 | B | Workflow가 전체 자동화 흐름을 정의 |
| 2 | A | `needs`는 Job Dependency |
| 3 | A | `workflow_dispatch`는 수동 실행 |
| 4 | A | `workflow_call`은 Reusable Workflow 호출 진입점 |
| 5 | A | `run`은 Shell 명령 실행 |
| 6 | A | `uses`는 Action 호출 |
| 7 | C | 2×2 = 4 |
| 8 | A | `exclude`로 조합 제거 |
| 9 | A | Service Container는 DB 등 보조 서비스 |
| 10 | A | `concurrency`로 중복 실행 제어 |
| 11 | A | Trigger/Filter가 실행 여부의 시작점 |
| 12 | A | Skipped는 우선 `if`와 Context 확인 |
| 13 | A | API 권한 오류는 Token Permission 우선 |
| 14 | A | Runner 연결/Label/접근 범위 점검 |
| 15 | A | OS별 환경 차이를 Log로 비교 |
| 16 | A | Cache Key/Path가 핵심 |
| 17 | A | 실제 파일 생성 위치 확인 |
| 18 | A | 호출 값과 Input 정의 비교 |
| 19 | A | Composite Action은 Step 묶음 재사용 |
| 20 | A | Reusable Workflow는 Job/Workflow 구조 재사용 |
| 21 | A | Action Metadata는 `action.yml`/`action.yaml` |
| 22 | A | JavaScript Action은 Node 기반 |
| 23 | A | Docker Action은 Container 기반 |
| 24 | A | Output은 후속 로직에 값 전달 |
| 25 | A | Full SHA는 참조 불변성 강화 |
| 26 | A | GitHub-hosted는 GitHub가 환경 관리 |
| 27 | A | Self-hosted는 내부망 연결 요구에 적합할 수 있음 |
| 28 | A | 패치·보안은 사용자 책임 |
| 29 | A | Label로 Runner Capability 선택 |
| 30 | A | Runner Group으로 접근 범위 관리 |
| 31 | A | 허용 Action 정책은 공급망 위험 제어 |
| 32 | A | 중앙 Workflow로 정책 일관성 확보 |
| 33 | A | Org 범위 공통 설정 중앙화 |
| 34 | A | Governance는 여러 Resource에 최소 권한 적용 |
| 35 | A | 공유 Runner는 신뢰 경계 관리가 핵심 |
| 36 | A | 필요한 최소 권한만 부여 |
| 37 | A | OIDC는 장기 Cloud Key 의존 감소 |
| 38 | A | 외부 기여 코드가 Secret을 노출할 수 있음 |
| 39 | A | Cache=가속, Artifact=결과 보존/전달 |
| 40 | A | 여러 병목 요소를 함께 분석 |

## Score

- 36–40: 90–100% — EXAM-READY 후보
- 34–35: 85–87.5% — Gate 통과 후보
- 30–33: 75–82.5% — 약점 Domain 복습
- <30: 핵심 Lab 재수행
