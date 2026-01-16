points = {
    "jack": [1, 1],
    "queen": [2, 2],
    "king": [3, 3],
    "ace": [4, 4],
}

point = []
player = {
    "A": 0,
    "B": 0
}

for i in range(52):
    card = input()
    if len(point) > 0:
        point[1] -= 1
    if card in points.keys():
        point = points[card] + ["A" if i % 2 == 0 else "B"]
    if len(point) > 0 and point[1] == 0:
        player[point[2]] += point[0]
        print(f"Player {point[2]} scores {point[0]} point(s).")

for play, points in player.items():
    print(f"Player {play}: {points} point(s).")
