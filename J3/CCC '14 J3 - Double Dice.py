import sys 

rolls = int(sys.stdin.readlines(1)[0].strip())

num1 = 100
num2 = 100

for i in range(rolls):
    roll = sys.stdin.readlines(1)[0].strip().split(" ")
    die1 = int(roll[0])
    die2 = int(roll[1])
    if die1 > die2:
        num2 -= die1
    elif die2 > die1:
        num1 -= die2
    
print(num1)
print(num2)
