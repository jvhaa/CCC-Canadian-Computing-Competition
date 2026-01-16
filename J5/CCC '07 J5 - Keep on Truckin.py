import sys

locations = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
mi = int(sys.stdin.readlines(1)[0])
ma = int(sys.stdin.readlines(1)[0])
num = int(sys.stdin.readlines(1)[0])
memo = {}
for i in range(num):
    locations.append(int(sys.stdin.readlines(1)[0]))
locations.sort()

def destinations(index):
    if (index) in memo:
        return memo[(index)]
    if index == len(locations)-1:
        return 1
    result = 0
    for i in range(1, len(locations) -index):
        if ma >= (locations[i + index] - locations[index]) >= mi:
            result += destinations(index + i)
    memo[(index)] = result
    return result


print(destinations(0))
