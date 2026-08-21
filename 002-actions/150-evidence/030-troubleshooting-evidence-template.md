# 030 문제 해결 Evidence Template (030 Troubleshooting Evidence Template, TET)

```text
Date:
Failure scenario:
Workflow run URL:
Failed job:
Failed step:
Observed error:
Log clue:
Hypothesis:
Root cause:
Fix:
Successful run URL:
Prevention:
Related Lab:
Related official docs:
```

## Diagnostic 순서 (Diagnostic Order, DO)

```text
Trigger
→ Condition
→ Context / Input
→ Permission / Secret
→ Runner
→ Dependency / Path
→ Log
→ Fix / Re-run
```

## 완료 기준

- [ ] 실패 원인을 재현 또는 설명 가능
- [ ] Log 근거를 남김
- [ ] 수정 후 성공 Run 확인
- [ ] 재발 방지 한 문장 기록
