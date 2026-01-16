import sys
input = sys.stdin.readline

floors, rows, cols = int(input()), int(input()), int(input())
floor = [input() for i in range(rows)]

visited = []

def moves(x, y, v):
    move = [(x+1,y), (x-1, y), (x,y+1), (x,y-1)]
    move = [m for m in move if 0 <= m[0] < cols and 0 <= m[1] < rows]
    return [m for m in move if floor[m[1]][m[0]] == "." and (m[0], m[1]) not in v]

def bfs(x, y):
    visit = [(x, y)]
    queue = [(x, y)]
    while queue:
        q = queue.pop()
        move = moves(q[0], q[1], visit)
        visit.extend(move)
        queue.extend(move)
    return [v for v in visit if v not in visited]

e = []

for y in range(rows):
    for x in range(cols):
        if (x, y) not in visited and floor[y][x] == ".":
            b = bfs(x, y)
            visited.extend(b)
            e.append(len(b))

e = sorted(e, reverse=True)
rooms = 0
for i in e:
  if floors - i >= 0:
    rooms += 1
    floors -= i
  else:
    break
r = "room" if rooms == 1 else "rooms"
print(f"{rooms} " + r + f", {floors} square metre(s) left over")
