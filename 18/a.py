import sys

def count(g, r1, c1, r2, c2):
  counts = {'.': 0, '|': 0, '#': 0}
  for r in range(r1, r2):
    for c in range(c1, c2):
      if r >= 0 and r < len(g) and c >= 0 and c < len(g[r]):
        counts[g[r][c]] += 1
  return counts

def tick(g):
  g2 = [[c for c in row] for row in g]
  for i in range(len(g)):
    for j in range(len(g[i])):
      counts = count(g, i-1, j-1, i+2, j+2)
      counts[g[i][j]] -= 1
      if g[i][j] == '.':
        g2[i][j] = '|' if counts['|'] >= 3 else '.'
      elif g[i][j] == '|':
        g2[i][j] = '#' if counts['#'] >= 3 else '|'
      else:
        g2[i][j] = '#' if counts['|'] and counts['#'] else '.'
  return g2

def p(g):
  for row in g:
    print "".join(row)
  print ""

g = [[c for c in line.strip()] for line in sys.stdin]
for i in range(10):
  p(g)
  g = tick(g)
p(g)
counts = count(g, 0, 0, len(g), len(g[0]))
print counts['|'] * counts['#']
