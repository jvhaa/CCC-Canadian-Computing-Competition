import sys

width = int(sys.stdin.readlines(1)[0])

trees = []

for i in range(int(sys.stdin.readlines(1)[0])):
    data = tuple(map(int, sys.stdin.readlines(1)[0].strip().split()))
    trees.append(data)
trees += [(0, 0), (width+1, width+1)]

allx = ally = set()

for x, y in trees:
    for x2, y2 in trees:
        if x != x2:
            allx.add(tuple(sorted((x, x2))))
        if y != y2:
            ally.add(tuple(sorted((y, y2))))

def sortbyabs(coords):
    return list(sorted(coords, key= lambda coord: abs(coord[0]-coord[1]), reverse=True))

allx, ally = sortbyabs(allx), sortbyabs(ally)

trees = trees[:-2]
total = []

for i in range(2):
    trees = sorted(trees, key=lambda x: x[i])
    for s, e in allx if i else ally:
        s2, e2 = 0, abs(s - e)
        for tree in trees:
            if i and s < tree[0] < e and s2 < tree[1] < e2: # if checking there is a tree between ys or there is a tree between x
                e2 += abs(tree[1] - s2) + 1 # shifts the x over by the tree to not intersect it again
                s2 = tree[1] + 1 # shifts start x over by tree to not intersect it again
            elif not i and s < tree[1] < e and s2 < tree[0] < e2: # reverse of before
                e2 += abs(tree[0] - s2) + 1
                s2 = tree[0] + 1
            # Square went out of bounds, is not valid
            if e2 > width + 1:
                break
        else:
            total.append(abs(s - e) - 1) # ends at the loop and when it finds a match as it is the largest
            break
print(max(total)) # prints max possible
