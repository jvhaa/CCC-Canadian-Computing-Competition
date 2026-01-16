length = 0
res = {}
character = ""
number = ""
x = input()

for char in x + "a":
    if char.isalpha():
        if number != "":
            res[int(number)+length] = character
            length += int(number)
            number = ""
        character = char
    else:
        number += char
        
index = int(input()) % length

for i, character in res.items():
    if i > index:
        print(character)
        break
