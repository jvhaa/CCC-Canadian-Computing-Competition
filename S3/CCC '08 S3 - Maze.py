import sys
input = sys.stdin.readline
from collections import deque

def spaces(position, grid, width, height, visited):
    eee = grid[position[1]][position[0]]
    move = []
    if eee == "+":
        move = [(position[0]+1, position[1]), (position[0]-1, position[1]), (position[0], position[1]+1), (position[0], position[1]-1)]
    elif eee == "-":
        move = [(position[0]+1, position[1]), (position[0]-1, position[1])]
    else:
        move = [(position[0], position[1]+1), (position[0], position[1]-1)]
    move = [m for m in move if -1 < m[0] < width and -1 < m[1] < height]
    return [m for m in move if grid[m[1]][m[0]] != "*" and m not in visited]

def bfs(height, width, grid):
    queue = deque([(0, 0)])
    visited = deque([(0, 0)])
    if grid[0][0] == "*":
        return -1
    moves = 1
    if width -1 == 0 and height -1 == 0:
        return moves
    while queue:
        moves += 1
        for _ in range(len(queue)):
            q = queue.popleft()
            space = spaces(q, grid, width, height, visited)
            queue.extend(space)
            visited.extend(space)
        if (width-1, height-1) in queue:
            return moves
    return -1



for i in range(int(input())):
    height, width = int(input()), int(input())

    grid = [input().strip() for _ in range(height)]
    print(bfs(height, width, grid))
