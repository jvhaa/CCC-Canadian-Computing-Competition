import sys

data = sys.stdin.readlines(1)[0].strip()

for i in range(len(data)):
    if data[i] == "+":
        print(" tighten ", end="")
    elif data[i] == "-":
        print(" loosen ", end="")
    elif data[i].isnumeric():
        print(data[i], end="")
    else:
        if data[i-1].isnumeric():
            print()
        print(data[i], end="")
