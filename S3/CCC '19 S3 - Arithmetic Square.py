grid = [list(map(lambda x: x if x == "X" else int(x), input().split())) for i in range(3)]

def fill():
    global grid
    change = False
    for turns in range(4):
        for i in range(3):
            if grid[i].count("X") == 1:
                change = True
                ind = grid[i].index("X")
                if ind == 0:
                    grid[i][0] = grid[i][1]*2 - grid[i][2]
                elif ind == 1:
                    grid[i][ind] = (grid[i][2] - grid[i][0]) //2 + grid[i][0]
                else:
                    grid[i][ind] = grid[i][1]*2-grid[i][0]
        grid = list(map(list, zip(*grid)))
    return change
        
X = lambda : sum(grid[i].count("X") for i in range(3))     

def fill2():
    global grid
    for y in range(3):
        for x in range(3):
            if grid[y][x] == "X":
                grid[y][x] = 0
                return

cross = [[1, 1], [0, 1], [2, 1], [1, 0], [1, 2]]

while X():
    if not fill():
        flag = False
        for x, y in cross:
            if grid[y][x] == "X":
                grid[y][x] = 0
                flag = True
                break
        if not flag:
            fill2()

for line in grid:
    print(*line)
