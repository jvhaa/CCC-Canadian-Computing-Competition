import math

start = int(input())
end = int(input())

realstart = math.ceil(start**(1/3))
realend = math.floor(end**(1/3)) + 2
ans = 0
for i in range(realstart, realend):
    cool = i **(3/2)
    if cool == round(cool):
        ans += 1
        
print(ans)
