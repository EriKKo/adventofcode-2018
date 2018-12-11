g = int(raw_input())
def power(x, y):
  if x == 0 or y == 0:
    return 0
  res = (x + 10) * y + g
  res *= x + 10
  res /= 100
  res %= 10
  return res - 5

p = [[power(x,y) for x in range(301)] for y in range(301)]
acc = [[0] * 301 for i in range(301)]
for i in range(1, 301):
  for j in range(1, 301):
    acc[i][j] = p[i][j] + acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1]
best = -100
bestCell = None
for x in range(1, 301):
  for y in range(1, 301):
    for l in range(min(301-x, 301-y)):
      s = acc[x+l][y+l] - acc[x-1][y+l] - acc[x+l][y-1] + acc[x-1][y-1]
      if s > best:
        best = s
        bestCell = (y,x,l+1)
print best
print ",".join(map(str,bestCell))
