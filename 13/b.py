import sys

dx = [0,1,0,-1]
dy = [-1,0,1,0]
dc = "^>v<"

grid = [line for line in sys.stdin]

cars = []
for i in range(len(grid)):
  for j in range(len(grid[i])):
    c = grid[i][j]
    if c in dc:
      cars.append((i,j,dc.index(c),0))

while len(cars) > 1:
  cars.sort()
  i = 0
  while i < len(cars):
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
    collided = filter(lambda index: cars[index][:2] == cars[i][:2], range(len(cars)))
    if len(collided) > 1:
      for index in reversed(collided):
        cars.pop(index)
        if index <= i:
          i -= 1
    i += 1
endY,endX,_,_ = cars[0]
print ",".join(map(str, [endX, endY]))
