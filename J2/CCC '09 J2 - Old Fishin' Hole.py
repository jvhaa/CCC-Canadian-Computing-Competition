import sys
import math

b = int(sys.stdin.readlines(1)[0])
n = int(sys.stdin.readlines(1)[0])
y = int(sys.stdin.readlines(1)[0])
total = int(sys.stdin.readlines(1)[0])
c = 0

for i in range(math.floor(total / y) + 1):
    for l in range(math.floor(total / n) + 1):
        for k in range(math.floor(total / b) + 1):
            if total >= (i * y + l * n + k * b) > 0:
                print(k, "Brown Trout,", l, "Northern Pike,", i, "Yellow Pickerel", sep=" ")
                c += 1

print("Number of ways to catch fish:", c, sep=" ")
