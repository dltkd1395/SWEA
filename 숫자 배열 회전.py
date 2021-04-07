# SWEA[숫자 배열 회전]

for t in range(int(input())):
  n=int(input())

  num=[list(map(int,input().split())) for _ in range(n)]
  graph=[[0]*n for _ in range(n)]
  
  lst_90=[]
  for j in range(n):
    tmp=[]
    for i in range(n):
      tmp.append(num[i][j])
    
    tmp.reverse()
    lst_90.append(tmp)
  
  
  lst_180=[]
  for j in range(n):
    tmp=[]
    for i in range(n):
      tmp.append(lst_90[i][j])
    
    tmp.reverse()
    lst_180.append(tmp)
  

  lst_270=[]
  for j in range(n):
    tmp=[]
    for i in range(n):
      tmp.append(lst_180[i][j])
    
    tmp.reverse()
    lst_270.append(tmp)
  print('#%d' %(t+1))
  for i in range(n):
    print(''.join(list(map(str, lst_90[i]))), ''.join(list(map(str, lst_180[i]))), ''.join(list(map(str, lst_270[i]))))
