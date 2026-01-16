row = int(input())
col = int(input())
num = int(input())

prev = [0] * col 
curr = [0] * col  

for y in range(row):
    for x in range(col):
        curr[x] = prev[x]
        if x > 0:
            curr[x] = min(curr[x], prev[x - 1])
        if x < col - 1:
            curr[x] = min(curr[x], prev[x + 1])
        
        curr[x] += (y * col + x) % num + 1
    
    prev, curr = curr, prev

print(min(prev))
