from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def rooting(root):
  graph = defaultdict(list)
  queue = deque([root])
  visited = set()
  while queue:
    node = queue.popleft()
    visited.add(node)
    for child in rel[node]:
      if child not in visited:
        visited.add(child)
        graph[node].append(child)
        queue.append(child)
  return graph, visited

def timming(graph, root):
  time = 0
  queue = deque([root])
  while queue:
    for i in range(len(queue)):
      node = queue.popleft()
      for child in graph[node]:
        queue.append(child)
    time += 1
  return (time-1)*20

for test_cases in range(int(input())):
  message = deque()
  rel = defaultdict(list)
  for messages in range(int(input())):
    message.append(input().strip())
  root_node = message[-1]
  message.appendleft(root_node)
  for i in range(len(message)-1):
    a, b = str(message[i]), str(message[i+1])
    rel[b].append(a)
  graph, children = rooting(root_node)
  time = (len(children)-1)*20
  print(time - timming(graph, root_node))
