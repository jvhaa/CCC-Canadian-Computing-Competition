import sys
input = sys.stdin.readline
N = int(input())
heights = list(map(int, input().split()))

vals = [0, 0] + [float('inf') for _ in range(N - 1)]

for i in range(N):
    start, end = i, i + 1
    length = 2
    asym = 0

    while end < N and start >= 0:
        asym += abs(heights[end] - heights[start])
        vals[length] = min(asym, vals[length])
        end += 1
        start -= 1
        length += 2

for i in range(1, N - 2):
    start, end = i, i + 2
    length = 3
    asym = 0

    while end < N and start >= 0:
        asym += abs(heights[end] - heights[start])
        vals[length] = min(asym, vals[length])
        end += 1
        start -= 1
        length += 2

print(*vals[1:])
