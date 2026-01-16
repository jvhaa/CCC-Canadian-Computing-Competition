import sys

times = int(sys.stdin.readlines(1)[0])
golds = 0


for i in range(times):
    points = int(sys.stdin.readlines(1)[0])
    fouls = int(sys.stdin.readlines(1)[0])
    if points * 5 - fouls * 3 > 40:
        golds += 1
        
if golds == times:
    print(str(golds) + "+")
else:
    print(golds)
