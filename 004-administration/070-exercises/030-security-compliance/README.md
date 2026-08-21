# 030 Security & Compliance — 수행형 연습

> GH-100의 **Implement secure software development and compliance** 영역을 Enterprise 관리자 관점에서 연습합니다.

## 연습문제 (Exercises, EXR)

1. 조직 전체에서 기본 브랜치 직접 Push를 제한하고 PR Review를 강제해야 합니다. Ruleset 또는 Branch Protection을 어떤 Scope에 적용할지 설계하세요.
2. Secret Scanning, Push Protection, Code Scanning을 서로 구분하고 각각 어떤 위험을 줄이는지 설명하세요.
3. GitHub Advanced Security 기능을 Organization 단위로 활성화할 때 비용·정책·예외 Repository를 어떻게 관리할지 설계하세요.
4. 외부 협력사가 특정 Repository에만 접근해야 합니다. 최소 권한 원칙으로 접근 모델을 설계하세요.
5. PAT(Personal Access Token), GitHub App, OAuth App 중 자동화 통합에 가장 적절한 방식을 선택하고 이유를 설명하세요.
6. 조직에서 승인되지 않은 OAuth App 사용을 통제해야 합니다. 정책·승인·감사 관점의 절차를 작성하세요.
7. Repository Ruleset이 기존 Branch Protection과 중복될 때 정책 충돌을 어떻게 점검할지 설명하세요.
8. 보안 Alert가 대량 발생했을 때 우선순위를 정하고 책임 Team에 연결하는 운영 절차를 설계하세요.
9. 규정 준수 감사에서 "누가 어떤 설정을 언제 변경했는가"를 증명해야 합니다. 어떤 Audit Evidence를 남길지 정리하세요.
10. 보안 정책 변경을 Production에 바로 적용하지 않고 Pilot → 검증 → 확대 적용하는 Change Management 절차를 설계하세요.

## 답안 기준

```text
Requirement
→ Scope (Enterprise / Organization / Repository)
→ Control / Feature
→ Least Privilege
→ Exception Policy
→ Audit Evidence
→ Verification
```

## 완료 기준

- [ ] 10개 Scenario 모두 답변
- [ ] Security Feature 간 차이를 설명 가능
- [ ] 최소 권한과 정책 상속 관계를 설명 가능
- [ ] 실제 Production 보안 설정을 약화시키지 않음

---
[← Exercises](../README.md) · [다음: 040 Actions Administration →](../040-actions-administration/README.md)
