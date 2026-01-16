from collections import deque
import sys
input = sys.stdin.readline

friendship = {1:[6], 2:[6], 3:[4, 5, 6, 15], 4:[3, 5, 6], 5:[3, 4, 6], 6:[1, 2, 3, 4, 5, 7], 7:[6, 8], 8:[7, 9], 9:[8, 10, 12], 10:[9, 11], 11:[10, 12], 12: [9, 11, 13], 13:[12, 14, 15], 14:[13], 15:[3, 13], 16:[17, 18], 17:[16, 18], 18:[16, 17], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[], 25:[], 26:[], 27:[], 28:[], 29:[], 30:[], 31:[], 32:[], 33:[], 34:[], 35:[], 36:[], 37:[], 38:[], 39:[], 40:[], 41:[], 42:[], 43:[], 44:[], 45:[], 46:[], 47:[], 48:[], 49:[], 50:[]}

def frfr(x):
  friends = [x] + friendship[x]
  frfr = []
  notfriend = set()
  for f in friends:
    notfriend.update({n for n in friendship[f] if n not in friends})
  return len(notfriend)

def bfs(start, end):
  length = 0
  queue = deque([start])
  visited = {start}
  while queue:
    length += 1
    for _ in range(len(queue)):
      node = queue.popleft()
      for friend in friendship[node]:
        if friend not in visited:
          queue.append(friend)
          visited.add(friend)
          if friend == end:
            return length
  return -1

while True:
  command = input().strip()
  if command == "i":
      x, y = int(input()), int(input())
      friendship[x].append(y)
      friendship[y].append(x)
  elif command == "d":
      x, y = int(input()), int(input())
      friendship[x].remove(y)
      friendship[y].remove(x)
  elif command == "n":
      x = int(input())
      print(len(friendship[x]))
  elif command == "f":
      print(frfr(int(input())))
  elif command == "s":
      b = bfs(int(input()), int(input()))
      if b == -1:
        print("Not connected")
      else:
         print(b)
  else:
      break
