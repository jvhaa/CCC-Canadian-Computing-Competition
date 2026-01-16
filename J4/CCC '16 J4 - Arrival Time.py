import sys

time = sys.stdin.readlines(1)[0].strip().split(":")

m = int(time[0]) * 60 + int(time[1])

time = float(120)

while True:
    if 420 <= m <= 600:
        time -= 0.5
        m += 1
        if time < 0.5:
            break
    elif 900 <= m <= 1140:
        time -= 0.5
        m += 1
        if time < 0.5:
            break
    else:
        time -= 1
        m += 1
        if time < 1:
            break
    if m >= 1440:
        m -= 1440
        
if m >= 1440:
        m -= 1440        

h = m // 60
m -= h * 60

print(str(h) if h > 9 else "0" + str(h), str(m) if m > 9 else str(m) + "0", sep=":")
