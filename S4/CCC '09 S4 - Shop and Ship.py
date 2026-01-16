import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra(graph, start):  
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, cur = heappop(pq)
        if dist[cur] < d:
            continue
        for adj, adj_d in enumerate(graph[cur]):
            new_d = adj_d + d
            if new_d < dist[adj]:
                dist[adj] = new_d
                heappush(pq, (new_d, adj))

    return dist


n = int(input()) + 1
t = int(input())

mat = [[float('inf')] * n for i in range(n)]

for i in range(t):
    a, b, c = map(int, input().split())

    mat[a][b] = c
    mat[b][a] = c


pencils = int(input())


stores = []
for _ in range(pencils):
    stores.append(list(map(int, input().split())))

start = int(input())
distances = dijkstra(mat, start)  


pencil = float('inf')
for d, c in stores:
    pencil = min(pencil, distances[d] + c)

print(pencil)
