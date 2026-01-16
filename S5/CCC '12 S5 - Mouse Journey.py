r, c = map(int, input().split())

x, y = 0, 0
grid = [[0 for i in range(c+1)] for g in range(r+1)]
grid[1][1] = 1

for cat in range(int(input())):
    cy, cx = map(int, input().split())
    grid[cy][cx] = -1

for i in range(1, r+1):
    for j in range(1, c+1):
        if grid[i][j] != -1:
          grid[i][j] += max(0, grid[i-1][j]) + max(0, grid[i][j-1])

print(grid[r][c])
