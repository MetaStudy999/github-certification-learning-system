# 030 Concepts — GitHub Actions 핵심 개념

## 1. 실행 구조

```text
Event
  ↓
Workflow
  ↓
Job A ─────┐
  ↓        │
Runner     │ needs
  ↓        │
Steps      ▼
        Job B
```

## 2. Workflow vs Action

- **Workflow**: Repository의 `.github/workflows/*.yml`에 정의되는 전체 자동화 흐름
- **Action**: Step에서 호출할 수 있는 재사용 가능한 기능 단위

## 3. Job vs Step

- **Job**은 Runner에서 실행되는 큰 단위입니다.
- **Step**은 Job 내부에서 순차적으로 실행됩니다.
- Job 간에는 `needs`로 의존성을 정의할 수 있습니다.

## 4. Cache vs Artifact

- **Cache**: 다음 실행을 빠르게 하기 위한 재사용 데이터
- **Artifact**: 현재 실행 결과를 저장·전달하기 위한 산출물

## 5. Reusable Workflow vs Composite Action

- **Reusable Workflow**: Job 수준의 Workflow 재사용에 적합
- **Composite Action**: Step 묶음을 Action처럼 재사용하는 데 적합

## 6. Security Model

```text
Minimum permissions
      +
Secret protection
      +
Trusted actions / pinning
      +
OIDC short-lived credentials
      +
Environment approval
```

## 7. Troubleshooting Flow

```text
Trigger 확인
→ Workflow YAML 확인
→ Job 상태 확인
→ Step log 확인
→ Context / Expression 확인
→ Permission / Secret 확인
→ Runner 환경 확인
```

## 완료 기준

- [ ] Event → Workflow → Job → Runner → Step 구조 설명
- [ ] Cache / Artifact 차이 설명
- [ ] Reusable Workflow / Composite Action 선택 기준 설명
- [ ] `GITHUB_TOKEN` 최소 권한 원칙 설명
