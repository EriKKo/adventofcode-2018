from u import *
l = rf()
n = 0
m = {}
m[0]= True
t = True
while t:
  for a in l:
    if a[0] == '+':
      n += int(a[1:])
    else:
      n -= int(a[1:])
    if n in m:
      print n
      t = False
      break
    m[n] = True
