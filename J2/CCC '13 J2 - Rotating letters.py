import sys

word = str(sys.stdin.readlines(1)[0]).strip()

letters = ["I", "O", "S", "H", "Z", "X", "N"]

for i in range(len(word)):
    if word[i] != "I" and word[i] != "O" and word[i] != "S" and word[i] != "H" and word[i] != "Z" and word[i] != "X" and\
            word[i] != "N":
        print("NO")
        sys.exit()
print("YES")
