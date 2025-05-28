table = [ 0xF8 , 0xE0 , 0xE6 , 0x9E , 0x7F , 0x32 , 0x68 , 0x31 ,
            0x05 , 0xDC , 0xA1 , 0xAA , 0xAA , 0x09 , 0xB3 , 0xD8 ,
            0x41 , 0xF0 , 0x36 , 0x8C , 0xCE , 0xC7 , 0xAC , 0x66 ,
            0x91 , 0x4C , 0x32 , 0xFF , 0x05 , 0xE0 , 0xD9 , 0x91 ]

unk_402068 = [0xDE , 0xAD , 0xBE , 0xEF]
unk_40206D = [0xEF , 0xBE , 0xAD , 0xDE]
unk_402072 = [0x11 , 0x33 , 0x55 , 0x77 , 0x99 , 0xBB , 0xDD]

def sub_001(a1 , a2):
    v4 = len(a2)
    result = []
    for i in range(32):
        result.append((a1[i] ^ a2[i%v4])&0xFF)
    return result

def sub_002(a1 , a2):
    result = []
    for i in range(32):
        result.append((a1[i]-a2)&0xFF)
    return result 

def sub_003(a1 , a2):
    result = []
    for i in range(32):
        result.append((a1[i] + a2)&0xFF)
    return result

input = sub_001(table , unk_402072) 
input = sub_002(input , 243)
input = sub_003(input , 77)
input = sub_001(input , unk_40206D)
input = sub_003(input , 90)
input = sub_002(input , 31)
input = sub_001(input , unk_402068)

for i in range(len(input)):
    input[i] = chr(input[i])

print("DH{"+''.join(input)+"}")




