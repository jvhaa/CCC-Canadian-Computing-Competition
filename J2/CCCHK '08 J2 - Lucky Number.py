import sys

num = int(sys.stdin.readlines(1)[0])

for i in range(num):
    e = str(sys.stdin.readlines(1)[0].strip())
    while int(e) > 9:
        l = 0
        for i in range(len(e)):
            l += int(str(e[i]))
        e = str(l)
    print(e)
