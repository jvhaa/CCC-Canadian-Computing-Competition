MAX_MIN = int(input())

riders = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b) if MAX_MIN == 1 else sorted(b, reverse=True)

answer = 0
for ridera, riderb in zip(a, b):
    answer += max(ridera, riderb)

print(answer)
