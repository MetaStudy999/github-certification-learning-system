# GH-100 Mock Exam 02 — Questions

> 제한시간 권장: 60분 / 40문항

1. EMU 환경에서 사용자의 GitHub Identity를 주로 통제하는 주체는?  
A. 개인 사용자  B. Enterprise/IdP  C. Repository Maintainer  D. Public community

2. SAML 인증은 성공하지만 사용자가 Team에 자동 포함되지 않는다. 가장 관련 깊은 기능은?  
A. Team Sync  B. Pages  C. Sponsors  D. Cache

3. SCIM Provisioning을 사용하는 주된 운영 이점은?  
A. 계정 Lifecycle 자동화  B. Workflow 가속  C. Markdown 변환  D. Artifact 압축

4. 직접 Repository 권한과 Team 권한이 동시에 있을 때 관리자가 확인해야 할 것은?  
A. Effective Permission  B. README  C. Star  D. Branch color

5. Privileged Role 검토 주기의 목적은?  
A. 불필요한 고권한 제거  B. 모든 사용자 Owner 승격  C. SSO 제거  D. Billing 중단

6. Enterprise-level Policy를 조직별로 완화하려 한다. 먼저 해야 할 일은?  
A. 상위 정책이 하위 완화를 허용하는지 확인  B. 무조건 변경  C. Audit 삭제  D. Repo Public 전환

7. GHEC를 선택하는 주요 운영상 장점 중 하나는?  
A. 인프라 운영 부담 감소  B. 고객이 모든 서버 패치  C. Offline only  D. Local only

8. GHES 선택 시 추가로 필요한 운영 항목은?  
A. Backup/Upgrade/Capacity  B. Sponsors  C. Profile README  D. Discussions only

9. Enterprise 배포 전 Pilot의 주요 목적은?  
A. 제한된 Scope에서 정책·통합 검증  B. 보안 해제  C. 비용 숨김  D. 감사 중단

10. Support Ticket에서 민감정보를 보호하려면?  
A. Secret/Token 원문 제거  B. Password 첨부  C. SSH Key 첨부  D. PAT 공개

11. Ruleset의 장점으로 가장 적절한 것은?  
A. 여러 Repo/Branch에 정책을 중앙 적용 가능  B. Commit 삭제  C. License 제거  D. Star 관리

12. 보안 예외정책에서 가장 위험한 형태는?  
A. 만료 없는 영구 예외  B. 승인·기간·Audit 포함  C. Scope 제한  D. 정기 재검토

13. GitHub App이 자동화에 선호될 수 있는 이유는?  
A. 설치 Scope·세밀한 Permission  B. Owner 권한 무제한  C. Password 공유  D. Audit 불가

14. OAuth App과 GitHub App을 선택할 때 가장 먼저 봐야 할 것은?  
A. 통합의 Identity/Permission 요구사항  B. Avatar  C. Star  D. Issue 색상

15. PAT Governance에 포함할 항목은?  
A. Scope·Expiration·Approval·Rotation  B. README 길이  C. Fork 수  D. Wiki

16. Secret Scanning의 역할은?  
A. Repository 내 Secret 노출 탐지  B. PR 승인  C. Project View  D. License 발급

17. Code Scanning Alert를 조직적으로 관리할 때 필요한 것은?  
A. Ownership·Severity·Remediation Workflow  B. Alert 삭제만  C. 모든 Rule 비활성화  D. Admin 공유

18. Dependency Update 자동화와 가장 관련 깊은 기능은?  
A. Dependabot  B. Discussions  C. Codespaces  D. Pages

19. 보안 Feature 활성화 시 비용 영향을 함께 봐야 하는 이유는?  
A. Scope 확대가 License/Usage에 영향을 줄 수 있음  B. Git이 느려짐  C. README 증가  D. Issue 감소

20. Security Policy Rollout의 올바른 방식은?  
A. Pilot→Validate→Expand  B. 즉시 전체 적용만  C. Audit 제거  D. Owner 전원 확대

21. Enterprise Actions에서 허용 Action 정책을 관리하는 목적은?  
A. 신뢰 가능한 자동화만 허용  B. README 단축  C. Fork 제거  D. Star 증가

