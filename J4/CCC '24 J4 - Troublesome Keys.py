import sys
input = sys.stdin.readline

og = input().strip()
new = input().strip()
alphabet = "abcdefghijklmnopqrstuvwxyz"
ogc = {letter: 0 for letter in alphabet}
newc = ogc.copy()
missing = []
added  = []
replace = ""
gone = "-"

for letter in og:
  ogc[letter] += 1

for letter in new:
  newc[letter] += 1
  
for l in alphabet:
    if ogc[l] - newc[l] > 0:
        missing.append((l, ogc[l]-newc[l]))
    if ogc[l]-newc[l] < 0:
        added.append(l)
        added.append(ogc[l]-newc[l])

if len(missing) > 1:
    if missing[0][1] == missing[1][1]:
        start = min(og.find(missing[1][0]), og.find(missing[0][0]))
        if new[start] != added[0]:
            if og[start] == missing[0][0]:
                gone = missing[0][0]
                replace = missing[1][0] + " " + added[0]
            else:
                gone = missing[1][0]
                replace = missing[0][0] + " " + added[0]
        else:
            length = 0
            key = og[start]
            end = start
            while og[end] == key:
                end+=1
                if end == len(og):
                    break
            while og[end] == added[0]:
                end+=1
                if end == len(og):
                    break
            for x in range(start, end):
                if new[x] != added[0]:
                    if key == missing[0][0]:
                        gone = missing[0][0]
                        replace = missing[1][0] + " " + added[0]
                    else:
                        gone = missing[1][0]
                        replace = missing[0][0] + " " + added[0]
                    break
            else:
                if key == missing[0][0]:
                    gone = missing[1][0]
                    replace = missing[0][0] + " " + added[0]
                else:
                    gone = missing[0][0] 
                    replace = missing[1][0] + " " + added[0]
                    
    else:
        if missing[0][1] == -added[1]:
            replace = missing[0][0] + " " + added[0]
            gone = missing[1][0]
        else:
            replace = missing[1][0] + " " + added[0]
            gone = missing[0][0]
else:
    replace = missing[0][0] + " " + added[0]
  
  
print(replace)
print(gone)
