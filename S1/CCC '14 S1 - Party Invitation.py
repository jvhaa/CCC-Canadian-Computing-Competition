import sys

friends = [i + 1 for i in range(int(sys.stdin.readlines(1)[0]))]
num = int(sys.stdin.readlines(1)[0])

for i in range(num):
    point = -1
    space = int(sys.stdin.readlines(1)[0])
    while True:
        point += space
        if point >= len(friends):
            break
        friends.pop(point)
        point -= 1

for i in friends:
    print(i)
