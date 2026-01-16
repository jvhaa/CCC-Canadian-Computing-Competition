import sys

a = int(sys.stdin.readlines(1)[0])
b = int(sys.stdin.readlines(1)[0])
c = int(sys.stdin.readlines(1)[0])
d = int(sys.stdin.readlines(1)[0])
steps = int(sys.stdin.readlines(1)[0])

nikky = 0
byron = 0

n = 0

while n < steps:
    for i in range(a):
        if n < steps:
            nikky += 1
            n += 1
    for i in range(b):
        if n < steps:
            nikky -= 1
            n += 1

n = 0

while n < steps:
    for i in range(c):
        if n < steps:
            byron += 1
            n += 1
    for i in range(d):
        if n < steps:
            byron -= 1
            n += 1
            
if abs(byron) > abs(nikky):
    print("Byron")
elif abs(byron) < abs(nikky):
    print("Nikky")
else:
    print("Tied")
