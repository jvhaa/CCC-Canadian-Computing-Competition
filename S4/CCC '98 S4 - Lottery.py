import sys
input = sys.stdin.readline
tests = int(input())
for l in range(tests):
  n = input().split()
  delay = 0
  equation = " ".join(n)
  ass = equation.count("+") + equation.count("-")
  mul = equation.count("X")
  ez = 1 if ass == 0 else 0
  for i in range(mul-ez):
    start = 0
    for i in range(start, len(n)):
      if n[i] == "X":
        e = "(" + " ".join(n[i-1:i+2]) + ")"
        n = n[:i-1] + [e] + n[i+2:]
        start = i
        break
  start = 0
  for e in range(equation.count("+") + equation.count("-")-1):
    for i in range(start, len(n)):
      if n[i] == "-" or n[i] == "+":
        e = "(" + " ".join(n[i-1:i+2]) + ")"
        n = n[:i-1] + [e] + n[i+2:]
        start = i
        break
  print(" ".join(n))
  if l != tests-1:
      print()
