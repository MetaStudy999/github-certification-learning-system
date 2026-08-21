# 050 Question Set — Security, Admin & Community (Q041–Q050)

## Q041
GitHub 계정 보안을 강화하기 위해 비밀번호 외에 추가 인증 요소를 요구하는 기능은?

A. 2FA  
B. Fork  
C. Star  
D. Gist

<details><summary>정답 및 해설</summary>

**정답: A** — 2FA(Two-Factor Authentication, 이중 인증)는 계정 탈취 위험을 줄이는 데 도움이 됩니다.
</details>

## Q042
중요한 `main` Branch에 직접 Push를 제한하고 Merge 전 Review나 Check를 요구하려 한다. 가장 관련 있는 기능은?

A. Branch Protection 또는 Ruleset  
B. Sponsors  
C. Wiki  
D. Star

<details><summary>정답 및 해설</summary>

**정답: A** — 보호 규칙을 통해 중요 Branch의 변경 조건을 강제할 수 있습니다.
</details>

## Q043
Repository에 대한 접근 권한을 업무에 필요한 수준으로만 부여하는 보안 원칙은?

A. Least Privilege  
B. Maximum Exposure  
C. Public by Default  
D. No Review

<details><summary>정답 및 해설</summary>

**정답: A** — 최소 권한 원칙은 불필요한 권한을 줄여 위험을 낮춥니다.
</details>

## Q044
API Token이나 Password를 Source Code에 직접 Commit하면 안 되는 가장 중요한 이유는?

A. Commit 메시지가 길어지기 때문  
B. 민감정보가 Git 이력과 Remote에 노출될 수 있기 때문  
C. Branch를 만들 수 없기 때문  
D. README가 삭제되기 때문

<details><summary>정답 및 해설</summary>

**정답: B** — Secret은 적절한 비밀정보 관리 기능을 사용하고 코드에 직접 저장하지 않는 것이 기본 원칙입니다.
</details>

## Q045
Organization에서 여러 사용자를 역할이나 업무 단위로 묶어 Repository 권한을 관리하는 데 유용한 것은?

A. Team  
B. Gist  
C. Star  
D. Release note만

<details><summary>정답 및 해설</summary>

**정답: A** — Team을 사용하면 여러 사용자의 접근을 그룹 단위로 관리하기 쉽습니다.
</details>

## Q046
Repository Visibility에 대한 설명으로 가장 적절한 것은?

A. Public/Private 설정은 누가 Repository를 볼 수 있는지와 관련된다.  
B. Visibility는 Git Commit 메시지 형식만 결정한다.  
C. Private Repository에는 Issue를 만들 수 없다.  
D. Public Repository는 Branch를 사용할 수 없다.

<details><summary>정답 및 해설</summary>

**정답: A**
</details>

## Q047
오픈소스 협업 원칙을 회사 내부 개발에 적용하는 방식은?

A. InnerSource  
B. Codespaces  
C. Pages  
D. Sponsors

<details><summary>정답 및 해설</summary>

**정답: A** — InnerSource는 조직 내부에서 오픈소스식 협업 모델을 적용합니다.
</details>

## Q048
Open Source와 InnerSource의 차이를 가장 잘 설명한 것은?

A. 둘 다 항상 외부 공개가 필수다.  
B. Open Source는 일반적으로 외부 공개 협업을 포함할 수 있고, InnerSource는 조직 내부에서 오픈소스 방식의 협업을 적용한다.  
C. InnerSource에서는 Pull Request를 사용할 수 없다.  
D. Open Source는 License가 필요 없다.

<details><summary>정답 및 해설</summary>

**정답: B**
</details>

## Q049
관심 있는 Repository의 활동 알림을 받고 싶을 때 가장 직접적으로 관련 있는 기능은?

A. Watch  
B. Fork 삭제  
C. License 변경  
D. Codespace 종료

<details><summary>정답 및 해설</summary>

**정답: A** — Watch는 Repository 활동에 대한 알림 구독과 관련됩니다.
</details>

## Q050
외부 공개 프로젝트에 기여하기 전 가장 적절한 행동은?

A. 프로젝트의 README, CONTRIBUTING, LICENSE 등 관련 문서를 먼저 확인한다.  
B. 규칙을 확인하지 않고 대규모 PR을 보낸다.  
C. 원본 `main`에 무단 Push한다.  
D. 보안 취약점을 반드시 공개 Issue로만 게시한다.

<details><summary>정답 및 해설</summary>

**정답: A** — 프로젝트별 기여 규칙과 라이선스, 보안 정책을 먼저 확인하는 것이 적절합니다.
</details>

## 50-Question Gate

Q001–Q050을 모두 풀고 점수를 기록하세요.

- **40/50 이상**: 1차 Gate 통과
- **43/50 이상**: 권장 목표
- 오답만 다시 풀었을 때 **90% 이상** 목표

오답은 [`120-wrong-answers`](../../120-wrong-answers/README.md)에 원인까지 기록합니다.

---

[← 040 Modern Development](../040-modern-development-projects/README.md) · [Question Bank Index →](../README.md) · [Final Review →](../../090-final-review/README.md)
