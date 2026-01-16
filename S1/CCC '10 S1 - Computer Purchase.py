computers = {}

for i in range(int(input())):
    data = input().split()
    computers[data[0]] = int(data[1]) *2 + int(data[2]) * 3 + int(data[3])

sorted_dict = list(dict(sorted(list(computers.items()), key=lambda item: (item[1], 0-len(item[0]), 0-ord(item[0][0].lower())), reverse=True))) 
if len(computers) > 0:
    print(sorted_dict[0])
if len(computers) > 1:
    print(sorted_dict[1])
