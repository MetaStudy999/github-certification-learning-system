# 090 Final Review — GH-300 시험 직전 복습

## 빠른 시작 (Quick Start, QS)

시험 직전에는 새 기능을 무작정 추가 학습하지 않습니다.

```text
최신 Study Guide 확인
→ 6개 Skill Area
→ 헷갈리는 기능 비교
→ QBank 오답
→ Mock 오답
→ Final Gate
```

## 2026-08-07 Skills Measured

| Skill Area | 비중 |
|---|---:|
| Use GitHub Copilot responsibly | 15–20% |
| Use GitHub Copilot features | 25–30% |
| Understand GitHub Copilot data and architecture | 10–15% |
| Apply prompt engineering and context crafting | 10–15% |
| Improve developer productivity with GitHub Copilot | 10–15% |
| Configure privacy, content exclusions, and safeguards | 10–15% |

## 10분 핵심 비교

| A | B | 핵심 차이 |
|---|---|---|
| Inline Suggestion | Chat | 작성 중 제안 vs 대화형 지원 |
| Chat | Edits | 설명·탐색 vs 변경 적용 중심 |
| Edits | Agent Mode | 편집 중심 vs 다단계 자율 작업 |
| Agent Mode | CLI | Agentic Task 수행 vs Terminal 인터페이스 |
| Tool | MCP | 실제 기능 vs Tool/Context 연결 프로토콜 |
| Prompt | Context | 직접 지시 vs 참고 정보 |
| Prompt Crafting | Prompt Engineering | 개별 Prompt 작성 vs 반복 전략·성능 개선 |
| Zero-shot | Few-shot | 예시 없음 vs 예시 포함 |
| Instruction File | Prompt File | 지속 지침 vs 반복 Task Prompt |
| Space | Spark | 지식/Context 공간 vs 자연어 기반 앱 생성 |
| Explanation | Verification | 설명 vs 실제 검증 |
| Content Exclusion | Secret Management | Context 사용 제한 vs Secret 생명주기·권한 관리 |
| AI Review | Human Review | 보조 제안 vs 최종 책임 판단 |
| Privacy | Security | 데이터 보호 vs 시스템·코드 위험 방어 |

## Data Flow 한 줄 암기보다 이해

```text
Developer Input / Context
→ Prompt Building
→ Filtering / Proxy
→ LLM
→ Post-processing
→ Suggestion
→ Human Verification
```

## Agentic 흐름 (Agentic Flow, AF)

```text
Goal
→ Agent Mode
→ Context / Instructions
→ Tools / MCP
→ Agent Session / Sub-Agent
→ Changes / Actions
→ Test / Review
→ Human Approval
```

## Final 리뷰 파일 (Final Review Files, FRF)

- [`010-final-checklist.md`](./010-final-checklist.md) — 응시 전 체크
- [`020-confusion-matrix.md`](./020-confusion-matrix.md) — 유사 개념 비교
- [`030-exam-day-strategy.md`](./030-exam-day-strategy.md) — 시험 당일 전략

## 시험 Gate (Exam Gate, EG)

- [ ] Microsoft Learn Study Guide의 최신 적용일 확인
- [ ] 6개 Skill Area와 비중 설명
- [ ] IDE / CLI / Edits / Agent Mode / MCP 구분
- [ ] Data Flow 설명
- [ ] Prompt / Context / Instructions / Prompt Files 구분
- [ ] Responsible AI / Human Review 설명
- [ ] Testing / Edge Case / Assertion 설명
- [ ] Privacy / Content Exclusion / Safeguard 설명
- [ ] QBank 2회차 85% 이상
- [ ] 최근 Mock 2회 연속 85% 이상
- [ ] Final Mock 90% 이상 권장
- [ ] 오답 재시험 90% 이상

---
[← 080 Question Bank](../080-question-bank/README.md) · [다음: 100 Projects →](../100-projects/README.md)
