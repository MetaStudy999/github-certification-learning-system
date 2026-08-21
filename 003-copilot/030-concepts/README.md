# 030 Concepts — GitHub Copilot 핵심 개념

## 기본 흐름

```text
Developer Intent
  ↓
Prompt + Repository / Editor Context
  ↓
Copilot
  ↓
Suggestion / Chat Response
  ↓
Human Review
  ↓
Run / Test / Verify
```

## 반드시 구분

| A | B | 핵심 차이 |
|---|---|---|
| Completion | Chat | 코드 작성 중 제안 vs 대화형 문제 해결 |
| Prompt | Context | 직접 지시 vs AI가 참고하는 주변 정보 |
| Zero-shot | Few-shot | 예시 없음 vs 예시 포함 |
| Generate | Refactor | 새 코드 생성 vs 기존 코드 구조 개선 |
| Explanation | Verification | 코드 설명 vs 실제 실행·Test 검증 |
| AI Suggestion | Correct Code | 제안일 뿐 정답 보장 없음 |
| Privacy | Security | 데이터 처리 보호 vs 시스템·코드 위험 방어 |
| Content Exclusion | Delete | Context 사용 제외 vs 원본 콘텐츠 삭제 |

## 핵심 원칙

1. 명확한 목적과 제약조건을 Prompt에 제공합니다.
2. 관련 코드와 오류 메시지 등 필요한 Context만 제공합니다.
3. 생성된 코드는 인간이 검토합니다.
4. Test, Lint, Security Check로 결과를 검증합니다.
5. 민감정보를 Prompt에 불필요하게 포함하지 않습니다.

---
[← 020 Terms](../020-terms/README.md) · [다음: 040 Official Docs →](../040-official-docs/README.md)
