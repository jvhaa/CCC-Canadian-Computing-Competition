import sys
input = sys.stdin.readline
from collections import Counter
paths = {}

path = []
while True:
    data = input()
    a, b = data[0], data[1]
    path.append(tuple((a, b)))
    if a+b == "**":
        break
    if a not in paths:
        paths[a] = []
    if b not in paths:
        paths[b] = []
    paths[a].append(b)
    paths[b].append(a)


position = "A"

def possibility(position, path):
  path = path + [position]
  pathed = []
  if position == "B":
    return [path]
  for neighbour in paths[position]:
    if neighbour not in path:
      new_paths = possibility(neighbour, path)
      for new_path in new_paths:
        pathed.append(new_path)
  return pathed

Ps = possibility(position, [])
locations = Counter()

for path in Ps:
    for location in range(len(path)-1):
      locations[(path[location], path[location+1])] += 1

ans = [0]

for key, value in locations.items():
    if value == len(Ps):
        ans[0] += 1
        ans.append(key)

for road in ans[1:]:
  print(road[0] + road[1])

print(f"There are {ans[0]} disconnecting roads.")
