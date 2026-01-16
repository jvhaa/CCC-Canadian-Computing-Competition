import sys
input = sys.stdin.readline
N = int(input())
sheep = []
for i in range(N):
    sheep.append((int(float(input())*1000),int(float(input())*1000)))
sheep.sort(key=lambda x:(x[0],x[1]))
deadSheep = [True for x in range(N)]
for i in range(0,N):
    a = 0
    b = 1000000
    for j in range(0,N):
        if not deadSheep[i]:
            break
        if deadSheep[j] and i != j:
            if sheep[i][0] == sheep[j][0]:
                deadSheep[max(i,j)] = False
            else:
                x = (sheep[j][0]**2-sheep[i][0]**2+sheep[j][1]**2-sheep[i][1]**2)/(2*(sheep[j][0]-sheep[i][0]))
                if j<i:
                    a = max(x,a)
                else:
                    b = min (x,b)
    if a>b:
        deadSheep[i] = False
for i in range(N):
    if deadSheep[i]:
        print(f"The sheep at ({sheep[i][0]/1000:.2f}, {sheep[i][1]/1000:.2f}) might be eaten.")
