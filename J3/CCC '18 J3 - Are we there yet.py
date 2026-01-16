import sys

arr = [0]

for item in sys.stdin.readlines(1)[0].strip().split(" "):
    arr.append(int(item) + arr[len(arr)-1])
    
for l in arr:
    print(l, "",sep=" ", end="")
print()

for i in range(len(arr)-1):
    diff = arr[i+1]
    for l in range(0, i+1):
        arr[l] += diff
    for l in range(i+1, len(arr)):
        arr[l] -= diff
    for l in arr:
        print(l, "",sep=" ", end="")
    print()
    diff = arr
