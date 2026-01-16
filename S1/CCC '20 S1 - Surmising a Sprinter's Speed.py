num = int(input()) 
position = []
max_speed = 0

for i in range(num):
    data = input().strip().split()
    data = list(map(int, data))
    position.append(data)

position = sorted(position, key = lambda x: x[0])

for i in range(num-1):
    time = abs(position[i+1][0] - position[i][0])
    distance = abs(position[i+1][1] - position[i][1])
    speed = abs(distance/time)
    max_speed = max(speed, max_speed)

print(max_speed)
