import sys
scale = int(sys.stdin.readlines(1)[0])

symbol = ["*x*", " xx", "* *"]

for i in range(3):
    for l in range(scale):
        for k in range(len(symbol[i])):
            print(symbol[i][k]*scale, end = "")
        print()
