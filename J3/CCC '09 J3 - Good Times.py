import sys

times = {
    0 : ["in Ottawa", 0],
    1 : ["in Victoria", -300],
    2 : ["in Edmonton", -200],
    3 : ["in Winnipeg", -100],
    4 : ["in Toronto", 0],
    5 : ["in Halifax", 100],
    6 : ["in St. John's", 130]
}

time = int(sys.stdin.readlines(1)[0].strip())

for i in range(7):
    t = time + times[i][1]
    if t >= 2400:
        t -= 2400
    elif t < 0:
        t += 2400
    if t % 100 >= 60:
        t = t+ 40
    print(t, times[i][0], sep=" ")
