import sys

times = int(sys.stdin.readlines(1)[0])
name = ""
money = 0

for i in range(times):
    new_name = str(sys.stdin.readlines(1)[0])
    new_money = int(sys.stdin.readlines(1)[0])
    if new_money > money:
        money = new_money
        name = new_name
        
print(name)
