import sys
from collections import Counter

input = sys.stdin.readline

height = int(input())
width = int(input())
row = Counter()
col = Counter()

for _ in range(int(input())):
    action, number = input().split()
    number = int(number)
    if action == "R":
        row[number] += 1
    else:
        col[number] += 1

r = sum(1 for count in row.values() if count % 2 != 0)
c = sum(1 for count in col.values() if count % 2 != 0)

ans = width * r + height * c - r * c * 2
print(ans)
