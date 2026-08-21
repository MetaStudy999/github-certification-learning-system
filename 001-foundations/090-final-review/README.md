# 090 Final Review — 시험 직전 압축 복습

## 빠른 시작 (Quick Start, QS)

시험 직전에는 새로운 내용을 크게 늘리지 않습니다. **헷갈리는 비교 + 최근 오답 + 공식 Domain** 중심으로 압축합니다.

추가 자료:

- [`010-final-checklist.md`](./010-final-checklist.md) — 최종 점검표
- [`020-confusion-matrix.md`](./020-confusion-matrix.md) — 헷갈리는 개념 비교
- [`030-exam-day-strategy.md`](./030-exam-day-strategy.md) — 시험 당일 전략

## 1. 10분 핵심 비교

| A | B | 핵심 차이 |
|---|---|---|
| Git | GitHub | 버전 관리 시스템 vs 협업 플랫폼 |
| Clone | Fork | Local 복제 vs GitHub 공간의 독립 Repository 복제 |
| Fetch | Pull | 정보만 가져오기 vs 가져와 현재 Branch에 통합 |
| Branch | Fork | 같은 Repo 내부 작업선 vs 별도 Repo |
| Issue | Discussion | 작업 추적 vs 장기 토론·Q&A |
| PR | Merge | 변경 제안·검토 과정 vs 실제 병합 |
| Organization | Enterprise | 협업 관리 단위 vs 여러 Org의 상위 거버넌스 |
| Role | Permission | 사용자 역할 개념 vs Resource별 허용 수준 |
| Actions | Codespaces | 자동화 vs 개발환경 |
| Copilot | Actions | AI 개발 보조 vs Workflow 자동화 |
| Open Source | InnerSource | 공개 협업 vs 조직 내부 오픈소스 방식 |

더 많은 비교는 [`020-confusion-matrix.md`](./020-confusion-matrix.md)를 사용합니다.

## 2. Repository 파일 5종

```text
README       → 프로젝트 소개
LICENSE      → 사용 조건
CONTRIBUTING → 기여 방법
CODEOWNERS   → Review 책임
SECURITY     → 취약점 신고 정책
```

## 3. GitHub Flow

```text
Issue
→ Branch
→ Commit
→ Push
→ Pull Request
→ Review / Checks
→ Merge
```

## 4. Git 명령 최소 세트

```bash
git status
git add .
git commit -m "message"
git branch
git switch -c feature/example
git fetch
git pull
git push
git log --oneline
```

## 5. Modern Development 기능

```text
Actions    → 자동화 / CI/CD
Copilot    → AI 개발 보조
Codespaces → Cloud 개발환경
Projects   → 작업·Issue·PR 관리
Pages      → 정적 웹사이트
Wiki       → Repository 지식 문서
Gist       → 작은 코드·메모 공유
```

## 6. Security / Administration

반드시 구분:

- 2FA / Passkey
- Repository Visibility
- Branch Protection / Ruleset
- Organization / Team
- Role / Permission
- Enterprise Managed Users, EMU

## 7. Community

- Open Source
- InnerSource
- GitHub Sponsors
- Marketplace
- Fork
- Template Repository
- Star / Watch / Follow

## 8. 시험 직전 Gate

- [ ] Domain 7개를 순서와 비중까지 확인했다.
- [ ] 핵심 비교 항목을 자료 없이 설명한다.
- [ ] GitHub Flow를 직접 설명한다.
- [ ] Repository 핵심 파일 5종을 구분한다.
- [ ] Mock Exam 최근 2회가 85% 이상이다.
- [ ] Final Mock 90% 이상을 권장한다.
- [ ] 최근 오답 재시험이 90% 이상이다.
- [ ] 공식 Study Guide 변경사항을 다시 확인했다.

## 9. 시험 당일 원칙

1. 문제의 목적과 제약조건을 먼저 찾습니다.
2. `BEST`, `MOST appropriate`, `FIRST` 같은 표현을 주의합니다.
3. 익숙한 단어 하나만 보고 답을 고르지 않습니다.
4. 비슷한 기능은 목적을 기준으로 비교합니다.
5. 모르는 문제에 오래 머무르지 않고 전체 시간을 관리합니다.

상세 전략은 [`030-exam-day-strategy.md`](./030-exam-day-strategy.md)를 확인합니다.

---

[← 080 Question Bank](../080-question-bank/README.md) · [다음: 100 Projects →](../100-projects/README.md)
