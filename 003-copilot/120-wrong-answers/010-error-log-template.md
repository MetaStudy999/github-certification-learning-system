# 010 오류 Log Template — GH-300 (010 Error Log Template — GH-300, ELTGH-300)

복사해서 문제별로 사용합니다.

```text
ID:
Date:
Source: QBank / Mock 01 / Mock 02 / Final
Skill area:
Question summary:

My answer:
Correct answer:
Confidence before check: HIGH / MEDIUM / LOW

Error code:
- RAI / FEATURE / AGENT / ORG / ARCH / CONTEXT
- PROMPT / USECASE / TEST / PRIVACY / SAFEGUARD
- READING / STALE

Why I was wrong:

Correct concept in one sentence:

Why my choice was less appropriate:

Why the correct choice is best:

Official source checked:
Checked date:

Related exercise:
Related lab:

Action taken:
[ ] Read concept
[ ] Checked official docs
[ ] Repeated exercise
[ ] Repeated lab

+1 day retry date:
+1 day result: PASS / FAIL

+7 day retry date:
+7 day result: PASS / FAIL

Final status: OPEN / FIXED
```

## 좋은 오답노트의 기준

나쁜 예:

```text
Q17 정답 A. 외운다.
```

좋은 예:

```text
Error: AGENT
I confused Agent Mode with MCP.
Correct concept: Agent Mode performs multi-step work; MCP is a protocol that connects models/agents to external tools and context.
Action: repeat Lab 110 and retry tomorrow.
```
