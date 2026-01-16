m = int(input())
n = int(input())
a = [input() for i in range(n)]
b = [input() for i in range(n)]
ans = []

def solve(tempa="", tempb="", steps=[]):
    if len(steps) > m:
        return
    if len(tempa) >= 40 or len(tempb) >= 40:
        return
    if tempa == tempb and tempa != "":
        global ans
        ans = [step+1 for step in steps]
        return 
    for choice in range(len(a)):
        ta = tempa + a[choice]
        tb = tempb + b[choice]
        length = min(len(ta), len(tb))
        if ta[:length] == tb[:length]:
            solve(ta, tb, steps + [choice])

solve() 
if ans != []:
    print(len(ans))
    for step in ans:
        print(step)
else:
    print("No solution.")
