# 110 Mock Exams — 모의고사

## 목적

실제 GH-900 문항을 복제하지 않고, 공식 Domain 범위를 참고해 **자체 모의고사**를 구성합니다.

## Quick Start

```text
Question Bank 50문제
      ↓
Mock 01 (진단)
      ↓
오답 분류 + 약점 Lab
      ↓
Mock 02 (응시 Gate)
      ↓
오답 재시험
      ↓
Final Mock
      ↓
EXAM-READY 판단
```

## 현재 구성

| 코드 | 시험 | 문항 | 목표 | 역할 |
|---:|---|---:|---:|---|
| 010 | [Mock Exam 01](./010-mock-01/questions.md) | 40 | 85%+ | 진단 |
| 020 | [Mock Exam 02](./020-mock-02/questions.md) | 40 | 85%+ | 응시 Gate |
| 030 | [Final Mock](./030-final-mock/questions.md) | 40 | 90%+ 권장 | 최종 확인 |

각 모의고사는 `questions.md`와 `answers.md`를 분리했습니다. 문제를 모두 푼 뒤에만 정답 파일을 엽니다.

## 점수 기준

| 정답률 | 판정 | 행동 |
|---:|---|---|
| 90%+ | EXAM-READY | 최종 오답만 복습 |
| 85–89% | READY | 오답 재시험 후 판단 |
| 75–84% | REVIEW | 약점 Domain 재학습 |
| <75% | NOT READY | Terms/Concepts/Labs 재수행 |

## Exam Gate

최소 권장 기준:

- [ ] Mock 01: 34/40 이상
- [ ] Mock 02: 34/40 이상
- [ ] 최근 2회 연속 85% 이상
- [ ] Final Mock: 36/40 이상 권장
- [ ] 최근 오답 재시험: 90% 이상
- [ ] 공식 Study Guide 최신 범위 확인

## 회차 기록 Template

```text
Date:
Mock:
Elapsed time:
Score:
Correct / Total:
Weak Domains:
Error codes:
Top 3 Confusions:
Labs to repeat:
Retry date:
```

## 오답 처리

틀린 문제는 [`../120-wrong-answers/`](../120-wrong-answers/) 규칙에 따라 다음 코드 중 하나 이상을 붙입니다.

- `CONCEPT`
- `COMPARE`
- `READING`
- `MEMORY`
- `PRACTICE`
- `SCOPE`

## 주의

- 실제 시험 유출문제 사용 금지
- 기억에 의존한 실제 시험문항 재작성 금지
- 공식 학습목표에 기반한 독립 문제만 작성
- 정답률보다 **왜 틀렸는지 설명할 수 있는지**를 우선 확인

---

[← 100 Projects](../100-projects/README.md) · [다음: 120 Wrong Answers →](../120-wrong-answers/README.md)
