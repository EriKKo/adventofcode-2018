import sys,re,Queue


def parseLine(line):
  tmp = map(int,re.findall("\d+", line))
  if line[0] == 'x':
    return tmp[1],tmp[2],tmp[0],tmp[0]
  else:
    return tmp[0],tmp[0],tmp[1],tmp[2]

clay = [parseLine(line) for line in sys.stdin]
minX = min(map(lambda (y1,y2,x1,x2): x1, clay)) - 1
maxX = max(map(lambda (y1,y2,x1,x2): x2, clay)) + 1
minY = min(map(lambda (y1,y2,x1,x2): y1, clay))
maxY = max(map(lambda (y1,y2,x1,x2): y2, clay))
grid = [['.' for i in range(maxX - minX + 1)] for j in range(maxY - minY + 1)]
for y1,y2,x1,x2 in clay:
  for y in range(y1, y2 + 1):
    for x in range(x1, x2 + 1):
      grid[y - minY][x - minX] = '#'

def isSolid(grid, y, x):
  return y < len(grid) and (grid[y][x] == '#' or grid[y][x] == '~')

def isFree(grid, y, x):
  return y < len(grid) and grid[y][x] == '.'

def fillRow(grid, y, x):
  l = x
  r = x
  while l >= 0 and grid[y][l] == '|':
    l -= 1
  while r < len(grid[y]) and grid[y][r] == '|':
    r += 1
  if l >= 0 and grid[y][l] == '#' and r < len(grid[y]) and grid[y][r] == '#':
    for i in range(l + 1, r):
      grid[y][i] = '~'

def dfs(grid, startY, startX):
  q = Queue.deque()
  q.appendleft((startY,startX))
  while len(q):
    y,x = q.popleft()
    if grid[y][x] == '|':
      if isSolid(grid, y+1, x):
        if isFree(grid, y, x-1) or isFree(grid, y, x+1):
          q.appendleft((y,x))
          if isFree(grid, y, x-1):
            q.appendleft((y,x-1))
          if isFree(grid, y, x+1):
            q.appendleft((y,x+1))
        elif isSolid(grid, y, x-1) or isSolid(grid, y, x+1):
          fillRow(grid, y, x)
    elif grid[y][x] == '.':
      grid[y][x] = '|'
      q.appendleft((y,x))
      if isFree(grid, y+1, x):
        q.appendleft((y+1,x))

dfs(grid, 0, 500 - minX)
count = 0
for row in grid:
  for cell in row:
    if cell == '~':
      count += 1
  print "".join(row)
print count
