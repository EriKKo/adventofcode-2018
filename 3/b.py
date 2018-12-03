import re,sys
d = [[int(t) for t in re.sub("[:,x]"," ", l).split() if t.isdigit()] for l in sys.stdin]
g = {}
for [x,y,w,h] in d:
  for i in range(x, x + w):
    for j in range(y, y + h):
      g[(i,j)] = (i,j) in g
for n,[x,y,w,h] in enumerate(d):
  if all(map(lambda x: not g[x], [(i,j) for j in range(y, y + h) for i in range(x, x + w)])):
    print n + 1
