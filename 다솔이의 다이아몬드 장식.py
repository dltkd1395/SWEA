# SWEA[다솔이의 다이아몬드 장식]

for t in range(int(input())):

  s=list(input())
  data=['']*5
  a='..#.'
  b='.#.#'
  last='.'
  c1='#.'
  c2='.'
  c_last='#'
  n=len(s)
  data[0]+=a*n+last
  data[1]+=b*n+last
  for i in s:
    data[2]+=c1+i+c2
  data[2]+=c_last
  data[3]+=b*n+last
  data[4]+=a*n+last

  for i in data:
    print(i) 
