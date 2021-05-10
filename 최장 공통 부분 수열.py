# SWEA[최장 공통 부분 수열]

for t in range(int(input())):
  a,b=list(map(str,input().split()))

  matrix=[[0]*(len(b)+1) for _ in range(len(a)+1)]
  for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
  
  
  print('#%d %d' %(t+1,matrix[-1][-1]))

