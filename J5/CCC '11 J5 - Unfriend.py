def ways(friends, n, x):
    answer = 1
    for y in range(n - 1):
        if friends[y] == x:  # read: "x invited y"
                             # except y is really y+1 because
                             # indexes start at 0, not 1
            answer = answer * (1 + ways(friends, n, y + 1))
    return answer

# input the info
n = int(input())
friends = []
for i in range(1, n):
    friends.append(int(input()))

print(ways(friends, n, n))
