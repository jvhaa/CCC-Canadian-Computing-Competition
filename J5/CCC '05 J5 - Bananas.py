def aWord(s):
    if s == "A":
        return True
    elif len(s) >= 3 and s[0] == "B" and monkeyWord(s[1:-1]) and s[-1] == "S":
        return True
    else:
        return False

def monkeyWord(s):
    if aWord(s):
        return True
    else:
        found = False
        for i in range(1, len(s) - 1):
            found = found or (aWord(s[:i]) and s[i] == "N" and monkeyWord(s[i + 1:]))
        return found

while True:
    s = input()
    if s == "X":
        break
    if monkeyWord(s):
        print("YES")
    else:
        print("NO")
