# SWEA[Base64 Decoder]

def binary_to_decimal(bi_num):   
    
    decimal_number = 0
    bi_num_str = str(bi_num)
   
    for i, digit in enumerate(bi_num_str):
        decimal_number += int(digit) * pow(2, len(bi_num_str) - 1 - i)
    
    return decimal_number

for t in range(int(input())):
  base=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h'\
        ,'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
  s=input()
  b=''
  res=[]
  print('#%d' %(t+1))
  for i in s:
    a=base.index(i)
    a=bin(a)[2:].zfill(6)
    b+=a

  for i in range(0,len(b),8):
    c=b[0+i:8+i]

    r=binary_to_decimal(c)
    print(chr(r),end='')

    
