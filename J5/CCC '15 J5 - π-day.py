pie, ppl = int(input()), int(input())
memo = {}

def solve(ppl, pie, maxx):
  if ppl == 0 == pie:
    return 1
  if ppl < 0:
    return 0
  if (ppl, pie, maxx) in memo: return memo[(ppl, pie, maxx)]
  ans = 0
  for i in range(1, maxx+1):
    if pie-i > -1:
      ans += solve(ppl-1, pie-i, i)
  memo[(ppl, pie, maxx)] = ans
  return ans
print(solve(ppl, pie, pie))
