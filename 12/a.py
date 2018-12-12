import sys
lines = [l.strip() for l in sys.stdin]
s = lines[0].split()[2]
m = {}
for i in range(len(s)):
  if s[i] == '#':
    m[i] = True
trans = {}
for l in lines[2:]:
  a,b = l.split(" => ")
  trans[a] = b == "#"

def simulate(state):
  start = min(state.keys()) - 2
  end = max(state.keys()) + 2
  newState = {}
  for i in range(start, end + 1):
    s = ""
    for j in range(i - 2, i + 3):
      s += "#" if j in state else "."
    if s in trans and trans[s]:
      newState[i] = True
  return newState

def score(state):
  return sum(state.keys())

for i in range(20):
  m = simulate(m)

print sum(m.keys())
