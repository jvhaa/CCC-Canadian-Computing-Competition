from collections import Counter 
import sys
input = sys.stdin.readline
acid = Counter()

for i in range(int(input())):
    acid[int(input())] += 1

counts = acid.most_common()
arr = [count for count in counts if count[1] == counts[0][1]]
ans = 0
if len(arr) == 1:
    need = arr[0][0]
    arr = [count for count in counts if count[1] == counts[1][1]]
    for element, count in arr:
        ans = max(ans, abs(need-element))
else:
    for i, element1 in enumerate(arr):
        for element2 in arr[i+1:]:
            ans = max(ans, abs(element1[0]-element2[0]))

print(ans)
