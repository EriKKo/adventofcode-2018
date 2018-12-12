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

def hash(state):
  s = ""
  for i in range(min(state.keys()), max(state.keys()) + 1):
    s += "#" if i in state else "."
  return s

def score(state):
  return sum(state.keys())

cc = 50000000000
prevHash = hash(m)
prevMin = min(m.keys())
while cc:
  cc -= 1
  m = simulate(m)
  currHash = hash(m)
  currMin = min(m.keys())
  if currHash == prevHash:
    break
  prevHash = currHash
  prevMin = currMin

finalScore = score(m) + cc * (currMin - prevMin) * len(m)
print finalScore
