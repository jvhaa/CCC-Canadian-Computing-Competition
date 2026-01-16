import sys

s = list(map(int, sys.stdin.readlines(1)[0].strip().split(" ")))
e = list(map(int, sys.stdin.readlines(1)[0].strip().split(" ")))


def bfs(start, end):
    count = 0
    visited = [start]
    queue = [start]
    if start == end:
        return count
    while queue:
        count += 1
        pos = []
        for i in range(len(queue)):
            pos.extend(moves(queue.pop(0)))
        if end in pos: 
            return count
        else:
            queue = []
            visited.extend(pos)
            queue.extend(pos)


def moves(pos):
    ps = [[pos[0] + 1, pos[1] + 2], [pos[0] + 1, pos[1] -2], [pos[0] - 1, pos[1] + 2], [pos[0] -1, pos[1]- 2],
                 [pos[0] + 2, pos[1] + 1], [pos[0] + 2, pos[1] - 1], [pos[0] - 2, pos[1] + 1], [pos[0] -2, pos[1]- 1]]
    return [position for position in ps if position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9]


print(bfs(s, e))
