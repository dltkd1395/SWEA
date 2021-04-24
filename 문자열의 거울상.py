# SWEA[문자열의 거울상]

for t in range(int(input())):
  s=list(input())
  res=[]
  for i in range(len(s)):
    if s[i]=='b':
      res.append('d')
    elif s[i]=='d':
      res.append('b')
    elif s[i]=='p':
      res.append('q')
    elif s[i]=='q':
      res.append('p')

  res.reverse()
  print('#%d' %(t+1),end=' ')
  for i in res:
    print(i,end='')
  print()

