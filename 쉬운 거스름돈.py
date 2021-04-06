# SWEA[쉬운 거스름돈]

for i in range(int(input())):

  moneys=[50000,10000,5000,1000,500,100,50,10]

  n=int(input())

  money=[0]*8

  for j in range(8):
    if n//moneys[j]!=0:
      money[j]=n//moneys[j]
      n=n%moneys[j]

  print('#%d' %(i+1))

  for j in money:
    print(j,end=' ')
  print()
  
