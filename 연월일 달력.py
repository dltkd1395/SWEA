# SWEA[연월일 달력]

for i in range(int(input())):
  data=list(map(int,input()))
  year=int(data[0:4])
  month=int(data[4:6])
  day=int(data[6:8])

  if month in [1,3,5,7,8,10,12]:
    if day<1 or day>31:
      print(-1)
      continue

  if month in [4,6,9,11]:
    if day<1 or day>30:
      print(-1)
      continue

  if month in [2]:
    if day<1 or day>28:
      print(-1)
      continue

  print('#%d %04d/%02d/%02d' %(i+1,year,month,day))
