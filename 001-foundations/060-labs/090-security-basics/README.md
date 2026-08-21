# Lab 090 — Security Basics

> **2FA · Permissions · Visibility · Rulesets / Branch Protection · Secrets 기본 이해**

## 000. Quick Start

이 Lab에서는 GitHub 보안 기능을 깊게 설정하기보다 **계정 보안, 접근 권한, Repository 보호의 목적**을 구분합니다.

> 실습 중 실제 보안 설정을 약화시키지 않습니다. 2FA 해제, 공개 전환, 보호 규칙 제거 같은 작업은 하지 않습니다.

## 010. Objective (목표)

완료 후 다음 개념을 설명할 수 있어야 합니다.

- Two-Factor Authentication, 2FA (2단계 인증)
- Repository Visibility (가시성)
- Role / Permission (역할 / 권한)
- Least Privilege (최소 권한)
- Ruleset / Branch Protection (규칙 집합 / 브랜치 보호)
- Secret (비밀정보)

## 020. Concept (개념)

| 개념 | 목적 |
|---|---|
| 2FA | 비밀번호 외 추가 인증 요소로 계정 보호 |
| Visibility | Repository 접근 범위를 제어 |
| Role / Permission | 사용자가 할 수 있는 작업 범위를 제어 |
| Least Privilege | 필요한 최소 권한만 부여 |
| Ruleset / Branch Protection | 중요한 Branch 변경 조건과 보호 정책 적용 |
| Secret | 토큰·키 등 민감한 값을 코드에 직접 저장하지 않도록 관리 |

## 030. Practice (안전한 관찰 실습)

### 031. 계정 보안 상태 확인

GitHub 계정의 보안 설정에서 2FA 관련 상태를 확인합니다.

확인만 하고 기존 보호 설정을 약화시키지 않습니다.

기록:

```text
2FA 개념 설명 가능: YES / NO
Recovery 방법 확인: YES / NO
```

복구 코드 자체는 Repository나 학습 노트에 저장하지 않습니다.

### 032. Repository Visibility 확인

현재 학습 Repository의 가시성을 확인합니다.

```text
Public / Private / 기타 제공 옵션
```

질문:

```text
Public Repository와 Private Repository의 접근 차이는 무엇인가?
```

### 033. Permission 관찰

Repository의 Collaborator/Access 관련 화면에서 권한 개념을 확인합니다.

핵심 원칙:

```text
필요한 사람에게 필요한 권한만 제공한다.
```

### 034. Branch 보호 관찰

Repository의 Rules 또는 Branch protection 관련 설정 위치를 확인합니다.

다음과 같은 보호 목적을 찾습니다.

- Pull Request를 통한 변경 요구
- Review 요구
- Status Check 요구
- 강제 Push 제한
- 삭제 제한

사용 가능한 설정과 명칭은 Repository 유형과 GitHub UI에 따라 달라질 수 있습니다.

### 035. Secret과 일반 Variable 비교

예를 들어 API Token 같은 민감정보를 다음처럼 코드에 직접 넣으면 안 됩니다.

```text
API_TOKEN=실제-비밀-토큰
```

학습용 문서에는 실제 Secret을 절대 Commit하지 않습니다.

비교:

```text
Secret   → 노출되면 안 되는 민감 값
Variable → 일반 설정값
```

## 040. Challenge (스스로 해보기)

다음 상황에 가장 적절한 보안 개념을 연결합니다.

1. 비밀번호가 유출되어도 추가 인증이 필요하게 한다.
2. 외부인이 Repository 내용을 보지 못하게 한다.
3. 개발자에게 관리자 권한까지 주지 않는다.
4. `main`에 바로 Push하지 못하도록 한다.
5. API 키를 코드에 직접 쓰지 않는다.

## 050. Verify (검증)

- [ ] 2FA의 목적을 설명할 수 있다.
- [ ] Public/Private Visibility 차이를 설명할 수 있다.
- [ ] Role과 Permission의 관계를 설명할 수 있다.
- [ ] Least Privilege 원칙을 설명할 수 있다.
- [ ] Ruleset/Branch Protection의 목적을 설명할 수 있다.
- [ ] Secret을 코드에 Commit하면 안 되는 이유를 설명할 수 있다.

## 060. Evidence (증거 기록)

민감정보 없이 다음만 기록합니다.

```text
2FA 개념 확인: 완료/미완료
Repository Visibility:
Branch 보호 기능 관찰:
Permission 학습 내용:
Secret vs Variable 설명:
```

## 070. 시험 포인트

보안 문제에서는 기술 이름보다 **목적에 맞는 기능 선택**이 중요합니다.

```text
계정 보호       → 2FA
접근 범위       → Visibility / Permission
권한 최소화     → Least Privilege
중요 Branch 보호 → Ruleset / Branch Protection
민감 값 보호    → Secret
```

---

[← Lab 080](../080-modern-development/README.md) · [다음: Lab 100 →](../100-community-contribution/README.md)
