# SWEA[정곤이의 단조 증가하는 수]

def check(num):
  res=str(num)

  for i in range(len(res)-1):
    if int(res[i])>int(res[i+1]):
      return False
  return True

for t in range(int(input())):
  n=int(input())

  a=list(map(int,input().split()))
  result=-1
  for i in range(n):
    for j in range(i+1,n):
      num=a[i]*a[j]
      if result<num and check(num):
        result=num
  
  print('#%d %d' %(t+1,result))
