import sys

f = int(sys.stdin.readlines(1)[0])
s = int(sys.stdin.readlines(1)[0])
total = 0

for i in range(f):
    for l in range(s):
        if i + l + 2 == 10:
            total += 1
if total == 1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are " + str(total) + " ways to get the sum 10.")
