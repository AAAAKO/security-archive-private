# Reversing Write-up (리버싱 라이트업)

## 1. Scope & Objective
- 분석 목적: (예: 알고리즘 추출 / 취약점 분석 / 난독화 해제)
- 우선순위: (Primary / Secondary)
- 분석 범위: (정적/동적, 특정 함수/섹션 등)
- 제외 범위: (해당 없는 부분)

---

## 2. Preliminary Recon (정적 1차 관찰)
### 2.1 파일 메타정보
- 파일 타입(ELF/PE 등):
- 아키텍처:
- Build Info / Compiler 특징:
- 보호기법(PIE/NX/Canary/ASLR 등):

### 2.2 Surface Indicators (표면 레벨 단서)
- 주요 스트링 목록:
- Import/Export 함수 단서:
- 난독화 여부:
- 특이한 섹션 / 패킹 흔적:

---

## 3. Execution Model (프로그램 실행 모델)
### 3.1 High-Level Flow (상위 레벨 동작)
- 입력 → 처리 → 출력 요약
- 핵심 로직의 위치 (함수 / 섹션 기준)

### 3.2 Entry Point(S) 분석
- init 루틴 요약
- 흐름 제어 패턴 (분기/루프/핵심 호출)

---

## 4. Static Deep Dive (정적 심층 분석)
> 분석 중 중요한 “Hard Point” 발견 순서대로 서술

### 4.x Hard Point: {이름 or 주소}
- 위치: (주소/함수명)
- 목적:
- 근거 기반 분석:
  - 관찰된 바이트코드/연산
  - 추출된 제약 조건
  - 제어 흐름(분기/루프)
  - 사용된 상수/테이블
- (필요 시) 역추적된 데이터 흐름(DFG)
- 해석된 기능:
- 의문점 / 다음 분석 지점(TODO):

> Hard Point가 여러 개면 4.1 / 4.2 / 4.3 … 식으로 계속 작성

---

## 5. Dynamic Analysis (동적 분석)
### 5.1 실행 흐름 관찰
- 브레이크포인트 위치:
- 레지스터 변화:
- 메모리/스택 변화:
- 주요 비교/루프 시점:

### 5.2 Behavior Indicators (행위적 특징)
- 파일/네트워크/레지스트리 접근 등
- 시간 기반, 안티 디버깅 기반 동작

---

## 6. Algorithm / Routine Extraction
### 6.1 알고리즘 구조
- 전체 로직 요약:
- 세부 단계:
- 수학적/논리적 핵심:

### 6.2 의사코드(Pseudo-code)
(필요 시만 작성 / 과도한 재작성 금지)

---

## 7. Vulnerability / Insight (취약점 및 핵심 포인트)
- 취약점 유형 분석 (BOF / UAF / Logic Bug 등)
- 근거:
- 악용 가능성:
- 영향도:
- 패치 포인트:

---

## 8. Consolidated Flow (최종 동작 정리)
- Entry → 주요 함수 → 핵심 로직 → 출력까지  
텍스트 기반 흐름도(DFD/CALL FLOW):


---

## 9. 확정 사항 / 미확정 사항
### 9.1 Confirmed (관찰로 확정된 사실)
- 예: 특정 루틴은 XOR 기반 복호화 루틴임(주소/근거)

### 9.2 Unconfirmed (근거 부족/추적 필요)
- 예: 특정 루틴의 일부는 난독화되어 판단 불가

### 9.3 TODO (추가 분석 필요)
- 예: 특정 테이블의 의미 분석 필요

---

## 10. Final Summary
- 핵심 기능 3줄 요약:
- 리버싱 관점에서 가장 중요한 지점:
- 추가 작업 제안:
