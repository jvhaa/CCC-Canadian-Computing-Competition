n = int(input())

memo = {}

def patrick_win(a, b, c, d):
    k = (a, b, c, d)
    if k in memo:
        return memo[k]
    x = False
    if a >= 2 and b >= 1 and d >= 2:
        x = not patrick_win(a-2, b-1, c, d-2)
    if a >= 1 and b >= 1 and c >=1 and d >= 1 and not x:
        x = not patrick_win(a-1, b-1, c-1, d-1)
    if c >= 2 and d >= 1 and not x:
        x = not patrick_win(a, b, c-2, d-1)
    if b >= 3 and not x:
        x = not patrick_win(a, b-3, c, d)
    if a >= 1 and d >= 1 and not x:
        x = not patrick_win(a-1, b, c, d-1)
    memo[k] = x
    return x
    

for i in range(n):
    a, b, c, d = map(int, input().split())
    print("Patrick" if patrick_win(a, b, c, d) else "Roland")
