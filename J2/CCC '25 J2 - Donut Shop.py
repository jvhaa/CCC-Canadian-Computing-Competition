ans = int(input())
for i in range(int(input())):
    if input().strip() == "+": ans += int(input())
    else: ans -= int(input())
print(ans)
