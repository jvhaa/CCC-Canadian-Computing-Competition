from collections import deque
import sys

r = int(sys.stdin.readline())
c = int(sys.stdin.readline())

points = {
    "S" : 1,
    "M" : 5,
    "L" : 10
}

graph = [sys.stdin.readline() for i in range(r)]
y, x = int(sys.stdin.readline()), int(sys.stdin.readline())

queue = deque([(x, y)])
visited = set([(x, y)])
score = 0
while queue:
    q = queue.popleft()
    score += points[graph[q[1]][q[0]]]
    for neighbour in [(1,0), (-1,0), (0, 1), (0, -1)]:
        nx = q[0] + neighbour[0]
        ny = q[1] + neighbour[1]
        if c > nx >= 0:
            if r > ny >= 0:
                if (nx, ny) not in visited and graph[ny][nx] != "*":
                    visited.add((nx, ny))
                    queue.append([nx, ny])

print(score)
