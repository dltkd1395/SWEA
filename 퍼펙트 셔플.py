# SWEA[퍼펙트 셔플]

for t in range(int(input())):
  n=int(input())
  data=list(input().split())
  m=n//2
  res=[]
  idx=1
  if n%2==0:
    for i in range(n):
      if i<m:
        res.append(data[i])
      else:
        res.insert(idx,data[i])
        idx+=2

  else:
    for i in range(n):
      if i<m+1:
        res.append(data[i])
      else:
        res.insert(idx,data[i])
        idx+=2

  print('#%d' %(t+1),' '.join(res))
  
  
