# SWEA[회문1]

for t in range(10):
  n=int(input())

  data=[list(input()) for _ in range(8)]
  cnt=0
  for i in range(8):
    for j in range(8-n+1):
      row=[]
      for k in range(j,n+j):
        row.append(data[i][k])
      row_reverse=list(reversed(row))
      
      if row==row_reverse:
        cnt+=1

  for i in range(8):
    for j in range(8-n+1):
      col=[]
      for k in range(j,n+j):
        col.append(data[k][i])
      col_reverse=list(reversed(col))
      
      if col==col_reverse:
        cnt+=1
  print('#%d %d' %(t+1,cnt))
  

