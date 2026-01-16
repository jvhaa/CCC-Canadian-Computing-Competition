import sys

changes = sys.stdin.readlines(1)

total = 0

for i in range(int(changes[0])):
    pepper = sys.stdin.readlines(1)
    if str(pepper[0]).strip() == "Poblano":
        total += 1500
    elif str(pepper[0]).strip() == "Mirasol":
        total += 6000
    elif str(pepper[0]).strip() == "Serrano":
        total += 15500
    elif str(pepper[0]).strip() == "Cayenne":
        total += 40000
    elif str(pepper[0]).strip() == "Thai":
        total += 75000
    else:
        total += 125000
        
print(total)
