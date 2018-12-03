def r():
  return raw_input().strip()

def ra():
  return r().split()

def ri():
  return int(r())

def ria():
  return map(int, ra())

def rf():
  return map(lambda s: s.strip(), open("in").readlines())

def pa(a):
  print " ".join(map(str, a))
