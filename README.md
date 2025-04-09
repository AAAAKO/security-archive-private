# security-archive-private


# writeup template
# [문제 이름 / Problem Title]

## 🔍 문제 설명 / Problem Description
- 문제 출처 / Source: [링크 or 대회명 / link or CTF name]
- 요약 / Summary:
  - (한국어) 문제의 개요나 목적 서술
  - (EN) Brief overview or goal of the challenge

## 🧠 분석 / Analysis
- 실행 포맷 / Executable format: (e.g., ELF 64-bit, PE 32-bit)
- 주요 함수 및 흐름 / Key functions & flow
- 의심 지점 / Suspicious parts
- 디버깅 관찰 / Observations during debugging

## 🛠 사용 도구 및 환경 / Tools & Environment
- 사용한 도구 / Tools used: (e.g., IDA Free, Ghidra, x64dbg)
- 분석 환경 / Analysis environment: (e.g., Windows 10, Ubuntu 20.04)

## 🔓 풀이 과정 / Solution Steps
1. (KR) 실행 및 초기 동작 관찰  
   (EN) Observe initial behavior and runtime
2. (KR) 문자열 및 함수 분석  
   (EN) Analyze strings and functions
3. (KR) 주요 루틴 역추적 및 조건 해제  
   (EN) Trace key routines and bypass conditions
4. (KR) 키/플래그 추출  
   (EN) Extract key/flag

## ✅ 결과 / Result
- 플래그 / Flag: `FLAG{example_flag}`
- 또는 기타 출력 결과 / Or any other output result

## 📝 기타 메모 / Notes
- (KR) 분석 중 삽질하거나 기록해두고 싶은 것들  
- (EN) Extra notes, pitfalls, or things to remember later

## 🖼️ 이미지 / Images
> 이미지는 `img/` 폴더에 넣고 아래처럼 링크합니다  
> Images should be placed in the `img/` folder like this:

```markdown
![description](./img/example.png)