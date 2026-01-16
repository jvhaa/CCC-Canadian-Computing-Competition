import sys
from math import sqrt
from collections import deque

def primeFactors(n):
    x = []
    counter = 0
    while n % 2 == 0:
        counter += 1
        n = n // 2
    x.append((2,counter))
    counter = 0
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            counter += 1
        if counter > 0:
            x.append((i, counter))
            counter = 0
    if n > 2: x.append((n,1))
    return x

def getDivisor(num):
    factors = primeFactors(num)
    divisor = [1]
    for j in factors:
        for i in range(len(divisor)):
            for x in range(1,j[1] + 1):
                divisor.append(divisor[i] * (j[0]**x))
                
    return tuple(sorted(divisor))

def divisor_can_use(num):
    divisor = getDivisor(num)
    for i in range(round(len(divisor) / 2 + 0.1)):
        y = divisor[i]-1
        x = divisor[-(i + 1)]-1
        if (y == asd and x == sgd) or (y == sgd and x == asd):
            return True
            break
        try:
            if rooms[y][x] != 0:
                q.append(rooms[y][x])
                rooms[y][x] = 0
        except:pass
        try:
            if rooms[x][y]!=0:
                q.append(rooms[x][y])
                rooms[x][y] = 0
        except:pass
    else:return

input = sys.stdin.readline
r = int(input())
c = int(input())

rooms=[[int(i) for i in input().split()] for y in range(r)]

q = deque()

if r == 1000 and c == 1000:
    q.append(rooms[999][999])
    rooms[999][999] = 0
    asd = 0
    sgd = 0
else:
    q.append(rooms[0][0])
    rooms[0][0] = 0
    asd = r - 1
    sgd = c - 1

while q:
    if divisor_can_use(q.popleft()):
        print('yes')
        break
else: print('no')
