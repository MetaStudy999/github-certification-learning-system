# Lab 040 — Deployment / Licensing

## Objective

현재 GH-100에서 명시하는 주요 Enterprise 배포 Scenario를 비교하고 적합한 모델을 선택합니다.

## Deployment Models

```text
A. GHEC + EMU
B. GHEC + Data Residency + EMU
C. GHEC + Personal Accounts
D. GHES
```

## Practice — Decision Matrix

| 기준 | GHEC + EMU | GHEC + Data Residency + EMU | GHEC + Personal | GHES |
|---|---|---|---|---|
| GitHub가 서비스 운영 | | | | |
| Enterprise-managed identity | | | | |
| Personal account 사용 | | | | |
| 특정 Data Residency 요구 | | | | |
| 조직의 Server 운영 책임 | | | | |
| Upgrade 운영 책임 | | | | |
| 적합 Scenario | | | | |

## Scenario 1 — 중앙 Identity

요구사항:

- Cloud 선호
- 기업이 업무 계정 수명주기 통제
- 자체 Server 운영 불필요

어떤 모델을 우선 검토할지 작성합니다.

## Scenario 2 — Data Location

요구사항:

- Cloud 사용
- 기업 관리 계정
- 특정 지역 Data Residency 요구

어떤 모델이 후보인지 설명합니다.

## Scenario 3 — Server Control

요구사항:

- 자체 Infrastructure 운영
- Network / Upgrade / Maintenance를 조직이 통제

GHES가 주는 통제와 운영 책임을 함께 기록합니다.

## Licensing / Billing

다음 항목을 별도로 추적합니다.

```text
License entitlement
License consumption
Metered product usage
Runner / storage / product consumption
Inactive / underused licenses
```

## Challenge

`GHES는 내부망이므로 운영 부담이 없다`라는 주장에 반박하세요.

## Verify

- [ ] 4개 Deployment Scenario 구분
- [ ] Identity와 Deployment 관계 설명
- [ ] Data Residency 요구사항 연결
- [ ] GHES 운영 책임 설명
- [ ] License와 Metered Usage 구분

---
[← Lab 030](../030-roles-teams-permissions/README.md) · [Lab 050 →](../050-support-standards-diagnostics/README.md)
