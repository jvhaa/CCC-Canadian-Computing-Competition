import sys
input = sys.stdin.readline

j = int(input())
r = int(input())
jerseys = {}

size_comp = {
  "S" : 1,
  "M" : 2,
  "L" : 3,
  "sold" : 0   
}

for i in range(j):
    jerseys[i+1] = input().strip()
answer = 0    

for i in range(r):
    size, number = input().split()
    if size_comp[jerseys[int(number)]] >= size_comp[size]:
        answer += 1
        jerseys[int(number)] = "sold"

print(answer)
