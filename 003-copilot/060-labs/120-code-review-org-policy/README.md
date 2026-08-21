# Lab 120 — Copilot Code Review / Organization Policy

## Objective

Copilot을 개인 개발 보조 도구로만 보지 않고, **Code Review와 Organization-wide Governance** 관점에서 이해합니다.

## Concept

```text
Developer
   ↓
Pull Request
   ↓
Copilot Code Review
   ↓
AI Review Suggestions
   ↓
Human Reviewer
   ↓
Accept / Modify / Reject
```

조직에서는 기능 사용 범위를 Policy로 관리하고 Audit Log 등을 통해 관리 이벤트를 추적할 수 있습니다.

## Practice 1 — AI Review와 Human Review

Sandbox PR 또는 예제 Diff를 대상으로 다음 두 열을 작성합니다.

| Copilot이 도울 수 있는 것 | 사람이 최종 확인할 것 |
|---|---|
| 반복 패턴·잠재 문제 제안 | 요구사항 충족 여부 |
| 가독성·일관성 제안 | 비즈니스 로직 정확성 |
| 보안 개선 아이디어 | 실제 위협 모델·권한 영향 |
| Test 아이디어 | Test가 요구사항을 충분히 검증하는지 |

## Practice 2 — Review Standard 설계

Repository의 Review 지침을 다음 형식으로 작성합니다.

```text
Review priorities:
1. Correctness
2. Security
3. Tests
4. Maintainability
5. Documentation

Never approve only because AI says PASS.
```

Instructions File을 사용할 수 있는 환경이라면 어떤 지침을 넣을지 초안을 작성합니다.

## Practice 3 — Organization Policy Scenario

가상의 조직 `ACME-AI`를 가정합니다.

요구사항:

- 승인된 IDE에서 Copilot 사용
- Code Review 기능의 조직 정책 관리
- 기능 활성화 여부를 중앙에서 관리
- 관리 변경 이벤트를 추적
- Subscription 관리 자동화를 검토

다음 표를 채웁니다.

| 요구사항 | GitHub Copilot 관리 개념 |
|---|---|
| 기능 사용 범위 제어 | Organization Policy |
| 관리 이벤트 확인 | Audit Log |
| 구독 자동 관리 | REST API |
| Review 기준 일관성 | Instructions / Review Standards |

## Challenge

다음 주장에 반박하세요.

> “Copilot Code Review가 있으면 사람 Reviewer를 없앨 수 있다.”

최소 5개의 이유를 작성하고 **AI Review와 Human Accountability**의 역할을 구분합니다.

## Verify

- [ ] Code Review와 단순 Chat의 목적 차이를 설명 가능
- [ ] AI Review가 최종 승인 권한을 대체하지 않는 이유 설명
- [ ] Organization Policy의 목적 설명
- [ ] Audit Log의 목적 설명
- [ ] REST API를 통한 Subscription 관리가 어떤 관리 시나리오에 쓰이는지 설명

## Evidence

```text
Date:
PR / sample diff:
AI review findings:
Human review findings:
Policy scenario:
Audit scenario:
Final conclusion:
```

---
[← Lab 110](../110-cli-agent-mcp/README.md) · [Lab 130 →](../130-spaces-spark-instructions/README.md)
