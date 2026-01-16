import sys

length = int(sys.stdin.readlines(1)[0])

Swifts = list(map(int, sys.stdin.readlines(1)[0].strip().split()))
Semaphores = list(map(int, sys.stdin.readlines(1)[0].strip().split()))

k = 0
swift = 0
sem = 0

for i in range(1, length + 1):
    swift += Swifts[i - 1]
    sem += Semaphores[i - 1]
    if swift == sem:
        k = i

print(k)
