c, r = list(map(int, input().split()))

position = [0, 0]

while True:
    x, y = list(map(int, input().split()))
    
    if x == 0 and y == 0:
        break
    position[0] += x
    position[1] += y
    if position[0] < 0:
        position[0] = 0
    if position[0] > c:
        position[0] = c
    if position[1] < 0:
        position[1] = 0
    if position[1] > r:
        position[1] = r
    print(" ".join(map(str, position)))
