# 실습 (Lab, LAB) 030 — 푸시 보호와 사용자 정의 패턴 (Push Protection & Custom Patterns, PPCP)

## 목표 (Objective, OBJ)

Secret이 Repository에 들어오기 전에 차단하는 Prevention-first 흐름을 이해합니다.

## 실습 (Practice, PRAC)

1. Push Protection의 동작 시점을 설명합니다.
2. 학습용 비유효 Pattern으로 차단 시나리오를 설계합니다.
3. Bypass가 허용되는 경우 필요한 사유·권한·Audit 조건을 정리합니다.
4. 조직 고유 Credential 형식에 Custom Secret Pattern이 필요한 이유를 설명합니다.
5. False Positive를 줄이면서 탐지 범위를 유지하는 방법을 정리합니다.

## 검증 (Verify, VER)

- [ ] Push Protection과 Secret Alert 차이 설명 가능
- [ ] Bypass Governance 설명 가능
- [ ] Custom Pattern 사용 목적 설명 가능

---
[← Lab 020](../020-secret-protection-basics/README.md) · [다음 Lab 040 →](../040-dependency-graph-alerts/README.md)
