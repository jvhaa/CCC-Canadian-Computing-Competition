import sys
import time

n, m, k = map(int, input().split())

cal = lambda x : (x+1)*x//2

max_sams = cal(min(m, n)) + m * max(0, n-m)

if max_sams < k or n > k:
    print(-1)
    sys.exit()

good_samples = 0
ans = []
dist = 0

for i in range(n):
    good_samples += 1
    if (n-i-1) + good_samples +i <= k and i < m:
        ans.append(i+1)
        good_samples += i
        dist += 1
    else:
        while True:
            if (dist) * (n-i) + good_samples > k:
                dist -= 1
            else:
                break
        ans.append(ans[-dist-1])
        good_samples += dist
print(" ".join(map( str, ans)))
