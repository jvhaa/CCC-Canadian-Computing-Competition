import sys

x = int(sys.stdin.readlines(1)[0])
m = int(sys.stdin.readlines(1)[0])

for i in range(1, m):
    if (i * x) % m == 1:
        print(i)
        break
    if i == m-1 and (i * x) % m != 1:
        print("No such integer exists.")
