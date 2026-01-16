import sys
import math

date = [2007, 2, 27]

num = int(sys.stdin.readlines(1)[0])

for i in range(num):
    birth = list(map(int, sys.stdin.readlines(1)[0].strip().split()))
    day = date[2] - birth[2]
    month = math.floor(date[1] - birth[1] + day/31)
    year = math.floor(date[0] - birth[0] + month/12)
    if year >= 18:
        print("Yes")
    else:
        print("No")
