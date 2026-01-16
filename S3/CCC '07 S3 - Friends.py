from collections import deque
import sys
input = sys.stdin.readline
graph = {}

for i in range(int(input())):
    a, b = input().split()
    if a not in graph:
        graph[a] = []
    graph[a].append(b)

def fewest(start, end, visited):
  queue = deque([start])
  length = 0
  while queue:
    if end in queue:
      return length
    length += 1
    for i in range(len(queue)):
      thing = queue.popleft()
      for neighbour in graph[thing]:
        if neighbour not in visited:
          queue.append(neighbour)


while True:
    a, b = input().split()
    if a == "0" and b == "0":
      break
    answer = ""
    main = fewest(a, b, [a]) 
    if main != None and fewest(b, a, [b]) != None:
        answer = "Yes " + str(main-1)
    else:
        answer = "No"
    print(answer)
