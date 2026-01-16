from collections import deque
import sys
input = sys.stdin.readline
for i in range(int(input())):
  carts = [int(input()) for i in range(int(input()))]
  start = 1
  lake = deque()

  for cart in reversed(carts):
      if cart == start:
          start += 1
      else:
          lake.append(cart)
      while len(lake) > 0:
          if lake[-1] == start:
            start += 1
            lake.pop()
          else:
            break
  if len(lake) == 0:
      print("Y")
  else:
      print("N")
