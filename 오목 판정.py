# SWEA[오목 판정]

dx=[0,1,1,1]
dy=[1,1,0,-1]

def dfs(i,j,k,cnt):
  global cnt_break

  if cnt>=5:
    cnt_break=1
    return
  nx=i+dx[k]
  ny=j+dy[k]
  if 0<=nx<n and 0<=ny<n:
    if data[nx][ny]=='o':
      dfs(nx,ny,k,cnt+1)
    else:
      return
  else:
    return


for t in range(int(input())):
  n=int(input())

  data=[list(input()) for _ in range(n)]

  cnt_break=0
  for i in range(n):
    if cnt_break==1:
      break
    for j in range(n):
      if cnt_break==1:
        break
      if data[i][j]=='o':
        for k in range(4):
          if k==0:
            if n-j>=5:
              dfs(i,j,k,1)
          elif k==1:
            if n-i>=5 and n-j>=5:
              dfs(i,j,k,1)
          elif k==2:
            if n-i>=5:
              dfs(i,j,k,1)
          elif k==3:
            if n-i>=5 and j>=4:
              dfs(i,j,k,1)
          else:
            if cnt_break==1:
              break

  if cnt_break==1:
    print('#%d YES' %(t+1))
  else:
    print('#%d NO' %(t+1))
      
