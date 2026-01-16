import sys

arr = ["A", "B", "C", "D", "E"]

running = True

while running:
    b = int(sys.stdin.readlines(1)[0].strip())
    n = int(sys.stdin.readlines(1)[0].strip())

    for i in range(n):
        if b == 1:
            arr.append(arr[0])
            arr.pop(0)
        elif b == 2:
            arr.insert(0, arr[4])
            arr.pop(5)
        elif b == 3:
            arr[0], arr[1] = arr[1], arr[0]
        elif b == 4:
            running = False

for i in range(len(arr)):
    print(arr[i], end="")
    print(" ", end="")

print()
