cities, roads, destination = map(int, input().split())

bridges = [list(map(int, input().split())) for i in range(roads)]
bridges = sorted(bridges, key = lambda x: x[2], reverse=True)

dest = [int(input()) for i in range(destination)]

def kruskals():
    minweight = float("inf")
    parent = [i for i in range(cities+1)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
        
    for x, y, dist in bridges:
        for d in dest:
            if find(d) != 1:
                break
        else:
            break
        a = find(x)
        b = find(y)
        if a != b:
            parent[max(a,b)] = min(a, b)
            minweight = min(minweight, dist)
    
    return minweight

print(kruskals())
