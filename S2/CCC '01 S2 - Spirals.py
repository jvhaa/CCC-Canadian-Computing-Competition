import math
start = int(input())
end = int(input())
point = start
space = math.ceil((abs(start - end)+1)**0.5)
directions = ["d", "r", "u", "l"]
grid = [[" " for i in range(space)] for l in range(space)]
coord = [math.ceil(len(grid)/2)-1, math.ceil(len(grid)/2)-1]
moves = 1
while point <= end:
    for d in directions:
        for move in range(moves):
            if point > end:
                break
            grid[coord[1]][coord[0]] = point
            point += 1
            if d == "d":
                coord[1] += 1
            if d == "l":
                coord[0] -= 1
                if move == moves-1:
                    moves += 1
            if d == "u":
                coord[1] -= 1
            if d == "r":
                coord[0] += 1
                if move == moves-1:
                    moves += 1
for line in grid:
    print(" ".join(map(str, line)))
