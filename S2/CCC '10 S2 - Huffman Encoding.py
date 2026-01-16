codes = []

for i in range(int(input())):
    codes.append(input().split())
    
    
code = input()
answer = ""
while len(code) > 0:
    for huff in codes:
        if code.find(huff[1]) == 0:
            code = code[len(huff[1]):]
            answer += huff[0]

print(answer)
