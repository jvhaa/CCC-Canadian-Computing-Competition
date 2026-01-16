seats = input()
l = len(seats)

A = seats.count("A")
B = seats.count("B") + A
C = seats.count("C") + B
C2 = seats.count("C")
B2 = seats.count("B") + C2
A2 = seats.count("A") + B2

ans = float('inf')

seats = " " + 2*seats

pa = [0 for i in range(l*2+1)]
pb = [0 for i in range(l*2+1)]
pc = [0 for i in range(l*2+1)]

for i in range(2*l+1):
    pa[i] = pa[i-1] + (seats[i] == "A")
    pb[i] = pb[i-1] + (seats[i] == "B")
    pc[i] = pc[i-1] + (seats[i] == "C")
    
for i in range(1, l+1):
    ans = min(ans, pa[i+C]-pa[i+A] + max(pb[i+C]-pb[i+B], pc[i+B] - pc[i+A]))
    ans = min(ans, pc[i+A2] - pc[i+C2] + max(pb[i+A2]-pb[i+B2], pa[i+B2] -pa[i+C2]))
    
print(ans)
