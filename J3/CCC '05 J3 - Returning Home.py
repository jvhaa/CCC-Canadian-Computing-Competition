import sys

directions = []
locations = ["into your HOME."]
d = sys.stdin.readlines(1)[0].strip()

while d != "SCHOOL":
    if d == "L":
        directions.append("Turn RIGHT")
    elif d == "R":
        directions.append("Turn LEFT")
    else:
        locations.append("onto " + d + " street.")
    d = sys.stdin.readlines(1)[0].strip()
    
for i in range(len(directions)):
    print(directions.pop(), locations.pop())
