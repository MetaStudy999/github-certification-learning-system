# 실습 (Lab, LAB) 050 — 저장소 문서화 (Repository Documentation, RD)

> **README · LICENSE · CONTRIBUTING · SECURITY · CODEOWNERS 이해와 구성**

## 000. 빠른 시작 (Quick Start, QS)

Repository는 코드만 저장하는 공간이 아닙니다. 다른 사람이 프로젝트를 이해하고, 사용하고, 기여하고, 보안 문제를 신고할 수 있도록 문서 구조를 갖추는 것이 중요합니다.

## 010. Objective (목표)

완료 후 다음 파일의 역할을 설명할 수 있어야 합니다.

- `README.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CODEOWNERS`

## 020. Concept (개념)

| 파일 | 핵심 목적 |
|---|---|
| README | 프로젝트 소개·설치·사용법·구조 안내 |
| LICENSE | 사용·복제·수정·배포 권한 조건 명시 |
| CONTRIBUTING | 기여 절차와 개발 규칙 안내 |
| SECURITY | 취약점 신고 정책과 지원 범위 안내 |
| CODEOWNERS | 특정 경로의 코드 소유자·리뷰 책임자 지정 |

## 030. Practice (따라하기)

### 031. README 점검

README에 최소 다음 항목이 있는지 확인합니다.

```text
프로젝트 이름
목적
Quick Start
사용 방법
Repository 구조
기여 방법
라이선스
```

### 032. CONTRIBUTING.md 작성 연습

예시 구조:

```markdown
# Contributing

## Workflow
1. Create an issue.
2. Create a branch.
3. Make and verify changes.
4. Open a pull request.
5. Request review.

## Commit Convention
- feat: 기능
- fix: 수정
- docs: 문서
- test: 테스트
```

### 033. SECURITY.md 작성 연습

공개 Repository에서는 실제 비밀정보를 넣지 않습니다.

예시 구조:

```markdown
# Security Policy

## Supported Versions
현재 지원 중인 버전을 기록합니다.

## Reporting a Vulnerability
보안 취약점은 공개 Issue 대신 지정된 비공개 신고 경로를 사용합니다.
```

### 034. LICENSE 확인

GitHub에서 Repository의 라이선스 파일을 열어 다음을 확인합니다.

- 라이선스 이름
- 허용되는 행위
- 조건
- 제한·면책

> 이 Lab에서는 특정 라이선스를 법률 자문처럼 추천하지 않습니다. 프로젝트 목적에 맞는 라이선스를 선택해야 합니다.

### 035. CODEOWNERS 구조 이해

예시:

```text
* @owner
/docs/ @docs-team
/src/ @dev-team
```

핵심은 **경로 패턴 → 담당 Reviewer**의 관계입니다.

실제 적용 시 Repository 권한과 조직 구조에 맞는 사용자 또는 Team을 지정합니다.

## 040. Challenge (스스로 해보기)

가상의 오픈소스 프로젝트를 가정하고 다음 5개 문서의 목차를 직접 설계합니다.

1. README
2. LICENSE
3. CONTRIBUTING
4. SECURITY
5. CODEOWNERS

## 050. Verify (검증)

- [ ] README의 목적을 설명할 수 있다.
- [ ] LICENSE와 README의 역할 차이를 설명할 수 있다.
- [ ] CONTRIBUTING이 필요한 이유를 설명할 수 있다.
- [ ] SECURITY에서 공개 Issue와 취약점 신고를 구분할 수 있다.
- [ ] CODEOWNERS가 Review 흐름과 어떻게 연결되는지 설명할 수 있다.

## 060. Evidence (증거 기록)

```text
README 개선 항목:
CONTRIBUTING 초안 경로:
SECURITY 초안 경로:
LICENSE 확인 내용:
CODEOWNERS 예시:
배운 점:
```

## 070. 시험 포인트

다음 질문에 바로 답할 수 있어야 합니다.

- 프로젝트의 첫 안내 문서는 무엇인가?
- 기여 규칙은 어디에 두는가?
- 보안 취약점 신고 절차는 어디에 두는가?
- 코드 영역별 Reviewer 책임을 정의하는 파일은 무엇인가?

---

[← Lab 040](../040-github-flow/README.md) · [다음: Lab 060 →](../060-collaboration/README.md)
