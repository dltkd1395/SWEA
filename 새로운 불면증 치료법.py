# SWEA[새로운 불면증 치료법]

for t in range(int(input())):

  num=[10,10,10,10,10,10,10,10,10,10]

  n=int(input())
  count=1
  while True:
    cnt=count*n

    for i in str(cnt):
      i=int(i)
      num[i]=i

    if num ==[0,1,2,3,4,5,6,7,8,9]:
      print(cnt)
      break

    count+=1
  
    
