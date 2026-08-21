# 실습 (Lab, LAB) 010 — 첫 워크플로 (First Workflow, FW)

## 목표 (Objective, OBJ)

`push` 이벤트가 발생하면 Ubuntu Runner에서 간단한 명령을 실행하는 첫 Workflow를 만듭니다.

## 실습 (Practice, PRAC)

`.github/workflows/hello.yml`

```yaml
name: hello-actions

on:
  push:

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Say hello
        run: echo "Hello GitHub Actions"
```

## 검증 (Verify, VER)

- [ ] Workflow 파일이 `.github/workflows/`에 있다.
- [ ] Push 후 Actions 탭에서 실행을 확인했다.
- [ ] `hello` Job이 성공했다.
- [ ] Log에서 메시지를 확인했다.

## 도전 과제 (Challenge, CHL)

`pull_request` 이벤트에서도 실행되도록 수정합니다.

## 핵심 한 문장

> Event가 Workflow를 시작하고, Job이 Runner에서 Step을 실행한다.
