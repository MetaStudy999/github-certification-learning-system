# 030 시험-Day 전략 — GH-200 (030 Exam-Day Strategy — GH-200, ESGH-200)

## 1. 문제를 읽는 순서

```text
요구사항
→ 제약조건
→ BEST / MOST appropriate / FIRST 확인
→ 후보 기능 비교
→ 최소 권한·운영 책임·재사용 범위 확인
→ 정답 선택
```

## 2. 자주 놓치는 조건

- `FIRST`: 첫 진단 단계인지 확인
- `BEST`: 단순히 가능한 답이 아니라 가장 적합한 답
- `MOST secure`: 최소 권한과 Secret 수명까지 고려
- `enterprise`: 중앙 정책·Runner Group·Governance 관점 추가
- `reuse`: Workflow 재사용인지 Step 재사용인지 구분
- `troubleshoot`: Trigger → Condition → Permission → Runner → Log 순으로 접근

## 3. 시간 관리

- 쉬운 정의형 문제를 먼저 확보합니다.
- YAML 세부문법에 오래 머물지 않습니다.
- Scenario 문제는 요구사항에 밑줄을 긋는다는 느낌으로 핵심 조건을 추립니다.
- 모르는 문제는 표시하고 후반에 다시 봅니다.

## 4. 마지막 10분 확인

- Cache와 Artifact를 뒤집지 않았는지
- Reusable Workflow와 Composite Action을 뒤집지 않았는지
- GitHub-hosted와 Self-hosted의 운영 책임을 반대로 선택하지 않았는지
- Secret 문제에서 OIDC/최소 권한을 놓치지 않았는지
- Troubleshooting 문제에서 원인보다 먼저 무리한 수정부터 선택하지 않았는지

## 5. 시험 직전 금지

- 새로운 범위를 대량으로 추가하지 않기
- 실제 시험 유출문제에 의존하지 않기
- 점수가 낮은 Domain을 무시하고 암기만 반복하지 않기
