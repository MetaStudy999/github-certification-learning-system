# 010 Certificate Tracker — 자격 취득 추적

| 코드 | 시험 | 예약일 | 응시일 | Result | Issued | Expiration/Renewal | Credential URL |
|---:|---|---|---|---|---|---|---|
| 001 | GH-900 | - | - | - | - | - | - |
| 002 | GH-200 | - | - | - | - | - | - |
| 003 | GH-300 | - | - | - | - | - | - |
| 004 | GH-100 | - | - | - | - | - | - |
| 005 | GH-500 | - | - | - | - | - | - |
| 006 | GH-600 | - | - | - | - | - | - |

## 결과 값 (Result Values, RV)

```text
SCHEDULED
TAKEN
PASSED
NOT-PASSED
RETAKE-PLANNED
```

실제 결과가 확인된 뒤에만 값을 기록합니다.

## 합격 후 절차 (After Passing, AP)

```text
PASSED
→ Credential URL 기록
→ 과정 Progress를 PASSED로 변경
→ Project / Evidence 완료 여부 확인
→ Portfolio 연결
→ CLEAR 판단
```

---
[Certificates Home](./README.md)