arr = []
count = 0
arrN = []
for i in range(int(input())):
    arrN.append(input().strip())
  
arrN.append("P")
  
for i in range(len(arrN)):
    if arrN[i] == "P":
      arr.append(count)
      count = 0
    else:
      count += 1

ans = 1 
for i in range(len(arr)-1): ans = max(ans, arr[i] + arr[i+1]+1)

if len(arr) == 1:
    ans = arr[0]-1

if arrN == ["S", "P"]:
    ans = 0

print(ans)
