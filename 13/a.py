import sys

dx = [0,1,0,-1]
dy = [-1,0,1,0]
dc = "^>v<"

def collision(cars):
  crashed = {}
  for (y,x,_,_) in cars:
    crashed[(x,y)] = (x,y) in crashed
  return filter(lambda coord: crashed[coord], crashed.keys())

grid = [line for line in sys.stdin]

cars = []
for i in range(len(grid)):
  for j in range(len(grid[i])):
    c = grid[i][j]
    if c in dc:
      cars.append((i,j,dc.index(c),0))

while not collision(cars):
  cars.sort()
  for i in range(len(cars)):
    y,x,d,t = cars[i]
    x += dx[d]
    y += dy[d]
    if grid[y][x] == '+':
      d = (d + t - 1) % 4
      t = (t + 1) % 3
    elif grid[y][x] == '/':
      d = (d + (-1 if d % 2 else 1)) % 4
    elif grid[y][x] == '\\':
      d = (d + (1 if d % 2 else -1)) % 4 
    cars[i] = (y,x,d,t)
    if collision(cars):
      break
print ",".join(map(str,collision(cars)[0]))
