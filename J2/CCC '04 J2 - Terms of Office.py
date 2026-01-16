import sys

start = int(sys.stdin.readlines(1)[0])
year = int(sys.stdin.readlines(1)[0])

for i in range(start, year+1, 60):
    print("All positions change in year", i, sep = " ")
