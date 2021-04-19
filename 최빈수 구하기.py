# SWEA[최빈수 구하기]

for t in range(int(input())):

  n=int(input())

  grade=list(map(int,input().split()))
  max_count=0
  max_value=0

  for i in range(100,-1,-1):
    count=grade.count(i)

    if max_count<count:
      max_count=count
      max_value=i

  print('#%d %d' %(t+1,amx_value)
