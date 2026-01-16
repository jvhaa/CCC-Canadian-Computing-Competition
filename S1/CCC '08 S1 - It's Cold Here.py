import sys

temps = {}

while True:
    data = sys.stdin.readlines(1)[0].strip().split()
    temps[data[0]] = int(data[1])
    if data[0] == "Waterloo":
        break


answer = ["damn", float('inf')]

for city, temp in temps.items():
    if temp < answer[1]:
        answer = [city, temp]
    

print(answer[0])
