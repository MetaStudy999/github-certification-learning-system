# 100 Projects — GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) 통합 프로젝트

## 프로젝트 001 — AI-보조 개발 프로젝트 (Project 001 — AI-Assisted Development Project, PADP)

### 목표

하나의 작은 애플리케이션을 Copilot으로 **요구사항 분석 → Prompt/Context 설계 → 구현 → Test → Debug → Refactor → Review → 문서화 → 검증**까지 수행합니다.

단순히 `AI로 코드 만들기`가 아니라 **AI 제안을 사람이 통제하고 검증하는 개발 과정**을 Evidence로 남깁니다.

## 권장 예제

아래 중 하나를 선택합니다.

- CLI Todo Manager
- 간단한 Expense Tracker
- Markdown Link Checker
- JSON/CSV Data Validator
- 작은 REST API
- 학습 Progress Tracker

복잡한 서비스보다 **AI 활용 과정과 검증 Evidence를 명확하게 남길 수 있는 작은 프로젝트**가 적합합니다.

## 전체 흐름

```text
Requirement
→ Prompt Plan
→ Context Plan
→ Implementation
→ Test Generation
→ Edge Case Review
→ Debugging
→ Refactoring
→ Documentation
→ Code Review
→ Responsible AI / Privacy Review
→ Final Verification
```

## 단계 (Phase, PH) 1 — Requirement

- [ ] 기능 요구사항 작성
- [ ] Non-functional Requirement 2개 이상
- [ ] 입력·출력·Error Case 정의
- [ ] 완료 기준(Definition of Done) 작성

## 단계 (Phase, PH) 2 — 프롬프트 / 컨텍스트 (Prompt / Context, PC)

Prompt를 최소 5개 기록합니다.

```text
Prompt ID:
Goal:
Context:
Constraints:
Expected output:
Verification:
Result:
Accept / Modify / Reject:
Reason:
```

- [ ] Zero-shot 사례
- [ ] Few-shot 사례
- [ ] 관련 Context 선택 사례
- [ ] 불필요 Context를 줄인 사례
- [ ] Instructions 또는 Prompt File 초안

## 단계 (Phase, PH) 3 — Implementation

- [ ] Copilot Suggestion 또는 Chat을 사용
- [ ] Copilot Edits 또는 다중 파일 편집 Scenario 기록
- [ ] 가능하면 Agent Mode Task를 작은 범위에서 실습
- [ ] Agent 권한·Tool 범위를 기록
- [ ] AI Output을 그대로 사용하지 않고 Review

## 단계 (Phase, PH) 4 — 테스트 (Testing, T)

- [ ] Unit Test
- [ ] Edge Case
- [ ] Error Case
- [ ] 필요한 경우 Integration Test
- [ ] Assertion 품질 확인
- [ ] AI가 누락한 Test를 사람이 최소 1개 추가

## 단계 (Phase, PH) 5 — 디버깅 (Debugging, D)

- [ ] 의도적 또는 실제 실패 사례 1개 기록
- [ ] Error Message / Stack Trace를 Context로 제공
- [ ] AI가 제안한 원인 가설 기록
- [ ] 실제 Root Cause 검증
- [ ] 수정 후 Test 성공 확인

## 단계 (Phase, PH) 6 — 리팩터링 (Refactoring, R)

- [ ] Refactoring 전 코드 저장
- [ ] Public Behavior 유지 Constraint
- [ ] Refactoring 후 Test
- [ ] Readability / Maintainability 개선 설명

## 단계 (Phase, PH) 7 — 문서화 / 리뷰 (Documentation / Review, DR)

- [ ] README 초안 작성
- [ ] AI가 작성한 문서와 실제 동작 비교
- [ ] Copilot Code Review 또는 Review Scenario 수행
- [ ] AI Review Finding 중 Accept / Reject 사례 기록
- [ ] Human Review 결론 작성

## 단계 (Phase, PH) 8 — 2026 기능 Extension (2026 Feature Extension, FE)

환경에서 사용 가능한 범위에 따라 다음을 실습하거나 설계합니다.

- [ ] Copilot CLI Scenario
- [ ] Agent Mode Scenario
- [ ] MCP Trust Boundary 설계
- [ ] Instructions File 초안
- [ ] Prompt File 초안
- [ ] Spaces 사용 Scenario 설명
- [ ] Spark 적용 가능성 설명
- [ ] Organization Policy / Audit Log Scenario 설명

## 단계 (Phase, PH) 9 — 책임 있는 AI / 개인정보 보호 (Responsible AI / Privacy, RAIP)

- [ ] Secret / Token을 Prompt에 넣지 않음
- [ ] Privacy 영향 검토
- [ ] Content Exclusion 적용 Scenario 설명
- [ ] Public Code Matching Safeguard 설명
- [ ] 라이선스·정책 확인 필요성 기록
- [ ] AI Output의 한계와 Human Accountability 회고

## 필수 증빙 (Required Evidence, RE)

- [ ] 요구사항 문서
- [ ] Prompt 5개 이상
- [ ] Context 선택 기록
- [ ] Accept / Modify / Reject 각각 최소 1개
- [ ] Unit Test / Edge Case
- [ ] Debugging 사례
- [ ] Refactoring 전후 비교
- [ ] README / Documentation
- [ ] Code Review 사례
- [ ] Agent/CLI/MCP 중 1개 이상 실습 또는 상세 설계
- [ ] Responsible AI / Privacy Review
- [ ] 최종 Reflection

## 평가

상세 평가는 [`010-project-rubric.md`](./010-project-rubric.md)를 사용하고, 증거 누락 여부는 [`020-evidence-checklist.md`](./020-evidence-checklist.md)를 사용합니다.

**80점 이상:** PASS  
**90점 이상 + Evidence 완비:** CLEAR 후보

---
[← 090 Final Review](../090-final-review/README.md) · [다음: 110 Mock Exams →](../110-mock-exams/README.md)
