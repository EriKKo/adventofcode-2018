unit = map(ord, raw_input())

def test(forbidden):
  next = [i + 1 for i in range(len(unit))]
  next[-1] = -1
  prev = [i - 1 for i in range(len(unit))]
  alive = [True for c in unit]

  p = 0
  while p >= 0:
    if unit[p] == forbidden or unit[p] == forbidden + 32:
      alive[p] = False
      if prev[p] >= 0:
        next[prev[p]] = next[p]
      if next[p] >= 0:
        prev[next[p]] = prev[p]
      p = prev[p] if prev[p] >= 0 else next[p]
    else:
      b = next[p]
      if b >= 0 and abs(unit[p] - unit[b]) == 32:
        alive[p] = alive[b] = False
        if prev[p] >= 0:
          next[prev[p]] = next[b]
        if next[b] >= 0:
          prev[next[b]] = prev[p]
        p = prev[p] if prev[p] >= 0 else next[b]
      else:
        p = b
  return sum(alive)

print min(map(test, range(65, 91)))
