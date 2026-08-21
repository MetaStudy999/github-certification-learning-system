# 090 문제 해결 — Q081–Q090 (090 Troubleshooting — Q081–Q090, TQ081Q090)

## Q081
Workflow가 전혀 시작되지 않을 때 가장 먼저 확인할 것은?

A. Trigger와 Branch/Path Filter  B. Artifact 이름  C. Cache 용량  D. Issue Label

<details><summary>정답</summary>**A**</details>

## Q082
특정 Step이 예상치 않게 Skipped 됐을 때 우선 확인할 것은?

A. `if` 조건과 관련 Context 값  B. Repository Star  C. License  D. Milestone

<details><summary>정답</summary>**A**</details>

## Q083
`Resource not accessible by integration` 오류에서 우선 점검할 것은?

A. Token/Workflow Permission  B. Matrix 크기  C. Artifact 이름  D. README

<details><summary>정답</summary>**A**</details>

## Q084
Self-hosted Runner Job이 계속 Queue 상태라면 무엇을 확인해야 하는가?

A. Runner Online 상태, Label, 접근 범위  B. Issue Assignee  C. Wiki  D. CODEOWNERS

<details><summary>정답</summary>**A**</details>

## Q085
Matrix에서 Windows만 실패한다. 가장 좋은 다음 행동은?

A. OS별 Shell/Path/Tool 차이를 Log로 비교  B. 전체 Matrix 삭제  C. Secret 공개  D. Runner Group 삭제

<details><summary>정답</summary>**A**</details>

## Q086
Cache가 계속 Miss된다. 가장 먼저 확인할 것은?

A. Cache Key와 Path  B. PR 제목  C. Label  D. Repository 설명

<details><summary>정답</summary>**A**</details>

## Q087
Artifact Upload Step에서 파일을 찾지 못한다. 우선 확인할 것은?

A. 앞선 Step의 실제 생성 경로  B. Enterprise 이름  C. Secret Masking  D. Git Tag

<details><summary>정답</summary>**A**</details>

## Q088
Reusable Workflow Input Type 오류의 진단 방법은?

A. 호출부 값과 `workflow_call.inputs` 정의 비교  B. Cache 삭제만 수행  C. Runner 재설치만 수행  D. README 수정

<details><summary>정답</summary>**A**</details>

## Q089
Third-party Action 업데이트 후 Workflow가 갑자기 실패했다. 가장 직접적으로 확인할 것은?

A. Action Version Reference와 변경사항  B. Issue Milestone  C. Repository Visibility  D. Project View

<details><summary>정답</summary>**A**</details>

## Q090
Workflow 전체 실행시간을 줄이기 위한 접근으로 가장 적절한 것은?

A. Cache, 불필요한 Matrix, Job Dependency, 중복 실행을 함께 분석  B. 모든 Job을 하나로 합치기만 함  C. 모든 Log 삭제  D. Secret을 코드에 저장

<details><summary>정답</summary>**A**</details>

---
관련 Lab: [`100-troubleshooting-optimization`](../../060-labs/100-troubleshooting-optimization/README.md)
