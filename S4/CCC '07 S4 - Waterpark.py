import sys
input = sys.stdin.readline

paths = {}
connections = {}

nodes = input().strip()

def bfs(node):
  if node == nodes:
    return 1
  if node in paths:
    return paths[node]
  ans = 0
  if node in connections:
    for neighbour in connections[node]:
      ans += bfs(neighbour)
    paths[node] = ans
  return ans


while True:
  a, b = input().split()
  if a == "0" and b == "0":
    break
  if a not in connections:
    connections[a] = []
  connections[a].append(b)

print(bfs("1"))
