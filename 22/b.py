import re
from Queue import PriorityQueue

dx = [0,1,0,-1]
dy = [1,0,-1,0]
M = 20183
parse = lambda: map(int, re.findall("\d+", raw_input()))
depth = parse()[0]
targetX, targetY = parse()

class Cave():
  def __init__(self, depth, target):
    self.depth = depth
    self.target = target
    self.eros = {}

  def erosion(self, x, y):
    if (x,y) in self.eros:
      return self.eros[(x,y)]
    if (x,y) == self.target:
      return 0
    if x == 0:
      res = y * 48271 % M
    elif y == 0:
      res = x * 16807 % M
    else:
      res = self.erosion(x-1, y) * self.erosion(x, y-1) % M
    self.eros[(x,y)] = (res + self.depth) % M
    return self.eros[(x,y)]

  def terrain(self, x, y):
    return self.erosion(x,y) % 3

dist = {}
q = PriorityQueue()
q.put((0,1,0,0))
cave = Cave(depth, (targetX, targetY))
while not q.empty():
  d,tool,x,y = q.get()
  if tool == 1 and x == targetX and y == targetY:
    print d
    break
  terrain = cave.terrain(x,y)
  nTool = terrain ^ tool ^ 3
  if (nTool,x,y) not in dist or d + 7 < dist[(nTool,x,y)]:
    dist[(nTool,x,y)] = d + 7
    q.put((d + 7,nTool,x,y))
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and ny > 0 and cave.terrain(nx,ny) != tool:
      if (tool,nx,ny) not in dist or d + 1 < dist[(tool,nx,ny)]:
        dist[(tool,nx,ny)] = d + 1
        q.put((d+1,tool,nx,ny))
