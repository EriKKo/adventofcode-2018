good = raw_input()

def done(nums, index):
  return good == "".join(map(str, nums[index - len(good):index]))

nums = [0]*(100000)
a,b = 0,1
nums[a] = 3
nums[b] = 7
n = 2
while True:
  if n + 2 > len(nums):
    nums = nums + [0]*len(nums)
  t = nums[a] + nums[b]
  if t > 9:
    nums[n] = t / 10
    nums[n + 1] = t % 10
    n += 2
  else:
    nums[n] = t
    n += 1
  if done(nums, n-1) or done(nums, n):
    break
  a = (a + nums[a] + 1) % n
  b = (b + nums[b] + 1) % n
print (n if done(nums, n) else n-1) - len(good)
