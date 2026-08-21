# 실습 (Lab, LAB) 120 — 보안 SDLC 통합 (Secure SDLC Integration, SSDLCI)

## 목표 (Objective, OBJ)

Secret, Dependency, Code Security를 하나의 개발 흐름에 통합합니다.

## 시나리오 (Scenario, SCN)

학습용 애플리케이션 Repository에 다음 흐름을 설계합니다.

```text
Code
→ Push Protection
→ Pull Request
→ Dependency Review
→ CodeQL / Code Security
→ Merge Gate
→ Security Overview
→ Alert Triage
→ Campaign / Remediation
→ Enterprise Policy
```

## 실습 (Practice, PRAC)

1. 어떤 보안 기능을 어느 SDLC 단계에 배치할지 표로 작성합니다.
2. Prevention-first 기능과 Merge Gate 기능을 구분합니다.
3. Alert Ownership과 SLA를 정의합니다.
4. 한 종류의 Alert를 선택해 Detection → Remediation → Verification Evidence를 작성합니다.
5. Repository 실습을 Organization/Enterprise 정책으로 확장하는 방안을 작성합니다.

## 검증 (Verify, VER)

- [ ] 3개 Security Suite를 한 흐름으로 설명 가능
- [ ] Prevention / Detection / Remediation 구분 가능
- [ ] Secure SDLC Architecture를 다른 사람에게 설명 가능

---
[← Lab 110](../110-enterprise-rollout/README.md) · [다음: 070 Exercises →](../../070-exercises/README.md)
