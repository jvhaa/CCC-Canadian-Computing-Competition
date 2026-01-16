n = int(input())

group = []

for i in range(n):
	group.append(int(input()))

n //= 2

group1 = group[:n]
group2 = group[n:]

ans = 0

for member1, member2 in zip(group1, group2):
	if member1 == member2:
		 ans += 2
print(ans)
