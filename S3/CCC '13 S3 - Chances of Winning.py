import sys
input = sys.stdin.readline

team = int(input())
games = int(input())
points = {1 : 0, 2 : 0, 3 : 0, 4 : 0}
played = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

for i in range(games):
    A, B, scoreA, scoreB = list(map(int, input().split()))
    played.remove(sorted([A, B]))
    if scoreA > scoreB:
        points[A] += 3
    elif scoreB > scoreA:
        points[B] += 3
    else:
        points[A] += 1
        points[B] += 1

def possiblity(loop, ans):
  pos = []
  if loop == 0:
    return [ans]
  for i in "wtl":
    pos.extend(possiblity(loop - 1, ans+i))
  return pos

p = possiblity(6-games, "")
ans = 0
copy = points.copy()

for pos in p:
    for index, game in enumerate(pos):
        if game == "w":
            points[played[index][0]] += 3
        elif game == "l":
            points[played[index][1]] += 3
        else:
            points[played[index][0]] += 1
            points[played[index][1]] += 1
    points = sorted(points.items(), key = lambda x: (x[1], x[0] != team), reverse=True)
    if points[0][0] == team:
        ans += 1
    points = copy.copy()

print(ans)
