# 070 Exercises — 수행형 연습

> 단순 YAML 암기가 아니라 상황에 맞는 Actions 기능을 선택하고 설명하는 연습입니다.

## Exercise Areas

| 코드 | 영역 | 예시 과제 |
|---:|---|---|
| 010 | Workflow | Event와 Job 구조 설계 |
| 020 | Context | Expression과 조건문 판단 |
| 030 | Reuse | Reusable Workflow vs Composite Action |
| 040 | Runner | GitHub-hosted vs Self-hosted 선택 |
| 050 | Security | Permission, Secret, OIDC 시나리오 |
| 060 | Troubleshooting | 실패 Log 분석 |

## Starter Exercises

1. Push와 PR에서만 Test가 실행되는 Workflow 구조를 설명하세요.
2. Python 3.11/3.12 × Ubuntu/Windows Matrix의 Job 개수를 계산하세요.
3. Build 결과를 다음 Job에 전달할 때 Cache와 Artifact 중 무엇을 쓸지 설명하세요.
4. 회사 공통 CI를 여러 Repository에서 사용하려면 Reusable Workflow와 Composite Action 중 무엇이 적합한지 판단하세요.
5. 내부망 DB에 접근해야 할 때 Self-hosted Runner를 고려하는 이유와 보안 책임을 설명하세요.
6. Cloud 배포에서 장기 Access Key 대신 OIDC를 고려하는 이유를 설명하세요.

## 완료 기준

답에 반드시 **기능 이름 + 선택 이유 + 대안이 덜 적절한 이유**를 포함합니다.
