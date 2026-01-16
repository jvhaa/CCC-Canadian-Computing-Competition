import sys
text = str(sys.stdin.readlines(1)[0])

h = text.count(":-)")
s = text.count(":-(")

if h > s:
    print("happy")
elif s > h: 
    print("sad")
elif s == h != 0:
    print("unsure")
else:
    print("none")
