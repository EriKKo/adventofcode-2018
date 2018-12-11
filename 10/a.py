import sys,re,time
points = [map(int, re.findall("-?\d+", s)) for s in sys.stdin]
print points

def pp():
  x = map(lambda p: p[0], points)
  y = map(lambda p: p[1], points)
  minX = min(x)
  maxX = max(x)
  minY = min(y)
  maxY = max(y)
  w = maxX - minX + 1
  h = maxY - minY + 1
  print w, h
  if w > 100 or h > 100:
    return False
  s = [['.'] * (maxX - minX + 1) for i in range(maxY - minY + 1)]
  for i in range(len(x)):
    s[y[i] - minY][x[i] - minX] = '#'
  for line in s:
    print "".join(line)
  print ""
  return True

def update():
  for p in points:
    p[0] += p[2]
    p[1] += p[3]

while True:
  if pp():
    time.sleep(0.3)
  update()
