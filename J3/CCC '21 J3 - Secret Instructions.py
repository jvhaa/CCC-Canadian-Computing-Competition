import sys

d = ""

while True:
    data = sys.stdin.readlines(1)[0].strip()
    if data == "99999":
        break
    f = int(data[0]) + int(data[1])
    turn = data[2:]
    
    if f % 2 == 1:
        d = "left"
    elif f == 0:
        pass
    else:
        d = "right"
    print(d, turn, sep = " ")
