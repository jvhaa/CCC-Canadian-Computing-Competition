boxes = sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x: x[0]*x[1]*x[2])
items = [list(map(int, input().split())) for _ in range(int(input()))]
boxes.append([1001, 1001, 1001])

def fits(item):
  for i in range(len(boxes)):
    b = boxes[i]
    box = sorted(b)
    if item[0] <= box[0] and item[1] <= box[1] and item[2] <= box[2]:
      if boxes[i][0] == 1001:
        return "Item does not fit."
      return boxes[i][0] * boxes[i][1] * boxes[i][2]

for item in items:
  i = sorted(item)
  print(fits(i))
