import math
while True:
  radius = int(input())
  if radius == 0:
    break
  answer = 0
  for x in range(-1*radius, radius+1):
    answer += math.floor((radius**2-x**2 )**0.5)*2 + 1
  print(answer)
