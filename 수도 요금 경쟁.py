# SWEA[수도 요금 경쟁]

for t in range(int(input())):
  P, Q, R, S, W=map(int,input().split())

  A=P*W
  
  if R>=W:
    B=Q
  else:
    B=Q+((W-R)*S)
  print('#%d' %(t+1),end=' ')
  if A<B:
    print(A)
  else:
    print(B)
