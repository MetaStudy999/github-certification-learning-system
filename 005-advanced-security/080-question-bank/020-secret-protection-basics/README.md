# 문제은행 (Question Bank, QB) 020 — 비밀 보호 기초 (Secret Protection Basics, SPB)

## Q011–Q020

**Q011.** Secret Protection의 주된 목적은? A. 노출된 자격증명 탐지·관리 B. 코드 포맷팅 C. 브랜치 생성 D. 문서 번역  
**Q012.** Push Protection은 언제 가장 직접적으로 작동하는가? A. 민감정보가 저장소로 들어가기 전 B. Release 후 C. Wiki 수정 시 D. Issue 닫을 때  
**Q013.** Validity Check의 목적은? A. 발견된 자격증명의 유효성 판단 보조 B. 코드 컴파일 C. 라이선스 구매 D. 브랜치 이름 변경  
**Q014.** Custom Pattern이 필요한 이유는? A. 조직 고유 형식 탐지 B. Commit 삭제 C. PR 제목 변경 D. Runner 확장  
**Q015.** Secret Alert 대응에서 가장 우선되는 사고방식은? A. 노출 영향과 자격증명 상태 확인 B. 무조건 삭제만 수행 C. Alert 숨기기 D. 저장소 이름 변경  
**Q016.** Organization 수준 설정의 장점은? A. 여러 저장소에 일관된 정책 적용 B. Git 기록 제거 C. 코드 자동 번역 D. Issue 자동 생성  
**Q017.** Push Protection Bypass에 필요한 운영 원칙은? A. 제한된 권한과 근거 기록 B. 누구나 무기한 사용 C. 감사 기록 제거 D. 기본 활성화 해제  
**Q018.** 실제 Secret을 학습 자료에 넣지 말아야 하는 이유는? A. 추가 노출 위험 방지 B. Git이 지원하지 않음 C. Markdown 제한 D. 시험 규칙과 무관  
**Q019.** Alert를 단순히 Dismiss하는 것과 Remediate하는 것의 차이는? A. 위험 수용/오탐 처리 vs 실제 위험 제거 B. 동일 C. 둘 다 저장소 삭제 D. 둘 다 Branch 보호  
**Q020.** Secret Protection 학습의 적절한 흐름은? A. Detection → Triage → Response → Verification B. Delete → Ignore C. Fork → Star D. Clone → Tag

## 정답 (Answers, ANS)

011 A · 012 A · 013 A · 014 A · 015 A · 016 A · 017 A · 018 A · 019 A · 020 A

### 핵심 복습
- Push Protection = 예방 중심
- Secret Alert = 탐지 후 대응
- Bypass/예외 = 최소 권한 + 근거 + 감사 가능성
- 실제 민감정보는 학습 자료에 사용하지 않음

[← 이전](../010-security-suites-ecosystem/README.md) · [다음 →](../030-secret-protection-operations/README.md)
