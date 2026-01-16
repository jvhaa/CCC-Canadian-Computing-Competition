for i in range(int(input())):
    ans = 0
    string = input().strip() + "l"
    code = ""
    hold = ""
    for char in string:
        if char.isnumeric(): hold += char
        else: 
          if hold != "" : 
            ans += int(hold)
            hold = ""
        if char == "-": hold += "-"
        if char.isupper(): code += char
    print(code + str(ans))
