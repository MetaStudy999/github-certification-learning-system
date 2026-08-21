# 010 Final 점검표 — GH-300 (010 Final Checklist — GH-300, FCGH-300)

## 1. 공식 기준선 (Official Baseline, OB)

- [ ] Microsoft Learn GH-300 Study Guide를 열었다.
- [ ] `Skills measured as of` 날짜를 확인했다.
- [ ] Change Log에 새 변경이 없는지 확인했다.
- [ ] 시험 언어·시간·예약 정보를 최신 Certification Page에서 확인했다.

## 2. 책임 있는 AI (Responsible AI, RAI)

- [ ] Hallucination을 설명한다.
- [ ] Bias / Fairness / Privacy / Transparency 위험을 설명한다.
- [ ] AI Output 검증이 필요한 이유를 설명한다.
- [ ] Human Accountability를 설명한다.
- [ ] Potential Harm 완화 방법을 예시로 말한다.

## 3. Copilot 기능 (Copilot Features, CF)

- [ ] Inline Suggestion / Chat 차이
- [ ] Chat / Edits 차이
- [ ] Edits / Agent Mode 차이
- [ ] Copilot CLI의 목적
- [ ] Agent Session / Sub-Agent 역할
- [ ] MCP의 목적
- [ ] Code Review / PR Summary 역할
- [ ] Spaces / Spark 역할
- [ ] Instructions / Prompt Files 차이
- [ ] Organization Policy / Audit Log / REST API 목적

## 4. 데이터 / 아키텍처 (Data / Architecture, DA)

자료 없이 다음을 그립니다.

```text
Input / Context
→ Prompt Building
→ Filter / Proxy
→ LLM
→ Post-processing
→ Suggestion
→ Human Verification
```

- [ ] Context Window 한계 설명
- [ ] 최신성·Bias·Hallucination 한계 설명
- [ ] Public Code Matching 처리 개념 설명

## 5. 프롬프트 / 컨텍스트 (Prompt / Context, PC)

- [ ] Goal
- [ ] Context
- [ ] Constraints
- [ ] Output
- [ ] Verification
- [ ] Zero-shot / Few-shot
- [ ] Chat History 영향
- [ ] Relevant Context 선택

## 6. Productivity / 테스트 (Productivity / Testing, PT)

- [ ] Code Generation
- [ ] Refactoring
- [ ] Documentation
- [ ] Debugging
- [ ] Legacy Modernization
- [ ] Unit / Integration Test
- [ ] Edge Case
- [ ] Assertion 품질
- [ ] Security Suggestion 검증
- [ ] Performance Benchmark

## 7. 개인정보 보호 / Safeguards (Privacy / Safeguards, PS)

- [ ] Content Exclusion 목적
- [ ] Content Exclusion 한계
- [ ] Suggestions matching public code filtering
- [ ] Output Ownership 확인 원칙
- [ ] Suggestion이 안 보일 때 Troubleshooting 순서
- [ ] Exclusion이 기대대로 작동하지 않을 때 Troubleshooting 순서

## 8. 점수 통과 기준 (Score Gate, SG)

| 지표 | 목표 | 결과 |
|---|---:|---:|
| Question Bank 2회차 | 85%+ | |
| Mock 01 | 85%+ | |
| Mock 02 | 85%+ | |
| 최종 모의고사 (Final Mock, FM) | 90%+ 권장 | |
| Wrong Answer Retry | 90%+ | |

## 최종 판정

```text
[ ] EXAM-READY
[ ] REVIEW NEEDED
```

`REVIEW NEEDED`이면 점수가 낮은 Skill Area의 Exercise → Lab → QBank 순서로 되돌아갑니다.
