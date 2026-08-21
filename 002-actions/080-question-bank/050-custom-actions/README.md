# 050 Custom Actions — Q041–Q050

## Q041
Custom Action의 입력·출력·실행 방식을 정의하는 Metadata 파일은?

A. `action.yml`  B. `package-lock.json`  C. `runner.yml`  D. `workflow.ini`

<details><summary>정답</summary>**A. `action.yml` 또는 `action.yaml`**</details>

## Q042
JavaScript Action의 장점으로 가장 적절한 것은?

A. Node 기반 로직을 Action으로 배포할 수 있다.  B. Docker가 항상 필요하다.  C. Runner가 필요 없다.  D. Secret을 자동 생성한다.

<details><summary>정답</summary>**A**</details>

## Q043
특정 Runtime과 도구 버전을 컨테이너로 묶어 실행하고 싶을 때 적합한 Action 유형은?

A. Docker Container Action  B. Composite Action  C. Matrix  D. Reusable Workflow

<details><summary>정답</summary>**A. Docker Container Action**</details>

## Q044
Composite Action의 핵심 목적은?

A. 여러 Step을 재사용 가능한 하나의 Action으로 묶기  B. Enterprise User 관리  C. Runner Image 생성  D. Artifact 암호화

<details><summary>정답</summary>**A**</details>

## Q045
Action Input을 정의하는 이유는?

A. 호출자가 동작을 구성할 수 있게 하기 위해  B. Workflow를 삭제하기 위해  C. Runner를 생성하기 위해  D. Secret을 공개하기 위해

<details><summary>정답</summary>**A**</details>

## Q046
Action Output의 주요 목적은?

A. Action의 결과값을 후속 Step/Workflow 로직에서 사용할 수 있게 하기 위해  B. Repository Visibility 변경  C. Runner 등록  D. Billing 설정

<details><summary>정답</summary>**A**</details>

## Q047
Third-party Action 참조를 특정 Commit SHA로 고정하는 주된 이유는?

A. 공급망 변경 위험을 줄이고 실행 버전을 고정하기 위해  B. Workflow 이름을 줄이기 위해  C. Artifact 용량을 늘리기 위해  D. Matrix를 비활성화하기 위해

<details><summary>정답</summary>**A**</details>

## Q048
Custom Action을 유지보수할 때 가장 중요한 항목은?

A. 입력/출력 계약, 버전, 의존성, 보안 검토  B. Star 수  C. Issue 색상  D. Wiki 테마

<details><summary>정답</summary>**A**</details>

## Q049
JavaScript Action과 Docker Action을 선택할 때 가장 핵심적인 판단 기준은?

A. 실행환경 격리와 Runtime 요구사항  B. Repository 설명 길이  C. PR 개수  D. Branch 이름

<details><summary>정답</summary>**A**</details>

## Q050
반복되는 Shell 명령 4개를 여러 Workflow에서 사용하려고 한다. 가장 단순한 재사용 단위는?

A. Composite Action  B. Enterprise Account  C. Runner Group  D. Artifact

<details><summary>정답</summary>**A. Composite Action**</details>

---
관련 Lab: [`070-custom-actions`](../../060-labs/070-custom-actions/README.md)
