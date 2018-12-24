import sys
from collections import deque

sys.setrecursionlimit(1500)

dr = [-1,0,1,0]
dc = [0,1,0,-1]
direction = "NESW"

path = raw_input().strip()[1:-1]
split = [[[]]]
graph = split[-1]
for c in path:
  if c == '(':
    split.append([[]])
    split[-2][-1].append(split[-1])
  elif c == '|':
    split[-1].append([])
  elif c == ')':
    split.pop()
  else:
    split[-1][-1].append(c)

edges = {}

def addEdge(r, c, d):
  if (r,c) not in edges:
    edges[(r,c)] = set()
  edges[(r,c)].add(d)

def edge(r, c, d):
  i = direction.index(d)
  r2 = r + dr[i]
  c2 = c + dc[i]
  addEdge(r, c, i)
  addEdge(r2, c2, (i + 2) % 4)
  return r2,c2

def traverse2(r, c, l, f):
  res = set([(r,c)])
  for subpath in l:
    res = reduce(lambda s1,s2: s1.union(s2), map(lambda (pr,pc): set(f(subpath, pr, pc)), res))
  return res

def traverse(g, r, c):
  if type(g) == str:
    return [edge(r, c, g)]
  res = map(lambda x: traverse2(r, c, x, traverse), g)
  res = [item for sublist in res for item in sublist]
  return res 

traverse(graph, 0, 0)
dist = {}
dist[(0,0)] = 0
q = deque()
q.append((0,0))
while len(q):
  r,c = q.popleft()
  for i in edges[(r,c)]:
    r2 = r + dr[i]
    c2 = c + dc[i]
    if (r2,c2) not in dist:
      dist[(r2,c2)] = dist[(r,c)] + 1
      q.append((r2,c2))
print len(filter(lambda x: x >= 1000, dist.values()))
