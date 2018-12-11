class Node:
  def __init__(self, score):
    self.score = score
    self.left = self
    self.right = self

  def add(self, node):
    node.right = self.right
    node.left = self
    node.right.left = node
    self.right = node

  def remove(self):
    self.left.right = self.right
    self.right.left = self.left
    return self.right

  def move(self, steps):
    node = self
    if steps < 0:
      for i in range(-steps):
        node = node.left
    else:
      for i in range(steps):
        node = node.right
    return node

pl,_,_,_,_,_,po,_ = raw_input().split()
players = int(pl)
maxPoints = int(po)
points = [0] * players
node = Node(0)
for p in range(1, maxPoints + 1):
  curr = (p - 1) % players
  if p % 23 == 0:
    points[curr] += p
    node = node.move(-7)
    points[curr] += node.score
    node = node.remove()
  else:
    node = node.move(1)
    n2 = Node(p)
    node.add(n2)
    node = n2
print max(points)
