import sys

num = int(sys.stdin.readlines(1)[0])
phone = {
    2 : "ABC",
    3 : "DEF",
    4 : "GHI",
    5 : "LJK",
    6 : "MNO",
    7 : "PQRS",
    8 : "TUV",
    9 : "WXYZ"
}

for i in range(num):
    text = "".join(list(map(str, sys.stdin.readlines(1)[0].strip().split("-"))))
    answer = ""
    for character in text:
        if character.isnumeric():
            answer += character
        else:
            for number in phone:
                if character in phone[number]:
                    answer += str(number)

    print(answer[:3] + "-" + answer[3:6] + "-" + answer[6:10])
