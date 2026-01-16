import sys

pages = int(sys.stdin.readlines(1)[0])

vertex = [n + 1 for n in range(pages)]
edge = []
graph = {}

for i in range(pages):
    data = list(map(int, sys.stdin.readlines(1)[0].strip().split(" ")))
    paths = data[0]
    for l in range(paths):
        edge.append((i + 1, data[l + 1]))

for v in vertex:
    graph[v] = []
for e1, e2 in edge:
    graph[e1].append(e2)
for key, value in graph.items():
    if value == []:
        graph[key] = [0]


def dfs(node):
    visited = [node]
    queue = [node]
    if len(visited) == len(graph):
        return "Y"
    while queue:
        v = queue.pop()
        for neighbour in graph[v]:
            if neighbour not in visited and neighbour != 0:
                visited.append(neighbour)
                queue.append(neighbour)
        if len(visited) == pages:
            return "Y"
    return "N"


def bfs(node):
    visited = [node]
    queue = [node]
    cycle = 0
    while queue:
        cycle += 1
        for i in range(len(queue)):
            v = queue.pop(0)
            if graph[v] == [0]:
                return cycle
            for neighbour in graph[v]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    return


print(dfs(1))
print(bfs(1))
