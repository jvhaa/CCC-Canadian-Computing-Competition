x1, y1, x2, y2 = map(int, input().split())

ex = max(min(x1, x2), min(y1, y2))

print((x1+y1+x2+y2-ex)*2)
