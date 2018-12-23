import re

M = 20183
parse = lambda: map(int, re.findall("\d+", raw_input()))
depth = parse()[0]
targetX, targetY = parse()

erosion = [[0] * (targetX + 1) for i in range(targetY + 1)]
res = 0
for y in range(targetY + 1):
  for x in range(targetX + 1):
    if x == 0:
      erosion[y][x] = y * 48271 % M
    elif y == 0:
      erosion[y][x] = x * 16807 % M
    else:
      erosion[y][x] = erosion[y-1][x] * erosion[y][x-1] % M
    if x == targetX and y == targetY:
      erosion[y][x] = 0
    erosion[y][x] = (erosion[y][x] + depth) % M
    res += erosion[y][x] % 3
  #print "".join(map(lambda x: ".=|"[x%3], erosion[y]))
print res
