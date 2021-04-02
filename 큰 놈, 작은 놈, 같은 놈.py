# SWEA[큰 놈, 작은 놈, 같은 놈]
data=[]
for _ in range(int(input())):
  a,b=map(int,input().split())

  if a<b:
    data.append('<')
  elif a>b:
    data.append('>')
  elif a==b:
    data.append('=')


for i in range(len(data)):
  print('#%d %d' %(i+1,data[i]))
