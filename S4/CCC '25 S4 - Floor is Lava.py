import heapq

N, M = map(int, input().split())

levels = [set() for _ in range(N)]
tunnels = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1  
    b -= 1
    tunnels.append((a, b, c))
    levels[a].add(c)
    levels[b].add(c)

levels[0].add(0)

for i in range(N):
    levels[i] = sorted(levels[i])

offset = [0] * (N + 1)
total_nodes = 0
for i in range(N):
    offset[i] = total_nodes
    total_nodes += len(levels[i])
offset[N] = total_nodes

maps = []
for i in range(N):
    d = {}
    for j, val in enumerate(levels[i]):
        d[val] = j
    maps.append(d)

graph = [[] for _ in range(total_nodes)]

for i in range(N):
    base = offset[i]
    L = levels[i]
    for j in range(len(L) - 1):
        u = base + j
        v = base + j + 1
        diff = L[j+1] - L[j]
        graph[u].append((v, diff))
        graph[v].append((u, diff))

for a, b, c in tunnels:
    u = offset[a] + maps[a][c]
    v = offset[b] + maps[b][c]
    graph[u].append((v, 0))
    graph[v].append((u, 0))

INF = 10**18
dist = [INF] * total_nodes

start_node = offset[0] + maps[0][0]
dist[start_node] = 0

heap = []
heapq.heappush(heap, (0, start_node))

while heap:
    d, u = heapq.heappop(heap)
    if d != dist[u]:
        continue
    for v, cost in graph[u]:
        nd = d + cost
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(heap, (nd, v))

ans = INF
base = offset[N-1]
for j in range(len(levels[N-1])):
    node = base + j
    if dist[node] < ans:
        ans = dist[node]

print(ans)
