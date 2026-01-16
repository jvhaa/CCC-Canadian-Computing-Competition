for i in range(int(input())):
    n, k, w = map(int, input().split())
    cursum = 0
    pins = []
    best = [[0 for i in range(k+1)] for i in range(n)]
    for i in range(n):
        pins.append(int(input()))
        cursum += pins[-1]
        if len(pins) > w:
            cursum -= pins.pop(0)
        if i ==0:best[i][1] = cursum
        else:best[i][1] = max(cursum, best[i-1][1])
        if i > w:
            for ball in range(2, k+1):
                best[i][ball] = max(cursum + best[i-w][ball-1], best[i-1][ball], best[i][ball-1])
        
    print(max(best[-1]))
