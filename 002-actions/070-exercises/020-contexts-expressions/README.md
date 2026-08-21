# 020 컨텍스트와 표현식 (Contexts & Expressions, CE) — 연습문제 (Exercises, EXR)

## 목표

Context, Expression, Conditional을 읽고 올바른 값을 선택합니다.

### E011
현재 Branch 이름을 판단할 때 어떤 `github` Context 값을 확인할지 설명하세요.

### E012
Step Output을 다음 Step에서 사용하는 흐름을 설명하세요.

### E013
Job Output을 다른 Job에서 사용하려면 어떤 연결이 필요한지 설명하세요.

### E014
`${{ }}` Expression이 필요한 위치와 단순 문자열이 가능한 위치의 차이를 설명하세요.

### E015
`if: success()`, `failure()`, `always()`, `cancelled()`의 용도를 비교하세요.

### E016
Matrix 값에 따라 특정 Step만 실행하도록 Conditional을 설계하세요.

### E017
Repository Variable과 Environment Variable을 Context 관점에서 구분하세요.

### E018
민감값을 일반 `env`에 하드코딩하면 안 되는 이유와 `secrets` Context의 역할을 설명하세요.

### E019
PR Event와 Push Event에서 사용 가능한 Payload가 다를 수 있는 이유를 설명하세요.

### E020
잘못된 Context 참조로 빈 문자열이 발생하는 Workflow를 어떻게 진단할지 순서를 작성하세요.

## 완료 기준

Context 이름을 암기하는 데 그치지 않고 **값의 출처와 사용 시점**을 설명합니다.

관련 Lab: [`030-contexts-expressions`](../../060-labs/030-contexts-expressions/README.md)
