# SWEA[신뢰]
for t in range(int(input())):
  data=list(input().split())
  n=int(data[0])
  B,O,order=[],[],[]
  B_idx,O_idx=1,1
  for i in range(1,2*n+1,2):
    order.append(data[i])
    if data[i]=='B':
      B.append(int(data[i+1]))
    if data[i]=='O':
      O.append(int(data[i+1]))
  time=0
  while order:
    time+=1
    x=order[0]
    if len(B):
      if B_idx==B[0]:
        if x=='B':
          B.pop(0)
          order.pop(0)
      elif B_idx-B[0]>0:
        B_idx-=1
      else:
        B_idx+=1
    if len(O):
      if O_idx==O[0]:
        if x=='O':
          O.pop(0)
          order.pop(0)
      elif O_idx-O[0]>0:
        O_idx-=1
      else:
        O_idx+=1
  print('#%d %d' %(t+1,time))
