import sys

position = [0, -1]
passed = [position.copy()]  # Store a copy of the initial position
safety = True

def move(direction, movement):
    global safety
    for i in range(movement):
        if direction == "l":
            position[0] -= 1
        elif direction == "r":
            position[0] += 1
        elif direction == "u":
            position[1] += 1
        elif direction == "d":
            position[1] -= 1
        if position in passed and safety:
            safety = False
        passed.append(position.copy())  # Append a copy of the current position

move("d", 2)
move("r", 3)
move("d", 2)
move("r", 2)
move("u", 2)
move("r", 2)
move("d", 4)
move("l", 8)
move("u", 2)

while True:
    data = sys.stdin.readlines(1)[0].strip().split(" ")
    direction, movement = data[0], int(data[1])
    if direction == "q":
        break
    else:
        move(direction, movement)

    print(" ".join(str(x) for x in position), " safe" if safety else " DANGER")
    if not safety:
        break
