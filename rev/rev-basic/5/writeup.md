# [rev-basic-05]

## 🔍 문제 설명 / Problem Description
- 문제 출처 / Source: https://dreamhack.io/wargame/challenges/19
- 요약 / Summary:
  - 간단한 문자열 비교를 통해 플래그를 찾는 리버싱 문제입니다.  
  - This is a simple reversing challenge based on string comparison.

## 🛠 사용 도구 및 환경 / Tools & Environment
- 사용한 도구 / Tools used: IDA Free 9.1

- 분석 환경 / Analysis environment: MS Windows 10

## 🧠 분석 / Analysis
- 실행 포맷 / Executable format: Portable executable for AMD64 (PE)

- 주요 함수 및 흐름 / Key functions & flow
![의사 코드 / Pseudocode](/img/pseudocode.jpg)
1. 문자를 입력 / Input string
2. 입력값 검증 / Verify input data
3. 분기별 출력 / Output divergence

- 의심 지점 / Suspicious parts
X

- 디버깅 관찰 / Observations during debugging
= 풀이 과정 / = Solution Steps

## 🔓 풀이 과정 / Solution Steps
1. (KR) 의사코드로 디컴파일 후 분석  
   (EN) After decompiling the assembly code into pseudocode, I analyzed it

   ![의사 코드 / Pseudocode](/img/pseudocode2.jpg)
   (KR) 의사코드 중 입력값을 검증하는 부분을 알아야 플래그를 알아낼 수 있기에
      가장 먼저 보았다.
   (EN) I focused first on the input validation part of the pseudocode since understanding it was key to retrieving the flag.
   
2. (KR) 어셈블리와 비교하여 분석  
   (EN) Analysis and comparison of pseudocode and assembly

   ![어셈블리 코드 / Assembly code](/img/assembly.jpg)
   (KR) 보아하니 별 다른 문제는 없는 모양
   (EN) From the looks of it, there didn’t seem to be any unexpected behavior or hidden logic.

3. (KR) 주요 루틴 역추적 및 조건 해제  
   (EN) Trace key routines and bypass conditions

   ![생각 1 / Idea 1](/img/thinking1.jpg)
   (KR) 이런 느낌으로 입력값을 검증하는구나
   (EN) It became clear that the program validates the input using a specific pattern like this.

   (KR) 그런데 이 느낌으로 가면 뒤에가 0이니까 특정 값을 주는게 아닐까?
   (EN) Given that the comparison ends with 0, I assumed the program might rely on a specific value at the end.

   (KR) 그렇다면 그 값을 기반으로 코드를 짜보자
   (EN) So I wrote code to reverse the logic based on that assumption.

4. (KR) 키/플래그 추출  
   (EN) Extract key/flag

```
table = [ 0xAD , 0xD8 , 0xCB , 0xCB , 0x9D , 0x97 , 0xCB , 0xC4 , 
         0x92 , 0xA1 , 0xD2 , 0xD7 , 0xD2 , 0xD6 , 0xA8 , 0xA5 ,
         0xDC , 0xC7 , 0xAD , 0xA3 , 0xA1 , 0x98 , 0x4C , 0x00 , 
         0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 ]

a = [0] * 25
a[22] = 0x4C  # 임의의 시작값. 추정값.

for i in range(22, 0, -1):
    a[i] = (table[i] - a[i+1])

a[0] = (table[0] - a[1])


flag = ''.join(chr(x) for x in a[:23])

print("DH{"+flag+"}")
```

## ✅ 결과 / Result
- ![결과창 / Result](/img/result.jpg)

## 📝 기타 메모 / Notes
- (KR) 분석 중 삽질하거나 기록해두고 싶은 것들  
- (EN) Extra notes, pitfalls, or things to remember later

1. (KR)계산식 분석 중 너무 많은 삽질을 해버림
   (EN) Spent too much time analyzing the formula due to misinterpretation of the decryption loop.