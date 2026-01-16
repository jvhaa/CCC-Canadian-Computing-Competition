from collections import deque, defaultdict 
import sys
input = sys.stdin.readline
people, comparisions = map(int, input().split())

taller = defaultdict(list)

for i in range(comparisions):
  a, b = input().split()
  taller[a].append(b)

def bfs(start, end):
  visited = set()
  queue = deque([start])
  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      if node in taller:
        for i in taller[node]:
          if i not in visited:
            if i == end:
                return True
            queue.append(i)
  return False

x, y = input().split()

if bfs(x, y):
  print("yes")
elif bfs(y, x):
  print("no")
else:
  print("unknown")
