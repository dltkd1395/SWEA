# SWEA[두 개의 숫자열]

for t in range(int(input())):

  n,m=map(int,input().split())

  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  max_value=0
  if n>m:
    for i in range(n-m+1):
      count=0
      for j in range(m):
        count+=a[i+j]*b[j]
      max_value=max(max_value,count)
  else:
    for i in range(m-n+1):
      count=0
      for j in range(n):
        count+=a[j]*b[i+j]
      max_value=max(max_value,count)

  print('#%d %d' %(t+1,max_value))

