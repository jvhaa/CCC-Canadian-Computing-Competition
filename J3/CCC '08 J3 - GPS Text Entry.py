phrase = input()
movements = 0
r = 1
c = 1

for i in range(len(phrase)):
    letter = phrase[i]
    
    if 'A' <= letter <= 'Z':
        x = ord(letter) - ord('A') + 1
        newr = (x - 1) // 6 + 1
        newc = (x - 1) % 6 + 1
    elif letter == ' ':
        newr = 5
        newc = 3
    elif letter == '-':
        newr = 5
        newc = 4
    elif letter == '.':
        newr = 5
        newc = 5
        
    movements += abs(newr - r) + abs(newc - c)
    r = newr
    c = newc

# Don't forget to go to the end at (5, 6)
movements += abs(newr - 5) + abs(newc - 6)

print(movements)
