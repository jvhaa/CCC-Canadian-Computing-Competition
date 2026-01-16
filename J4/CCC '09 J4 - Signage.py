import sys
import math

length = int(sys.stdin.readlines(1)[0])
text = "WELCOME TO CCC GOOD LUCK TODAY"

for i in range(math.ceil(len(text) / length)):
    if 0 < len(text) < length:
        for l in range(length - len(text)):
            text += " "
    leng = 0
    if len(text) > length:
        for l in text[length::-1]:
            if l == " ":
                break
            else:
                leng += 1
    subtext = text[:length-leng].strip()
    space = []
    for l in range(len(subtext)):
        if subtext[l] == " ":
            space.append(l)
    if len(space) == 0 and len(subtext) < length:
        space.append(len(subtext))
        subtext += " "
    spaced = []
    for l in range(length - len(subtext)):
        spaced.append(space[l%len(space)])
        spaced.sort()
    for l in spaced[::-1]:
        subtext = subtext[:l] + " " + subtext[l:]

    print(subtext.replace(" ", "."))
    text = text[length-leng+1:]
