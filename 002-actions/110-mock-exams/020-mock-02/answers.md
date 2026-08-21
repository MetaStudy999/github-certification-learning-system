# Mock 시험 02 — 정답 (Mock Exam 02 — Answers, MEA)

| Q | Ans | 핵심 이유 |
|---:|:---:|---|
| 1 | A | PR Event는 `pull_request` |
| 2 | A | Trigger/Branch와 Job 조건을 목적에 맞게 사용 |
| 3 | A | 같은 Job의 Step Output은 `steps` Context |
| 4 | A | 선행 Job Output은 `needs` Context |
| 5 | A | `failure()`는 실패 시 조건 |
| 6 | A | `always()`는 이전 결과와 무관하게 평가 |
| 7 | A | `include`로 Matrix 조합 추가 |
| 8 | A | `restore-keys`로 대체 Cache Key 탐색 |
| 9 | A | Artifact는 결과 보존/전달 |
| 10 | A | Cache는 의존성 재사용과 실행 가속 |
| 11 | A | API/Integration 오류는 권한부터 확인 |
| 12 | A | Queue 문제는 Runner 상태/Label/Access 확인 |
| 13 | A | Skipped Step은 `if` 조건 우선 |
| 14 | A | 호출값과 `workflow_call.inputs` 정의 비교 |
| 15 | A | Service 설정과 Port/Network 확인 |
| 16 | A | 외부 Action 참조 버전/변경 확인 |
| 17 | A | Composite Action은 Step 묶음 재사용 |
| 18 | A | Reusable Workflow는 Job/Workflow 구조 재사용 |
| 19 | A | 호출은 Job 수준 `uses` |
| 20 | A | Action Metadata에서 Input 정의 |
| 21 | A | JavaScript Action은 Node 기반 |
| 22 | A | Docker Action은 Container 기반 |
| 23 | A | 반복 Step 묶음에 Composite 적합 |
| 24 | A | Output은 후속 단계에 값 전달 |
| 25 | A | Full SHA로 참조 불변성 강화 |
| 26 | A | GitHub-hosted는 운영 부담 감소 |
| 27 | A | Self-hosted는 네트워크/하드웨어 제어 가능 |
| 28 | A | Label로 특정 Runner Capability 선택 |
| 29 | A | Runner Group은 접근/정책 관리 |
| 30 | A | Ephemeral은 상태 잔존 위험 감소 |
| 31 | A | Enterprise Policy는 중앙 통제 |
| 32 | A | 중앙 Workflow는 버전/호환성 관리 필요 |
| 33 | A | 공통 설정 중앙화 |
| 34 | A | Public 코드가 내부 Runner에서 실행될 위험 |
| 35 | A | 최소 권한과 신뢰 경계가 핵심 |
| 36 | A | OIDC는 장기 Cloud Key 의존 감소 |
| 37 | A | `GITHUB_TOKEN`도 최소 권한 적용 |
| 38 | A | Fork PR은 Secret 신뢰 경계 주의 |
| 39 | A | Full SHA는 참조 코드 변경 위험 감소 |
| 40 | A | 먼저 병목 측정 후 여러 요소를 최적화 |

## 점수 (Score, SCR)

- 36–40: EXAM-READY 후보
- 34–35: Gate 통과 후보
- 30–33: 약점 Domain 재학습
- <30: Terms/Concepts/Labs 재수행
