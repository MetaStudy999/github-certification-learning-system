# 090 Status Policy — 상태 변경 정책

## Content Status

| 상태 | 의미 |
|---|---|
| BOOTSTRAPPED | 기본 폴더/README만 존재 |
| BUILDING | 학습 콘텐츠 구축 중 |
| CONTENT-READY | 학습에 필요한 주요 콘텐츠 구축 완료 |
| MAINTENANCE | 최신 시험범위와 제품 변경을 유지보수 중 |

## Learning Status

| 상태 | 의미 |
|---|---|
| PLANNED | 학습 예정 |
| READY | 즉시 학습 시작 가능 |
| LEARNING | 이론·용어·공식 자료 학습 중 |
| PRACTICING | Lab/Exercise 중심 학습 중 |
| REVIEWING | QBank/오답/Mock 중심 복습 중 |
| EXAM-READY | 시험 준비도 Gate 통과 |
| PASSED | 자격시험 합격 |
| CLEAR | 시험 + 실습 + 프로젝트 + Evidence 완료 |

## 변경 규칙

- `CONTENT-READY`를 이유로 `Learning Status`를 자동 변경하지 않습니다.
- `EXAM-READY`는 실제 점수와 Gate 근거가 있어야 합니다.
- `PASSED`는 실제 시험 결과가 있어야 합니다.
- `CLEAR`는 각 과정의 프로젝트와 Evidence까지 확인한 뒤 변경합니다.

## Audit Note

상태 변경 시 가능하면 날짜와 근거 링크를 남깁니다.

```text
Date:
Course:
Old Status:
New Status:
Evidence:
Reason:
```

---
[Progress Home](./README.md)