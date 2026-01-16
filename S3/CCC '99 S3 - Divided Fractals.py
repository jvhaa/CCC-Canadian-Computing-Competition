import sys
input = sys.stdin.readline

for r in range(int(input())):
    it = int(input())
    grid = [['*' for i in range(3**it)] for _ in range(3**it)]

    square = [((0, 3**it-1), (0, 3**it-1))]
    for level in range(it):
        for i in range(len(square)):
            s = square.pop(0)
            width = (abs(s[0][0] - s[0][1]) + 1) // 3
            for y in range(s[1][0] + width, s[1][1] - width+1):
                for x in range(s[0][0] + width, s[0][1] - width+1):
                    grid[y][x] = " "
            squares = [((s[0][0], s[0][0]+width-1), (s[1][0], s[1][0]+width-1)), 
               ((s[0][0]+width, s[0][1]-width), (s[1][0], s[1][0]+width-1)),
               ((s[0][1]-width+1, s[0][1]), (s[1][0], s[1][0]+width-1)), 
               ((s[0][0], s[0][0]+width-1), (s[1][0]+width, s[1][1]-width)), 
               ((s[0][0], s[0][0]+width-1), (s[1][1]-width+1, s[1][1])), 
               ((s[0][0]+width, s[0][1]-width), (s[1][1]-width+1, s[1][1])), 
               ((s[0][1]-width+1, s[0][1]), (s[1][1]-width+1, s[1][1])), 
               ((s[0][1]-width+1, s[0][1]), (s[1][0]+width, s[1][1]-width))]
            square.extend(squares)

    y = 3**it-int(input())
    y2 = 3**it-int(input())
    x = int(input())-1
    x2 = int(input())
    for w in range(y2, y+1):
        line = " ".join(grid[w][x:x2])
        print(line)
    print()
