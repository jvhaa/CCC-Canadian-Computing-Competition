import sys
from collections import defaultdict, deque
import heapq

input = sys.stdin.readline

N, W, D = map(int, input().split())
graph = defaultdict(list)

for path in range(W):
    a, b = map(int, input().split())
    graph[b].append(a)

dist = [10000000] * (N+1)
dist[N] = 0
path = list(map(int, input().split()))
ids = [0 for i in range(N+1)]
for i in range(N):
    ids[path[i]] = i
q = deque([N])

while q:
    node = q.popleft()
    for neighbour in graph[node]:
        if dist[neighbour] == 10000000:
            dist[neighbour] = dist[node] + 1
            q.append(neighbour)

q = []

for i in range(1, N+1):
    heapq.heappush(q, (dist[i]+ids[i], i))

for day in range(D):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    c, d = path[a], path[b]
    ids[c], ids[d] = ids[d], ids[c]
    path[a], path[b] = path[b], path[a]
    heapq.heappush(q, (dist[c] + ids[c], c))
    heapq.heappush(q, (dist[d] + ids[d], d))
    while dist[q[0][1]] + ids[q[0][1]] != q[0][0]:
        heapq.heappop(q)
    
    print(q[0][0])
