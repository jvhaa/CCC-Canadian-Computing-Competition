n = a = b = 0
diff = []
pattern = 0

while True:
    n = input().strip().split(" ")
    if n[0] == '0':
        break
    if len(n)-1 == 1:
        print(0)
    else:
        diff = [0] * 21
        for i in range(len(n) - 1):
            b = int(n[i+1])
            diff[i] = b - a
            a = b

        pattern = 1
        while True:
            a = 1

            while a + pattern <= len(n) - 1 and diff[a] == diff[a + pattern]:
                a += 1
            if a + pattern == len(n) - 1:
                break
            pattern += 1
        print(pattern)
