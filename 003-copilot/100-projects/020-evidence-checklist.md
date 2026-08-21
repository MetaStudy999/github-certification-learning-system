# 020 프로젝트 Evidence 점검표 — GH-300 (020 Project Evidence Checklist — GH-300, PECGH-300)

## 1. 요구사항 (Requirement, R)

- [ ] `requirements.md` 또는 동등한 요구사항 기록
- [ ] Functional Requirement
- [ ] Non-functional Requirement
- [ ] Error Case
- [ ] Definition of Done

## 2. 프롬프트 / 컨텍스트 (Prompt / Context, PC)

- [ ] Prompt 5개 이상
- [ ] Goal / Context / Constraints / Output / Verification 기록
- [ ] Zero-shot 사례
- [ ] Few-shot 사례 또는 왜 불필요했는지 설명
- [ ] Context 선택 근거
- [ ] Prompt 개선 Before / After

## 3. AI 의사결정 Evidence (AI Decision Evidence, AIDE)

- [ ] Accept 사례
- [ ] Modify 사례
- [ ] Reject 사례
- [ ] 각 판단 이유

## 4. 코드 / Test (Code / Test, CT)

- [ ] 구현 Commit 또는 Diff
- [ ] Unit Test
- [ ] Edge Case
- [ ] Error Case
- [ ] 사람이 직접 추가한 Test 1개 이상
- [ ] Test 결과

## 5. 디버그 / 리팩터 (Debug / Refactor, DR)

- [ ] 실패 증상
- [ ] AI 가설
- [ ] 실제 Root Cause
- [ ] Fix
- [ ] 성공 Test
- [ ] Refactor Before / After

## 6. 현재 Copilot 기능 (Current Copilot Features, CCF)

가능한 환경에서 최소 1개 이상 실제 수행하고, 나머지는 Scenario로 설명합니다.

- [ ] Copilot CLI
- [ ] Edits
- [ ] Agent Mode
- [ ] MCP
- [ ] Code Review
- [ ] Instructions
- [ ] Prompt File
- [ ] Spaces
- [ ] Spark

## 7. 책임 있는 AI / 개인정보 보호 (Responsible AI / Privacy, RAIP)

- [ ] Secret 미노출 확인
- [ ] PII / 민감 Data 미포함 확인
- [ ] Hallucination 또는 부정확성 검토 사례
- [ ] Security Review
- [ ] Content Exclusion Scenario
- [ ] Public Code Matching Safeguard 이해
- [ ] Human Accountability 기록

## 8. 최종 증빙 (Final Evidence, FE)

```text
Repository URL:
Primary branch:
Key PR:
Test evidence:
Prompt log:
Review evidence:
Project score:
Reflection:
```

## CLEAR 통과 기준 (CLEAR Gate, CLEARG)

- [ ] Project Rubric 90점 이상
- [ ] 필수 Evidence 완비
- [ ] 민감정보 노출 없음
- [ ] Project를 5분 안에 설명 가능
