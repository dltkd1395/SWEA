# SWEA[영준이의 카드 카운팅]

def isCard():
  for i in range(len(a)):
      for j in range(i+1,len(a)):
        if (a[i]+b[i])==(a[j]+b[j]):
          return False
  return True

for t in range(int(input())):
  card=list(input())
  a=card[::3]
  b=[]
  for i in range(1,len(card),3):
    b.append(card[i]+card[i+1])

  if isCard()==False:
    print('#%d' %(t+1),'ERROR')
  else:
    s,d,h,c=a.count('S'),a.count('D'),a.count('H'),a.count('C')
    print('#%d %d %d %d %d' %(t+1,13-s,13-d,13-h,13-c))
