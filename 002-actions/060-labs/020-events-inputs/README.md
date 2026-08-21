# 실습 (Lab, LAB) 020 — 이벤트와 입력값 (Events & Inputs, EI)

## 목표 (Objective, OBJ)

자동 이벤트와 수동 실행을 구분하고 `workflow_dispatch` 입력값을 사용합니다.

## 실습 (Practice, PRAC)

```yaml
name: manual-greeting

on:
  workflow_dispatch:
    inputs:
      name:
        description: Who to greet
        required: true
        type: string
        default: student

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello ${{ inputs.name }}"
```

## 학습 포인트 (Learn, LRN)

- Repository Event
- Manual Event (`workflow_dispatch`)
- Reusable Workflow Event (`workflow_call`)
- Input type / required / default

## 검증 (Verify, VER)

- [ ] Actions UI에서 Run workflow를 실행했다.
- [ ] 입력값이 Log에 반영되었다.
- [ ] `inputs` Context의 목적을 설명한다.

## 도전 과제 (Challenge, CHL)

`choice` 타입 입력을 추가하고 조건에 따라 다른 Step을 실행합니다.
