# 실습 (Lab, LAB) 060 — 메모리 / 상태 / 체크포인트 (Memory / State / Checkpoint, MSC)

## 목표 (Objective, OBJ)

Memory와 State를 구분하고 중단·재개 가능한 실행 기록을 설계합니다.

## 핵심 비교

- **Memory**: 다음 작업에서도 활용할 수 있는 정보
- **State**: 현재 실행의 진행 상태
- **Checkpoint**: 특정 시점의 State를 저장한 복구 지점

## 실습 (Practice, PRAC)

```text
Run ID:
Current step:
Completed steps:
Pending steps:
Inputs used:
Artifacts produced:
Checkpoint condition:
Resume condition:
Stop condition:
```

## 도전 과제 (Challenge, CHL)

같은 작업이 재시도될 때 중복 부작용을 피하기 위한 `Idempotency` 개념을 설명합니다.

## 검증 (Verify, VER)

- [ ] Memory vs State 설명
- [ ] Retry vs Resume 설명
- [ ] Checkpoint의 필요성 설명
- [ ] 중복 실행 위험과 Idempotency 설명

[← 이전](../050-environment-execution-context/README.md) · [다음 →](../070-evaluation-design/README.md)
