import sys
input = sys.stdin.readline

points=[]
for i in range(int(input())):
  points.append(int(input()))

points = sorted(points, reverse=True)

mode = [0]*76
point = points[0]
gold = points[0]
silver = None
bronze = None
for i in points:
  if point == i:
    mode[i] += 1
  else:
    point = i
    if silver == None:
      silver = i
      mode[i] = 1
    elif bronze == None:
      bronze = i
      mode[i] = 1
    else:
      break
print(f"{bronze} {mode[bronze]}")
