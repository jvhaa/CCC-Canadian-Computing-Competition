import sys

num = int(sys.stdin.readlines(1)[0])

text = ""

for i in range(num):
    text += sys.stdin.readlines(1)[0].lower()
if text.count('t') > text.count('s'):
    print("English")
else:
    print("French")
