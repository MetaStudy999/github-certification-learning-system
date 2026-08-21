# 920 Wrong Answers — 통합 오답 Control Tower

오답을 저장하는 폴더가 아니라 **실패 원인 → 재학습 → 재시험 → 약점 제거**를 관리하는 공통 시스템입니다.

## Quick Start

1. [`010-error-code-map.md`](./010-error-code-map.md)에서 공통 오류 코드를 선택합니다.
2. 틀린 문제마다 `왜 틀렸는가`를 한 문장으로 기록합니다.
3. 관련 `Terms → Concepts → Official Docs → Lab`을 다시 확인합니다.
4. [`020-retry-dashboard.md`](./020-retry-dashboard.md)에 +1일 / +7일 재시험을 기록합니다.
5. 최근 오답 재시험 **90% 이상**을 목표로 합니다.

## Common Error Codes

| 코드 | 의미 |
|---|---|
| CONCEPT | 개념 이해 부족 |
| COMPARE | 유사 기능·개념 혼동 |
| MEMORY | 용어·기능 기억 실패 |
| READING | 문제 조건 해석 실패 |
| SCOPE | Enterprise/Org/Repo 등 범위 판단 오류 |
| PRACTICE | 실습 경험 부족 |
| SECURITY | 보안·권한 판단 오류 |
| TROUBLE | Troubleshooting 순서 오류 |
| SCENARIO | 상황에 맞는 최선의 선택 실패 |
| REPEAT | 같은 개념 반복 오답 |

각 과정의 전문 Error Code는 과정별 `120-wrong-answers/`에서 추가합니다.

## Standard Retry Cycle

```text
Wrong Answer
   ↓
Error Code
   ↓
Root Cause 1문장
   ↓
Correct Principle 1문장
   ↓
Official Reference
   ↓
Related Lab
   ↓
+1 Day Retry
   ↓
+7 Day Retry
   ↓
90%+
```

## Course Links

| 코드 | 과정별 오답 시스템 |
|---:|---|
| 001 | [`Foundations`](../001-foundations/120-wrong-answers/) |
| 002 | [`Actions`](../002-actions/120-wrong-answers/) |
| 003 | [`Copilot`](../003-copilot/120-wrong-answers/) |
| 004 | [`Administration`](../004-administration/120-wrong-answers/) |
| 005 | [`Advanced Security`](../005-advanced-security/120-wrong-answers/) |
| 006 | [`Agentic AI Developer`](../006-agentic-ai-developer/120-wrong-answers/) |

## 운영 원칙

오답 개수보다 **같은 오류 코드가 반복되는지**를 더 중요하게 봅니다. `REPEAT`가 발생하면 문제를 더 풀기 전에 해당 개념의 공식 문서와 Lab을 다시 수행합니다.

---
[통합 README](../README.md)