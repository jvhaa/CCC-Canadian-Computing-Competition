import sys

data = sys.stdin.readlines(1)[0].strip()
L = data.count("L")
M = data.count("M")
S = data.count("S")

sm = sl = ml = ms = ls = lm = 0
total = 0

for i in range(L):
    if data[i] == "S":
        sl += 1
    if data[i] == "M":
        ml += 1
    
for i in range(M):
    if data[i+L] == "S":
        sm += 1
    if data[i+L] == "L":
        lm += 1

for i in range(S):
    if data[i+L+M] == "L":
        ls += 1
    if data[i+L+M] == "M":
        ms += 1
        
x = min(sl, ls)
sl -= x
ls -= x
total += x
x = min(ml, lm)
ml -= x
lm -= x
total += x
x = min(sm, ms)
sm -= x
ms -= x
total += x

print(total + (sm + ms + ml + lm + sl + ls)//3*2)
