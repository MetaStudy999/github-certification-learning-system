# 050 Guides — 입문자 가이드

## Copilot을 이해하는 순서

```text
왜 필요한가?
→ 무엇을 할 수 있는가?
→ 어떤 Context를 사용하는가?
→ 좋은 Prompt는 무엇인가?
→ 생성 결과를 어떻게 검증하는가?
→ Privacy와 Responsible AI를 어떻게 지키는가?
```

## Prompt 기본 구조

좋은 Prompt는 가능하면 다음을 포함합니다.

1. **Goal** — 무엇을 원하는가
2. **Context** — 현재 코드/환경/문제
3. **Constraints** — 지켜야 할 조건
4. **Output** — 원하는 결과 형식
5. **Verification** — 성공 여부 확인 기준

## 예시

```text
Goal: Python 함수의 입력 검증을 개선해 줘.
Context: 아래 함수는 문자열을 받아 날짜로 변환한다.
Constraints: 기존 API는 유지하고 표준 라이브러리만 사용한다.
Output: 수정 코드와 변경 이유를 설명한다.
Verification: 정상/비정상 입력 Unit Test도 작성한다.
```

## 핵심 원칙

Copilot의 출력은 **초안·제안**으로 취급하고 직접 Review/Test합니다.

---
[← 040 Official Docs](../040-official-docs/README.md) · [다음: 060 Labs →](../060-labs/README.md)
