# SWEA[삼성시의 버스 노선]

for t in range(int(input())):
  n=int(input())
  res=[0]*5001
  bus_stop=[]
  for i in range(n):
    a,b=map(int,input().split())
    
    for j in range(a,b+1):
      res[j]+=1
  
  p=int(input())
  
  for i in range(p):
    c=int(input())
    bus_stop.append(res[c])

  print('#%d' %(t+1), ' '.join(map(str,bus_stop)))

  
    
