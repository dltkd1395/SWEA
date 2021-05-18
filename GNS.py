# SWEA[GNS]
T=int(input())
dic={"ZRO":0 , "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
for t in range(1,T+1):
  tc,n=map(str,input().split())

  data=list(map(str,input().split()))

  idx=[[],[],[],[],[],[],[],[],[],[]]

  for i in data:
    idx[dic[i]].append(i)

  for j in idx:
    for k in j:
      print(' '.join(k))

