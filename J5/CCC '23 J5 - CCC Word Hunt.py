import sys

text = sys.stdin.readlines(1)[0].strip()
height = int(sys.stdin.readlines(1)[0])
width = int(sys.stdin.readlines(1)[0])

chars = {}
for char in text:
    chars[char] = []

for y in range(height):
    data = sys.stdin.readlines(1)[0].strip().split()
    for x in range(width):
        if data[x] in chars:
            chars[data[x]].append(tuple((x, y)))

def findcon(chars):
    keys = list(chars.keys())
    connections = {}
    for i in range(len(keys)-1):
        connections[keys[i] + keys[i+1]] = []
    for i in range(len(keys)-1):
        for coord1 in chars[keys[i]]:
            for coord2 in chars[keys[i+1]]:
                if abs(coord1[0]-coord2[0]) < 2 and abs(coord1[1]-coord2[1]) < 2:
                    connections[keys[i] + keys[i+1]].append(list((coord1, coord2)))
    return connections

def makecon(chars):
    start = list(chars.keys())[0]
    end = list(chars.keys())[1]
    connections = {start[:-1] + end: []}
    connections.update(chars)
    for coords1 in connections[start]:
        for coords2 in connections[end]:
            if coords1[-1] == coords2[0]:
                connections[start[:-1] + end].append(coords1[:-1] + coords2)
    del connections[start], connections[end]
    return connections

def neg_recip(coords):
    return ((coords[1]*-1, coords[0]), (coords[1], coords[0]*-1))

def retpath(paths):
    rpaths = []
    for path in paths:
        diff = []
        for i in range(len(path)-1):
            diff.append((path[i+1][0] - path[i][0], path[i+1][1] - path[i][1]))
        diffs = 0
        if len(diff) - 1 < 1:
            rpaths.extend(paths)
            break
        for i in range(len(diff)-1):
            if diff[i] != diff[i+1]:
                diffs += 1
                if diff[i] not in neg_recip(diff[i+1]):
                    break
            if diffs < 2 and i == len(diff)-2:
                rpaths.append(path)
    return rpaths

chars = findcon(chars)
for i in range(len(text)-2):
    chars = makecon(chars)
chars = tuple(chars.values())[0]
print(len(retpath(chars)))
