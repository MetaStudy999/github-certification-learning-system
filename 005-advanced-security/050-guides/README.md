# 050 Guides — GHAS 입문자 가이드

## 이해 순서

```text
무슨 위험인가?
→ 어디에서 탐지하는가?
→ 어떻게 예방하는가?
→ Alert가 생기면 누가 대응하는가?
→ 어떻게 수정하고 검증하는가?
→ 조직 전체 정책으로 어떻게 확장하는가?
```

## 3개 핵심 Suite를 먼저 구분

### Secret Protection

Credential·Token·Key가 코드에 노출되는 위험을 다룹니다.

### Supply Chain Security

Dependency와 Package를 통해 들어오는 취약성·라이선스·구성요소 위험을 다룹니다.

### Code Security

Source Code 자체의 취약한 Data Flow와 Pattern을 분석합니다.

## Alert 대응 기본 공식

```text
Alert 확인
→ 실제 위험인가?
→ 영향 범위는?
→ Credential/Dependency/Code 중 무엇인가?
→ 우선순위
→ Remediation
→ 재검증
→ Evidence
```

## 주의

- 실제 Secret을 실습용으로 Commit하지 않습니다.
- Production 보호기능을 실습을 위해 끄지 않습니다.
- 공개 Repository에는 민감한 Security Evidence를 저장하지 않습니다.

---
[← 040 Official Docs](../040-official-docs/README.md) · [다음: 060 Labs →](../060-labs/README.md)
