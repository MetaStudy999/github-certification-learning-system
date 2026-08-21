# 060 Troubleshooting Exercises

## 목표

실패한 Workflow를 Log, Event, Context, Permission, Runner, Dependency 순서로 진단합니다.

### E051
Workflow가 아예 시작되지 않았습니다. 가장 먼저 Trigger와 Branch/Path Filter를 확인해야 하는 이유를 설명하세요.

### E052
Job은 시작됐지만 특정 Step이 Skipped 되었습니다. `if`와 Context 값을 어떻게 점검할지 설명하세요.

### E053
`Resource not accessible by integration` 오류가 발생했습니다. Token Permission 관점에서 점검 순서를 작성하세요.

### E054
Self-hosted Runner Job이 Queue에 오래 머뭅니다. Label, Online 상태, Runner Group 접근을 어떻게 확인할지 설명하세요.

### E055
Matrix 중 Windows에서만 실패합니다. OS별 Shell/Path 차이를 어떻게 분리해 진단할지 설명하세요.

### E056
Cache가 매번 Miss 됩니다. Key, Restore Key, Path를 어떻게 점검할지 설명하세요.

### E057
Artifact Upload가 실패했습니다. 생성 경로와 실행 순서를 어떻게 검증할지 설명하세요.

### E058
Reusable Workflow 호출에서 Input Type 오류가 발생했습니다. 호출부와 `workflow_call` 정의를 어떻게 비교할지 설명하세요.

### E059
외부 Action 업데이트 이후 갑자기 실패했습니다. Version Reference와 Pinning 정책을 어떻게 점검할지 설명하세요.

### E060
전체 Workflow가 느립니다. Matrix 규모, Cache, Job Dependency, 중복 실행, Runner 선택을 기준으로 최적화 순서를 작성하세요.

## 기본 진단 순서

```text
Trigger
→ Job condition
→ Context / Input
→ Permission / Secret
→ Runner
→ Dependency / Path
→ Logs
→ Re-run / Fix
```

관련 Lab: [`100-troubleshooting-optimization`](../../060-labs/100-troubleshooting-optimization/README.md)
