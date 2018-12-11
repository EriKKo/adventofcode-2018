a = map(int, raw_input().split())

def parse(a, index):
  n,m = a[index:index+2]
  index += 2
  res = 0
  for i in range(n):
    score,newIndex = parse(a, index)
    res += score
    index = newIndex
  res += sum(a[index:index+m])
  return (res, index + m)

print parse(a, 0)[0]
