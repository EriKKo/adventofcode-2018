import sys,re

class Army:
  def __init__(self, kind, count, hp, ap, at, init, weak, immune):
    self.kind = kind
    self.count = count
    self.hp = hp
    self.ap = ap
    self.at = at
    self.init = init
    self.weak = weak
    self.immune = immune

  def power(self):
    return self.count * self.ap

K = 0
armies = []

def damage(attacker, defender):
  if attacker.kind == defender.kind or defender.count <= 0 or attacker.at in defender.immune:
    return 0
  return attacker.count * attacker.ap * (2 if attacker.at in defender.weak else 1)

for line in sys.stdin:
  line = line.strip()
  if line.startswith("Immun"):
    K = 0
  elif line.startswith("Infec"):
    K = 1
  elif len(line):
    count,hp,ap,init = map(int, re.findall("\d+", line))
    at = re.findall("\S+ damage", line)[0].split()[0]
    special = re.findall("\(.*\)", line)
    weak = []
    immune = []
    if special:  
      special = special[0][1:-1].replace(",","").split(";")
      for s in special:
        spl = s.split()
        if spl[0] == "immune":
          immune = spl[2:]
        else:
          weak = spl[2:]
    armies.append(Army(K,count,hp,ap,at,init,weak,immune))

while True:
  target = {}
  for attacker in sorted(armies, key = lambda army: (-army.power(),-army.init)):
    for defender in sorted(armies, key = lambda army: (-damage(attacker, army),-army.power(),-army.init)):
      if damage(attacker, defender) > 0 and defender not in target.values():
        target[attacker] = defender
        break
  if not target:
    break
  for attacker in sorted(armies, key = lambda army: (-army.init)):
    if attacker.count and attacker in target:
      defender = target[attacker]
      defender.count = max(0, defender.count - damage(attacker, defender) / defender.hp)

print sum(map(lambda army: army.count, armies))
