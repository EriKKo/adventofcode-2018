import sys

point = [map(int, l.split(", ")) for l in sys.stdin]
minX = min(map(lambda x: x[0], point))
maxX = max(map(lambda x: x[0], point))
minY = min(map(lambda x: x[1], point))
maxY = max(map(lambda x: x[1], point))

c = 0
for x in range(minX, maxX + 1):
  for y in range(minY, maxY + 1):
    dist = sum(map(lambda (px,py): abs(px - x) + abs(py - y), point))
    if dist < 10000:
      c += 1
print c
