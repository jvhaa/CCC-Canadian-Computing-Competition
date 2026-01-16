import heapq

k, n, m = map(int, input().split())

routes = [[] for i in range(n+1)]

for i in range(m):
    a, b, t, h = map(int, input().split())
    routes[a].append((t, h, b))
    routes[b].append((t, h, a))

A, B = map(int, input().split())

dists = [[float('inf'), float('inf')] for i in range(n+1)]
dists[A] = (0,0)

queue = [(0, 0, A)]
ans = -1

while queue:
    time, hull, point = heapq.heappop(queue)
    if point == B:
        ans = time
        break
    if time > dists[point][0] and hull > dists[point][1]:
        continue
    for ntime, nhull, npoint in routes[point]:
        fullTime = time + ntime
        fullHull = hull + nhull
        if fullHull >= k:
            continue
        if fullHull < dists[npoint][1] or fullTime < dists[npoint][0]:
            dists[npoint][0] = fullTime
            dists[npoint][1] = fullHull
            heapq.heappush(queue, (fullTime, fullHull, npoint))

print(ans)
