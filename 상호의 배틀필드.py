# SWEA[상호의 배틀필드]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
 
def shoot(i,j,d):

  y,x=i,j
  while True:
    y+=dx[d]
    x+=dy[d]

    if 0<=x<w and 0<=y<h:
      if data[y][x]=='#':
        return
      elif data[y][x]=='*':
        data[y][x]='.'
        return
    else:
      return
 

for t in range(int(input())):
  h, w= map(int, input().split())
  data = [list(map(str, input())) for _ in range(h)]
  n = int(input())
  c = input() 

  tank = '^>v<'
  tank_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}
  for i in range(h):
    for j in range(w):
      if data[i][j] in tank:
        tank_idx = [i, j, tank_dir[data[i][j]]]
        data[i][j] = '.'

  move = 'URDL' 
  for i in range(n):
    if c[i] == 'S':
      shoot(tank_idx[0], tank_idx[1], tank_idx[2])
    else:
      for j in range(len(move)):
        if c[i] == move[j]:
          my = tank_idx[0]+dx[j]
          mx = tank_idx[1]+dy[j]
          if 0 <= my < h and 0 <= mx < w:
            if data[my][mx] == '.':
              tank_idx[0] += dx[j]
              tank_idx[1] += dy[j]
          tank_idx[2] = j
  data[tank_idx[0]][tank_idx[1]] = tank[tank_idx[2]]
  print('#%d' %(t+1),end=' ')
  for i in range(len(data)):
      print(''.join(data[i]))
