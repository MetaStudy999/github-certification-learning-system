# Lab 100 — Troubleshooting & Optimization

## Objective

실패 Workflow를 체계적으로 진단하고 실행시간·비용을 줄이는 기본 전략을 익힙니다.

## Troubleshooting Order

```text
1. Event / Filter
2. YAML syntax
3. Job dependency
4. Step log
5. Context / Expression
6. Permission / Secret
7. Runner environment
8. External service
```

## Optimization Topics

- 불필요한 Matrix 조합 제거
- Cache 사용
- Artifact Retention 조정
- Job Dependency 최적화
- `max-parallel` 이해
- 긴 Workflow를 Reusable Workflow로 공통화
- 실패 Job / Workflow 재실행 시나리오 이해

## Verify

- [ ] Workflow가 아예 시작되지 않는 문제와 실행 중 실패를 구분한다.
- [ ] Job / Step Log에서 첫 실패 지점을 찾는다.
- [ ] Cache가 성능 향상에 적합한 경우를 설명한다.
- [ ] Matrix 크기가 비용에 미치는 영향을 설명한다.

## Challenge

의도적으로 실패하는 Test Step을 만들고 Log에서 원인을 찾아 수정한 뒤 성공 실행을 Evidence로 남깁니다.
