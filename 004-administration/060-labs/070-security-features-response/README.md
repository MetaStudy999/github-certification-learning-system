# Lab 070 — Security Features / Response

## Objective

Enterprise Admin 관점에서 **Vulnerability Alerts, Secret Scanning, CodeQL, Dependabot, Security Advisories**를 활성화·운영하고 대응 흐름을 설계합니다.

## Feature Map

| 기능 | 주요 목적 |
|---|---|
| Vulnerability Alerts | Dependency 취약점 정보 알림 |
| Dependabot | 취약 Dependency와 Update 관리 |
| Secret Scanning | 노출된 Secret 탐지 |
| CodeQL | Source Code의 보안 취약점 분석 |
| Security Advisory | 취약점을 비공개로 협업·공개하는 절차 지원 |

## Practice 1 — Alert Routing

가상 조직의 보안 Alert 흐름을 설계합니다.

```text
Alert
→ Triage Owner
→ Severity / Scope
→ Remediation
→ Credential rotation if needed
→ Verification
→ Close / Report
```

다음 Role을 배정하세요.

- Repository Maintainer
- Security Team
- Platform Team
- Incident Response

## Practice 2 — Secret Exposure

가상 Secret 노출 상황:

```text
1. Secret Scanning Alert 확인
2. Secret 종류와 영향 범위 파악
3. Credential 폐기 / Rotate
4. 코드·History·Configuration의 노출 원인 수정
5. 재발 방지
6. Audit / Incident 기록
```

`파일에서 Secret 문자열만 삭제하면 끝`이 아닌 이유를 설명합니다.

## Practice 3 — CodeQL / Dependabot

각각 다음 질문에 답합니다.

```text
무엇을 탐지하는가?
누가 Alert를 처리하는가?
어떤 Repository에 적용하는가?
어떤 Policy/Compliance Evidence가 필요한가?
```

## Practice 4 — Security Response Plan

```text
Detection
→ Triage
→ Containment
→ Remediation
→ Verification
→ Communication
→ Lessons Learned
```

각 단계의 Owner와 Evidence를 작성하세요.

## Challenge

`GHAS 기능을 켜면 보안 사고 대응 계획은 필요 없다`라는 주장에 반박하세요.

## Verify

- [ ] CodeQL / Secret Scanning / Dependabot 목적 구분
- [ ] Alert → Response 흐름 설명
- [ ] Secret 노출 시 Rotate가 필요한 이유 설명
- [ ] Security Advisory와 Response Plan의 역할 설명
- [ ] Admin 관점의 Enable / Policy / Report까지 연결

---
[← Lab 060](../060-security-policies-rulesets/README.md) · [Lab 080 →](../080-pat-apps-integrations/README.md)
