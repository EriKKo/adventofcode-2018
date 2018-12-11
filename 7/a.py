import sys
from queue import PriorityQueue

nodes = set()
countIn = {}
outNodes = {}

def init(k):
  nodes.add(k)
  if k not in outNodes:
    outNodes[k] = []
  if k not in countIn:
    countIn[k] = 0

for line in sys.stdin:
  _,a,_,_,_,_,_,b,_,_ = line.split()
  init(a)
  init(b)
  outNodes[a].append(b)
  countIn[b] += 1

pq = PriorityQueue()
for node in nodes:
  if countIn[node] == 0:
    pq.put(node)

res = ""
while not pq.empty():
  node = pq.get()
  res += node
  for outNode in outNodes[node]:
    countIn[outNode] -= 1
    if countIn[outNode] == 0:
      pq.put(outNode)
print res
