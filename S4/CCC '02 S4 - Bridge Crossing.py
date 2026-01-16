M = int(input())

names = []
Q = int(input())
times = [0] * (Q+M)
dp = [(float('inf'), 0)] * (Q + M)
for i in range(M):
  dp[i] = (0, dp[i][1])

for i in range(M, Q+M):
    names.append(input().strip())
    times[i] = int(input())
    for start in range(i-M+1, i+1):
      value = max(times[start:i+1]) + dp[start-1][0]
      if dp[i][0] >= value:
        dp[i] = (value, start)

ans = []
temp = []
i = Q+M-1

while names:
  for x in range(i-dp[i][1]+1):
    temp.append(names.pop())
  ans.append(temp)
  temp = []
  i = dp[i][1] - 1
        
print(f"Total Time: {dp[-1][0]}")
          
for name in ans[::-1]:
  print(" ".join(name[::-1]))
