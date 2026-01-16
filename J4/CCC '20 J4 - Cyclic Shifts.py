import sys

string = sys.stdin.readlines(1)[0].strip()
cycle = sys.stdin.readlines(1)[0].strip()
cycle = [x for x in cycle]

for i in range(len(cycle)):
    text = ""
    text = text.join(cycle)
    if text in string:
        print("yes")
        break
    elif text not in string and i == len(cycle)-1:
        print("no")
    else:
        cycle.append(cycle[0])
        cycle.pop(0)
