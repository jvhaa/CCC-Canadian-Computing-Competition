import sys
f = int(sys.stdin.readlines(1)[0])
s = int(sys.stdin.readlines(1)[0])
t = 0
tt = 0

for i in range(f, s+1):
    t = 0
    for l in range(1, i+1):
        if i % l == 0:
            t += 1
    if t == 4:
        tt += 1


print("The number of RSA numbers between " + str(f) +  " and " + str(s) + " is " + str(tt))
