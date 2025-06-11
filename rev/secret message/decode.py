import io

def decode(a1,a2):
    v5 = -1
    while(1):
        c = a1.read(1)
        if not c :
            break ## EOF 만나면 1차 루프 종료
        a2.write(c)

        if(c == v5):
            while(1):
                c = a1.read(1)
                if not c :
                    break ## EOF 만나면 2차 루프 종료

                if (c != v5):
                    v3 = int.from_bytes(c) ## 3차 루프 횟수 저장
                    for i in range(v3):
                        a2.write(v5)
                    break
        else:
            v5 = c

if __name__ == '__main__':
    with open('secretMessage.raw','wb') as raw, open('secretMessage.enc','rb') as enc:
        decode(enc,raw) ## .raw 랑 .enc 스트림 생성 후 decode 함수 실행


