def check(line1, line2): 
    difference = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        difference += abs(line1.count(letter) - line2.count(letter))
    if line2.count("*") == difference:
        return True
    return False

if check(input(), input()):
    print("A")
else:
    print("N")
