# 060 Labs — GitHub 액션 (GitHub Actions, GHACT / GH-200) 단계별 실습

## 실습 로드맵 (Lab Roadmap, LR)

| 코드 | Lab | 핵심 기술 | 상태 |
|---:|---|---|---|
| 010 | First Workflow | workflow, push, job, step | READY |
| 020 | Events & Inputs | workflow_dispatch, pull_request, inputs | READY |
| 030 | Contexts & Expressions | github, env, vars, secrets, `${{ }}` | READY |
| 040 | Matrix & Services | matrix, include/exclude, services | PLANNED |
| 050 | Cache & Artifacts | cache, upload/download artifact | PLANNED |
| 060 | Reusable Automation | workflow_call, reusable workflow | PLANNED |
| 070 | Custom Actions | composite, JavaScript, Docker action | PLANNED |
| 080 | Runners & Enterprise | GitHub-hosted, self-hosted, policy | PLANNED |
| 090 | Security & OIDC | permissions, GITHUB_TOKEN, OIDC, pinning | PLANNED |
| 100 | Troubleshooting & Optimization | logs, retry, performance, cost | PLANNED |

## 공통 실습 구조

```text
Objective
→ Concept
→ Practice
→ Challenge
→ Verify
→ Evidence
```

## 안전 원칙

- 실제 Production 배포는 기본 실습에서 요구하지 않습니다.
- Cloud 장기 Access Key를 Repository Secret에 넣는 실습보다 OIDC 개념을 우선합니다.
- `permissions: write-all` 같은 과도한 권한을 기본값으로 사용하지 않습니다.
- 외부 Action은 출처·버전·Pinning을 확인합니다.

---

[← 050 Guides](../050-guides/README.md) · [Lab 010 시작 →](./010-first-workflow/README.md)
