import sys
input = sys.stdin.readline
to = [input().split() for i in range(int(input()))]
sep = [input().split() for i in range(int(input()))]
partners = {}

for i in range(int(input())):
    a, b, c = input().split()
    partners[a], partners[b], partners[c] = i, i, i

ans = 0

for partner1, partner2 in to:
    if partners[partner1] != partners[partner2]:
        ans += 1

for partner1, partner2 in sep:
    if partners[partner1] == partners[partner2]:
        ans += 1
        
print(ans)
