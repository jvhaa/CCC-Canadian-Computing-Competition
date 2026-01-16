import sys

x, y = map(int, sys.stdin.readlines(1)[0].split(" "))
x2, y2 = map(int, sys.stdin.readlines(1)[0].split(" "))
t = int(sys.stdin.readlines(1)[0])

distance = abs(x-x2) + abs(y-y2)

if t < distance:
    print("N")
elif (t - distance) % 2 == 0:
    print("Y")
else:
    print("N")
