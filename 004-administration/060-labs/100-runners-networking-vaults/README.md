# Lab 100 — Runners / Networking / Vaults

## Objective

GitHub-hosted / Self-hosted Runner, Runner Group, Network Boundary, Secret/Vault를 Enterprise 운영 관점에서 연결합니다.

## Runner Comparison

| 기준 | GitHub-hosted | Self-hosted |
|---|---|---|
| Infrastructure 운영 | GitHub | 조직 |
| OS/Patch 책임 | 낮음 | 조직 책임 |
| 내부망 접근 | 제한/별도 설계 | 설계 가능 |
| Custom HW/SW | 제한적 | 유연 |
| Isolation 책임 | GitHub 중심 | 조직 중심 |
| Capacity 관리 | 상대적으로 단순 | 조직 관리 |

## Practice 1 — Runner Selection

Scenario:

- Workflow가 사내 DB에 접근해야 함
- Custom Toolchain 필요
- 민감 Network
- 장시간 Job 존재

Self-hosted Runner를 선택할 장점과 다음 위험을 기록합니다.

```text
Patch:
Isolation:
Credential:
Network access:
Capacity:
Monitoring:
Cleanup:
```

## Practice 2 — Runner Group

가상의 Runner Group을 설계합니다.

```text
runner-group-prod
Allowed organizations:
Allowed repositories:
Labels:
Network:
Owner:
Monitoring:
```

어떤 Repository라도 Production Runner를 사용할 수 있게 하지 않는 이유를 설명하세요.

## Practice 3 — Networking

다음을 비교합니다.

- IP Allow List
- Self-hosted Runner Network
- Azure Private Networking

각각 어떤 접근 문제를 해결하는지 작성합니다.

## Practice 4 — Vault

고위험 Cloud Credential을 GitHub Secret에 장기 저장하는 대신 Third-party Vault Integration을 검토한다고 가정합니다.

```text
Secret source:
Access policy:
Rotation:
Audit:
Workflow authentication:
Failure handling:
```

## Troubleshooting

Runner가 느릴 때:

```text
Queue time
→ Runner availability
→ CPU / Memory / Disk
→ Network
→ Job characteristics
→ Concurrent jobs
→ Logs
→ Scale / Optimize
```

## Verify

- [ ] GitHub-hosted / Self-hosted 차이 설명
- [ ] Runner Group 접근 범위 설명
- [ ] IP Allow List와 Private Networking 목적 설명
- [ ] Self-hosted 운영 책임 설명
- [ ] Third-party Vault Integration 목적 설명
- [ ] Runner Performance 진단 순서 설명

---
[← Lab 090](../090-actions-governance/README.md) · [Lab 110 →](../110-audit-usage-cost/README.md)
