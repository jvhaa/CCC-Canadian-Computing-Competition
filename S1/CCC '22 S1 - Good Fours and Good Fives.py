import math

num = int(input())

for i in range(num//4, -1, -1):
    if (num - (i * 4)) % 5 == 0:
        fours = i
        break
    if i == 0:
        fours = -5
        
print(1 + math.floor(fours/5))
