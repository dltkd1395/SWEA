# SWEA[전봇대]

for t in range(int(input())):
  n=int(input())
  line=[list(map(int,input().split())) for _ in range(n)]
  cnt=0
  for i in line:
    a=i[0]
    b=i[1]
    for j in line:
      if j[1]<b:
        if j[0]>a:
          cnt+=1
      elif j[1]>b:
        if j[0]<a:
          cnt+=1
  
  print('#%d %d' %(t+1,cnt//23))
