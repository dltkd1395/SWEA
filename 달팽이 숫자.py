# SWEA[달팽이 숫자]

for t in range(int(input())):

  n=int(input())

  graph=[[0]*n for _ in range(n)]

  dx=[0,1,0,-1]
  dy=[1,0,-1,0]

  x=y=0
  mode=0
  graph[x][y]=1

  for i in range(2,n**2+1):
    
    x+=dx[mode]
    y+=dy[mode]
    
    graph[x][y]=i

    if 0<=x+dx[mode]<n and 0<=y+dy[mode]<n and not graph[x+dx[mode]][y+dy[mode]]:
      continue
 
    else:
      if mode!=3:
        mode+=1
      else:
        mode=0

  print('#%d' %(t+1))
  for i in graph:
    for j in i:
      print(j,end=' ')
    print()
