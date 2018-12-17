import sys,re

def addr(regs, a, b, c):
  regs[c] = regs[a] + regs[b]

def addi(regs, a, b, c):
  regs[c] = regs[a] + b

def mulr(regs, a, b, c):
  regs[c] = regs[a] * regs[b]

def muli(regs, a, b, c):
  regs[c] = regs[a] * b

def banr(regs, a, b, c):
  regs[c] = regs[a] & regs[b]

def bani(regs, a, b, c):
  regs[c] = regs[a] & b

def borr(regs, a, b, c):
  regs[c] = regs[a] | regs[b]

def bori(regs, a, b, c):
  regs[c] = regs[a] | b

def setr(regs, a, b, c):
  regs[c] = regs[a]

def seti(regs, a, b, c):
  regs[c] = a

def gtir(regs, a, b, c):
  regs[c] = 1 if a > regs[b] else 0

def gtri(regs, a, b, c):
  regs[c] = 1 if regs[a] > b else 0

def gtrr(regs, a, b, c):
  regs[c] = 1 if regs[a] > regs[b] else 0

def eqir(regs, a, b, c):
  regs[c] = 1 if a == regs[b] else 0

def eqri(regs, a, b, c):
  regs[c] = 1 if regs[a] == b else 0

def eqrr(regs, a, b, c):
  regs[c] = 1 if regs[a] == regs[b] else 0

def test(op, a, b, c, before, after):
  regs = [n for n in before]
  op(regs, a, b, c)
  return regs == after

opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
opmapping = [[i for i in range(len(opcodes))] for j in range(len(opcodes))]

before = []
after = []
ops = []
for line in sys.stdin:
  nums = map(int, re.findall("\d+", line))
  if not nums:
    continue
  if line.startswith("Before"):
    before.append(nums)
  elif line.startswith("After"):
    after.append(nums)
  else:
    ops.append(nums)

for i in range(len(before)):
  o,a,b,c = ops[i]
  opmapping[o] = filter(lambda index: test(opcodes[index], a, b, c, before[i], after[i]), opmapping[o])
while sum(map(len, opmapping)) > len(opcodes):
  for i in range(len(opcodes)):
    if len(opmapping[i]) == 1:
      for j in range(len(opcodes)):
        if i != j and opmapping[i][0] in opmapping[j]:
          opmapping[j].remove(opmapping[i][0])
opmapping = map(lambda l: opcodes[l[0]], opmapping)
regs = [0]*4
for o,a,b,c in ops[len(before):]:
  opmapping[o](regs, a, b, c)
print regs[0]
