# GH-500 Mock 시험 01 — 질문 (GH-500 Mock Exam 01 — Questions, GH-500MEQ)

> 자체 제작 40문항. 실제 시험문제를 복제하지 않습니다. 먼저 정답 파일을 보지 않고 풉니다.

## 질문 (Questions, Q)

1. 여러 Repository의 보안 상태를 한 화면에서 비교하는 데 가장 적합한 기능은? A Codespaces B Security Overview C Pages D Wiki
2. Code Security가 주로 다루는 위험은? A 코드 취약점 B 사용자 프로필 C Issue Label D Repository 이름
3. Prevention-first 접근의 핵심은? A 사고 후 보고만 B 위험 유입을 가능한 앞 단계에서 차단 C 모든 Merge 금지 D Alert 숨김
4. Security Campaign의 가장 적절한 용도는? A 특정 위험 집합의 목표형 Remediation B Branch 생성 C Release 작성 D 사용자 인증
5. Secret Protection과 Code Security의 차이를 가장 잘 설명한 것은? A 둘은 동일 B 코드 스타일 vs 문서 C 자격증명 노출 vs 코드 취약점 D Build vs Deploy
6. Alert Dismissal에 가장 필요한 것은? A 근거와 추적 가능성 B Star 수 C README 길이 D Fork 수
7. Secure SDLC의 역할 분담으로 적절한 것은? A 관리자만 책임 B 개발·보안·관리 역할이 협업 C 개발자만 책임 D 외부 사용자만 책임
8. 자격증명 노출을 Commit/Push 단계에서 예방하는 기능은? A Dependency Review B Push Protection C SBOM D CodeQL
9. Validity Check가 도움을 주는 것은? A 자격증명의 현재 유효성 판단 B Branch 보호 C 라이선스 구매 D PR 제목 생성
10. 조직 고유 자격증명 형식을 탐지하려면? A Custom Pattern B SARIF C SAML D SBOM
11. Secret Alert 대응에서 가장 적절한 첫 판단은? A 노출 영향과 자격증명 상태 확인 B 즉시 모든 Alert 삭제 C Repository 삭제 D 로그 제거
12. Bypass 예외 운영에서 가장 적절한 원칙은? A 무제한 허용 B 제한된 권한·근거·감사 C 누구나 사용 D 기록 금지
13. 실제 운영 Secret을 학습 샘플로 쓰는 판단은? A 권장 B Public Repo에서만 권장 C 부적절 D 만료 전이면 권장
14. 여러 저장소에 Secret Protection을 일관되게 적용하려면? A Organization/Enterprise 수준 정책 B 개인 로컬 설정만 C README만 D Issue Template
15. Dependency Graph의 주된 역할은? A 의존성 관계 파악 B Secret 저장 C 사용자 인증 D 코드 리팩터링
16. Pull Request에서 새 의존성 위험을 검토하는 기능은? A Dependency Review B Push Protection C Security Campaign D SAML
17. 알려진 취약 의존성 경고에 가장 직접적인 기능은? A Dependabot Alerts B Code Owners C Projects D Discussions
18. SBOM의 핵심 목적은? A 소프트웨어 구성요소 명세 B Commit 삭제 C 사용자 초대 D Branch 생성
19. Transitive Dependency는? A 직접 선언한 의존성만 B 다른 의존성을 통해 간접 포함 C Public Repository D Secret 유형
20. 취약 의존성 Alert 처리의 완료에 가까운 상태는? A Alert 닫기만 B 실제 수정 후 테스트·검증 C Issue 생성만 D 담당자 지정만
21. 자동 의존성 업데이트를 바로 Merge하지 않는 이유는? A 호환성·테스트 검증 필요 B GitHub가 금지 C SBOM 삭제 D Secret 생성
22. Supply Chain Security의 핵심 질문은? A 어떤 구성요소에 의존하고 어떤 위험이 있는가 B 누가 Star를 눌렀는가 C README는 몇 줄인가 D Wiki는 몇 개인가
23. CodeQL은 무엇에 가장 가깝나? A 코드 분석 엔진 B 비밀번호 관리자 C 프로젝트 보드 D 패키지 저장소
24. 빠른 CodeQL 도입에 적합한 방식은? A Advanced Setup B Default Setup C 분석 중단 D 수동 리뷰만
25. 세밀한 분석 Workflow 제어가 필요할 때 적합한 방식은? A Default Setup B Security Overview C Advanced Setup D Secret Protection
26. SARIF는? A 정적 분석 결과 교환 형식 B Secret 유형 C 인증 프로토콜 D 의존성 관리자
27. PR 기반 Code Security의 장점은? A Merge 전에 변경 코드 문제를 발견 B 모든 문제 100% 보장 C Secret 교체 D 사용자 인증
28. False Positive 가능성이 있는 Alert에 적절한 대응은? A 근거를 검토하고 기록 B 무조건 삭제 C 분석 중단 D Repository 삭제
29. Security Operations의 목표로 가장 적절한 것은? A 위험을 우선순위화하고 실제 감소 B Alert 숫자 숨김 C 모든 개발 금지 D 로그 제거
30. Alert Prioritization에서 Severity 외에 볼 것은? A 영향 범위·실제 노출 B Star 수 C Repository 색상 D README 글꼴
31. Security Campaign의 완료 증거는? A 이름 생성 B 대상 위험이 수정되고 검증됨 C Issue만 생성 D Alert 숨김
32. 반복되는 동일 유형 문제를 줄이는 방법은? A 예방 통제와 원인 개선 B 매번 Dismiss C 로그 제거 D Repository 이동
33. MTTR은 Security Operations에서 무엇을 보조하는가? A Remediation 속도 측정 B Branch 개수 C 사용자 수 D Commit 크기
34. Dismissal과 Remediation의 차이는? A 위험 수용/오탐 처리 vs 실제 수정 B 동일 C Branch vs Tag D Issue vs PR
35. 조직 보안 정책의 기본 원칙은? A 최소 권한과 일관된 Scope B 모든 사용자 관리자 C 감사 제거 D 예외 무제한
36. Default Configuration의 이점은? A 여러 저장소에 표준 보안 설정 확장 B 모든 Alert 삭제 C Branch 생성 D 사용자 인증
37. 보안 관련 Bypass 권한은 어떻게 운영하는 것이 적절한가? A 영구·전사 기본 B 제한된 대상·기간·근거 C 누구나 허용 D 기록하지 않음
38. 관리 API/Automation에 필요한 통제는? A 최소 권한·변경 추적·검증 B 공용 관리자 토큰 C 감사 비활성화 D 무기한 자격증명
39. 정책 적용 후 가장 중요한 후속 작업은? A 실제 적용 상태와 예외 검증 B 문서만 저장 C UI 닫기 D 모든 경고 제거
40. GH-500 준비에서 가장 적절한 방법은? A 기능 이름만 암기 B 실제 유출문제 수집 C 공식 범위+실습+문제+오답 검증 D 운영 보안 통제 약화
