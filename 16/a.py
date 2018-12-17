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

res = 0
for i in range(len(before)):
  o,a,b,c = ops[i]
  if len(filter(lambda op: test(op, a, b, c, before[i], after[i]), opcodes)) >= 3:
    res += 1
print res
