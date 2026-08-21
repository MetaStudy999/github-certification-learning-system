#!/usr/bin/env python3
"""Normalize GCLS Markdown labels to Korean (English, ABBR) notation.

The normalizer is intentionally documentation-focused. It translates Markdown
headings and common documentation labels, while leaving commands, source code,
paths, URLs, YAML/JSON keys, and code blocks untouched unless a line is an
explicit GCLS course-structure label.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADING_MAP = {
    "Quick Start": "빠른 시작 (Quick Start, QS)",
    "Certification Roadmap": "자격증 로드맵 (Certification Roadmap, CR)",
    "System Control Tower": "시스템 통합 관제 (System Control Tower, SCT)",
    "Control Tower": "통합 관제 (Control Tower, CT)",
    "Current Learning Content Scale": "현재 학습 콘텐츠 규모 (Current Learning Content Scale, CLCS)",
    "Current System Status": "현재 시스템 상태 (Current System Status, CSS)",
    "Status Model": "상태 모델 (Status Model, SM)",
    "Content Status": "콘텐츠 상태 (Content Status, CS)",
    "Learning Status": "학습 상태 (Learning Status, LS)",
    "Learning Architecture": "학습 아키텍처 (Learning Architecture, LA)",
    "Standard Internal Course Structure": "표준 과정 내부 구조 (Standard Internal Course Structure, SICS)",
    "Standard Structure Verification": "표준 구조 검증 (Standard Structure Verification, SSV)",
    "Exam Readiness Gate": "시험 준비도 통과 기준 (Exam Readiness Gate, ERG)",
    "Exam Readiness Policy": "시험 준비도 정책 (Exam Readiness Policy, ERP)",
    "Readiness Gate": "준비도 통과 기준 (Readiness Gate, RG)",
    "Repository Map": "저장소 맵 (Repository Map, RM)",
    "Portfolio Growth Path": "포트폴리오 성장 경로 (Portfolio Growth Path, PGP)",
    "Growth Summary": "성장 요약 (Growth Summary, GS)",
    "Verification": "검증 (Verification, VER)",
    "Current Phase": "현재 단계 (Current Phase, CP)",
    "Next Phase": "다음 단계 (Next Phase, NP)",
    "Next Operational Phase": "다음 운영 단계 (Next Operational Phase, NOP)",
    "Course Status": "과정 상태 (Course Status, CRS)",
    "Status Semantics": "상태 의미 (Status Semantics, SS)",
    "Maintenance Rule": "유지관리 규칙 (Maintenance Rule, MR)",
    "Shared Systems": "공통 시스템 (Shared Systems, SHS)",
    "Integrated Content Scale": "통합 콘텐츠 규모 (Integrated Content Scale, ICS)",
    "Control Flow Verification": "제어 흐름 검증 (Control Flow Verification, CFV)",
    "PASS Criteria": "통과 기준 (PASS Criteria, PC)",
    "System-Level PASS Criteria": "시스템 수준 통과 기준 (System-Level PASS Criteria, SLPC)",
    "Overview": "개요 (Overview, OVW)",
    "Terms": "용어 (Terms, TRM)",
    "Concepts": "개념 (Concepts, CPT)",
    "Concept": "개념 (Concept, CPT)",
    "Concept Map": "개념 맵 (Concept Map, CM)",
    "Official Docs": "공식 문서 (Official Docs, ODC)",
    "Official Documentation": "공식 문서 (Official Documentation, ODC)",
    "Official Sources": "공식 출처 (Official Sources, OS)",
    "Primary Sources": "주요 출처 (Primary Sources, PS)",
    "Source Priority": "출처 우선순위 (Source Priority, SP)",
    "Official Links": "공식 링크 (Official Links, OL)",
    "Guides": "가이드 (Guides, GDE)",
    "Labs": "실습 (Labs, LAB)",
    "Lab Roadmap": "실습 로드맵 (Lab Roadmap, LR)",
    "10-Lab Learning Path": "10개 실습 학습 경로 (10-Lab Learning Path, 10LP)",
    "Exercises": "연습문제 (Exercises, EXR)",
    "Exercise Roadmap": "연습문제 로드맵 (Exercise Roadmap, ER)",
    "Exercise Areas": "연습문제 영역 (Exercise Areas, EA)",
    "Planned Areas": "계획 영역 (Planned Areas, PA)",
    "Question Bank": "문제은행 (Question Bank, QB)",
    "Answers": "정답 (Answers, ANS)",
    "Answer Pattern": "정답 패턴 (Answer Pattern, AP)",
    "Self Check": "자가 점검 (Self Check, SC)",
    "Final Review": "최종 복습 (Final Review, FR)",
    "Projects": "프로젝트 (Projects, PRJ)",
    "Mock Exams": "모의고사 (Mock Exams, ME)",
    "Wrong Answers": "오답 관리 (Wrong Answers, WA)",
    "Progress": "진행 현황 (Progress, PRG)",
    "Resources": "자료 (Resources, RES)",
    "Evidence": "증빙 (Evidence, EVD)",
    "Required Evidence": "필수 증빙 (Required Evidence, RE)",
    "Exam Snapshot": "시험 개요 (Exam Snapshot, ES)",
    "Content Inventory": "콘텐츠 구성 (Content Inventory, CI)",
    "Core Areas": "핵심 영역 (Core Areas, CA)",
    "Learning Flow": "학습 흐름 (Learning Flow, LF)",
    "Flow": "흐름 (Flow, FL)",
    "Study Plan": "학습 계획 (Study Plan, SP)",
    "Fast Track": "단기 집중 과정 (Fast Track, FT)",
    "7-Day Fast Track": "7일 단기 집중 과정 (7-Day Fast Track, 7DFT)",
    "Final Checklist": "최종 점검표 (Final Checklist, FC)",
    "Confusion Matrix": "혼동 개념 비교표 (Confusion Matrix, CM)",
    "Exam Day Strategy": "시험 당일 전략 (Exam Day Strategy, EDS)",
    "Exam-Day Rule": "시험 당일 규칙 (Exam-Day Rule, EDR)",
    "Project Rubric": "프로젝트 평가 기준 (Project Rubric, PR)",
    "Evidence Checklist": "증빙 점검표 (Evidence Checklist, EC)",
    "Error Log": "오류 기록 (Error Log, EL)",
    "Retry Queue": "재도전 대기열 (Retry Queue, RQ)",
    "Daily Tracker": "일일 추적 (Daily Tracker, DT)",
    "Score Log": "점수 기록 (Score Log, SL)",
    "Study Session": "학습 세션 (Study Session, SS)",
    "Final Capstone": "최종 종합 프로젝트 (Final Capstone, FCAP)",
    "Portfolio Map": "포트폴리오 맵 (Portfolio Map, PM)",
    "Evidence Matrix": "증빙 매트릭스 (Evidence Matrix, EM)",
    "Environment": "환경 (Environment, ENV)",
    "Objective": "목표 (Objective, OBJ)",
    "Practice": "실습 (Practice, PRAC)",
    "Practice Topics": "실습 주제 (Practice Topics, PT)",
    "Learn": "학습 포인트 (Learn, LRN)",
    "Challenge": "도전 과제 (Challenge, CHL)",
    "Verify": "검증 (Verify, VER)",
    "Review": "검토 (Review, REV)",
    "Merge": "병합 (Merge, MRG)",
    "Next Step": "다음 단계 (Next Step, NS)",
    "Exam Link": "시험 연계 (Exam Link, EL)",
    "Scenario": "시나리오 (Scenario, SCN)",
    "Scenario A": "시나리오 A (Scenario A, SCN-A)",
    "Scenario B": "시나리오 B (Scenario B, SCN-B)",
    "Compare": "비교 (Compare, CMP)",
    "Types": "유형 (Types, TYP)",
    "Topics": "주제 (Topics, TOP)",
    "Core Files": "핵심 파일 (Core Files, CF)",
    "Core Difference": "핵심 차이 (Core Difference, CD)",
    "Core Security Rules": "핵심 보안 규칙 (Core Security Rules, CSR)",
    "Safe Example": "안전한 예제 (Safe Example, SE)",
    "Safe Practice": "안전한 실습 (Safe Practice, SP)",
    "Troubleshooting": "문제 해결 (Troubleshooting, TS)",
    "Troubleshooting Order": "문제 해결 순서 (Troubleshooting Order, TSO)",
    "Troubleshooting Flow": "문제 해결 흐름 (Troubleshooting Flow, TSF)",
    "Optimization Topics": "최적화 주제 (Optimization Topics, OT)",
    "Matrix Example": "매트릭스 예제 (Matrix Example, MXE)",
    "Decision Table": "의사결정 표 (Decision Table, DT)",
    "Decision Matrix": "의사결정 매트릭스 (Decision Matrix, DM)",
    "Feature Map": "기능 맵 (Feature Map, FM)",
    "Deployment Models": "배포 모델 (Deployment Models, DM)",
    "Deliverables": "산출물 (Deliverables, DEL)",
    "Required Design": "필수 설계 (Required Design, RD)",
    "Failure Taxonomy": "실패 분류체계 (Failure Taxonomy, FT)",
    "Guardrail Layers": "가드레일 계층 (Guardrail Layers, GL)",
    "Accountability Checklist": "책임성 점검표 (Accountability Checklist, AC)",
    "Change Watch": "변경 감시 (Change Watch, CW)",
    "Current Naming Note": "현재 명칭 참고 (Current Naming Note, CNN)",
    "Agent Design Card": "에이전트 설계 카드 (Agent Design Card, ADC)",
    "Contributing": "기여 방법 (Contributing, CON)",
    "Workflow": "워크플로 (Workflow, WF)",
    "Commit Convention": "커밋 규칙 (Commit Convention, CC)",
    "Security Policy": "보안 정책 (Security Policy, SP)",
    "Supported Versions": "지원 버전 (Supported Versions, SV)",
    "Reporting a Vulnerability": "취약점 보고 (Reporting a Vulnerability, RV)",
    "Primary Source": "주요 출처 (Primary Source, PS)",
}

AREA_LINES = {
    "010 Overview": "010 개요 (Overview, OVW)",
    "020 Terms": "020 용어 (Terms, TRM)",
    "030 Concepts": "030 개념 (Concepts, CPT)",
    "040 Official Docs": "040 공식 문서 (Official Docs, ODC)",
    "050 Guides": "050 가이드 (Guides, GDE)",
    "060 Labs": "060 실습 (Labs, LAB)",
    "070 Exercises": "070 연습문제 (Exercises, EXR)",
    "080 Question Bank": "080 문제은행 (Question Bank, QB)",
    "090 Final Review": "090 최종 복습 (Final Review, FR)",
    "100 Projects": "100 프로젝트 (Projects, PRJ)",
    "110 Mock Exams": "110 모의고사 (Mock Exams, ME)",
    "120 Wrong Answers": "120 오답 관리 (Wrong Answers, WA)",
    "130 Progress": "130 진행 현황 (Progress, PRG)",
    "140 Resources": "140 자료 (Resources, RES)",
    "150 Evidence": "150 증빙 (Evidence, EVD)",
}

TABLE_CELL_MAP = {
    "Content Status": "콘텐츠 상태 (Content Status, CS)",
    "Learning Status": "학습 상태 (Learning Status, LS)",
    "Question Bank": "문제은행 (Question Bank, QB)",
    "Mock Exams": "모의고사 (Mock Exams, ME)",
    "Mock Exam": "모의고사 (Mock Exam, ME)",
    "Final Mock": "최종 모의고사 (Final Mock, FM)",
    "Evidence": "증빙 (Evidence, EVD)",
    "Progress": "진행 현황 (Progress, PRG)",
    "Resources": "자료 (Resources, RES)",
    "Labs": "실습 (Labs, LAB)",
    "Exercises": "연습문제 (Exercises, EXR)",
    "Projects": "프로젝트 (Projects, PRJ)",
    "Final Capstone": "최종 종합 프로젝트 (Final Capstone, FCAP)",
    "Overview": "개요 (Overview, OVW)",
    "Terms": "용어 (Terms, TRM)",
    "Concepts": "개념 (Concepts, CPT)",
    "Official Docs": "공식 문서 (Official Docs, ODC)",
    "Guides": "가이드 (Guides, GDE)",
    "Wrong Answers": "오답 관리 (Wrong Answers, WA)",
}

COURSES = {
    "GitHub Foundations": ("GitHub 기초", "GHF", "GH-900"),
    "GitHub Actions": ("GitHub 액션", "GHACT", "GH-200"),
    "GitHub Copilot": ("GitHub 코파일럿", "GHCOP", "GH-300"),
    "GitHub Administration": ("GitHub 관리", "GHADM", "GH-100"),
    "GitHub Advanced Security": ("GitHub 고급 보안", "GHAS", "GH-500"),
    "GitHub Agentic AI Developer": ("GitHub 에이전틱 AI 개발자", "GHAI", "GH-600"),
}

SUFFIX_MAP = {
    "Overview": "개요 (Overview, OVW)",
    "Terms": "용어 (Terms, TRM)",
    "Concepts": "개념 (Concepts, CPT)",
    "Official Docs": "공식 문서 (Official Docs, ODC)",
    "Guides": "가이드 (Guides, GDE)",
    "Labs": "실습 (Labs, LAB)",
    "Exercises": "연습문제 (Exercises, EXR)",
    "Question Bank": "문제은행 (Question Bank, QB)",
    "Final Review": "최종 복습 (Final Review, FR)",
    "Projects": "프로젝트 (Projects, PRJ)",
    "Mock Exams": "모의고사 (Mock Exams, ME)",
    "Wrong Answers": "오답 관리 (Wrong Answers, WA)",
    "Progress": "진행 현황 (Progress, PRG)",
    "Resources": "자료 (Resources, RES)",
    "Evidence": "증빙 (Evidence, EVD)",
}

PHRASE_MAP = {
    "Git Basics": "Git 기초",
    "Remote Repository": "원격 저장소",
    "Branch Workflow": "브랜치 워크플로",
    "GitHub Flow": "GitHub 플로",
    "Repository Documentation": "저장소 문서화",
    "Collaboration": "협업",
    "GitHub Projects": "GitHub 프로젝트",
    "Modern Development on GitHub": "GitHub 현대적 개발",
    "Modern Development": "현대적 개발",
    "Security Basics": "보안 기초",
    "Community Contribution": "커뮤니티 기여",
    "First Workflow": "첫 워크플로",
    "Events & Inputs": "이벤트와 입력값",
    "Contexts & Expressions": "컨텍스트와 표현식",
    "Matrix & Service Containers": "매트릭스와 서비스 컨테이너",
    "Cache & Artifacts": "캐시와 아티팩트",
    "Reusable Automation": "재사용 자동화",
    "Reusable Workflow": "재사용 워크플로",
    "Composite Action": "복합 액션",
    "Custom Actions": "사용자 정의 액션",
    "Runners & Enterprise": "러너와 엔터프라이즈",
    "Security & OIDC": "보안과 OIDC",
    "Troubleshooting & Optimization": "문제 해결과 최적화",
    "First Copilot Interaction": "첫 Copilot 상호작용",
    "Prompt Fundamentals": "프롬프트 기초",
    "Context Engineering": "컨텍스트 엔지니어링",
    "Code Generation": "코드 생성",
    "Explanation & Documentation": "설명과 문서화",
    "Testing with Copilot": "Copilot 활용 테스트",
    "Debugging with Copilot": "Copilot 활용 디버깅",
    "Refactoring with Copilot": "Copilot 활용 리팩터링",
    "Responsible AI & Privacy": "책임 있는 AI와 개인정보 보호",
    "End-to-End AI-Assisted Development": "엔드투엔드 AI 보조 개발",
    "Copilot CLI / Agent Mode / MCP": "Copilot CLI / 에이전트 모드 / MCP",
    "Copilot Code Review / Organization Policy": "Copilot 코드 리뷰 / 조직 정책",
    "Spaces / Spark / Instructions / Prompt Files": "Spaces / Spark / 지침 / 프롬프트 파일",
    "Identity Models": "식별 모델",
    "SAML SSO / SCIM / Team Synchronization": "SAML SSO / SCIM / 팀 동기화",
    "Roles / Teams / Permissions": "역할 / 팀 / 권한",
    "Deployment / Licensing": "배포 / 라이선싱",
    "Support / Standards / Diagnostics": "지원 / 표준 / 진단",
    "Security Policies / Rulesets": "보안 정책 / 규칙 집합",
    "Security Features / Response": "보안 기능 / 대응",
    "PAT / GitHub Apps / OAuth Apps / Integrations": "PAT / GitHub 앱 / OAuth 앱 / 통합",
    "Actions Governance": "Actions 거버넌스",
    "Runners / Networking / Vaults": "러너 / 네트워킹 / 볼트",
    "Audit / Usage / Cost Optimization": "감사 / 사용량 / 비용 최적화",
    "Enterprise Administration Blueprint": "엔터프라이즈 관리 청사진",
    "Security Suites Overview": "보안 제품군 개요",
    "Secret Protection Basics": "비밀 보호 기초",
    "Push Protection & Custom Patterns": "푸시 보호와 사용자 정의 패턴",
    "Dependency Graph & Dependabot Alerts": "의존성 그래프와 Dependabot 경고",
    "Dependency Review & SBOM": "의존성 검토와 SBOM",
    "CodeQL Default Setup": "CodeQL 기본 설정",
    "CodeQL Advanced Setup & SARIF": "CodeQL 고급 설정과 SARIF",
    "Alert Triage & Autofix": "경고 분류와 자동 수정",
    "Security Campaigns": "보안 캠페인",
    "Security Policies & Roles": "보안 정책과 역할",
    "Enterprise Rollout & Automation": "엔터프라이즈 도입과 자동화",
    "Secure SDLC Integration": "보안 SDLC 통합",
    "Agent Architecture & Success Criteria": "에이전트 아키텍처와 성공 기준",
    "Planning vs Execution": "계획과 실행 비교",
    "Tool Selection & Scope": "도구 선택과 범위",
    "MCP Concepts & Governance": "MCP 개념과 거버넌스",
    "Environment & Execution Context": "환경과 실행 컨텍스트",
    "Memory / State / Checkpoint": "메모리 / 상태 / 체크포인트",
    "Evaluation Design": "평가 설계",
    "Error Analysis & Tuning": "오류 분석과 조정",
    "Multi-Agent Coordination": "멀티에이전트 조정",
    "Failure & Conflict Handling": "실패와 충돌 처리",
    "Guardrails & Accountability": "가드레일과 책임성",
    "End-to-End Agentic SDLC Design": "엔드투엔드 에이전틱 SDLC 설계",
    "Version Control": "버전 관리",
    "GitHub Repository": "GitHub 저장소",
    "GitHub Products / Modern Development": "GitHub 제품 / 현대적 개발",
    "Account / Security / Administration": "계정 / 보안 / 관리",
    "Community / Open Source": "커뮤니티 / 오픈 소스",
    "Clone vs Fork": "Clone과 Fork 비교",
    "Issue vs Discussion vs Pull Request": "Issue / Discussion / Pull Request 비교",
    "Cache vs Artifact": "Cache와 Artifact 비교",
    "Reusable Workflow vs Composite Action": "재사용 워크플로와 복합 액션 비교",
    "Security Model": "보안 모델",
    "GitHub Codespaces": "GitHub 코드스페이스",
    "Secret Protection": "비밀 보호",
    "Supply Chain Security": "공급망 보안",
    "Code Security": "코드 보안",
    "Responsible AI Checklist": "책임 있는 AI 점검표",
    "Admin vs Support": "관리와 지원 비교",
    "Cost Optimization": "비용 최적화",
    "Fork vs Clone": "Fork와 Clone 비교",
    "Staging": "스테이징",
    "Commit": "커밋",
    "Push": "푸시",
    "Merge": "병합",
    "Hallucination": "환각",
    "Bias": "편향",
    "Secure Code": "보안 코드",
    "Privacy": "개인정보 보호",
    "Transparency": "투명성",
    "PAT": "개인용 액세스 토큰",
    "GitHub App": "GitHub 앱",
    "OAuth App": "OAuth 앱",
}

WORD_MAP = {
    "Basics": "기초", "Basic": "기초", "Advanced": "고급", "Modern": "현대적",
    "Git": "Git", "GitHub": "GitHub", "Repository": "저장소", "Repositories": "저장소",
    "Remote": "원격", "Branch": "브랜치", "Workflow": "워크플로", "Workflows": "워크플로",
    "Documentation": "문서화", "Collaboration": "협업", "Community": "커뮤니티",
    "Contribution": "기여", "Development": "개발", "Project": "프로젝트", "Projects": "프로젝트",
    "Security": "보안", "Privacy": "개인정보 보호", "Administration": "관리", "Admin": "관리",
    "Account": "계정", "Open": "오픈", "Source": "소스", "First": "첫", "Events": "이벤트",
    "Event": "이벤트", "Inputs": "입력값", "Input": "입력값", "Contexts": "컨텍스트",
    "Context": "컨텍스트", "Expressions": "표현식", "Expression": "표현식", "Matrix": "매트릭스",
    "Service": "서비스", "Containers": "컨테이너", "Container": "컨테이너", "Cache": "캐시",
    "Artifact": "아티팩트", "Artifacts": "아티팩트", "Reusable": "재사용", "Automation": "자동화",
    "Composite": "복합", "Action": "액션", "Actions": "액션", "Custom": "사용자 정의",
    "Runner": "러너", "Runners": "러너", "Enterprise": "엔터프라이즈", "Troubleshooting": "문제 해결",
    "Optimization": "최적화", "Prompt": "프롬프트", "Fundamentals": "기초", "Engineering": "엔지니어링",
    "Code": "코드", "Generation": "생성", "Explanation": "설명", "Testing": "테스트", "Debugging": "디버깅",
    "Refactoring": "리팩터링", "Responsible": "책임 있는", "AI": "AI", "End-to-End": "엔드투엔드",
    "Assisted": "보조", "Agent": "에이전트", "Mode": "모드", "Review": "리뷰", "Organization": "조직",
    "Policy": "정책", "Policies": "정책", "Instructions": "지침", "Instruction": "지침", "Files": "파일",
    "File": "파일", "Identity": "식별", "Models": "모델", "Model": "모델", "Team": "팀", "Teams": "팀",
    "Synchronization": "동기화", "Roles": "역할", "Role": "역할", "Permissions": "권한", "Permission": "권한",
    "Deployment": "배포", "Licensing": "라이선싱", "Support": "지원", "Standards": "표준", "Diagnostics": "진단",
    "Rulesets": "규칙 집합", "Features": "기능", "Feature": "기능", "Response": "대응", "Integrations": "통합",
    "Integration": "통합", "Governance": "거버넌스", "Networking": "네트워킹", "Vaults": "볼트", "Vault": "볼트",
    "Audit": "감사", "Usage": "사용량", "Cost": "비용", "Blueprint": "청사진", "Suites": "제품군",
    "Suite": "제품군", "Secret": "비밀", "Protection": "보호", "Push": "푸시", "Patterns": "패턴",
    "Pattern": "패턴", "Dependency": "의존성", "Graph": "그래프", "Alerts": "경고", "Alert": "경고",
    "Default": "기본", "Setup": "설정", "Triage": "분류", "Autofix": "자동 수정", "Campaigns": "캠페인",
    "Campaign": "캠페인", "Rollout": "도입", "Secure": "보안", "Architecture": "아키텍처", "Success": "성공",
    "Criteria": "기준", "Planning": "계획", "Execution": "실행", "Tool": "도구", "Tools": "도구",
    "Selection": "선택", "Scope": "범위", "Concepts": "개념", "Concept": "개념", "Environment": "환경",
    "Memory": "메모리", "State": "상태", "Checkpoint": "체크포인트", "Evaluation": "평가", "Design": "설계",
    "Error": "오류", "Analysis": "분석", "Tuning": "조정", "Multi-Agent": "멀티에이전트",
    "Coordination": "조정", "Failure": "실패", "Conflict": "충돌", "Handling": "처리", "Guardrails": "가드레일",
    "Accountability": "책임성", "Required": "필수", "Decision": "의사결정", "Table": "표", "Map": "맵",
    "Comparison": "비교", "Compare": "비교", "Difference": "차이", "Order": "순서", "Topics": "주제",
    "Topic": "주제", "Safe": "안전한", "Example": "예제", "Practice": "실습", "Learn": "학습",
    "Objective": "목표", "Challenge": "도전 과제", "Verify": "검증", "Next": "다음", "Step": "단계",
    "Scenario": "시나리오", "Phase": "단계", "Data": "데이터", "Location": "위치", "Server": "서버",
    "Control": "제어", "Billing": "청구", "Triage": "분류", "Developer": "개발자", "Process": "프로세스",
    "Protection": "보호", "Questions": "질문", "Question": "질문", "Routing": "라우팅", "Exposure": "노출",
    "Plan": "계획", "Approval": "승인", "Rate": "속도", "Limits": "제한", "Reuse": "재사용",
    "Strategy": "전략", "Least": "최소", "Privilege": "권한", "Runner": "러너", "Group": "그룹",
    "Selection": "선택", "API": "API", "Adoption": "도입", "Operations": "운영", "Deliverables": "산출물",
    "Primary": "주요", "Sources": "출처", "Current": "현재", "Naming": "명칭", "Note": "참고",
    "Change": "변경", "Watch": "감시", "Checklist": "점검표", "Answer": "정답", "Answers": "정답",
    "Area": "영역", "Areas": "영역", "Planned": "계획", "Flow": "흐름", "Rule": "규칙", "Rules": "규칙",
    "System": "시스템", "Status": "상태", "Course": "과정", "Shared": "공통", "Integrated": "통합",
    "Content": "콘텐츠", "Scale": "규모", "Verification": "검증", "Maintenance": "유지관리",
    "Operational": "운영", "Semantics": "의미", "Roadmap": "로드맵", "Learning": "학습", "Path": "경로",
    "Exam": "시험", "Link": "연계", "Domain": "영역", "Products": "제품", "Version": "버전",
    "Control": "제어", "Pull": "풀", "Request": "리퀘스트", "Discussion": "토론", "Issue": "이슈",
    "Clone": "Clone", "Fork": "Fork", "Codespaces": "코드스페이스", "Staging": "스테이징",
    "Commit": "커밋", "Hallucination": "환각", "Bias": "편향", "Transparency": "투명성",
}

SPECIAL_TECH = {
    "PAT": "개인용 액세스 토큰 (Personal Access Token, PAT)",
    "GitHub App": "GitHub 앱 (GitHub App, GHA)",
    "OAuth App": "OAuth 앱 (OAuth App, OA)",
}


def make_abbr(text: str) -> str:
    cleaned = re.sub(r"\([^)]*\)", " ", text)
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9-]*|[A-Z]{2,}", cleaned)
    if not tokens:
        return "TERM"
    pieces: list[str] = []
    for token in tokens:
        if token.isupper() and len(token) <= 8:
            pieces.append(token)
        elif token.lower() in {"and", "or", "vs", "with", "on", "of", "the", "to"}:
            continue
        else:
            pieces.append(token[0].upper())
    abbr = "".join(pieces) or "TERM"
    return abbr[:12]


def translate_phrase(text: str) -> str:
    stripped = text.strip()
    if stripped in PHRASE_MAP:
        return PHRASE_MAP[stripped]
    if stripped in SPECIAL_TECH:
        return SPECIAL_TECH[stripped]

    # Preserve punctuation and separators while translating known word tokens.
    parts = re.split(r"(\s+|/|&|\bvs\b|—|–|-)", stripped)
    translated: list[str] = []
    changed = False
    for part in parts:
        key = part.strip()
        if key in WORD_MAP:
            repl = WORD_MAP[key]
            translated.append(part.replace(key, repl))
            changed = changed or repl != key
        elif key == "&":
            translated.append(part.replace("&", "와"))
            changed = True
        elif key == "vs":
            translated.append(part.replace("vs", "비교"))
            changed = True
        else:
            translated.append(part)
    result = "".join(translated)
    return result if changed else stripped


def bilingual_topic(topic: str) -> str:
    topic = topic.strip()
    if re.search(r"[가-힣]", topic):
        return topic
    if topic in SPECIAL_TECH:
        return SPECIAL_TECH[topic]
    korean = translate_phrase(topic)
    if korean == topic or not re.search(r"[가-힣]", korean):
        return topic
    return f"{korean} ({topic}, {make_abbr(topic)})"


def normalize_heading(line: str) -> str:
    m = re.match(r"^(#{1,6}\s+)(.*?)(\s*)$", line)
    if not m:
        return line
    prefix, body, suffix = m.groups()

    # Idempotence: already contains Korean.
    if re.search(r"[가-힣]", body):
        return line

    # Code/command heading: preserve exactly.
    if re.fullmatch(r"`[^`]+`", body.strip()):
        return line

    if body in HEADING_MAP:
        return f"{prefix}{HEADING_MAP[body]}{suffix}"
    if body in SPECIAL_TECH:
        return f"{prefix}{SPECIAL_TECH[body]}{suffix}"

    # Translate official course names while preserving official names and exam codes.
    for english, (korean, abbr, exam) in COURSES.items():
        if english in body:
            body = body.replace(english, f"{korean} ({english}, {abbr} / {exam})")
            return f"{prefix}{body}{suffix}"

    # Lab NNN — Topic
    m_lab = re.fullmatch(r"Lab\s+(\d{3})\s+[—-]\s+(.+)", body)
    if m_lab:
        num, topic = m_lab.groups()
        return f"{prefix}실습 (Lab, LAB) {num} — {bilingual_topic(topic)}{suffix}"

    # Practice [N] — Topic
    m_prac = re.fullmatch(r"Practice(?:\s+(\d+))?\s+[—-]\s+(.+)", body)
    if m_prac:
        num, topic = m_prac.groups()
        label = "실습 (Practice, PRAC)" + (f" {num}" if num else "")
        return f"{prefix}{label} — {bilingual_topic(topic)}{suffix}"

    # Scenario [A/B/N] — Topic
    m_scn = re.fullmatch(r"Scenario(?:\s+([A-Z0-9]+))?\s+[—-]\s+(.+)", body)
    if m_scn:
        num, topic = m_scn.groups()
        label = "시나리오 (Scenario, SCN)" + (f" {num}" if num else "")
        return f"{prefix}{label} — {bilingual_topic(topic)}{suffix}"

    # Phase N — Topic
    m_phase = re.fullmatch(r"Phase\s+(\d+)\s+[—-]\s+(.+)", body)
    if m_phase:
        num, topic = m_phase.groups()
        return f"{prefix}단계 (Phase, PH) {num} — {bilingual_topic(topic)}{suffix}"

    # Domain N — Topic
    m_domain = re.fullmatch(r"Domain\s+(\d+)\s+[—-]\s+(.+)", body)
    if m_domain:
        num, topic = m_domain.groups()
        return f"{prefix}영역 (Domain, DOM) {num} — {bilingual_topic(topic)}{suffix}"

    # 010 Exercise — Topic / 010 Topic Exercises
    m_ex = re.fullmatch(r"(\d{3})\s+Exercise\s+[—-]\s+(.+)", body)
    if m_ex:
        num, topic = m_ex.groups()
        return f"{prefix}{num} 연습문제 (Exercise, EXR) — {bilingual_topic(topic)}{suffix}"
    m_ex2 = re.fullmatch(r"(\d{3})\s+(.+?)\s+Exercises", body)
    if m_ex2:
        num, topic = m_ex2.groups()
        return f"{prefix}{num} {bilingual_topic(topic)} — 연습문제 (Exercises, EXR){suffix}"

    # Exercise IDs with a topic, e.g. E010-02 — Hallucination
    m_eid = re.fullmatch(r"(E\d{3}(?:-\d{2})?)\s+[—-]\s+(.+)", body)
    if m_eid:
        eid, topic = m_eid.groups()
        return f"{prefix}{eid} — {bilingual_topic(topic)}{suffix}"

    # Question Set / QBank headings.
    m_qset = re.fullmatch(r"(\d{3})\s+Question Set\s+[—-]\s+(.+)", body)
    if m_qset:
        num, topic = m_qset.groups()
        tail = ""
        topic_core = topic
        m_range = re.search(r"\s+(\(Q\d{3}[–-]Q\d{3}\))$", topic)
        if m_range:
            tail = " " + m_range.group(1)
            topic_core = topic[: m_range.start()].strip()
        return f"{prefix}{num} 문제 세트 (Question Set, QS) — {bilingual_topic(topic_core)}{tail}{suffix}"

    m_qbank = re.fullmatch(r"QBank\s+(\d{3})\s+[—-]\s+(.+)", body)
    if m_qbank:
        num, topic = m_qbank.groups()
        return f"{prefix}문제은행 (Question Bank, QB) {num} — {bilingual_topic(topic)}{suffix}"

    # Numbered or lettered prefix, e.g. "4. GitHub Flow" or "A. GH-900 Study Guide".
    m_indexed = re.fullmatch(r"((?:\d+|[A-Z])\.\s+)(.+)", body)
    if m_indexed:
        index, topic = m_indexed.groups()
        translated = bilingual_topic(topic)
        if translated != topic:
            return f"{prefix}{index}{translated}{suffix}"

    # Numbered Quick Start, e.g. 000. Quick Start.
    m_num_title = re.fullmatch(r"(\d{3}\.\s+)(.+)", body)
    if m_num_title:
        index, topic = m_num_title.groups()
        if topic in HEADING_MAP:
            return f"{prefix}{index}{HEADING_MAP[topic]}{suffix}"
        translated = bilingual_topic(topic)
        if translated != topic:
            return f"{prefix}{index}{translated}{suffix}"

    # Standardized area suffixes used after an em dash or hyphen.
    for english, bilingual in SUFFIX_MAP.items():
        if re.search(rf"(\s+[—-]\s+){re.escape(english)}$", body):
            body = re.sub(rf"(\s+[—-]\s+){re.escape(english)}$", rf"\1{bilingual}", body)
            return f"{prefix}{body}{suffix}"

    # Generic fallback for English-only learning headings. If at least one term can
    # be translated, preserve the original English and add a generated GCLS abbreviation.
    korean = translate_phrase(body)
    if korean != body and re.search(r"[가-힣]", korean):
        return f"{prefix}{korean} ({body}, {make_abbr(body)}){suffix}"

    return line


def normalize_table_cells(line: str) -> str:
    if "|" not in line:
        return line
    parts = line.split("|")
    for i, part in enumerate(parts):
        stripped = part.strip()
        if stripped in TABLE_CELL_MAP:
            left = part[: len(part) - len(part.lstrip())]
            right = part[len(part.rstrip()) :]
            parts[i] = f"{left}{TABLE_CELL_MAP[stripped]}{right}"
        elif stripped in COURSES:
            korean, abbr, exam = COURSES[stripped]
            left = part[: len(part) - len(part.lstrip())]
            right = part[len(part.rstrip()) :]
            parts[i] = f"{left}{korean} ({stripped}, {abbr} / {exam}){right}"
    return "|".join(parts)


def normalize_labels(line: str) -> str:
    replacements = {
        "Content Status": "콘텐츠 상태 (Content Status, CS)",
        "Learning Status": "학습 상태 (Learning Status, LS)",
        "Quick Start": "빠른 시작 (Quick Start, QS)",
        "Exam Gate": "시험 통과 기준 (Exam Gate, EG)",
        "Final Mock": "최종 모의고사 (Final Mock, FM)",
    }
    for english, bilingual in replacements.items():
        patterns = [
            (rf"^(\s*[-*>]?\s*)\*\*{re.escape(english)}\*\*(\s*[:：])", rf"\1**{bilingual}**\2"),
            (rf"^(\s*[-*>]?\s*){re.escape(english)}(\s*[:：])", rf"\1{bilingual}\2"),
        ]
        for pattern, repl in patterns:
            line = re.sub(pattern, repl, line)
    return line


def normalize_markdown(text: str) -> str:
    out: list[str] = []
    in_fence = False
    fence_marker = ""

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            out.append(line)
            continue

        # Markdown headings are never normalized inside code fences.
        if not in_fence:
            line = normalize_heading(line)
            line = normalize_table_cells(line)
            line = normalize_labels(line)
        else:
            # Only normalize the known 010-150 structure labels inside text blocks.
            if stripped in AREA_LINES:
                indent = line[: len(line) - len(line.lstrip())]
                line = indent + AREA_LINES[stripped]

        out.append(line)

    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def is_identifier_heading(body: str) -> bool:
    raw = body.strip()
    if re.fullmatch(r"Q\d{3}", raw):
        return True
    if re.fullmatch(r"E\d{3}(?:-\d{2})?", raw):
        return True
    if re.fullmatch(r"Q\d{3}[–-]Q\d{3}", raw):
        return True
    if re.fullmatch(r"GH-\d{3}", raw):
        return True
    if re.fullmatch(r"`[^`]+`", raw):
        return True
    return False


def english_only_headings(path: Path, text: str) -> list[str]:
    findings: list[str] = []
    in_fence = False
    fence_marker = ""
    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence:
            continue

        m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if not m:
            continue
        body = re.sub(r"[`*_]", "", m.group(1)).strip()
        if is_identifier_heading(body):
            continue
        has_hangul = bool(re.search(r"[가-힣]", body))
        has_latin = bool(re.search(r"[A-Za-z]", body))
        if has_latin and not has_hangul:
            findings.append(f"- `{path.relative_to(ROOT)}` L{lineno}: `{body}`")
    return findings


def main() -> None:
    changed: list[Path] = []
    audit: list[str] = []

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if path.name == "061-language-audit.md":
            continue
        original = path.read_text(encoding="utf-8")
        normalized = normalize_markdown(original)
        if normalized != original:
            path.write_text(normalized, encoding="utf-8")
            changed.append(path)
        audit.extend(english_only_headings(path, normalized))

    audit_path = ROOT / "000-start-here" / "061-language-audit.md"
    audit_body = [
        "# 한글·영어·약어 표기 점검 (Korean-English-Abbreviation Audit, KEAA)",
        "",
        "이 문서는 `scripts/normalize-language-notation.py`가 Repository 전체 Markdown 제목을 점검하여 자동 생성합니다.",
        "",
        "## 점검 결과 (Audit Result, AR)",
        "",
    ]
    if audit:
        audit_body.extend([
            f"추가 검토가 필요한 영어 단독 제목: **{len(audit)}개**",
            "",
            "아래 항목은 공식 제품명·코드명인지, 한글·영어·약어 병기가 필요한 학습 제목인지 사람이 최종 확인합니다.",
            "",
            *audit,
        ])
    else:
        audit_body.append("영어만으로 작성된 일반 학습 제목을 발견하지 않았습니다. **PASS**")
    audit_body.extend([
        "",
        "## 적용 기준 (Applied Standard, AS)",
        "",
        "- 기준 문서: `000-start-here/060-language-notation-standard.md`",
        "- 표기 형식: `한글 (English Full Name, ABBR)`",
        "- 명령어·코드·경로·URL·YAML/JSON 키는 번역하지 않음",
        "- Q001/E001 같은 문제·연습문제 식별자는 번역 대상에서 제외",
        "",
    ])
    new_audit = "\n".join(audit_body)
    old_audit = audit_path.read_text(encoding="utf-8") if audit_path.exists() else ""
    if new_audit != old_audit:
        audit_path.write_text(new_audit, encoding="utf-8")
        changed.append(audit_path)

    print(f"Changed Markdown files: {len(changed)}")
    print(f"Remaining English-only headings: {len(audit)}")
    for path in changed:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
