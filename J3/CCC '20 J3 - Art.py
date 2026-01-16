import sys

xy = [101, 101]
xy2 = [0, 0]

num = int(sys.stdin.readlines(1)[0])

for i in range(num):
    data = sys.stdin.readlines(1)[0].strip().split(",")
    x = int(data[0])
    y = int(data[1])
    if x < xy[0]:
        xy[0] = x
    if y < xy[1]:
        xy[1] = y
    if x > xy2[0]:
        xy2[0] = x
    if y > xy2[1]:
        xy2[1] = y

print(xy[0]-1, ",", xy[1]-1, sep="")
print(xy2[0]+1, ",", xy2[1]+1, sep="")
