import io

def extract(a1,a2):     ## 테이블을 추출하는 함수
    output_str = []     
    key_table = [0] * 65    ## 추출된 테이블을 담기 위한 공간 

    while(1):
        c = a1.read()   ## 인코딩 되기 이전의 텍스트를 읽어옴
        if not c:       ## EOF 면 멈춤
            break
        input_8bit = ''.join(format(byte,'08b') for byte in c)  ## 추출된 텍스트를 8bit형태로 나열
        input_6bit = [int(input_8bit[i:i+6],2) for i in range(0,len(input_8bit),6)] ## 8bit 형태로 된 비트를
                                                                ## 6bit 단위로 쪼갠 뒤 10진수로 바꿈
    while(1):
        c = a2.read(1)  ## 인코딩 이후의 텍스트를 읽어옴
        if not c:       ## EOF 면 멈춤
            break
        output_str.append(chr(c[0]))    ## 텍스트들을 문자로 변환해서 저장

    for i in range(0,len(input_6bit)):
        if(key_table[input_6bit[i]] == 0 ): ## 추출되지 않았다면
            key_table[input_6bit[i]] = output_str[i] ## 그 테이블 인덱스에 인코딩 이후의 문자를 넣어 테이블을 만듦
    return key_table

def flag_decode(a1,a2): ## 추출된 키 테이블을 가지고 플래그를 도출
    flag = []
    flag_decimal = []
    s = a1.read()       ## 인코딩 된 플래그를 읽어옴

    for i in range(0,len(s)):
        for j in range(0,len(a2)):
            if(chr(s[i]) == a2[j]): ## 인코딩 된 플래그의 문자와 키 테이블의 문자가 같다면 키 테이블의 인덱스를 
                flag_decimal.append(j) ## 10진수로 넣는다. 한 마디로 문자를 키 테이블의 10진수로 바꾸는 과정

    flag_6bit = ''.join(format(byte,'06b') for byte in flag_decimal) ## 바꿔진 값들을 6bit단위로 쪼개고
    flag_8bit = flag_6bit + '0' * 6                        ## 8의 배수로 맞춰줄 생각이였으나 의미는 없었다.

    for i in range(0,len(flag_8bit),8):                 ## 8bit 씩 끊어서
        byte_str = flag_8bit[i:i+8]
        byte_val = int(byte_str, 2)                     ## 10진수로 바꾸고
        flag.append(chr(byte_val))                      ## 문자로 변환하여
    
    print("".join(flag))                                ## 플래그 추출

if __name__ == '__main__' :
    with open('text_in.txt','rb') as str_input , open('text_out.txt','rb') as str_output:
        key_table = extract(str_input,str_output) ## 주어진 예시 입출력 텍스트를 가지고 테이블을 추출
    
    with open('flag_out.txt','rb') as flag_output:
        flag_decode(flag_output,key_table) ## 추출된 키 테이블을 갖고 flag 값을 도출