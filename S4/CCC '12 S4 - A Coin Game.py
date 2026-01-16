import sys
from collections import deque

while True:
    n = int(sys.stdin.readline())
    if (n == 0):
        break
    position = tuple(sys.stdin.readline().rstrip("\n").split())
    dist = {}
    dist[position] = 0
    nodeQueue = deque()
    nodeQueue.append(position)
    finalSequence = [str(i) for i in range (1,n+1)]
    finalSequence = tuple(finalSequence)
    while nodeQueue:
        u = nodeQueue.popleft()
        if ( u == finalSequence):
            break
        for i in range (len(u)):
            if (u[i] == ""):
                continue
            if (i - 1 >= 0 and (u[i-1] == "" or (u[i])[0] < u[i-1][0])):
                newPos = u[:i-1] + (u[i][0] + u[i-1],) + (u[i][1:],) + u[i+1:]
                if (not newPos in dist):
                    dist[newPos] = dist[u] +1
                    nodeQueue.append(newPos)
            if (i + 1 < n and (u[i+1] == "" or  (u[i])[0] < u[i+1][0])):
                newPos = u[:i] + (u[i][1:],) + (u[i][0] + u[i+1],) + u[i+2:]
                if (not newPos in dist):
                    dist[newPos] = dist[u] +1
                    nodeQueue.append(newPos)
    if (finalSequence in dist):
        print(dist[finalSequence])
    else:
        print("IMPOSSIBLE")
