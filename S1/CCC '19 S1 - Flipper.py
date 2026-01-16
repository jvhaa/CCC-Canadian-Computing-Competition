import sys

grid = [["1", "2"],
        ["3", "4"]]

word = sys.stdin.readlines(1)[0].strip()

for letter in word:
    if letter == "H":
        grid[0][0], grid[1][0] = grid[1][0], grid[0][0]
        grid[0][1], grid[1][1] = grid[1][1], grid[0][1]
    elif letter == "V":
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

for x in grid:
    print(" ".join(x))