22. Reusable Workflow를 중앙 관리하는 장점은?  
A. 표준화와 유지보수성  B. Secret 공개  C. 권한 자동 최대화  D. Audit 제거

23. Self-hosted Runner를 Public Repo에서 무분별하게 사용하면 위험한 이유는?  
A. 신뢰되지 않은 코드가 내부 Runner에서 실행될 수 있음  B. README가 길어짐  C. Star가 줄어듦  D. Wiki가 느려짐

24. Runner Group 설계 시 핵심 질문은?  
A. 어떤 Org/Repo가 어떤 Runner를 사용할 수 있는가  B. Repo Topic  C. PR 제목  D. Avatar

25. OIDC를 사용할 수 있는 배포에서 장기 Secret보다 장점은?  
A. 단기 자격증명과 중앙 Trust 정책  B. Secret 영구 저장  C. Audit 제거  D. Runner 불필요

26. Third-party Vault를 도입할 때 필요한 통제는?  
A. 접근 정책·감사·회전  B. 모든 사용자 Read  C. Secret 로그 출력  D. Owner 공유

27. Workflow가 필요 이상으로 쓰기 권한을 가진다. 가장 적절한 개선은?  
A. `permissions` 최소화  B. Admin Token 사용  C. Check 삭제  D. Public 전환

28. Actions 비용이 높지만 실행 성공률도 낮다. 우선순위가 높은 개선은?  
A. 실패 원인과 불필요 재실행 제거  B. Runner 무조건 확대  C. Audit 삭제  D. 모든 Cache 삭제

29. Self-hosted Runner Capacity 부족의 신호는?  
A. Queue 증가와 대기시간 증가  B. Star 증가  C. README 증가  D. Issue Label 변화

30. Actions 정책 변경의 검증 Evidence는?  
A. 변경 전후 Workflow Run과 Audit 기록  B. Secret 원문  C. Password  D. SSH Private Key

31. Audit Log 조사에서 Actor가 의미하는 것은?  
A. 행동을 수행한 주체  B. Repository 설명  C. Runner OS  D. Billing Plan

32. 사용량 최적화에서 Baseline이 필요한 이유는?  
A. 변화와 이상치를 비교하기 위해  B. README 생성  C. Issue 삭제  D. Branch Rename

33. License가 많이 남는데 비용이 높다. FIRST로 할 일은?  
A. License와 Metered Product 비용을 분리 분석  B. 모든 Repo 삭제  C. SSO 제거  D. Audit 중지

34. API 자동화가 Rate Limit에 자주 걸린다. 개선으로 가장 적절한 것은?  
A. 호출 최적화·Caching·Backoff 검토  B. Token 권한 확대  C. Owner 추가  D. Audit 삭제

35. 월간 운영 Review에서 Trend를 보는 이유는?  
A. 단일 시점보다 변화 방향을 파악  B. Password 수집  C. Repo Public 전환  D. Secret 공유

36. Incident 후 Root Cause 문서가 필요한 이유는?  
A. 재발 방지와 운영 표준 개선  B. Star 증가  C. Fork 감소  D. Wiki 삭제

37. 사용자 Offboarding 시 자동화 Bot이 해당 사용자 Token을 사용하고 있었다. 가장 적절한 개선은?  
A. 사람 계정과 자동화 Identity 분리  B. Token 공유 확대  C. Owner 권한 부여  D. Audit 제거

38. Enterprise Architecture 문서의 가장 중요한 특성은?  
A. Scope·책임·Trust Boundary 명확화  B. 디자인 장식  C. Emoji 수  D. Commit 색상

39. 가장 좋은 관리자 변경 방식은?  
A. Requirement→Risk→Approval→Pilot→Verify  B. 바로 Production 변경  C. Audit 제거  D. 비공식 구두 변경

40. EXAM-READY 판단에서 가장 적절한 기준은?  
A. QBank/Mock/오답 Gate와 실습 수행 능력  B. 읽기만 완료  C. Admin 권한 보유  D. Repo Star 수

---
답안을 확정한 후 [`answers.md`](./answers.md)를 확인하세요.
