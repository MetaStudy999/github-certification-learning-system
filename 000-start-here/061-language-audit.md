# 한글·영어·약어 표기 점검 (Korean-English-Abbreviation Audit, KEAA)

이 문서는 `scripts/normalize-language-notation.py`가 Repository 전체 Markdown 제목을 점검하여 자동 생성합니다.

## 점검 결과 (Audit Result, AR)

추가 검토가 필요한 영어 단독 제목: **5개**

아래 항목은 공식 제품명·코드명인지, 한글·영어·약어 병기가 필요한 학습 제목인지 사람이 최종 확인합니다.

- `003-copilot/010-overview/README.md` L1: `010 Overview — GH-300`
- `003-copilot/070-exercises/020-copilot-features/README.md` L47: `E020-10 — Spaces / Spark`
- `003-copilot/150-evidence/090-content-verification.md` L66: `5. Exercises`
- `005-advanced-security/010-overview/README.md` L1: `010 Overview — GH-500`
- `006-agentic-ai-developer/010-overview/README.md` L1: `010 Overview — GH-600`

## 적용 기준 (Applied Standard, AS)

- 기준 문서: `000-start-here/060-language-notation-standard.md`
- 표기 형식: `한글 (English Full Name, ABBR)`
- 명령어·코드·경로·URL·YAML/JSON 키는 번역하지 않음
- Q001/E001 같은 문제·연습문제 식별자는 번역 대상에서 제외
