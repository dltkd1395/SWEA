# SWEA[암호문2]

for t in range(10):
  n=int(input())
  crypto=list(map(int,input().split()))

  c=int(input())
  cmd=list(map(str,input().split()))

  while len(cmd)>0:
    if cmd[0]=='I':
      crypto[int(cmd[1]):int(cmd[1])]+=cmd[3:int(cmd[2])+3]
      del cmd[:int(cmd[2])+3]
      continue

    if cmd[0]=='D':
      del crypto[int(cmd[1]):int(cmd[1])+int(cmd[2])]
      del cmd[:3]

  print('#%d' %(t+1),end=' ')
  for i in range(10):
    print(crypto[i],end=' ')
