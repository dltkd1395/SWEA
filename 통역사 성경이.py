# SWEA[통역사 성경이]

for t in range(int(input())):
  n=int(input())
  s=input()
  start=0
  res=[]

  for i in range(len(s)):
    cnt=0
    if s[i] in ('!','?','.'):
      for word in s[start:i].split():
        if (len(word)==0 and word[0].isupper()) or (word[0].isupper() and word.isalpha() and word[1:].islower()):
          cnt+=1
      start=i+2
      res.append(cnt)
  print('#%d' %(t+1),end=' ')
  
  for i in res:
    print('%d' %i,end=' ')
  print()
