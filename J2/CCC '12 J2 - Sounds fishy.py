import sys

fr = int(sys.stdin.readlines(1)[0])
sr = int(sys.stdin.readlines(1)[0])
tr = int(sys.stdin.readlines(1)[0])
ffr = int(sys.stdin.readlines(1)[0])

if fr == sr == tr == ffr:
    print("Fish At Constant Depth")
elif fr < sr < tr < ffr:
    print("Fish Rising")
elif fr > sr > tr > ffr:
    print("Fish Diving")
else:
    print("No Fish")
