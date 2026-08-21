# 020 Evidence Checklist — 프로젝트 증거 체크리스트

Foundations 프로젝트를 `CLEAR`로 판정하려면 결과물이 재현 가능하게 남아 있어야 합니다.

## 저장소 Evidence (Repository Evidence, RE)

- [ ] Repository URL
- [ ] README.md
- [ ] LICENSE
- [ ] CONTRIBUTING.md
- [ ] SECURITY.md
- [ ] `.github/CODEOWNERS`

## 협업 Evidence (Collaboration Evidence, CE)

- [ ] Issue URL
- [ ] Label 적용 화면 또는 기록
- [ ] Assignee 지정 기록
- [ ] Feature Branch 이름
- [ ] Commit SHA 최소 2개
- [ ] Pull Request URL
- [ ] Review 기록
- [ ] Merge 기록
- [ ] 연결 Issue Close 확인

## 프로젝트 Evidence (Project Evidence, PE)

- [ ] GitHub Projects Item
- [ ] Status Field 사용
- [ ] Issue/PR 상태 변화 기록

## 설명 Evidence

다음 질문에 대한 짧은 설명을 작성합니다.

1. Git과 GitHub의 차이
2. Clone과 Fork의 차이
3. Issue와 Discussion의 차이
4. Pull Request와 Merge의 차이
5. Actions / Copilot / Codespaces의 차이
6. Branch Protection/Ruleset의 목적
7. Open Source와 InnerSource의 차이

## 저장 위치

최종 증거는 `../../150-evidence/`에 정리합니다.

권장 파일명:

```text
001-project-summary.md
002-issue-pr-evidence.md
003-lab-evidence.md
004-exam-result.md
```

> 개인정보, Access Token, Secret, 복구 코드 등 민감정보는 Evidence에 포함하지 않습니다.
