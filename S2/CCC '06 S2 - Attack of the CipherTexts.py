text = input()
shifted_text = input()
shifted_message = input()
mapping = {}

KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
VALUE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

for key, value in zip(shifted_text, text):
    if key not in mapping:
        mapping[key] = value
        KEY = KEY.replace(key, "")
        VALUE = VALUE.replace(value, "")

if len(KEY) == 1:
  mapping[KEY] = VALUE

message = ""

for char in shifted_message:
    if char in mapping:
        message += mapping[char]
    else:
        message += "."

print(message)
