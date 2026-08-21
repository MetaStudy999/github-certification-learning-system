# GH-500 Mock Exam 02 — Questions

> 자체 제작 40문항. Scenario 중심입니다.

1. 회사가 여러 Repository의 보안 위험을 중앙에서 비교하려 한다. A Dependency Graph B Security Overview C Codespaces D Wiki
2. 개발자가 잘못 포함한 자격증명이 원격 저장소에 들어가기 전에 막고 싶다. A Push Protection B SBOM C CodeQL D Dependabot
3. 보안팀이 특정 유형의 취약점 80건을 30일 내 줄이려 한다. A Security Campaign B Release C Project Board만 D Fork
4. 조직 고유 형식의 민감정보를 탐지해야 한다. A SARIF B Custom Pattern C SBOM D SAML
5. 발견된 자격증명이 실제로 유효한지 판단을 돕는 기능은? A Validity Check B Dependency Review C CodeQL D Audit Log
6. Secret 관련 예외 권한을 설계할 때 가장 적절한 것은? A 전 직원 영구 허용 B 제한된 사용자·범위·기한 C 기록 금지 D 모든 경고 비활성화
7. 이미 노출된 자격증명 사고에서 가장 중요한 조합은? A Alert 닫기만 B 영향 파악·무효화/교체·검증 C Repository 이름 변경 D Branch 삭제
8. Secret Protection을 대규모로 도입할 때 우선할 것은? A 범위·정책·예외·교육 설계 B 즉시 모든 개발 중단 C 로그 삭제 D 모든 저장소 Public 전환
9. 새 라이브러리가 포함된 PR의 공급망 위험을 검토하려 한다. A Dependency Review B Push Protection C Security Campaign D CodeQL
10. 기존 Repository의 알려진 취약 의존성을 식별하는 데 직접적인 것은? A Dependabot Alerts B Content Exclusion C Copilot Chat D Pages
11. 의존성 관계의 기반 정보를 제공하는 것은? A SBOM만 B Dependency Graph C SARIF D SAML
12. 표준화된 소프트웨어 구성요소 목록으로 외부 시스템과 정보를 교환하려 한다. A SBOM B Secret Alert C Branch Protection D Code Owners
13. 간접 의존성 위험의 출처를 파악하려 할 때 가장 먼저 볼 개념은? A Transitive dependency chain B Star history C Wiki history D Label
14. 자동 의존성 업데이트 PR에 대한 적절한 태도는? A 항상 자동 Merge B 테스트와 호환성 검증 후 처리 C 모두 닫기 D 모두 무시
15. PR에서 취약 의존성이 새로 추가되는 것을 조기에 확인하는 전략은? A Dependency Review를 검토 흐름에 포함 B Release 후 확인 C SBOM 삭제 D Repository 이동
16. 공급망 보안의 핵심 목표는? A 구성요소·출처·위험·변화를 파악 B 사용자 프로필 관리 C Issue 정렬 D Wiki 편집
17. 빠르게 CodeQL을 켜고 표준 구성을 사용하려 한다. A Advanced Setup B Default Setup C Secret Protection D Security Campaign
18. 빌드 과정과 분석 조건을 세밀하게 관리해야 한다. A Default Setup B Advanced Setup C Dependabot D Push Protection
19. 외부 정적 분석 결과를 표준 형식으로 가져오려 한다. A SARIF B SBOM C SCIM D OIDC
20. CodeQL Alert가 많다. 가장 적절한 대응은? A 모두 Dismiss B 영향·신뢰도·노출 기준으로 우선순위화 C 분석 중단 D Repository 삭제
21. PR 기반 코드 분석의 가장 큰 장점은? A 변경 사항 Merge 전 조기 발견 B 모든 취약점 100% 제거 C Secret 교체 D 비용 제거
22. False Positive로 의심되는 Alert는? A 기술적 근거 검토 후 상태 처리 B 즉시 삭제 C 분석 비활성화 D 기록 금지
23. 정적 분석이 충분하지 않은 이유는? A 분석 한계가 있어 다른 보안 통제와 검증이 필요 B GitHub가 코드를 못 읽음 C 의존성을 자동 삭제 D Secret만 처리
24. Code Security 결과를 운영과 연결하는 올바른 흐름은? A Detect → Prioritize → Remediate → Verify B Ignore → Delete C Clone → Fork D Star → Watch
25. 다수 Repository의 위험을 위험도별로 분류해 조치하려 한다. A Security Overview + prioritization B README C Pages D Discussions
26. Security Campaign 대상 선정 시 중요한 것은? A 위험 유형·영향·범위 B Repository 이름 길이 C Star 수만 D Commit 이모지
27. Campaign 성공의 증거는? A Campaign 생성 B 대상 위험의 실제 감소와 검증 C Issue 수 증가 D Alert 숨김
28. 같은 종류의 취약점이 반복된다. 다음 단계는? A 원인 분석과 예방 통제 개선 B 매번 Dismiss C 로그 삭제 D 분석 중단
29. 보안 Alert를 Dismiss할 수 있는 역할을 제한하는 이유는? A 위험 수용 결정의 책임성과 감사 확보 B 개발 속도 저하 C UI 단순화 D Star 관리
30. Security Operations에서 MTTR을 보는 이유는? A Remediation 속도 추적 B 사용자 수 측정 C Branch 수 측정 D Repository 크기 측정
31. Organization 수준 정책의 장점은? A 여러 Repository에 일관성 제공 B 모든 예외 자동 승인 C 감사 제거 D README 통일만
32. 보안 역할을 설계할 때 기본 원칙은? A 최소 권한 B 최대 권한 C 공용 관리자 D 익명 변경
33. Default Configuration이 유용한 이유는? A 대규모 표준 설정 Rollout B Secret 값 저장 C Branch 삭제 D Issue 생성
34. 정책 예외가 필요한 경우 적절한 것은? A 사유·기한·승인·감사 기록 B 무기한 허용 C 누구나 사용 D 기록 삭제
35. 관리 자동화에 필요한 것은? A 최소 권한·검증·변경 추적 B 관리자 권한 고정 C 로그 제거 D 무제한 자격증명
36. 정책 Rollout 후 해야 할 것은? A 실제 적용 여부와 예외 상태 검증 B 기능 설명서만 저장 C UI 종료 D Alert 일괄 닫기
37. Public Repository와 Enterprise 환경 비교에서 중요한 것은? A 기능 가용성과 운영 책임 차이 B README 차이만 C Git 명령 차이 D Markdown 차이
38. Secure SDLC에서 Prevention과 Detection의 관계는? A 서로 보완 B 둘 중 하나만 필요 C 완전히 동일 D 관련 없음
39. GH-500에서 기능 정의보다 중요한 능력은? A 상황에 맞는 기능 선택과 대응 판단 B 아이콘 암기 C 메뉴 색상 암기 D 시험문제 유출 수집
40. 시험 직전 가장 적절한 Gate는? A 최신 Study Guide + QBank + Mock + 오답 재검증 B 문서 제목만 읽기 C 실습 생략 D 실제 운영 설정 약화
