from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**10000
cells = {}

for row in "ABCDEFGHIJ":
  line = input().split()
  for col, cell in zip(range(1, 10), line):
    cells[row + str(col)] = cell.split("+")

def path(c, visited=set()):
  ans = 0
  for cell in c:
    if cell in visited or cell == "*":
      return False
    if cell in memo:
      ans += memo[cell]
    elif cell[0].isalpha():
      e = path(cells[cell], visited | set([cell]))
      if e == False:
        return False
      else:
        memo[cell] = int(e)
        ans += int(e)
    else:
      memo[cell] = int(cell)
      ans += int(cell)
  return str(ans)

memo = {}

for cell, value in cells.items():
  ans = path(value)
  if ans == False:
    cells[cell] = "*"
  else:
    cells[cell] = [ans]
    if cell not in memo:
      memo[cell] = int(ans)


row = "A"
for cell, value in cells.items():
  if cell[0] == row:
    print(*value, end = " ")
  else:
    print()
    print(*value, end = " ")
    row = cell[0]
