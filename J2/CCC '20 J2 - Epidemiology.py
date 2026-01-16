limit = int(input())
start = int(input())
spread = int(input())
infected = start
day = 0

while infected <= limit:
    infected += start * spread
    start *= spread
    day += 1

print(day)
