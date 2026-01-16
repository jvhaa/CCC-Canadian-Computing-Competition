import heapq

for i in range(int(input())):
    sl = int(input())

    mountain, mountainoxy = [[int(input()) for x in range(sl)] for y in range(sl)], [[float("inf") for x in range(sl)] for y in range(sl)]

    oxylimit = mountain[0][0]
    queue = [(0,0,0)]
    mountainoxy[0][0] = 0

    while queue:
        oxygen, x, y = heapq.heappop(queue)
        if oxygen != mountainoxy[y][x]: continue
        for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if sl> x + nx >= 0 and sl> y + ny >= 0:
                if abs(mountain[y+ny][x+nx] - mountain[y][x]) <= 2:
                    moxy = (1 if mountain[y+ny][x+nx] > oxylimit or mountain[y][x] > oxylimit else 0)
                    if oxygen + moxy < mountainoxy[y+ny][x+nx]:
                        heapq.heappush(queue, (oxygen + moxy, x+nx, y+ny))
                        mountainoxy[y+ny][x+nx] = oxygen + moxy
    if i:print()
    if mountainoxy[sl-1][sl-1] != float('inf'):
        print(mountainoxy[sl-1][sl-1])
    else:
        print("CANNOT MAKE THE TRIP")
