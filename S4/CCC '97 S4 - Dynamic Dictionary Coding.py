import sys
input = sys.stdin.readline
length = int(input())
for i in range(length):
    position = 0
    replace = {}
    while True:
        text = input().split()
        output = []
        if text == []:
            break
        for word in text:
            if word in replace:
                output.append(replace[word])
            else:
                position += 1
                replace[word] = str(position)
                output.append(word)
        print(" ".join(output))
    print("")
