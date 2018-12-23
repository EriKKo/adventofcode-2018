import sys,re

bots = [map(int, re.findall("-?\d+", line)) for line in sys.stdin]
maxR = max(map(lambda (x,y,z,r): r, bots))
mx,my,mz,mr = next(((x,y,z,r) for x,y,z,r in bots if r == maxR))
print len(filter(lambda (x,y,z,r): abs(mx - x) + abs(my - y) + abs(mz - z) <= mr, bots))
