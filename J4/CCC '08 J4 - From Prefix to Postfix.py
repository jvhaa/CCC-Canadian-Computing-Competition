def postfix(s):
    if s[0] == '+':
        first, temp1 = postfix(s[2:])
        second, temp2 = postfix(temp1)
        post1 = f"{first} {second} +"
        rest = temp2
    elif s[0] == '-':
        first, temp1 = postfix(s[2:])
        second, temp2 = postfix(temp1)
        post1 = f"{first} {second} -"
        rest = temp2
    else:
        post1 = s[0]
        if len(s) > 1:
            rest = s[2:]
        else:
            rest = ""
    return post1, rest

while True:
    prefix = input()
    if prefix == "0":
        break
    post1, _ = postfix(prefix)
    print(post1)
