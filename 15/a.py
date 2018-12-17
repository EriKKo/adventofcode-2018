import sys
from Queue import PriorityQueue as pq

dr = [-1,0,0,1]
dc = [0,-1,1,0]

def isUnit(cell):
  return cell != '.' and cell != '#'

def getUnits(grid):
  res = []
  for row in grid:
    for cell in row:
      if isUnit(cell):
        res.append(cell)
  return res

def isOver(units, kind, hp):
  teams = set()
  for unit in units:
    if hp[unit] > 0:
      teams.add(kind[unit])
  return len(teams) < 2

def getCoord(grid, unit):
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == unit:
        return r,c

def printGrid(grid, kind):
  for row in grid:
    print "".join(map(lambda c: kind[c] if isUnit(c) else c, row))
  print ""

def bfs(grid, unit):
  startR,startC = getCoord(grid, unit)
  q = pq()
  dist = {}
  prev = {}
  q.put((0, startR, startC))
  dist[(startR,startC)] = 0
  prev[(startR,startC)] = (startR,startC)
  while not q.empty():
    di,r,c = q.get()
    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]
      if isUnit(grid[nr][nc]) and kind[grid[nr][nc]] != kind[grid[startR][startC]]:
        while dist[(r,c)] > 1:
          r,c = prev[(r,c)]
        return r,c
    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]
      if grid[nr][nc] == '.':
        if (nr,nc) not in dist or di + 1 < dist[(nr,nc)]:
          dist[(nr,nc)] = di + 1
          prev[(nr,nc)] = (nr,nc) if di == 0 else prev[(r,c)]
          q.put((di + 1, nr, nc))
        elif di + 1 == dist[(nr,nc)]:
          prev[(nr,nc)] = min(prev[(nr,nc)], prev[(r,c)])
  return startR,startC

g = [[c for c in line.strip()] for line in sys.stdin]
R = len(g)
C = len(g[0])
kind = []
hp = []
for r in range(R):
  for c in range(C):
    if g[r][c] == 'G' or g[r][c] == 'E':
      kind.append(g[r][c])
      hp.append(200)
      g[r][c] = len(kind) - 1

rounds = 0
while True:
  print "Round:", rounds
  printGrid(g, kind)
  print hp
  units = getUnits(g)
  completed = True
  for unit in units:
    if hp[unit] <= 0:
      continue
    if isOver(units, kind, hp):
      completed = False
      break
    enemy = -1
    startR,startC = getCoord(g, unit)
    r,c = bfs(g, unit)
    g[startR][startC] = '.'
    g[r][c] = unit
    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]
      if isUnit(g[nr][nc]):
        otherUnit = g[nr][nc]
        if kind[otherUnit] != kind[unit] and (enemy == -1 or hp[otherUnit] < hp[enemy]):
          enemy = otherUnit
    if enemy != -1:
      hp[enemy] -= 3
      if hp[enemy] <= 0:
        er,ec = getCoord(g, enemy)
        g[er][ec] = '.'
  if not completed:
    break
  rounds += 1
printGrid(g, kind)
hpSum = sum(map(lambda x: x if x > 0 else 0, hp))
score = rounds * hpSum
print score
