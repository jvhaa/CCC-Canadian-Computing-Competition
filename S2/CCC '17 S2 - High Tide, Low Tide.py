import math

num = int(input())

tides = list(sorted(map(int, input().split())))
low = tides[:math.ceil(len(tides)/2)][::-1]
high = tides[math.ceil(len(tides)/2):]

answer = []

for i in range(len(high)):
  answer.append(low[i])
  answer.append(high[i])

if len(low) != len(high):
  answer.append(low[-1])

print(" ".join(map(str, answer)))
