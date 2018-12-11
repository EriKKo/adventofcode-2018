import sys

point = [map(int, l.split(", ")) for l in sys.stdin]
minX = min(map(lambda x: x[0], point))
maxX = max(map(lambda x: x[0], point))
minY = min(map(lambda x: x[1], point))
maxY = max(map(lambda x: x[1], point))

def onEdge((x,y)):
  return x == minX or x == maxX or y == minY or y == maxY

bad = {index: False for index in range(len(point))}
counts = {index: 0 for index in range(len(point))}
for x in range(minX, maxX + 1):
  for y in range(minY, maxY + 1):
    dist = map(lambda (px,py): abs(x - px) + abs(y - py), point)
    minPoints = filter(lambda i: dist[i] == min(dist), range(len(dist)))
    if len(minPoints) == 1:
      if onEdge((x,y)):
        bad[minPoints[0]] = True
      counts[minPoints[0]] += 1
print max(map(lambda index: 0 if bad[index] else counts[index], range(len(point))))
