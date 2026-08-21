# 010 프로젝트 Rubric — AI-보조 개발 프로젝트 (010 Project Rubric — AI-Assisted Development Project, PRADP)

총점: **100점**

## 평가표

| 영역 | 배점 | 만점 기준 |
|---|---:|---|
| Requirement / Definition of Done | 10 | 입력·출력·Error·완료 기준이 명확 |
| Prompt / Context Design | 15 | Goal/Context/Constraints/Output/Verification을 체계적으로 기록 |
| Feature Selection | 10 | Suggestion/Chat/Edits/Agent/CLI 등을 목적에 맞게 선택 |
| Code Correctness | 15 | 요구사항 충족, 실행 가능, 오류 처리 적절 |
| Testing | 15 | Unit/Edge/Error/필요한 Integration Test와 강한 Assertion |
| Debugging / Refactoring | 10 | Root Cause 검증과 동작 보존 Refactor Evidence |
| Documentation / Review | 10 | 실제 동작과 일치하는 문서, AI Review + Human Review |
| Responsible AI / Privacy | 10 | 위험·Secret·Data·Exclusion·Safeguard 검토 |
| Evidence / Reflection | 5 | 재현 가능한 기록과 최종 회고 |
| **합계** | **100** | |

## 세부 판정

### 90–100 — CLEAR 후보

- AI를 단순 생성기가 아닌 **검증 가능한 Engineering Assistant**로 사용
- Accept / Modify / Reject 판단 근거가 명확
- Test와 Human Review가 충분
- Privacy/Security/Responsible AI Evidence가 있음

### 80–89 — PASS

- 핵심 Workflow는 완료
- 일부 Evidence 또는 고급 기능 실습이 부족할 수 있음
- 부족 영역을 보완하면 CLEAR 가능

### 70–79 — REVIEW

- 기능 구현은 되었지만 Prompt/Context, Test, Review 또는 Evidence 중 핵심 축이 약함
- 해당 Lab을 다시 수행

### 69 이하 — REBUILD

- AI Output을 무검증 사용했거나 요구사항·Test·Privacy 검토가 부족
- Project Phase 1부터 다시 점검

## 감점 기준 예시

| 문제 | 권장 감점 |
|---|---:|
| 실제 Secret / Token을 Prompt 또는 Evidence에 기록 | 즉시 중단 후 제거·회전 검토 |
| AI Output 무검증 Merge | -15 이상 |
| Test 없음 | -15 |
| 요구사항 없음 | -10 |
| Accept/Modify/Reject 근거 없음 | -5 |
| Documentation이 실제 코드와 불일치 | -5 |
| Privacy / Responsible AI Review 없음 | -10 |

## Self-리뷰 (Self-Review, S)

```text
Score:
Strongest area:
Weakest area:
AI suggestion I rejected:
AI suggestion I modified:
Most important test I added manually:
Most important privacy/security lesson:
Next improvement:
```
