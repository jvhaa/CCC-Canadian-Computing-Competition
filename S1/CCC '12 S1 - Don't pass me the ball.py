import sys
num = int(sys.stdin.readlines(1)[0])

counter = 0

for i in range(1, num-2):
    for l in range(i+1, num-1):
        for k in range(l+1, num):
            counter += 1

print(counter)
