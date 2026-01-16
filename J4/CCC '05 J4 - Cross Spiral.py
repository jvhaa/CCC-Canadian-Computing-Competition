g = [[False] * 22 for _ in range(22)]
w = int(input())
h = int(input())
cw = int(input())
ch = int(input())
steps = int(input())

# Initialize grid
for i in range(22):
    for j in range(22):
        if 1 <= i <= h and 1 <= j <= w and not ((i <= ch and (j <= cw or j > w - cw)) or
                                                (i > h - ch and (j <= cw or j > w - cw))):
            g[i][j] = True
        else:
            g[i][j] = False

c = cw + 1
r = 1
direction = 0

for _ in range(steps):
    g[r][c] = False
    moving = True

    if direction == 0:
        if g[r - 1][c]:
            r -= 1
            direction = 90
        elif g[r][c + 1]:
            c += 1
            direction = 0
        elif g[r + 1][c]:
            r += 1
            direction = 270
        elif g[r][c - 1]:
            c -= 1
            direction = 180
        else:
            moving = False
    elif direction == 90:
        if g[r][c - 1]:
            c -= 1
            direction = 180
        elif g[r - 1][c]:
            r -= 1
            direction = 90
        elif g[r][c + 1]:
            c += 1
            direction = 0
        elif g[r + 1][c]:
            r += 1
            direction = 270
        else:
            moving = False
    elif direction == 180:
        if g[r + 1][c]:
            r += 1
            direction = 270
        elif g[r][c - 1]:
            c -= 1
            direction = 180
        elif g[r - 1][c]:
            r -= 1
            direction = 90
        elif g[r][c + 1]:
            c += 1
            direction = 0
        else:
            moving = False
    elif direction == 270:
        if g[r][c + 1]:
            c += 1
            direction = 0
        elif g[r + 1][c]:
            r += 1
            direction = 270
        elif g[r][c - 1]:
            c -= 1
            direction = 180
        elif g[r - 1][c]:
            r -= 1
            direction = 90
        else:
            moving = False

    if not moving:
        break

print(c)
print(r)
