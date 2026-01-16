import sys

cars = int(sys.stdin.readlines(1)[0])
y = str((sys.stdin.readlines(1)[0])).strip()
t = str((sys.stdin.readlines(1)[0])).strip()

total = 0

for i in range(cars):
    if y[i] == t[i] == "C":
        total += 1

print(total)
