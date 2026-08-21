# Lab 030 — Contexts & Expressions

## Objective

Context와 Expression을 사용해 실행 정보를 읽고 조건부 Step을 작성합니다.

## Practice

```yaml
name: context-demo

on:
  push:
  workflow_dispatch:

jobs:
  inspect:
    runs-on: ubuntu-latest
    env:
      APP_ENV: training
    steps:
      - name: Show safe metadata
        run: |
          echo "repo=${{ github.repository }}"
          echo "ref=${{ github.ref }}"
          echo "env=$APP_ENV"

      - name: Main branch only
        if: ${{ github.ref == 'refs/heads/main' }}
        run: echo "Running on main"
```

## Learn

- `github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`
- `${{ }}` Expression
- Workflow parse 시점과 Runtime 값의 차이
- Secret을 Log에 직접 노출하지 않는 원칙

## Verify

- [ ] Repository와 Ref 값이 출력된다.
- [ ] Branch 조건에 따라 Step 실행 여부가 달라진다.
- [ ] Context와 Shell 환경변수의 차이를 설명한다.
