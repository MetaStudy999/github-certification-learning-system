# 050 Guides — 입문자용 GitHub 액션 (GitHub Actions, GHACT / GH-200) 가이드

## 가장 먼저 이해할 문장

> GitHub Actions는 **GitHub에서 어떤 사건(Event)이 발생했을 때 정해진 자동화 절차(Workflow)를 실행하는 시스템**입니다.

## 예시

```text
개발자가 Push
      ↓
push Event
      ↓
CI Workflow
      ↓
Test Job
      ↓
Runner
      ↓
Checkout → Setup → Install → Test
```

## 처음 배울 때 순서

1. YAML 들여쓰기와 기본 구조
2. `on` — 언제 실행하는가
3. `jobs` — 무엇을 실행하는가
4. `runs-on` — 어디에서 실행하는가
5. `steps` — 어떤 순서로 실행하는가
6. `uses`와 `run` 차이
7. Context / Expression
8. Secret / Permission

## 자주 하는 실수

- YAML 들여쓰기 오류
- 이벤트 이름과 필터 조건 혼동
- `uses`와 `run` 혼동
- Job 간 데이터가 자동 공유된다고 생각함
- Secret을 로그로 출력
- `GITHUB_TOKEN` 권한을 과도하게 부여
- Cache와 Artifact를 같은 것으로 이해

## 학습 원칙

화면 위치보다 **실행 모델과 목적**을 먼저 이해합니다.
