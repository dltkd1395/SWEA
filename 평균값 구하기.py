# SWEA[평균값 구하기]
data=[]
res=[]
for _ in range(int(input())):
  data.append(list(map(int,input().split())))

for i in data:
  count=0
  for j in i:
    count+=j
  count=count/10
  res.append(round(count))

for i in range(len(res)):
  print('#%d %d' %(i+1,res[i]))
