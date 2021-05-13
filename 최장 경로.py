# SWEA[최장 경로]

def dfs(idx,cnt):
  global count
  visited[idx]=0
  cnt+=1
  if count<cnt:
    count=cnt
  
  for i in graph[idx]:
    if visited[i]:
      dfs(i,cnt)
  
  visited[idx]=1

for t in range(int(input())):
  n,m=map(int,input().split())

  visited=[1 for _ in range(n+1)]
  data=[list(map(int,input().split())) for _ in range(m)]
  graph=[[] for _ in range(n+1)]
  count=0

  for x,y in data:
    graph[x].append(y)
    graph[y].append(x)

  
  for i in range(n):
    dfs(i,0)

  print('#%d %d' %(t+1,count))

  
