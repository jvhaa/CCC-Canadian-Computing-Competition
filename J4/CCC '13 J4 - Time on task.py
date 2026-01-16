t = int(input())
c = int(input())
x = []
for i in range(int(c)):
    x.append(int(input()))

x.sort()

sum = 0
count = 0
while count < len(x) and sum <= t:
    sum = sum + x[int(count)]
    count += 1
if sum > t:
    print(count - 1)
else:
    print(count)
