# Lab 050 — Support / Standards / Diagnostics

## Objective

문제를 **Enterprise Admin이 해결할 범위**와 **GitHub Support로 Escalate할 범위**로 나누고, Support Bundle과 Diagnostics의 역할을 이해합니다.

## Practice 1 — Triage

다음 상황을 `ADMIN`, `SUPPORT`, `INVESTIGATE FIRST`로 분류하세요.

1. 사용자의 Repository Role이 잘못 설정됨
2. Organization Policy가 기대와 다르게 구성됨
3. Self-hosted Runner Label이 잘못됨
4. 문서화된 해결 절차와 Diagnostics 후에도 GHES 내부 서비스 오류가 지속
5. GitHub.com 서비스 자체 이상이 의심됨
6. Branching/Review 표준이 조직마다 달라 혼란 발생

## Practice 2 — Admin Triage Flow

```text
Symptom
→ Scope 확인
→ Recent change 확인
→ Settings / Permission / Policy 확인
→ Audit / Logs / Diagnostics
→ Documented fix
→ Re-test
→ unresolved platform issue?
→ Support
```

각 단계에 실제 확인할 항목을 적으세요.

## Practice 3 — Developer Process Standards

가상의 회사 표준을 정의합니다.

```text
Branching:
Pull request:
Required review:
Required checks:
Release naming:
Emergency change:
```

Enterprise Admin은 개발 방식을 직접 코딩하기보다 **조직 전체의 일관된 Guardrail과 표준**을 지원합니다.

## Support Bundle 안전 원칙

- Support Bundle은 진단에 필요한 시스템 정보를 포함할 수 있습니다.
- 공개 Repository에 Upload하지 않습니다.
- 공식 Support 절차와 보안 요구사항을 따릅니다.
- 불필요하게 수집·공유하지 않습니다.

## Challenge

`모든 문제는 GitHub Support에 보내는 것이 가장 안전하다`라는 주장과 `관리자가 모든 문제를 직접 해결해야 한다`라는 주장이 둘 다 잘못될 수 있는 이유를 설명하세요.

## Verify

- [ ] Admin vs Support 책임 경계 설명
- [ ] 기본 Triage 순서 설명
- [ ] Support Bundle / Diagnostics 목적 설명
- [ ] Workflow / Branch / Review / Release 표준 예시 작성

---
[← Lab 040](../040-deployment-licensing/README.md) · [Lab 060 →](../060-security-policies-rulesets/README.md)
