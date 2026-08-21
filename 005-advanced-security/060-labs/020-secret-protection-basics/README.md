# Lab 020 — Secret Protection Basics

## Objective

Secret Protection Alert의 생성·상태·Remediation 흐름을 이해합니다.

## Safe Practice

실제 유효 Secret을 만들지 않습니다. 공식 샘플 또는 비활성 Test Pattern만 사용합니다.

## Practice

1. Secret Protection 설정과 Alert 화면 구조를 확인합니다.
2. Provider, Secret Type, Location, Status를 구분합니다.
3. Validity Check가 제공하는 신호를 설명합니다.
4. 노출 Secret 발견 시 `Revoke/Rotate → 영향 확인 → 코드 제거 → 재검증` 절차를 작성합니다.
5. Dismissal 사유를 임의로 사용하면 안 되는 이유를 설명합니다.

## Verify

- [ ] Secret Alert Lifecycle 설명 가능
- [ ] Rotation과 단순 코드 삭제의 차이 설명 가능
- [ ] Validity 신호의 의미 설명 가능

---
[← Lab 010](../010-security-suites-overview/README.md) · [다음 Lab 030 →](../030-push-protection-patterns/README.md)
