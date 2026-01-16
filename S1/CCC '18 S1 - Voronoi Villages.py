villages = []

for i in range(int(input())):
    villages.append(int(input()))
    
villages.sort()
villages.insert(0, float('-inf'))
villages.append(float("inf"))

minsize = float("inf")

for i in range(1, len(villages)-1):
    size = (abs(villages[i]-villages[i-1]) + abs(villages[i]-villages[i+1]))/2
    minsize = min(size, minsize)
    
print(minsize)
