import sys

word = sys.stdin.readlines(1)[0].strip()
total = 0

for i in range(len(word)-1):
    for l in range(i+1, len(word)):
        if word[i:l] == word[l:i:-1]:
            if total < l-i+1:
                total = l-i+1

print(total)
