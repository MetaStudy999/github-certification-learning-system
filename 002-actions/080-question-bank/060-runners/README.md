# 060 러너 — Q051–Q060 (060 Runners — Q051–Q060, RQ051Q060)

## Q051
GitHub-hosted Runner의 특징으로 가장 적절한 것은?

A. GitHub가 Runner 환경을 관리한다.  B. 사용자가 항상 OS 패치를 직접 수행한다.  C. 사내망 접근이 자동 보장된다.  D. Runner Group이 필요 없다.

<details><summary>정답</summary>**A**</details>

## Q052
사내망 전용 서비스에 접근해야 하는 Workflow에서 고려할 수 있는 것은?

A. Self-hosted Runner  B. Gist  C. Wiki  D. Discussion

<details><summary>정답</summary>**A. Self-hosted Runner**</details>

## Q053
Self-hosted Runner 운영 책임에 포함되는 것은?

A. OS 패치와 보안 관리  B. GitHub 계정 생성만  C. Issue Label만  D. Branch 이름만

<details><summary>정답</summary>**A**</details>

## Q054
GPU Runner와 일반 Runner를 Workflow에서 구분하는 데 가장 직접적인 기능은?

A. Runner Label  B. Artifact  C. Cache Key  D. Secret Name

<details><summary>정답</summary>**A. Runner Label**</details>

## Q055
Enterprise나 Organization에서 Self-hosted Runner 접근 범위를 관리하는 데 유용한 기능은?

A. Runner Group  B. Milestone  C. Project View  D. CODEOWNERS

<details><summary>정답</summary>**A. Runner Group**</details>

## Q056
Self-hosted Runner를 모든 Repository에 무제한 공개하면 위험한 이유는?

A. 신뢰하지 않는 Workflow가 내부 자원에 접근할 수 있기 때문  B. Artifact를 만들 수 없기 때문  C. Matrix를 사용할 수 없기 때문  D. Push가 불가능하기 때문

<details><summary>정답</summary>**A**</details>

## Q057
Job이 Runner를 찾지 못해 Queue에 오래 머무는 경우 가장 먼저 확인할 것은?

A. `runs-on` Label과 Runner Online/Access 상태  B. README  C. License  D. Issue Template

<details><summary>정답</summary>**A**</details>

## Q058
Ephemeral Runner의 장점으로 가장 적절한 것은?

A. Job마다 깨끗한 실행환경을 제공해 잔존 상태 위험을 줄일 수 있다.  B. 항상 무료다.  C. Secret이 필요 없다.  D. Workflow가 필요 없다.

<details><summary>정답</summary>**A**</details>

## Q059
GitHub-hosted Runner와 Self-hosted Runner 선택 시 가장 덜 중요한 기준은?

A. 네트워크 접근 요구  B. 운영 책임  C. 격리 요구  D. Repository 설명 문장 수

<details><summary>정답</summary>**D**</details>

## Q060
고정된 내부 도구와 사설 네트워크 접근이 핵심 요구사항이라면 어느 Runner가 더 적합할 가능성이 높은가?

A. Self-hosted Runner  B. GitHub-hosted Runner가 항상 정답  C. Runner가 필요 없음  D. Gist Runner

<details><summary>정답</summary>**A** — 단, 보안·운영 책임을 함께 감수해야 합니다.</details>

---
관련 Lab: [`080-runners-enterprise`](../../060-labs/080-runners-enterprise/README.md)
