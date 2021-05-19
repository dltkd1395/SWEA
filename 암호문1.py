# SWEA[암호문1]

for t in range(10):
  n=int(input())
  crypto=list(map(int,input().split()))

  c=int(input())
  command=input().split('I')
  data=[]

  for i in range(len(command)):
    data.append(command[i].split())

  
  for i in range(1,len(data)):
    x=int(data[i][0])
    y=int(data[i][1])
    s=data[i][2:]
    for j in range(y):
      crypto.insert(x+j,s[j])

  print('#%d' %(t+1), end=' ')

  for i in range(10):
    print(data[i],end=' ')

  
  

