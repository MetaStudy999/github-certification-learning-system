# 실습 (Lab, LAB) 090 — 보안과 OIDC (Security & OIDC, SOIDC)

## 목표 (Objective, OBJ)

Workflow 권한과 자격 증명을 최소화하고 외부 Action 사용을 안전하게 설계합니다.

## 핵심 보안 규칙 (Core Security Rules, CSR)

```text
Least privilege
+ trusted actions
+ immutable version pinning
+ protected secrets
+ OIDC short-lived credentials
+ environment approval
```

## 주제 (Topics, TOP)

- `permissions`와 `GITHUB_TOKEN`
- Repository / Organization Secret
- Environment Secret와 승인
- Fork PR에서 Secret 노출 위험
- 외부 Action Full Commit SHA Pinning
- OIDC (OpenID Connect)
- 장기 Cloud Access Key 대신 단기 자격 증명
- Artifact Attestation / Provenance 개념

## 안전한 예제 (Safe Example, SE)

```yaml
permissions:
  contents: read
```

필요한 권한만 추가합니다.

## 검증 (Verify, VER)

- [ ] `GITHUB_TOKEN` 최소 권한 원칙을 설명한다.
- [ ] Secret을 Log에 출력하면 안 되는 이유를 설명한다.
- [ ] OIDC가 장기 Secret 위험을 줄이는 원리를 설명한다.
- [ ] Action을 Full Commit SHA로 고정하는 보안상 이유를 설명한다.
