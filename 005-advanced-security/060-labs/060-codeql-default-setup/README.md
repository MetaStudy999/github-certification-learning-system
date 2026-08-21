# 실습 (Lab, LAB) 060 — CodeQL 기본 설정 (CodeQL Default Setup, CDS)

## 목표 (Objective, OBJ)

Code Security에서 CodeQL Default Setup을 활성화하고 분석 결과를 읽는 기본 흐름을 이해합니다.

## 실습 (Practice, PRAC)

1. CodeQL이 Source Code의 Data Flow와 취약 Pattern을 분석하는 방식을 개념적으로 설명합니다.
2. Default Setup과 Advanced Setup의 차이를 정리합니다.
3. 지원 언어, 분석 주기, Pull Request/Push Scan 흐름을 확인합니다.
4. Alert의 Severity, Location, Data Flow 정보를 읽습니다.
5. 실제 수정 후 재분석으로 Alert 상태가 어떻게 변하는지 설명합니다.

## 검증 (Verify, VER)

- [ ] CodeQL 역할 설명 가능
- [ ] Default vs Advanced Setup 구분 가능
- [ ] Alert → Remediation → Rescan 흐름 설명 가능

---
[← Lab 050](../050-dependency-review-sbom/README.md) · [다음 Lab 070 →](../070-codeql-advanced-sarif/README.md)
