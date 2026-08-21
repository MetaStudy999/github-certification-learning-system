# 110 Mock Exams — GH-300 자체 모의고사

> 실제 GH-300 문항을 복제하지 않습니다. 최신 공식 Skill Area를 참고해 **독립 제작한 40문항 모의고사 3회**를 사용합니다.

## Mock Structure

| 코드 | 시험 | 문항 | 목표 |
|---:|---|---:|---:|
| 010 | [Mock 01](./010-mock-01/) | 40 | 진단 / 85%+ |
| 020 | [Mock 02](./020-mock-02/) | 40 | 응시 Gate / 85%+ |
| 030 | [Final Mock](./030-final-mock/) | 40 | 최종 / 90%+ 권장 |

## Current Skill Balance

40문항 기준 권장 근사 배분입니다. 실제 시험 문항 배분과 동일하다고 보장하지 않습니다.

| Skill Area | 공식 비중 | Mock 권장 문항 |
|---|---:|---:|
| Responsible AI | 15–20% | 7 |
| Copilot Features | 25–30% | 11 |
| Data / Architecture | 10–15% | 5 |
| Prompt / Context | 10–15% | 5 |
| Developer Productivity | 10–15% | 6 |
| Privacy / Safeguards | 10–15% | 6 |
| **합계** |  | **40** |

## Flow

```text
Question Bank 100
      ↓
Mock 01
      ↓
오답 분류
      ↓
약점 Exercise / Lab
      ↓
Mock 02
      ↓
오답 재시험
      ↓
Final Mock
      ↓
Exam Readiness Gate
```

## Score Gate

| 점수 | 판정 | 행동 |
|---:|---|---|
| 90–100% | EXAM-READY | 최신 변경·오답만 확인 |
| 85–89% | READY | 약점 1회 추가 점검 |
| 75–84% | REVIEW | 약점 Skill Area 재학습 |
| <75% | NOT READY | Terms / Concepts / Labs로 복귀 |

**공통 응시 기준:** 최근 Mock **2회 연속 85% 이상**, 오답 재시험 **90% 이상**.

## Rules

1. `questions.md`를 먼저 풉니다.
2. 모든 문항에 답한 뒤 `answers.md`를 엽니다.
3. 틀린 문제는 [`120-wrong-answers`](../120-wrong-answers/)로 이동합니다.
4. 정답을 맞혔어도 근거를 설명하지 못하면 `UNCERTAIN`으로 기록합니다.
5. 실제 시험에서 본 문항을 기억해 Repository에 추가하지 않습니다.

---
[← 100 Projects](../100-projects/README.md) · [Mock 01 시작 →](./010-mock-01/questions.md)
