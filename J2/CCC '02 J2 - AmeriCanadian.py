import sys

text = ""
vowels = ["a", "e", "i", "o", "u", "y"]

while text != "quit!":
    text = str(sys.stdin.readlines(1)[0].strip())

    if text == "quit!":
        break
    elif "or" in text and len(text) > 4 and text[text.find("or")-1] not in vowels and text.find("or") == len(text)-2:
        print(text.replace("or", "our"))
    else:
        print(text)
