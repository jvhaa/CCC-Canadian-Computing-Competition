import sys
input = sys.stdin.readline

ds = {
  "left" : (-1, 0),
  "right" : (1, 0),
  "up" : (0, 1),
  "down" : (0, -1)
}

def realdir(d1, l1, direction):
  dir1 = direction
  dir2 = direction
  turns = 0
  while True:
    if dir1== d1:
      return [d1, "clockwise", turns]
    elif dir1 == l1:
      return [l1, "clockwise", turns]
    if dir2 == d1:
      return [d1, "counterclockwise", turns]
    elif dir2 == l1:
      return [l1, "counterclockwise", turns]

    if turns >= 4:
      return []

    if dir1 == "up":
      dir1 = "right"
    elif dir1 == "right":
      dir1 = "down"
    elif dir1 == "down":
      dir1 = "left"
    elif dir1 == "left":
      dir1 = "up"

    if dir2 == "up":
      dir2 = "left"
    elif dir2 == "right":
      dir2 = "up"
    elif dir2 == "down":
      dir2 = "right"
    elif dir2 == "left":
      dir2 = "down"
    turns += 1
length = int(input())
for i in range(length):
  direction = "up"
  position = (0, 0)
  while True:
    comm = int(input())
    if comm == 0:
      break
    elif comm == 1:
      steps = int(input())
      position = tuple(map(lambda x, y: x + y*steps, position, ds[direction]))
    elif comm == 2:
      if direction == "up":
        direction = "right"
      elif direction == "right":
        direction = "down"
      elif direction == "down":
        direction = "left"
      else:
        direction = "up"
    else:
      if direction == "up":
        direction = "left"
      elif direction == "right":
        direction = "up"
      elif direction == "down":
        direction = "right"
      else:
        direction = "down"
  print(f"Distance is {abs(position[0]) + abs(position[1])}")
  rl = "left" if position[0] > 0 else "right" if position[0] < 0 else ""
  ud = "down" if position[1] > 0 else "up" if position[1] < 0 else ""
  e = realdir(rl, ud, direction)
  if e == []:
    if i != length - 1:
      print()
  else:
    if e[1] == "clockwise":
      for _ in range(e[2]):
        print(2)
    else:
      for _ in range(e[2]):
        print(3)

    print(1)
    if e[0] == ud:
      print(abs(position[1]))
    else:
      print(abs(position[0]))

    if e[0] == ud:
      if rl != "":
        e = realdir(rl, "", ud)
        if e[1] == "clockwise":
          for _ in range(e[2]):
            print(2)
        else:
          for _ in range(e[2]):
            print(3)
        print(1)
        print(abs(position[0]))
    else:
      if ud != "":
        e = realdir(ud, "", rl)
        if e[1] == "clockwise":
          for _ in range(e[2]):
            print(2)
        else:
          for _ in range(e[2]):
            print(3)
        print(1)
        print(abs(position[1]))
    if i != length -1:
      print()
