import sys

num = int(sys.stdin.readlines(1)[0])
x = []
y = []
dx = 100000000000000000000

for i in range(num):
    data = sys.stdin.readlines(1)[0].strip().split(" ")
    x.append(int(data[0]))
    y.append(int(data[1]))


for i in range(num):
    for l in range(i+1, num):
        xx = max(x[i]- x[l], x[l] - x[i])
        yy = max(y[i]- y[l], y[l] - y[i])
        if dx > xx > yy:
            dx = xx
        elif dx > yy > xx:
            dx = yy
        elif dx > yy == xx:
            if dx > yy:
                dx = yy
print(dx ** 2)
