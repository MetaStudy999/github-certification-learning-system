# 030 Concepts — GHAS 핵심 개념

## Secure SDLC 흐름

```text
Plan
→ Code
→ Pull Request
→ Build / Test
→ Release
→ Operate

각 단계에
Secret / Dependency / Code / Policy / Alert 대응을 연결
```

## 반드시 구분

| A | B | 핵심 차이 |
|---|---|---|
| Secret Protection | Code Security | Credential 노출 vs 코드 취약점 |
| Push Protection | Secret Alert | Push 전 예방 vs 노출 후 탐지·대응 |
| Dependabot Alert | Dependency Review | 알려진 취약 Dependency Alert vs PR 변경 의존성 검토 |
| Dependency Graph | SBOM | GitHub 내 Dependency 관계 vs 표준화된 구성요소 명세 |
| CodeQL | SARIF | 분석 Engine/Query vs 분석 결과 교환 형식 |
| Default Setup | Advanced Setup | 간편 기본 설정 vs Workflow 세부 제어 |
| Alert Dismissal | Remediation | 위험 수용/오탐 처리 vs 실제 수정 |
| Security Overview | Security Campaign | 상태 관찰 vs 목표 기반 대규모 수정 활동 |
| Prevention-first | Gate-based | 위험을 조기에 차단 vs 특정 Gate에서 검증 |

## 운영 원칙

1. 가능한 한 위험을 **코드 작성·Push·PR 단계에서 조기 차단**합니다.
2. Alert는 Severity만 보지 않고 Exploitability, Context, Asset 중요도를 함께 봅니다.
3. Dismissal에는 이유와 Audit 가능성이 있어야 합니다.
4. 보안 기능은 Repo 단위 실습에서 끝내지 않고 Organization/Enterprise 정책으로 확장합니다.
5. 자동화 결과도 사람의 검토와 Remediation 책임이 필요합니다.

---
[← 020 Terms](../020-terms/README.md) · [다음: 040 Official Docs →](../040-official-docs/README.md)
