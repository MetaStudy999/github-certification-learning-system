# 010 워크플로 Authoring (Workflow Authoring, WA) — 연습문제 (Exercises, EXR)

## 목표

Event, Workflow, Job, Step, Dependency를 실제 요구사항에 맞게 설계합니다.

### E001
`push`와 `pull_request`에서 Test가 실행되고, 수동으로도 실행할 수 있도록 Trigger를 설계하세요.

### E002
`build`가 성공해야 `test`가 실행되도록 Job Dependency를 설계하고 `needs`의 역할을 설명하세요.

### E003
Linux와 Windows에서 Python 3.11/3.12를 모두 검증하는 Matrix를 설계하고 총 Job 수를 계산하세요.

### E004
특정 Branch에서만 배포 Job을 실행해야 합니다. Event Filter와 Job Conditional 중 어떤 방식을 언제 선택할지 비교하세요.

### E005
Database를 필요로 하는 Integration Test에 Service Container를 사용하는 구조를 설명하세요.

### E006
동일 Repository 안에서 자동화가 중복 실행되는 상황을 줄이기 위해 `concurrency`를 어떻게 활용할지 설명하세요.

### E007
긴 Workflow를 Build/Test/Deploy Job으로 분리하는 이유를 Runner 격리와 실패 분석 관점에서 설명하세요.

### E008
수동 실행 시 `environment` 값을 입력받아 `dev`와 `prod`를 구분하려고 합니다. `workflow_dispatch` Input을 설계하세요.

### E009
PR에서는 Test만 실행하고 `main` Push에서만 Package를 생성하도록 조건을 설계하세요.

### E010
Workflow가 지나치게 많은 권한을 갖지 않도록 Job별 `permissions`를 분리하는 이유를 설명하세요.

## 완료 기준

각 문제에서 YAML 전체를 외우는 것보다 **Trigger → Job → Runner → Step → 조건**의 구조를 정확히 설명합니다.

관련 Lab: [`010-first-workflow`](../../060-labs/010-first-workflow/README.md), [`020-events-inputs`](../../060-labs/020-events-inputs/README.md)
