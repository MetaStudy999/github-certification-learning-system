# 020 재도전 대기열 (Retry Queue, RQ) — GH-300

## 사용법

오답 또는 `맞혔지만 설명하지 못한 문제`를 Queue에 넣습니다.

## +1일 대기열 (+1 Day Queue, D1Q)

| ID | Skill Area | Error Code | Retry Date | Result | Next Action |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## +7일 대기열 (+7 Day Queue, D7Q)

| ID | Skill Area | Error Code | Retry Date | Result | Final Status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 반복 오류 (Repeated Errors, RE)

같은 개념을 2회 이상 틀렸다면 별도로 올립니다.

| Concept | Count | Related Skill | Lab | Status |
|---|---:|---|---|---|
|  |  |  |  |  |

## 우선순위 (Priority, PRI)

```text
P1: 반복 오류
P2: Copilot Features / Responsible AI
P3: Agent / MCP / Privacy
P4: Prompt / Architecture / Testing
P5: 단순 Reading / Memory
```

## 통과 기준 (Gate, GATE)

```text
+1 day retry >= 90%
AND
+7 day retry >= 90%
AND
Repeated critical errors = 0
→ Wrong Answer Gate PASS
```

## 주간 요약 (Weekly Summary, WS)

```text
Week:
Total wrong:
Fixed:
Open:
Most frequent error code:
Weakest skill area:
Lab to repeat:
Next action:
```
