import sys

todolist = [[1, 7], [1, 4], [2, 1], [3, 4], [3, 5]]

while True:
    data = []
    for i in range(2):
        data.append(int(sys.stdin.readlines(1)[0]))
    if data == [0, 0]:
        break
    todolist.append(data)
    
for i in range(1, 8):
    for l in range(1, 8):
        if l != i:
            for k in range(1, 8):
                if k != i and k != l:
                    for m in range(1, 8):
                        if m != i and m != l and m != k:
                            for o in range(1, 8):
                                if o != i and o != l and o != k and o != m:
                                    for u in range(1, 8):
                                      if u != i and u != l and u != k and u != m and u != o:
                                        for p in range(1, 8):
                                            if p != i and p != l and p != k and p != m and p != o and p != u:
                                                num = [i, l, k, m, o, u, p]
                                                for d in todolist:
                                                    if num.index(d[0]) > num.index(d[1]):
                                                        break
                                                    elif d == todolist[len(todolist)-1]:
                                                        print(i, l, k, m, o, u, p, sep=" ")
                                                        sys.exit()
print("Cannot complete these tasks. Going to bed.")
