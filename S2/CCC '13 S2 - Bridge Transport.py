weight = int(input())
car_num = int(input())
cars = [0, 0, 0] + [int(input()) for _ in range(car_num)] + [0, 0, 0]
cars = [[cars[i] + cars[i+1] + cars[i+2] + cars[i+3], i+1] for i in range(len(cars)-3)]
cars = sorted(cars, key=lambda x: (x[0]-weight > 0, 0-x[1]), reverse=True)

if cars[0][0] < weight:
    print(car_num)
else:
    print(cars[0][1]-1)
