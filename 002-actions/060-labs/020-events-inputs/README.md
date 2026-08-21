# Lab 020 — Events & Inputs

## Objective

자동 이벤트와 수동 실행을 구분하고 `workflow_dispatch` 입력값을 사용합니다.

## Practice

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

## Learn

- Repository Event
- Manual Event (`workflow_dispatch`)
- Reusable Workflow Event (`workflow_call`)
- Input type / required / default

## Verify

- [ ] Actions UI에서 Run workflow를 실행했다.
- [ ] 입력값이 Log에 반영되었다.
- [ ] `inputs` Context의 목적을 설명한다.

## Challenge

`choice` 타입 입력을 추가하고 조건에 따라 다른 Step을 실행합니다.
