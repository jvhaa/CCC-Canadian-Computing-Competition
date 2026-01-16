import sys
from heapq import heappush, heappop
iput = sys.stdin.readline
n, m, q = map(int, input().split())
c, p, pen, ans = [0]*(n+1), [0]*(n+1), [[] for i in range(m+1)], 0
for i in range(1, n+1):
    c[i], p[i] = map(int, input().split())
    heappush(pen[c[i]], (-p[i], i))
mx, mx2 = [], []

def getColorMax(color):
    while pen[color]:
        val, idx = pen[color][0]
        if c[idx] != color or p[idx] != -val:
            heappop(pen[color])
        else:
            return val, idx
    return 0, -1

def getColor2ndMax(color):
    val, idx = getColorMax(color)
    heappop(pen[color])
    while True:
        val2, idx2 = getColorMax(color)
        if idx2 != idx: break
        heappop(pen[color])
    heappush(pen[color], (val, idx))
    return val2, idx2

def updateMax():
    while mx:
        val, color, idx = mx[0]
        if c[idx] != color or p[idx] != val:
            heappop(mx); continue
        val2, idx2 = getColorMax(color)
        if -val2 != val or idx2 != idx:
            heappop(mx); continue
        return

def updateMax2():
    while mx2:
        val, color, idx = mx2[0]
        if c[idx] != color or p[idx] != -val:
            heappop(mx2); continue
        val2, idx2 = getColor2ndMax(color)
        if val2 != val or idx2 != idx:
            heappop(mx2); continue
        return

def insert(color):
    val, idx = getColorMax(color)
    heappush(mx, (p[idx], c[idx], idx))
    val2, idx2 = getColor2ndMax(color)
    if idx2 != -1: heappush(mx2, (-p[idx2], c[idx2], idx2))


def getans():
    updateMax(); updateMax2();
    if len(mx2)==0 or -mx2[0][0] <= mx[0][0]: return ans
    return ans - mx[0][0] - mx2[0][0]

for i in range(1, m+1):
    val, idx = getColorMax(i)
    heappush(mx, (p[idx], c[idx], idx))
    ans += p[idx]
    val2, idx2 = getColor2ndMax(i)
    if idx2 != -1: heappush(mx2, (-p[idx2], c[idx2], idx2))

print(getans())

for _ in range(q):
    op, i, x = map(int, input().split())
    if op == 1:
        if c[i] != x:
            ans = ans + getColorMax(c[i])[0] + getColorMax(x)[0]
            old, c[i] = c[i], x
            heappush(pen[c[i]], (-p[i], i))
            insert(old);  insert(c[i]);
            ans = ans - getColorMax(old)[0] - getColorMax(c[i])[0]
    else:
        if p[i] != x:
            ans = ans + getColorMax(c[i])[0]
            p[i] = x
            heappush(pen[c[i]], (-p[i], i))
            insert(c[i])
            ans = ans - getColorMax(c[i])[0]
    print(getans())
