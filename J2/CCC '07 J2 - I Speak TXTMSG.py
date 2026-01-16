import sys

text = ""
running = True

while running:
    text = str(sys.stdin.readlines(1)[0].strip())
    if text == "TTYL":
        print("talk to you later")
        running = False
    elif text == ":-)":
        print("I'm happy")
    elif text == ":-(":
        print("I'm unhappy")
    elif text == ";-)":
        print("wink")
    elif text == ":-P":
        print("stick out my tongue")
    elif text == "(~.~)":
        print("sleepy")
    elif text == "TA":
        print("totally awesome")
    elif text == "CCC":
        print("Canadian Computing Competition")
    elif text == "CUZ":
        print("because")
    elif text == "TY":
        print("thank-you")
    elif text == "YW":
        print("you're welcome")
    elif text == "CU":
        print("see you")
    else:
        print(text)
