import sys
from queue import PriorityQueue

WORKERS = 5
TIME = 60
nodes = set()
countIn = {}
outNodes = {}

def time(k):
  return ord(k) - 64 + TIME

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

events = PriorityQueue()
events.put((0,""))

res = ""
workers = WORKERS
while not events.empty():
  (t,e) = events.get()
  if e in nodes:
    workers += 1
    res += e
    for outNode in outNodes[e]:
      countIn[outNode] -= 1
      if countIn[outNode] == 0:
        pq.put(outNode)
    if pq.empty() and events.empty():
      print t
  while workers and not pq.empty():
    workers -= 1
    node = pq.get()
    events.put((t + time(node), node))
print res
