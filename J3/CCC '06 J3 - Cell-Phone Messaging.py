import sys

num = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}

while True:
    prev_chara = ""
    total = 0
    text = sys.stdin.readlines(1)[0].strip()
    if text == "halt":
        break
    for character in text:
        for letter in num:
            if character in num[letter]:
                if prev_chara in num[letter]:
                    total += 2
                total += num[letter].index(character)+1
                prev_chara = character
    print(total)
