# 060 Privacy & Safeguards — 수행형 연습

## 목표

Content Exclusion, Public Code Matching Filter, Editor Settings, Output Ownership, Troubleshooting을 **보호장치의 목적과 한계** 관점에서 이해합니다.

## 연습문제 (Exercises, EXR)

### E060-01 — Content Exclusion 목적
Content Exclusion이 해결하려는 문제를 한 문장으로 설명하고, `파일 삭제`와 다른 점을 적으세요.

### E060-02 — Content Exclusion 한계
Content Exclusion을 설정했으니 Secret Management가 필요 없다는 주장에 반박하세요.

### E060-03 — 적용 범위 확인
특정 파일이 제외되었다고 기대했지만 Copilot 응답에 관련 정보가 나타났습니다. 어떤 설정 범위·경로·Editor 지원·적용 지연 가능성을 확인할지 Checklist를 만드세요.

### E060-04 — Public 코드 Matching (Public Code Matching, PCM)
공개 코드와 일치하는 Suggestion을 필터링하는 기능의 목적과, 이것만으로 라이선스 검토가 완전히 끝나지 않는 이유를 설명하세요.

### E060-05 — 출력물 소유권 (Output Ownership, OO)
AI Output을 사용하기 전에 조직의 법무·라이선스·정책 기준을 확인해야 하는 이유를 작성하세요.

### E060-06 — 제안이 표시되지 않음 (Suggestions Not Showing, SNS)
Editor에서 Copilot Suggestion이 보이지 않을 때 확인할 순서를 작성하세요.

예시 범주:

```text
Extension / sign-in
→ Feature enabled?
→ File/language support
→ Policy / exclusion
→ Network / service
→ Restart / logs
```

### E060-07 — Prompt에 Secret 포함
API Key를 Prompt에 넣어 디버깅하려는 동료에게 더 안전한 대안을 제안하세요.

### E060-08 — 조직 정책 (Organization Policy, OP)
조직에서 특정 Copilot 기능을 제한해야 하는 이유를 Security, Compliance, Cost, Data Governance 관점에서 작성하세요.

### E060-09 — 개인정보 보호 비교 보안 (Privacy vs Security, PS)
`Privacy`와 `Security`를 각각 한 문장으로 정의하고 Copilot 사용 예시를 하나씩 연결하세요.

### E060-10 — 다층 방어 안전장치 (Safeguard Defense in Depth, SDD)
다음 보호 계층을 하나의 Defense-in-Depth 흐름으로 설명하세요.

```text
Policy
→ Content Exclusion
→ Public Code Matching Filter
→ Human Review
→ Test / Security Check
→ Audit / Monitoring
```

## 자가 검증

- [ ] Content Exclusion 목적과 한계를 구분한다.
- [ ] Public Code Matching Filter 목적을 설명한다.
- [ ] Output Ownership을 단순 기능 문제가 아닌 정책·법적 검토와 연결한다.
- [ ] Suggestion / Exclusion 문제를 단계적으로 Troubleshoot한다.
- [ ] Secret을 Prompt에 넣지 않는다.

## 관련 Lab

- [`090-responsible-ai-privacy`](../../060-labs/090-responsible-ai-privacy/)
- [`120-code-review-org-policy`](../../060-labs/120-code-review-org-policy/)

---
[← 050 Developer Productivity](../050-developer-productivity/README.md) · [080 Question Bank →](../../080-question-bank/README.md)
