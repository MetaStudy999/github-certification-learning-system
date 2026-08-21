# 010 Workflow Basics — Q001–Q010

## Q001
GitHub Actions에서 자동화 전체 흐름을 정의하는 단위는?

A. Step  B. Workflow  C. Runner  D. Artifact

<details><summary>정답</summary>**B. Workflow** — 하나 이상의 Job으로 자동화 흐름을 정의합니다.</details>

## Q002
Workflow 실행을 시작시키는 조건은?

A. Event  B. Cache  C. Label  D. Artifact

<details><summary>정답</summary>**A. Event** — `push`, `pull_request`, `workflow_dispatch` 같은 Event가 Workflow를 Trigger합니다.</details>

## Q003
하나의 Job은 일반적으로 어디에서 실행되는가?

A. 하나의 Runner  B. 여러 Organization  C. 여러 Repository  D. 하나의 Issue

<details><summary>정답</summary>**A. 하나의 Runner** — Job은 지정된 Runner 환경에서 Step들을 순서대로 실행합니다.</details>

## Q004
Job 내부에서 실행되는 최소 작업 단위는?

A. Workflow  B. Step  C. Event  D. Runner Group

<details><summary>정답</summary>**B. Step**</details>

## Q005
`build` Job 완료 후 `test` Job을 실행하려면 가장 관련 있는 키워드는?

A. `needs`  B. `uses`  C. `with`  D. `env`

<details><summary>정답</summary>**A. `needs`** — Job Dependency를 정의합니다.</details>

## Q006
Repository에 Push될 때마다 Workflow를 실행하려면 무엇을 사용해야 하는가?

A. `on: push`  B. `runs-on: push`  C. `uses: push`  D. `needs: push`

<details><summary>정답</summary>**A. `on: push`**</details>

## Q007
수동 실행 버튼을 제공하는 Event는?

A. `workflow_dispatch`  B. `repository_dispatch`  C. `schedule`  D. `release`

<details><summary>정답</summary>**A. `workflow_dispatch`**</details>

## Q008
Workflow 파일의 기본 위치는?

A. `.github/workflows/`  B. `.git/actions/`  C. `actions/`  D. `.workflow/`

<details><summary>정답</summary>**A. `.github/workflows/`**</details>

## Q009
Step에서 외부 또는 재사용 Action을 호출할 때 사용하는 키워드는?

A. `run`  B. `uses`  C. `needs`  D. `if`

<details><summary>정답</summary>**B. `uses`**</details>

## Q010
Shell 명령을 직접 실행하려면 가장 적절한 키워드는?

A. `uses`  B. `run`  C. `with`  D. `permissions`

<details><summary>정답</summary>**B. `run`**</details>

---
관련 Lab: [`010-first-workflow`](../../060-labs/010-first-workflow/README.md)
