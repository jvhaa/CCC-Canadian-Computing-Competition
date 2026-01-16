h = int(input())
houses = list(sorted([int(input()) for i in range(h)]))
firestations = int(input())

mil = 1000000

high = 1000000
low = 0

def needed(length):
    if length == 0:
        return h
    c = 1
    total = houses[0] + length
    for i in range(1, h):
        if houses[i] > total + length:
            c+= 1
            total = houses[i]+length
    
    b = 1
    total = houses[0]+ mil - length
    for i in range(h-1, 0, -1):
        if houses[i] < total - length:
            b += 1
            total = (houses[i] - length + mil)%mil
    return min(b, c)

while low < high:
    mid = (high+low) // 2
    if needed(mid) <= firestations:
        high = mid
    else:
        low = mid + 1

print(high)
