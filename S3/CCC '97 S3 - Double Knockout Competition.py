import sys
import math
input = sys.stdin.readline

test = int(input())

for t in range(test):
  undefeated = int(input())
  one_l = 0
  elim = 0
  round = 0
  while True: 
    print(f"Round {round}: {undefeated} undefeated, {one_l} one-loss, {elim} eliminated")

    if undefeated == 0 and one_l == 1:
      break
    elif undefeated == 1 and one_l == 1:
      one_l = 2
      undefeated = 0
    else:
      un_one = math.floor(undefeated/2)
      one_elim = math.floor(one_l/2)
      undefeated -= un_one
      one_l += un_one - one_elim
      elim += one_elim
    round += 1
  print(f"There are {round} rounds.")
  if t != test-1:
    print()
