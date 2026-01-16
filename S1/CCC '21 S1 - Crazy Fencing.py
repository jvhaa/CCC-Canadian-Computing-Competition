import sys

num = int(sys.stdin.readlines(1)[0])

height = list(map(int, sys.stdin.readlines(1)[0].strip().split()))
width = list(map(int, sys.stdin.readlines(1)[0].strip().split()))

area = 0

for i in range(num):
    area += (height[i]+height[i+1])/2 * width[i]
    
print(area)
