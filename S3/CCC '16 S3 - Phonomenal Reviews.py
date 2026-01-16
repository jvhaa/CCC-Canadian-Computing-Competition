N, M = map(int, input().split())
pho = set(map(int, input().split()))

graph = [set() for _ in range(N)] 
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


for node in range(N):
    while len(graph[node]) == 1 and node not in pho: 
        prev = node
        node = list(graph[node])[0]
        graph[prev].remove(node) 
        graph[node].remove(prev)


def farthest(start):
    dist = [-1] * N
    dist[start] = 0
    stack = [(start, -1)]
    while stack:
        cur, prev = stack.pop()
        for adj in graph[cur]:
            if adj != prev:
                stack.append((adj, cur))
                dist[adj] = dist[cur] + 1
    far = max(dist)
    return far, dist.index(far) 


_, end1 = farthest(list(pho)[0])
diameter, end2 = farthest(end1)

node_count = sum(len(u) != 0 for u in graph)  
total = (node_count - 1) * 2 

print(total - diameter)
