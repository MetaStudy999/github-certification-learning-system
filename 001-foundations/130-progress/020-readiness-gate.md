# 020 Readiness Gate — GH-900 응시 판단

## 원칙

시험 날짜가 왔다고 자동으로 응시하지 않습니다. 아래 Gate를 통과했을 때 `EXAM-READY`로 변경합니다.

## Gate A — Knowledge

- [ ] 공식 Study Guide 최신 범위를 확인했다.
- [ ] 7개 Domain의 목적을 설명할 수 있다.
- [ ] 핵심 용어 90% 이상 설명 가능하다.
- [ ] Confusion Matrix의 유사 개념을 구분할 수 있다.

## Gate B — Hands-on

- [ ] Lab 010–100 중 핵심 Lab 80% 이상 완료
- [ ] Issue → Branch → PR → Review → Merge 흐름 수행
- [ ] Clone / Fork / Fetch / Pull 차이를 실습 또는 설명으로 검증
- [ ] README / LICENSE / CONTRIBUTING / SECURITY / CODEOWNERS 역할 설명

## Gate C — Questions

- [ ] Q001–Q100 1회차 80% 이상
- [ ] Q001–Q100 2회차 85% 이상
- [ ] Mock 최근 2회 연속 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 최근 오답 재시험 90% 이상

## Gate D — 증빙 (Evidence, EVD)

- [ ] Lab Evidence 기록
- [ ] 프로젝트 Evidence 기록
- [ ] 점수 기록
- [ ] 약점 Domain과 보완 결과 기록

## 판정

```text
A+B+C+D 모두 통과
        ↓
   EXAM-READY
        ↓
      GH-900
        ↓
 PASS → PASSED
        ↓
Project + Evidence + Reflection
        ↓
      CLEAR
```

하나라도 핵심 Gate가 미충족이면 `REVIEWING` 상태를 유지합니다.
