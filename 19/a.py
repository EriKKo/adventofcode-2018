import sys

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

opf = {
  'addr': addr,
  'addi': addi,
  'mulr': mulr,
  'muli': muli,
  'banr': banr,
  'bani': bani,
  'borr': borr,
  'bori': bori,
  'setr': setr,
  'seti': seti,
  'gtir': gtir,
  'gtri': gtri,
  'gtrr': gtrr,
  'eqir': eqir,
  'eqri': eqri,
  'eqrr': eqrr
}

lines = [line.strip().split() for line in sys.stdin]
ip = int(lines[0][1])
ops = map(lambda (o,a,b,c): (o,int(a),int(b),int(c)), lines[1:])
regs = [0]*6
while regs[ip] >= 0 and regs[ip] < len(ops):
  op,a,b,c = ops[regs[ip]]
  opf[op](regs, a, b, c)
  regs[ip] += 1
print regs[0]
