# 실습 (Lab, LAB) 060 — 재사용 자동화 (Reusable Automation, RA)

## 목표 (Objective, OBJ)

중복 Workflow를 줄이기 위해 Reusable Workflow와 Composite Action의 사용 위치를 구분합니다.

## 재사용 워크플로 (Reusable Workflow, RW)

```yaml
on:
  workflow_call:
    inputs:
      python-version:
        required: true
        type: string
```

호출 측에서는 Job 수준에서 `uses`로 호출합니다.

## 복합 액션 (Composite Action, CA)

여러 Step을 하나의 Action으로 묶어 Step 수준에서 재사용합니다.

## 비교 (Compare, CMP)

| 항목 | Reusable Workflow | Composite Action |
|---|---|---|
| 재사용 단위 | Job/Workflow | Steps |
| 호출 위치 | Job | Step |
| 대표 목적 | 전체 CI 패턴 공통화 | 반복 Step 묶음 |

## 검증 (Verify, VER)

- [ ] `workflow_call`의 목적을 설명한다.
- [ ] Input과 Secret mapping을 설명한다.
- [ ] 두 재사용 방식 중 상황에 맞는 것을 선택할 수 있다.
