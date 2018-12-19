a = 0
c = 10551298
b = 1
while b*b <= c:
  if c % b == 0:
    a += b
    if b*b != c:
      a += c/b
  b += 1
print a
