# 110 Mock Exams — GH-600 모의고사

## Built Set

| 코드 | 시험 | 문항 | 목표 |
|---:|---|---:|---:|
| 010 | [Mock 01](./010-mock-01/) | 40 | 85%+ |
| 020 | [Mock 02](./020-mock-02/) | 40 | 85%+ |
| 030 | [Final Mock](./030-final-mock/) | 40 | 90%+ 권장 |

**총 120문항 구축 완료**

Question Bank 100문제와 합치면 GH-600 자체 제작 시험형 문제는 **총 220문항**입니다.

## Domain Balance

현재 6개 Domain 비중을 반영하고 특히 Tool/Environment, Evaluation, Multi-Agent, Guardrails Scenario를 균형 있게 구성합니다.

## Flow

```text
Mock 01
→ Error Analysis
→ 약점 Lab
→ Mock 02
→ Retry
→ Final Mock
→ Exam Gate
```

## Gate

- Mock 01: 85% 이상 목표
- Mock 02: 85% 이상 목표
- Final Mock: 90% 이상 권장
- 최근 오답 재시험: 90% 이상

## Rules

- 문제를 먼저 푼 뒤 별도 Answers 문서를 확인합니다.
- 정답률뿐 아니라 Error Code와 설계 판단 근거를 기록합니다.
- 실제 시험 문제·복원 문제·Brain Dump는 사용하지 않습니다.
- Agent가 더 많은 권한을 갖는 선택지를 무조건 선호하지 않습니다.

---
[← 100 Projects](../100-projects/README.md) · [다음: 120 Wrong Answers →](../120-wrong-answers/README.md)
