n, m, r, c = map(int, input().split())

grid = [["a" for _ in range(m)] for _ in range(n)]
passed = True

if n == r and m == c:
    pass
elif n > r and m > c:
    for y in range(n-r):
        grid[y][0] = "b"
    for x in range(m-c):
        grid[0][x] = "b"
    grid[0][0] = "c"
elif n > r:
    if n % 2 == 0 and r % 2 == 1:
        passed = False
    elif (n-r) % 2 == 0:
        space = (n-r) // 2
        for y in range(space):
            grid[y][0] = "b"
            grid[y][-2] = "b"
        for y in range(n-space, n):
            grid[y][0] = "b"
            grid[y][-2] = "b"
    else:
        for y in range(r//2, n - r//2):
            grid[y][0] = "b"
            grid[y][-2] = "b"
else:
    if m % 2 == 0 and c % 2 == 1:
        passed = False
    elif (m-c) % 2 == 0:
        space = (m-c) // 2
        for x in range(space):
            grid[0][x] = "b"
            grid[-2][x] = "b"
        for x in range(m - space, m):
            grid[0][x] = "b"
            grid[-2][x] = "b"
    else:
        for x in range(c//2, m-c//2):
            grid[0][x] = "b"
            grid[-2][x] = "b"

if passed:
    for line in grid:
        print("".join(line))
else:
    print("IMPOSSIBLE")
