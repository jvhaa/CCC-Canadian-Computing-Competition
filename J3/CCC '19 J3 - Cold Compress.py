import sys

num = int(sys.stdin.readlines(1)[0])

for i in range(num):
    text = sys.stdin.readlines(1)[0].strip() + " "
    symbol = text[0]
    total = 0
    for l in range(len(text)):
        if symbol == text[l]:
            total += 1
        else:
            print(total, symbol, "", end=" ")
            total = 1
            symbol = text[l]

    print()
