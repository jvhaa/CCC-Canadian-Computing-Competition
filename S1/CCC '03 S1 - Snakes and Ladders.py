steps = {
    54 : 19,
    90 : 48,
    99 : 77,
    9 : 34,
    40 : 64,
    67 : 86
}

position = 1

while True:
    dice = int(input())
    if dice == 0:
        print("You Quit!")
        break
    if position + dice <= 100:
        position += dice
    if position in steps.keys():
        position = steps[position]
    print(f"You are now on square {position}")
    if position == 100:
        print("You Win!")
        break
