# 실습 (Lab, LAB) 060 — 보안 정책 / 규칙 집합 (Security Policies / Rulesets, SPR)

## 목표 (Objective, OBJ)

Enterprise/Organization Policy와 Repository Ruleset을 사용해 **Governance 요구사항을 구체적인 통제로 변환**합니다.

## 개념 (Concept, CPT)

```text
Business / Compliance Requirement
        ↓
Enterprise / Org Policy
        ↓
Repository Ruleset / Settings
        ↓
Developer Workflow
        ↓
Audit / Report
```

## 실습 (Practice, PRAC) — 정책 맵 (Policy Map, PM)

가상 요구사항:

- 기본 Branch 직접 Push 제한
- PR Review 필수
- 중요한 Repository는 승인된 Workflow 정책 준수
- Security 기능을 조직 표준으로 사용
- 외부 Integration 사용을 통제

다음을 작성합니다.

| Requirement | Scope | Control | 증빙 (Evidence, EVD) |
|---|---|---|---|
| Direct push 제한 | | | |
| Review 필수 | | | |
| Action 사용 정책 | | | |
| Security posture | | | |
| App governance | | | |

## 실습 (Practice, PRAC) — Ruleset 설계 (Ruleset Design, RD)

예시:

```text
Target: default branch
Rules:
- Require pull request
- Require approvals
- Require status checks
- Restrict force push
- Restrict deletion
```

실제 Production Repository에 임의 적용하지 말고 Sandbox/설계 문서로 수행합니다.

## 데이터 보호 질문 (Data Protection Questions, DPQ)

- 누가 민감 Repository를 볼 수 있는가?
- 어떤 Audit Evidence가 필요한가?
- 어떤 Branch/Tag 변경을 막아야 하는가?
- 어떤 Security Feature를 중앙 활성화해야 하는가?

## 도전 과제 (Challenge, CHL)

`Policy`와 `Ruleset`을 동일한 것으로 설명하면 왜 부정확한지 예시와 함께 작성하세요.

## 검증 (Verify, VER)

- [ ] Enterprise / Org Policy 목적 설명
- [ ] Ruleset 목적 설명
- [ ] Requirement → Control → Evidence 흐름 작성
- [ ] Security Posture와 Data Protection 연결
- [ ] Governance를 단순 UI 설정으로만 이해하지 않음

---
[← Lab 050](../050-support-standards-diagnostics/README.md) · [Lab 070 →](../070-security-features-response/README.md)
