num = int(input())

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

answer = 3*(line1.count(1)+line2.count(1))

for i in range(num):
    if i < num-1:
        if line1[i] == line1[i+1] == 1:
            answer -=2
        if line2[i] == line2[i+1] == 1:
            answer -=2
    if line1[i] == line2[i] == 1 and i % 2 == 0:
        answer -=2

print(answer)
