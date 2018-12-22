a = 0
b = 0
d = 0
e = 0
f = 0

e = 123
while True:
  e &= 456
  if e == 72:
    break
e = 0
#6
while True:
  d = e | 65536
  e = 10283511
  #8
  while True:
    b = d & 255
    e += b
    e &= 16777215
    e *= 65899
    e &= 16777215
    if 256 > d:
      break
    #17
    b = 0
    while True:
      f = b + 1
      f *= 256
      if f > d:
        break
      b += 1  
    #26
    d = b
  #28
  print e
  break
