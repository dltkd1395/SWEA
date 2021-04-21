# SWEA[다트 게임]

for t in range(int(input())):
  n=int(input())
  
  for i in range(n):
    x,y=map(int,input().split())

    res=((x-0)**2+(y-0)**2)**(1/2)
    cnt=0
    if res<=20:
      cnt+=10
    elif res<=40:
      cnt+=9
    elif res<=60:
      cnt+=8
    elif res<=80:
      cnt+=7
    elif res<=100:
      cnt+=6
    elif res<=120:
      cnt+=5
    elif res<=140:
      cnt+=4
    elif res<=160:
      cnt+=3
    elif res<=180:
      cnt+=2
    elif res<=200:
      cnt+=1

  print('#%d %d' %(t+1,cnt))
