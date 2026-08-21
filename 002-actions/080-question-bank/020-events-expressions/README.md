# 020 이벤트 와 표현식 — Q011–Q020 (020 Events & Expressions — Q011–Q020, EEQ011Q020)

## Q011
Workflow를 다른 Workflow에서 호출 가능하게 만들기 위한 Event는?

A. `workflow_call`  B. `workflow_run`  C. `push`  D. `release`

<details><summary>정답</summary>**A. `workflow_call`** — Reusable Workflow의 진입점으로 사용합니다.</details>

## Q012
`workflow_dispatch`와 `workflow_call`의 핵심 차이는?

A. 둘 다 수동 실행 전용이다.  B. 전자는 수동 실행, 후자는 다른 Workflow 호출에 사용된다.  C. 전자는 Runner, 후자는 Job이다.  D. 차이가 없다.

<details><summary>정답</summary>**B**</details>

## Q013
현재 실행의 Repository, Actor, Ref 같은 정보를 제공하는 대표 Context는?

A. `github`  B. `matrix`  C. `runner`  D. `secrets`

<details><summary>정답</summary>**A. `github`**</details>

## Q014
Matrix의 현재 조합 값을 참조할 때 사용하는 Context는?

A. `env`  B. `matrix`  C. `needs`  D. `vars`

<details><summary>정답</summary>**B. `matrix`**</details>

## Q015
앞선 Job의 Output을 후속 Job에서 참조할 때 가장 관련 있는 Context는?

A. `needs`  B. `steps`  C. `runner`  D. `strategy`

<details><summary>정답</summary>**A. `needs`**</details>

## Q016
현재 Job의 앞선 Step Output을 참조할 때 사용하는 대표 Context는?

A. `steps`  B. `github`  C. `job`  D. `inputs`

<details><summary>정답</summary>**A. `steps`**</details>

## Q017
실패 여부와 관계없이 Cleanup Step을 실행하려는 경우 가장 적절한 Status Check Function은?

A. `always()`  B. `success()`  C. `cancelled()`  D. `contains()`

<details><summary>정답</summary>**A. `always()`** — 단, 실제 사용 시 취소/실패 상황의 부작용을 함께 고려해야 합니다.</details>

## Q018
앞선 Step이 실패했을 때만 진단 Step을 실행하려면?

A. `if: failure()`  B. `if: success()`  C. `if: always`  D. `if: runner()`

<details><summary>정답</summary>**A. `if: failure()`**</details>

## Q019
민감정보를 참조할 때 가장 적절한 Context는?

A. `secrets`  B. `vars`  C. `matrix`  D. `strategy`

<details><summary>정답</summary>**A. `secrets`**</details>

## Q020
일반 설정값을 Organization/Repository Variable로 관리할 때 대표적으로 사용하는 Context는?

A. `vars`  B. `secrets`  C. `needs`  D. `steps`

<details><summary>정답</summary>**A. `vars`** — 민감정보가 아니라 일반 구성값에 적합합니다.</details>

---
관련 Lab: [`020-events-inputs`](../../060-labs/020-events-inputs/README.md), [`030-contexts-expressions`](../../060-labs/030-contexts-expressions/README.md)
