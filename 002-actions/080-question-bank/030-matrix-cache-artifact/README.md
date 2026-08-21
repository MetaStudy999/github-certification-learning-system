# 030 Matrix, 캐시 와 아티팩트 — Q021–Q030 (030 Matrix, Cache & Artifact — Q021–Q030, MCAQ021Q030)

## Q021
Ubuntu/Windows × Python 3.11/3.12 Matrix는 기본적으로 몇 개 Job 조합을 만드는가?

A. 2  B. 3  C. 4  D. 6

<details><summary>정답</summary>**C. 4** — 2×2 조합입니다.</details>

## Q022
특정 Matrix 조합만 제외하려면 가장 관련 있는 기능은?

A. `exclude`  B. `needs`  C. `permissions`  D. `secrets`

<details><summary>정답</summary>**A. `exclude`**</details>

## Q023
기본 Matrix에 특정 조합을 추가하려면?

A. `include`  B. `restore-keys`  C. `concurrency`  D. `outputs`

<details><summary>정답</summary>**A. `include`**</details>

## Q024
Dependency 다운로드 시간을 다음 Workflow Run에서 줄이려는 목적에 가장 적합한 것은?

A. Artifact  B. Cache  C. Issue  D. Environment

<details><summary>정답</summary>**B. Cache** — 재사용 가능한 의존성/빌드 입력의 접근 속도를 높이는 데 사용합니다.</details>

## Q025
Build 결과 파일을 저장해 이후 확인하거나 다른 Job에서 사용하려면 가장 적합한 것은?

A. Artifact  B. Cache  C. Label  D. Secret

<details><summary>정답</summary>**A. Artifact**</details>

## Q026
Cache Key가 정확히 일치하지 않을 때 대체 Key 탐색에 사용할 수 있는 것은?

A. `restore-keys`  B. `needs`  C. `outputs`  D. `permissions`

<details><summary>정답</summary>**A. `restore-keys`**</details>

## Q027
Integration Test에서 PostgreSQL 같은 의존 서비스를 Job과 함께 띄우는 기능은?

A. Service Container  B. Artifact  C. Runner Group  D. Environment Variable

<details><summary>정답</summary>**A. Service Container**</details>

## Q028
Container Job과 Service Container의 관계를 가장 잘 설명한 것은?

A. 둘은 동일하다.  B. 전자는 Job 자체 실행환경, 후자는 Job이 사용하는 별도 서비스다.  C. 둘 다 Artifact 저장소다.  D. 둘 다 Runner Group이다.

<details><summary>정답</summary>**B**</details>

## Q029
Cache와 Artifact를 구분하는 가장 좋은 기준은?

A. 둘 다 Secret 저장용이다.  B. Cache는 실행 가속, Artifact는 결과 보존·전달에 초점이 있다.  C. Artifact만 Repository에 사용 가능하다.  D. Cache는 PR에서 사용할 수 없다.

<details><summary>정답</summary>**B**</details>

## Q030
동일 Group의 이전 실행을 취소하고 최신 실행만 유지하는 데 가장 관련 있는 기능은?

A. `concurrency`  B. `matrix`  C. `artifact`  D. `services`

<details><summary>정답</summary>**A. `concurrency`**</details>

---
관련 Lab: [`040-matrix-services`](../../060-labs/040-matrix-services/README.md), [`050-cache-artifacts`](../../060-labs/050-cache-artifacts/README.md)
