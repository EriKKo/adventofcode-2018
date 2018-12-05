unit = map(ord, raw_input())
next = [i + 1 for i in range(len(unit))]
next[-1] = -1
prev = [i - 1 for i in range(len(unit))]
alive = [True for c in unit]

p = 0
while next[p] >= 0:
  b = next[p]
  if abs(unit[p] - unit[b]) == 32:
    alive[p] = alive[b] = False
    if prev[p] >= 0:
      next[prev[p]] = next[b]
    if next[b] >= 0:
      prev[next[b]] = prev[p]
    p = prev[p] if prev[p] >= 0 else next[b]
  else:
    p = b

print sum(alive)
