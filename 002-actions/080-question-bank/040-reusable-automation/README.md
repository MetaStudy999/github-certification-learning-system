# 040 Reusable Automation — Q031–Q040

## Q031
여러 Repository에서 공통 CI Job 구조를 재사용하려면 가장 적절한 기능은?

A. Reusable Workflow  B. Cache  C. Artifact  D. Environment

<details><summary>정답</summary>**A. Reusable Workflow**</details>

## Q032
반복되는 여러 Step을 하나의 재사용 가능한 Step 단위로 묶는 데 적합한 것은?

A. Composite Action  B. Runner Group  C. Artifact  D. Matrix

<details><summary>정답</summary>**A. Composite Action**</details>

## Q033
Reusable Workflow를 호출 가능하게 하는 Trigger는?

A. `workflow_call`  B. `workflow_dispatch`  C. `pull_request`  D. `schedule`

<details><summary>정답</summary>**A. `workflow_call`**</details>

## Q034
Reusable Workflow가 입력값을 받도록 정의할 때 가장 관련 있는 개념은?

A. Inputs  B. Artifacts  C. Labels  D. Services

<details><summary>정답</summary>**A. Inputs**</details>

## Q035
호출하는 Workflow에서 Reusable Workflow를 사용하는 위치는 일반적으로?

A. Job 수준의 `uses`  B. Step의 `run`만 가능  C. Repository Settings  D. Runner Label

<details><summary>정답</summary>**A. Job 수준의 `uses`**</details>

## Q036
Composite Action과 Reusable Workflow의 핵심 차이는?

A. 전자는 Step 묶음 재사용, 후자는 Job/Workflow 구조 재사용에 적합하다.  B. 둘은 완전히 동일하다.  C. Composite는 Enterprise 전용이다.  D. Reusable Workflow는 Input을 받을 수 없다.

<details><summary>정답</summary>**A**</details>

## Q037
Reusable Workflow에서 Secret을 전달해야 할 때 중요한 원칙은?

A. 필요한 Secret만 명시적으로 전달  B. 모든 Secret 자동 공개  C. Secret을 YAML에 평문 저장  D. Log에 출력

<details><summary>정답</summary>**A** — 최소 노출 원칙을 적용합니다.</details>

## Q038
공통 CI 정책을 중앙 관리하고 여러 Repository가 호출하게 하려는 목적에 더 가까운 것은?

A. Reusable Workflow  B. Gist  C. Cache  D. Wiki

<details><summary>정답</summary>**A. Reusable Workflow**</details>

## Q039
Composite Action을 만들 때 Metadata 파일로 사용하는 것은?

A. `action.yml`  B. `workflow.json`  C. `runner.ini`  D. `matrix.yml`

<details><summary>정답</summary>**A. `action.yml` 또는 `action.yaml`**</details>

## Q040
Reusable Workflow와 Composite Action 중 무엇을 선택할지 판단할 때 가장 좋은 기준은?

A. 재사용하려는 단위가 Job/Workflow인지 Step 묶음인지  B. Repository 이름 길이  C. Branch 개수  D. Issue 수

<details><summary>정답</summary>**A**</details>

---
관련 Lab: [`060-reusable-automation`](../../060-labs/060-reusable-automation/README.md)
