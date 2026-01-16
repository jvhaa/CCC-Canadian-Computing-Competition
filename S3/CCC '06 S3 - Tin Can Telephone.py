import math

def blockView(building, segment):
    l = len(building)
    for i in range(l):
        edge = building[i]+building[(i+1)%l]
        if intersectionofsegment(edge, segment) is not None:
            return True
    return False

def intersectionofsegment(seg1, seg2):
    point = intersection(seg1, seg2)
    if point == None or point == math.inf:
        return point
    elif isPoint(point, seg1) and isPoint(point, seg2):
        return point
    return None

def isPoint(point, segment):
    x, y = point
    x1, y1, x2, y2 = segment

    return (x-x1)*(x-x2)<=0 and (y-y1)*(y-y2)<=0

def intersection(seg1, seg2):
    a1, b1, c1 = convert(seg1)
    a2, b2, c2 = convert(seg2)

    if (a1, b1, c1) == (a2, b2, c2):
        return math.inf
    
    return solve(a1, b1, c1, a2, b2, c2)

def solve(a1, b1, c1, a2, b2, c2):
    den = a1*b2 - a2*b1
    if den==0:
        return None

    num1 = c2*b1 - c1*b2
    num2 = a1*c2 - a2*c1

    x = num1 / den
    y = -num2 / den
    return (x, y)

def convert(line):
    x1, y1, x2, y2 = line
    b = x2-x1
    a = y1-y2
    c = x1*(y2-y1)-y1*(x2-x1)
    return (a, b, c)

rx, ry, jx, jy = map(int, input().split())
g = int(input())
ans = 0

for buildings in range(g):
    line = list(map(int, input().split()))
    coords = list(zip(line[1::2], line[2::2]))
    if blockView(coords, (rx, ry, jx, jy)):
        ans += 1
print(ans)
