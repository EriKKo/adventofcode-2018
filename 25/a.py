import sys

points = [map(int, line.split(",")) for line in sys.stdin]
v = [-1] * len(points)

def dist(p1, p2):
  return reduce(lambda s,p: s + abs(p[0] - p[1]), zip(p1, p2), 0)

def dfs(p, c, v):
  v[p] = c
  for i in range(len(points)):
    if v[i] == -1 and dist(points[p], points[i]) <= 3:
      dfs(i, c, v)

c = 0
for i in range(len(points)):
  if v[i] == -1:
    dfs(i, c, v)
    c += 1
print c
