# SWEA[외로운 문자]

for t in range(int(input())):
  s=list(input())

  res=[]

  for i in s:
    if i not in res:
      res.append(i)
    else:
      res.remove(i)
  res.sort()
  print('#%d' %(t+1), end=' ')
  
  if len(res)==0:
    print('Good')
  else:
    for i in res:
      print(i,end='')
    print()


