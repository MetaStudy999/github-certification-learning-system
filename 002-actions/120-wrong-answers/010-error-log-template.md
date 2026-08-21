# 010 Error Log Template — GH-200

문제 하나를 다음 형식으로 기록합니다.

```text
ID:
Date:
Source: Question Bank / Mock 01 / Mock 02 / Final Mock
Domain:
Difficulty:
Question summary:
My answer:
Correct answer:
Error code:
Why I was wrong:
Correct concept in one sentence:
Why my choice was tempting:
Why alternatives are less appropriate:
Related official docs:
Related Lab:
+1 day retry:
+7 day retry:
Final status: OPEN / FIXED
```

## Error Code

- `CONCEPT` — 개념 부족
- `YAML` — YAML 구조·문법 혼동
- `CONTEXT` — Context / Expression 혼동
- `REUSE` — Reusable Workflow / Action 혼동
- `RUNNER` — Runner 선택·운영 혼동
- `SECURITY` — Permission / Secret / OIDC / Pinning 혼동
- `TROUBLE` — Log·실패 원인 분석 오류
- `READING` — `FIRST`, `BEST`, `MOST appropriate` 조건 해석 실패

## 완료 기준

오답을 `FIXED`로 바꾸려면 다음을 모두 충족합니다.

- [ ] 정답 이유를 한 문장으로 설명
- [ ] 관련 Lab 또는 공식문서 재확인
- [ ] +1일 재시험 정답
- [ ] +7일 재시험 정답
