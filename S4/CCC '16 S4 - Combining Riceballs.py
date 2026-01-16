n = int(input())
rice = [0] + list(map(int, input().split()))
able = [[False for i in range(n)] for i in range(n)]

ans = 0

for i in range(n):
  ans = max(ans, rice[i+1])
  able[i][i] = True
  rice[i+1] += rice[i]

for dist in range(1, n):
    for p1 in range(1, n-dist+1):
        p4 = p1 + dist
        p2 = p1
        p3 = p4
        while p2 < p3:
            fir = rice[p2] - rice[p1-1]
            sec = rice[p4] - rice[p3-1]
            if fir == sec:
                if able[p1-1][p2-1] and able[p3-1][p4-1] and (able[p2][p3-2] or p3-p2 == 1):
                    ans = max(rice[p4]-rice[p1-1], ans)
                    able[p1-1][p4-1] = True
                    able[p4-1][p1-1] = True
                    break
                else:
                  p2 += 1
            elif fir < sec:
                p2 += 1
            else:
                p3 -= 1
                


print(ans)
