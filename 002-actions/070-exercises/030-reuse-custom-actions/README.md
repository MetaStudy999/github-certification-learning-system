# 030 Reuse & Custom Actions Exercises

## 목표

Reusable Workflow, Composite Action, JavaScript Action, Docker Action의 경계를 판단합니다.

### E021
여러 Repository가 동일한 CI Job 구조를 공유해야 합니다. Reusable Workflow가 적합한 이유를 설명하세요.

### E022
여러 Workflow에서 반복되는 5개의 Shell Step을 하나로 묶으려 합니다. Composite Action을 고려할 이유를 설명하세요.

### E023
Reusable Workflow와 Composite Action의 호출 단위 차이를 설명하세요.

### E024
Custom Action의 `action.yml` 또는 `action.yaml` Metadata가 담당하는 역할을 설명하세요.

### E025
빠른 실행과 Node 기반 로직이 필요한 Action에 JavaScript Action을 선택할 수 있는 이유를 설명하세요.

### E026
특정 Runtime과 도구를 컨테이너로 고정해야 할 때 Docker Container Action의 장단점을 설명하세요.

### E027
Action Input과 Output을 설계할 때 재사용성을 높이는 방법을 제시하세요.

### E028
Third-party Action을 사용할 때 버전 Tag만 참조하는 것과 Commit SHA로 고정하는 것의 보안 차이를 설명하세요.

### E029
공통 Workflow가 Secret을 필요로 할 때 호출자와 피호출자 사이의 Secret 전달을 어떻게 설계할지 설명하세요.

### E030
복잡한 로직을 Reusable Workflow로 만들지 Custom Action으로 만들지 판단하는 기준을 세 가지 제시하세요.

## 완료 기준

`Workflow 재사용`과 `Step 기능 재사용`을 구분할 수 있어야 합니다.

관련 Lab: [`060-reusable-automation`](../../060-labs/060-reusable-automation/README.md), [`070-custom-actions`](../../060-labs/070-custom-actions/README.md)
