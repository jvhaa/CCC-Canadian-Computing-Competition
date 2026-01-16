import sys

num = int(sys.stdin.readlines(1)[0])

def check_wins(arr):
    grid = [[arr[i+j*3] for i in range(3)] for j in range(3)]
    winners = []
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != ".":
            winners.append(grid[i][0])
        if grid[0][i] == grid[1][i] == grid[2][i] != ".":
            winners.append(grid[0][i])
    if grid[0][0] == grid[1][1] == grid[2][2] != ".":
        winners.append(grid[0][0])
    if grid[2][0] == grid[1][1] == grid[0][2] != ".":
        winners.append(grid[2][0])
    if len(winners) > 1 and not (all(wins == "O" for wins in winners) or all(wins == "X" for wins in winners)):
        return False
    if "X" in winners:
        return arr.count("O")+1 == arr.count("X")
    elif "O" in winners:
        return arr.count("X") == arr.count("O")
    return True

for i in range(num):
    data = sys.stdin.readlines(1)[0].strip()
    if data.count("O") > data.count("X") or data.count("X") > data.count("O") + 1:
        print("no")
    elif not check_wins(data):
        print("no")
    else:
        print("yes")

