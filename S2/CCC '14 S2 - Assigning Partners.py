num = int(input())
groups = sorted([sorted([i, x]) for i, x in zip(input().split(), input().split())])

def check(groups):
    if len(groups) < 1 or len(groups) % 2 != 0:
        return False
    for i in range(len(groups)//2):
        if groups[i*2] != groups[i*2+1] or groups[i*2][0] == groups[i*2][1]:
            return False
    return True


if check(groups):
    print("good")
else:
    print("bad")
