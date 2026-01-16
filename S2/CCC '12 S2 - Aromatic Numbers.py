number = input()

roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

aromatic = []
for i in range(0, len(number), 2):
    aromatic.append([int(number[i]) * roman[number[i+1]], roman[number[i+1]]])
aromatic.append([0, 0])
answer = 0
for i in range(len(aromatic)-1):
    if aromatic[i+1][1] <= aromatic[i][1]:
        answer += aromatic[i][0]
    else:
        answer -= aromatic[i][0]

print(answer)
