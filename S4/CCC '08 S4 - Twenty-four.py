import sys
input = sys.stdin.readline

a = lambda a,b : a+b
s = lambda a,b : a-b
m = lambda a,b : a*b
d = lambda a,b : a/b if b != 0 and a % b == 0 else -666

operation = [a, s, m, d]

def random(varible):
  perm = []
  for i in range(4):
    for l in range(4):
      if l != i:
        for k in range(4):
          if k not in [i, l]:
            for j in range(4):
              if j not in [i, l, k]:
                perm.append([varible[i], varible[l], varible[k], varible[j]])
  return perm

def thing(a, b, c, d):
  e = []
  for op1 in operation:
    for op2 in operation:
      for op3 in operation:
        e.append(op3(op1(a, b), op2(c, d)))
        e.append(op3(op2(op1(a, b), c), d))
  return e

for deck in range(int(input())):
  ans = 0
  a, b, c, d = int(input()), int(input()), int(input()), int(input())
  arr = random([a, b, c, d])
  for e, f, g, h in arr:
    d = thing(e, f, g, h)
    for number in d:
      if number == 24:
        ans = 24
        break
      if ans < number < 24:
        ans = number
    if ans == 24:
      break
  print(ans)
