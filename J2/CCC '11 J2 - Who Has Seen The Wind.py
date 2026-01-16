import sys

h = int(sys.stdin.readlines(1)[0])
t = int(sys.stdin.readlines(1)[0])

for i in range(1, t+1):
    if (-6 * i ** 4) + (h * i**3) + (2 * i ** 2) + i <= 0:
        print("The balloon first touches ground at hour:")
        print(i)
        break
    elif i == t:
        print("The balloon does not touch ground in the given time.")
