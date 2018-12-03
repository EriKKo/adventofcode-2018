import re,sys
g = {}
for _,x,y,w,h in [map(int, re.findall("\d+", l)) for l in sys.stdin]:
  for i in range(x, x + w):
    for j in range(y, y + h):
      g[(i,j)] = (i,j) in g
print sum(g.values())
