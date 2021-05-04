# SWEA[재미있는 오셀로 게임]
dx=[0,1,-1,0,1,-1,-1,1]
dy=[1,0,0,-1,1,1,-1,-1]
for t in range(int(input())):
  n,m=map(int,input().split())
  graph=[[0]*n for _ in range(n)]
  n1=n//2
  graph[n1][n1]=2
  graph[n1-1][n1]=1
  graph[n1][n1-1]=1
  graph[n1-1][n1-1]=2
  
  for _ in range(m):
    x,y,s=map(int,input().split())
    x,y=x-1,y-1
    reverse=[]
    for i in range(8):
      nx=x+dx[i]
      ny=y+dy[i]
      while True:
        if nx<0 or nx>=n or ny<0 or ny>=n:
          reverse=[]
          break
        if graph[nx][ny]==0:
          reverse=[]
          break
        if graph[nx][ny]==s:
          break
        else:
          reverse.append((nx,ny))

        nx,ny=nx+dx[i],ny+dy[i]
      for rx,ry in reverse:
        if s==1:
          graph[rx][ry]=1
        else:
          graph[rx][ry]=2
    graph[x][y]=s
  w=0
  b=0
  for i in range(n):
    for j in range(n):
      if graph[i][j]==1:
        w+=1
      elif graph[i][j]==2:
        b+=1
  print('#%d %d %d' %(t+1,w,b))
