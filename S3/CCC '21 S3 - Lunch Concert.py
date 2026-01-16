n = int(input())
friend = []

mini = float('inf')
maxi = -float('inf')

for i in range(n):
    pos, speed, hear = map(int, input().split())
    mini = min(mini, pos)
    maxi = max(maxi, pos)
    friend.append((pos, speed, hear))

def mintime(po):
    minitime = 0
    for pos, speed, hear in friend:
        time = max(0, abs(po-pos)-hear)*speed
        minitime += time
    return minitime
    
while mini < maxi-1:
    center = (mini + maxi)//2
    mi = mintime(center)
    ma = mintime(center+1)
    if mi > ma:
        mini = center
    else:
        maxi = center

print(min(mintime(maxi), mintime(maxi)))
