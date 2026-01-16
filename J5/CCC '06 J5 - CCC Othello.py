import sys

data = sys.stdin.readlines(1)[0].strip().split(" ")
config = data[0]
num = int(data[1])

if config == "a":
    black = [[5, 4], [4, 5]]
    white = [[4, 4], [5, 5]]
if config == "b":
    black = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
    white = [[8, 1], [7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8]]
if config == "c":
    black = [[3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5],
             [4, 6], [4, 7], [4, 8]]
    white = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5],
             [6, 6], [6, 7], [6, 8]]

for i in range(1, num+1):
    y, x = int(data[i * 2]), int(data[i * 2 + 1])
    if i % 2 == 1:
        black.append([x, y])
        for piece in black:
            if y == piece[1]:
                for l in range(min(x, piece[0]), max(x, piece[0])):
                    if 0 < l < 9:
                        if [l, y] not in black:
                            if [l, y] in white:
                                white.remove([l, y])
                                black.append([l, y])
            if x == piece[0]:
                for l in range(min(y, piece[1]), max(y, piece[1])):
                    if 0 < l < 9:
                        if [x, l] not in black:
                            if [x, l] in white:
                                white.remove([x, l])
                                black.append([x, l])
            if abs(piece[0] - x) == abs(piece[1] - y):
                for l in range(abs(piece[0] - x)):
                    if (x > piece[0] and y > piece[1]) or (x < piece[0] and y < piece[1]):
                        if [min(piece[0], x) + l, min(piece[1], y) + l] not in black:
                            if [min(piece[0], x) + l, min(piece[1], y) + l] in white:
                                white.remove([min(piece[0], x) + l, min(piece[1], y) + l])
                                black.append([min(piece[0], x) + l, min(piece[1], y) + l])
                    else:
                        if [max(piece[0], x) - l, min(piece[1], y) + l] not in black:
                            if [max(piece[0], x) - l, min(piece[1], y) + l] in white:
                                white.remove([max(piece[0], x) - l, min(piece[1], y) + l])
                                black.append([max(piece[0], x) - l, min(piece[1], y) + l])

    else:
        white.append([x, y])
        for piece in white:
            if y == piece[1]:
                for l in range(min(x, piece[0]), max(x, piece[0])):
                    if 0 < l < 9:
                        if [l, y] not in white:
                            if [l, y] in black:
                                black.remove([l, y])
                                white.append([l, y])
            if x == piece[0]:
                for l in range(min(y, piece[1]), max(y, piece[1])):
                    if 0 < l < 9:
                        if [x, l] not in white:
                            if [x, l] in black:
                                black.remove([x, l])
                                white.append([x, l])
            if abs(piece[0] - x) == abs(piece[1] - y):
                for l in range(abs(piece[0] - x)):
                    if x > piece[0] and y > piece[1] or piece[0] > x and piece[1] > y:
                        if [min(piece[0], x) + l, min(piece[1], y) + l] not in white:
                            if [min(piece[0], x) + l, min(piece[1], y) + l] in black:
                                black.remove([min(piece[0], x) + l, min(piece[1], y) + l])
                                white.append([min(piece[0], x) + l, min(piece[1], y) + l])
                    else:
                        if [max(piece[0], x) - l, min(piece[1], y) + l] not in white:
                            if [max(piece[0], x) - l, min(piece[1], y) + l] in black:
                                black.remove([max(piece[0], x) - l, min(piece[1], y) + l])
                                white.append([max(piece[0], x) - l, min(piece[1], y) + l])

print(len(black), len(white))
