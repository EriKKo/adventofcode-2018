g = int(raw_input())
def power(x, y):
  res = (x + 10) * y + g
  res *= x + 10
  res /= 100
  res %= 10
  return res - 5

best = -100
bestCell = None
for x in range(1, 301):
  for y in range(1, 301):
    s = sum(power(x + i, y + j) for i in range(3) for j in range(3))
    if s > best:
      best = s
      bestCell = (x,y)
print best
print bestCell
