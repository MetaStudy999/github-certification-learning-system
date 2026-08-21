# 010 Overview — GH-200 시험 구조

## 빠른 시작 (Quick Start, QS)

GH-200은 단순 YAML 문법 시험이 아니라 **Workflow 설계·사용·문제해결·Action 개발·Enterprise 운영·보안 최적화**를 함께 평가합니다.

## 5개 영역 (5 Domains, 5D)

| Domain | 비중 | 핵심 질문 |
|---|---:|---|
| 1. Author and Manage Workflows | 20–25% | Workflow를 올바르게 설계할 수 있는가? |
| 2. Consume and Troubleshoot Workflows | 15–20% | 재사용하고 실패 원인을 분석할 수 있는가? |
| 3. Author and Maintain Actions | 15–20% | Action을 만들고 배포·유지할 수 있는가? |
| 4. Manage GitHub Actions for the Enterprise | 20–25% | Runner·Policy·사용 범위를 규모 있게 관리할 수 있는가? |
| 5. Secure and Optimize Automation | 10–15% | 권한·Secret·OIDC·Pinning·비용을 안전하게 다룰 수 있는가? |

## 학습 우선순위

```text
Workflow 구조
→ Context / Expression
→ Reuse / Matrix / Artifact
→ Custom Action
→ Runner / Enterprise
→ Security / OIDC / Pinning
→ Troubleshooting
```

## Foundations에서 가져올 선수지식

- Repository / Branch / Pull Request
- GitHub 이벤트의 의미
- 기본 Permission / Secret 개념
- GitHub Flow

## 완료 기준

- [ ] 5개 Domain을 설명한다.
- [ ] Workflow 실행 구조를 그림 없이 설명한다.
- [ ] 실습 Workflow를 직접 작성한다.
- [ ] 실패 Workflow의 로그를 읽고 원인을 찾는다.
