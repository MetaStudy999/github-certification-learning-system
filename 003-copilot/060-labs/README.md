# 060 Labs — GitHub 코파일럿 (GitHub Copilot, GHCOP / GH-300) 단계별 실습

## 빠른 시작 (Quick Start, QS)

GH-300 실습은 **AI Output을 많이 만드는 것**보다 `적절한 기능 선택 → Context 설계 → 검증 → Evidence`를 반복하는 것이 핵심입니다.

## Lab Roadmap

| Level | Lab | 핵심 기술 |
|---:|---|---|
| 010 | [First Copilot Interaction](./010-first-interaction/) | Completion / Chat |
| 020 | [Prompt Fundamentals](./020-prompt-fundamentals/) | Goal / Context / Constraints |
| 030 | [Context Engineering](./030-context-engineering/) | File / Selection / Repository Context |
| 040 | [Code Generation](./040-code-generation/) | 기능 구현 / Human Review |
| 050 | [Explanation & Documentation](./050-explanation-documentation/) | 설명 / README / Comment |
| 060 | [Testing](./060-testing/) | Unit Test / Integration / Edge Case |
| 070 | [Debugging](./070-debugging/) | Error Analysis / Fix / Verification |
| 080 | [Refactoring](./080-refactoring/) | 구조 개선 / Review |
| 090 | [Responsible AI & Privacy](./090-responsible-ai-privacy/) | 검증 / 민감정보 / Exclusion |
| 100 | [End-to-End AI Development](./100-end-to-end-development/) | 요구사항 → 구현 → Test → Review |
| 110 | [CLI / Agent / MCP](./110-cli-agent-mcp/) | Copilot CLI / Agent Mode / MCP |
| 120 | [Code Review & Organization Policy](./120-code-review-org-policy/) | Code Review / Policy / Audit Log |
| 130 | [Spaces / Spark / Instructions](./130-spaces-spark-instructions/) | Spaces / Spark / Instructions / Prompt Files |

## 공통 Lab 구조

```text
Objective (목표)
→ Concept (개념)
→ Practice (따라하기)
→ Challenge (스스로 해보기)
→ Verify (검증)
→ Evidence (증거 기록)
```

## 실습 권장 순서

```text
010–030  사용법 + Prompt/Context 기초
   ↓
040–080  개발 생산성
   ↓
090      Responsible AI / Privacy
   ↓
100      End-to-End 통합
   ↓
110–130  2026 시험 핵심 확장 기능
```

## 안전 원칙

- 실제 Secret, Password, Token, Production Credential을 Prompt에 넣지 않습니다.
- AI Output은 실행·Test·Review 전에 신뢰하지 않습니다.
- Production Code를 무검증으로 적용하지 않습니다.
- Agent에게 불필요하게 넓은 Tool·File·Credential 권한을 주지 않습니다.
- MCP Server와 외부 Tool의 신뢰성·권한 범위를 확인합니다.
- 라이선스·보안·개인정보 요구사항을 별도로 검토합니다.

## 완료 기준

- [ ] Inline Suggestion / Chat / Edits / Agent Mode 사용 목적 구분
- [ ] Prompt와 Context를 개선한 Before/After Evidence
- [ ] 생성 코드의 Accept / Modify / Reject 사례 기록
- [ ] Test와 Edge Case 검증
- [ ] CLI / Agent / MCP 역할 설명
- [ ] Code Review / Organization Policy 시나리오 설명
- [ ] Content Exclusion / Safeguard 한계 설명
- [ ] End-to-End Project 완료

---
[← 050 Guides](../050-guides/README.md) · [Lab 010 시작 →](./010-first-interaction/README.md)
