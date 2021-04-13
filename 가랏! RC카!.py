# SWEA[가랏! RC카!]

for t in range(int(input())):

  n=int(input())
  res=0
  speed=0
  for i in range(n):
    c=list(map(int,input().split()))
  
    if c[0]==1:
      speed+=c[1]
      
    if c[0]==2:
      if speed < c[1]:
        speed = 0
      else:
        speed -= c[1]

    res+=speed
  print('#%d %d' %(t+1,res))   
