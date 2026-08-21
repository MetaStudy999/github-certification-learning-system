# 090 Verification Standard — 실습 검증 기준

## Lab PASS

다음 항목을 모두 만족할 때 Lab을 `PASS`로 기록합니다.

- [ ] 목표를 한 문장으로 설명할 수 있다.
- [ ] 핵심 개념과 사용 이유를 설명할 수 있다.
- [ ] 따라하기를 재현할 수 있다.
- [ ] Expected Result와 Actual Result를 비교했다.
- [ ] 실패 시 최소 한 가지 Troubleshooting 경로를 확인했다.
- [ ] Evidence를 남겼다.

## Lab CLEAR

`PASS`에 더해 다음을 만족하면 `CLEAR` 후보로 봅니다.

- [ ] 힌트 없이 핵심 단계 재수행
- [ ] 관련 Exercise 또는 QBank 문제 해결
- [ ] 다른 유사 기능과의 차이 설명
- [ ] 보안·권한·운영 영향 설명

## 실패 처리 (Failure Handling, FH)

```text
FAIL
→ 실패 지점 식별
→ 로그/상태 관찰
→ 원인 가설
→ 최소 변경
→ 재실행
→ Verify
→ Evidence 갱신
```

실패 기록도 학습 Evidence이며 삭제하지 않고 원인과 해결 과정을 남깁니다.

---
[Labs Home](./README.md)