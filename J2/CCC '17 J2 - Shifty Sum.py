import sys
base = int(sys.stdin.readlines(1)[0])
exponent = int(sys.stdin.readlines(1)[0])
answer = 0

for i in range(exponent+1):
    answer += base * 10**i
    
print(answer)
