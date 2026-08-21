# Lab 090 — GitHub 액션 (GitHub Actions, GHACT / GH-200) Governance

## Objective

Enterprise 관리자 관점에서 **Workflow/Action 재사용, Organization Policy, Secret Scope**를 설계합니다.

## Concept

```text
Enterprise Standards
      ↓
Approved Actions / Reusable Workflows
      ↓
Organization Actions Policy
      ↓
Repository Workflow
      ↓
Runner / Secret / Network
      ↓
Audit / Usage
```

## Practice 1 — Reuse Strategy

여러 Repository가 동일한 Build/Test/Deploy 패턴을 사용한다고 가정합니다.

다음을 비교하세요.

```text
Repository마다 Workflow 복사
vs
Reusable Workflow 중앙 관리
```

평가 기준:

- 일관성
- 유지보수
- Security Update
- Versioning
- 변경 영향

## Practice 2 — Actions Policy

가상 Organization 정책을 설계합니다.

```text
Allowed actions:
Third-party action policy:
Required pinning/version policy:
Reusable workflow source:
Who can change policy:
Audit method:
```

## Practice 3 — Secret Scope

다음 Secret을 어디에 두는 것이 적절한지 판단합니다.

1. 한 Repository만 사용하는 Test API Secret
2. 여러 Repository에서 동일 환경 배포에 사용하는 Secret
3. 외부 Vault에서 관리되어야 하는 고위험 Credential

후보:

```text
Repository Secret
Organization Secret
Third-party Vault
```

## Practice 4 — Least Privilege

Workflow가 필요로 하는 권한만 주도록 다음을 작성합니다.

```text
Workflow purpose:
Required repository permissions:
Required secret access:
Required environment:
Unneeded permissions removed:
```

## Challenge

`공통 Workflow를 중앙화하면 보안 검토가 필요 없어지는가?`를 설명하세요.

## Verify

- [ ] Reusable Workflow의 Enterprise 장점 설명
- [ ] Actions Policy 목적 설명
- [ ] Repository/Organization Secret Scope 구분
- [ ] 외부 Vault를 고려할 Scenario 설명
- [ ] 최소 권한 Workflow Governance 설명

---
[← Lab 080](../080-pat-apps-integrations/README.md) · [Lab 100 →](../100-runners-networking-vaults/README.md)
