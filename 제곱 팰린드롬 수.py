# SWEA[제곱 팰린드롬 수]
import math

for t in range(int(input())):
  a,b=map(int,input().split())
  cnt=0
  for i in range(a,b+1):
    
    x=math.sqrt(i)
    if x%1>0:
      continue
    x=str(int(x))
    y=str(i)
    if x==x[::-1] and y==y[::-1]:
      cnt+=1

  print('#%d %d' %(t+1,cnt))
