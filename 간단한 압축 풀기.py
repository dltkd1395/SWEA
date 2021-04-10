# SWEA[간단한 압축 풀기]

for t in range(int(input())):

  n=int(input())
  data=''
  for i in range(n):
    a,b=input().split()
    b=int(b)
    while True:
      if b<=0:
        break
      else:
        data+=a
      b-=1

  count=1
  print('#%d' %(t+1))
  for i in data:
    print(i,end='')
    if count%10==0:
      print()
    count+=1
  print()
