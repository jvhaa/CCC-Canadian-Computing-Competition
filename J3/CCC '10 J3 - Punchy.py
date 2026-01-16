import sys

varibles = {
    "A": 0,
    "B": 0
}

while True:
    data = sys.stdin.readlines(1)[0].strip().split(" ")

    if data[0] == "1":
        varibles[data[1]] = int(data[2])
    elif data[0] == "2":
        print(varibles[data[1]])
    elif data[0] == "3":
        varibles[data[1]] += varibles[data[2]]
    elif data[0] == "4":
        varibles[data[1]] *= varibles[data[2]]
    elif data[0] == "5":
        varibles[data[1]] -= varibles[data[2]]
    elif data[0] == "6":
        varibles[data[1]] //= varibles[data[2]]
    else:
        break
