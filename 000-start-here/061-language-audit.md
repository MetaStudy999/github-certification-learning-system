# 한글·영어·약어 표기 점검 (Korean-English-Abbreviation Audit, KEAA)

이 문서는 GitHub 자격증 통합 학습 시스템(GitHub Certification Learning System, GCLS)의 Markdown 문서에 **한글 (English Full Name, ABBR)** 표준이 일관되게 적용되었는지 점검합니다.

## 점검 결과 (Audit Result, AR)

영어만으로 작성된 일반 학습 제목을 발견하지 않았습니다. **PASS**

초기 자동 점검에서 발견된 영어 단독 제목을 Repository 전체에 걸쳐 정규화하고, 잔여 항목을 추가 검토하여 반영했습니다.

| 점검 항목 | 결과 |
|---|---:|
| 주요 문서 제목 (Document Titles, DT) | **PASS** |
| 섹션 제목 (Section Headings, SH) | **PASS** |
| 공통 과정 영역 010–150 (Standard Course Areas, SCA) | **PASS** |
| 자격증 과정명 (Certification Course Names, CCN) | **PASS** |
| 실습·연습문제·문제은행 제목 (Lab / Exercise / Question Bank Headings, LEQH) | **PASS** |
| 진행·오답·모의고사·증빙 제목 (Progress / Wrong Answer / Mock / Evidence Headings, PWMEH) | **PASS** |
| 메인 대시보드 핵심 라벨 (Main Dashboard Labels, MDL) | **PASS** |
| 포트폴리오 성장 경로 Mermaid 라벨 (Portfolio Growth Path Labels, PGPL) | **PASS** |

## 적용 형식 (Applied Format, AF)

```text
한글 명칭 (English Full Name, ABBR)
```

예시:

```text
문제은행 (Question Bank, QB)
모의고사 (Mock Exams, ME)
시험 준비도 통과 기준 (Exam Readiness Gate, ERG)
증빙 (Evidence, EVD)
GitHub 기초 (GitHub Foundations, GHF / GH-900)
```

## 예외 원칙 (Exception Policy, EP)

정확성과 재현성을 위해 다음 항목은 영어 원문 또는 공식 식별자를 유지할 수 있습니다.

- 명령어와 소스 코드 (Commands / Source Code, CSC)
- 파일·디렉터리 경로 (File / Directory Paths, FDP)
- URL
- YAML / JSON 키
- API 이름·파라미터
- GitHub 화면에서 실제로 선택해야 하는 공식 UI 라벨
- `Q001`, `E010-01`, `GH-900` 같은 문제·연습·시험 식별자
- `MCP`, `OIDC`, `SAML`, `SCIM`, `SBOM`, `SARIF`처럼 약어 자체가 표준 식별자로 널리 쓰이는 기술 용어

이러한 항목은 번역으로 원문 정확성이 손상되지 않도록 보존하며, 학습 설명에서는 가능한 경우 한국어 의미와 영어 원문을 함께 제공합니다.

## 적용 기준 (Applied Standard, AS)

- 기준 문서: [`060-language-notation-standard.md`](./060-language-notation-standard.md)
- 1차 정규화: `scripts/normalize-language-notation.py`
- 잔여 제목 정규화: `scripts/finalize-language-notation.py`
- 자동 실행: `.github/workflows/normalize-language-notation.yml`
- 적용 범위: Root `README.md`, `000`, `001–006`, `900–990`의 Markdown 문서

## 유지관리 규칙 (Maintenance Rule, MR)

앞으로 새 문서를 생성하거나 기존 문서를 수정할 때도 같은 표준을 사용합니다. 영어 단독 학습 제목이나 공통 라벨이 다시 추가되면 정규화 스크립트와 점검 절차를 통해 동일한 형식으로 맞춥니다.
