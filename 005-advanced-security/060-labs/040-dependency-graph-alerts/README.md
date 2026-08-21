# Lab 040 — Dependency Graph & Dependabot Alerts

## Objective

Repository 의존성과 알려진 취약점 Alert의 관계를 이해합니다.

## Practice

1. Dependency Graph에서 Direct / Transitive Dependency를 구분합니다.
2. Dependabot Alert의 Package, Vulnerable Version, Patched Version, Severity를 읽습니다.
3. 취약 Dependency가 실제 Runtime 경로에 포함되는지 Context를 확인하는 절차를 작성합니다.
4. Alert 우선순위를 `Severity + Reachability/Usage + Asset 중요도`로 판단합니다.
5. Dismissal이 필요한 경우 근거와 재검토 조건을 기록합니다.

## Verify

- [ ] Dependency Graph 역할 설명 가능
- [ ] Direct / Transitive 차이 설명 가능
- [ ] Dependabot Alert Triage 흐름 설명 가능

---
[← Lab 030](../030-push-protection-patterns/README.md) · [다음 Lab 050 →](../050-dependency-review-sbom/README.md)
