flowers = [list(map(int, input().split())) for i in range(int(input()))]

def real(flowers):
    for i in range(len(flowers)-1):
        if flowers[i][0] > flowers[i+1][0] or flowers[i][-1] > flowers[i+1][-1] or flowers[i][0] > flowers[i][-1] or flowers[i+1][0] > flowers[i+1][-1]:
            return False
    return True
if real(flowers):
    for flower in flowers:
        print(" ".join(list(map(str, flower))))
else:
    flowers = [flower[::-1] for flower in flowers[::-1]]
    if real(flowers):
        for flower in flowers:
            print(" ".join(list(map(str, flower))))
    else:
        flowers = [list(t)[::-1] for t in zip(*flowers)]
        if real(flowers):
            for flower in flowers:
                print(" ".join(list(map(str, flower))))
        else:
            for flower in flowers[::-1]:
                print(" ".join(list(map(str, flower[::-1]))))
