a = map(int, raw_input().split())

def parse(a, index):
  n,m = a[index:index+2]
  index += 2
  res = 0
  child = [0]*n
  for i in range(n):
    score,newIndex = parse(a, index)
    child[i] = score
    index = newIndex
  if n:
    for i in range(m):
      x = a[index + i]
      if x >= 1 and x <= n:
        res += child[x - 1]
  else:
    res += sum(a[index:index+m])
  return (res, index + m)

print parse(a, 0)[0]
