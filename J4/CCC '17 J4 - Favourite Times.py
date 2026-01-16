import sys

index = []
total = 0

for i in range(1, 13):
    hr = str(i)
    for i in range(-4, 5):
        if int(hr) < 10:
            m1 = int(hr) + i
            m2 = m1 + i
        else:
            m1 = int(hr[1]) - (int(hr[0]) - int(hr[1]))
            m2 = m1 - (int(hr[0]) - int(hr[1]))
        if -1 < m1 < 6 and -1 < m2 < 10:
            index.append((int(hr)-1) * 60 + m1 * 10 + m2)
            if int(hr) > 9:
                break

index.append(1000000001)
time = int(sys.stdin.readlines(1)[0])

if time >= 34:
    total += 1
    time -= 60
    loops = time // 720
    total += (len(index)-1) * loops
    time -= loops * 720
    if index[0] <= time:
        for i in range(1, len(index)):
            if index[i] > time:
                time -= index[i-1]
                total += index.index(index[i-1]) + 1
                break
    print(total)
else:
    print(0)
