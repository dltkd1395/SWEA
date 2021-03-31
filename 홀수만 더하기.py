# SWEA[홀수만 더하기]

data=[]
res=[]
for _ in range(int(input())):
  data.append(list(map(int,input().split())))

for i in data:
  count=0
  for j in range(10):
    if i[j]%2!=0:
      count+=i[j]
    else:
      continue
  res.append(count)

for i in range(len(res)):
  print('#%d %d' %(i+1,res[i]))
