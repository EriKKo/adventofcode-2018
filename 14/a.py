good = int(raw_input())
nums = [0]*(good + 11)
a,b = 0,1
nums[a] = 3
nums[b] = 7
n = 2
while n < good + 10:
  t = nums[a] + nums[b]
  if t > 9:
    nums[n] = t / 10
    nums[n + 1] = t % 10
    n += 2
  else:
    nums[n] = t
    n += 1
  a = (a + nums[a] + 1) % n
  b = (b + nums[b] + 1) % n
print "".join(map(str,nums[good:good+10]))
