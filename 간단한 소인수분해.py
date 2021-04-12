# SWEA[간단한 소인수분해]

for t in range(int(input())):

  n=int(input())
  num=[11,7,5,3,2]
  result=[0]*5
  i=0
  while True:
      
    if i==5:
      break
    if n%num[i]==0:
      n=n//num[i]
      result[i]+=1
    else:
      i+=1
  result.reverse()
  
  print('#%d' %(t+1),end=' ')
  for i in result:
    print(i,end=' ')
  print()
