# SWEA[이진수 표현]

for t in range(int(input())):
  n,m=map(int,input().split())

  x=list(str(bin(m)[2:]))
  x.reverse()
  cnt=0
  print('#%d' %(t+1),end=' ')
  while True:

    for i in range(len(x)):

      if cnt==n:
        break
      if x[i]=='1':
        cnt+=1
      else:
        break
    if cnt==n:
      print('ON')
    else:
      print('OFF')
    break
    
        
