import sys

num = int(sys.stdin.readlines(1)[0])

cope = [0]

for i in range(num):
    answer = int(sys.stdin.readlines(1)[0])
    if answer == 0:
        cope.pop()
    else:
        cope.append(answer)

print(sum(cope))
