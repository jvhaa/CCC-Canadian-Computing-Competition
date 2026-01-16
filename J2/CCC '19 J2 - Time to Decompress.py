import sys

symbols = int(sys.stdin.readlines(1)[0])

for i in range(symbols):
    data = sys.stdin.readlines(1)[0].strip().split(" ")
    times = int(data[0])
    symbol = data[1]
    for i in range(times):
        print(symbol, end="")
    print()
