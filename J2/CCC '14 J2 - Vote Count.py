import sys

votes = sys.stdin.readlines(1)
vote = sys.stdin.readlines(2)
A = 0
B = 0


for i in range(0, int(votes[0]) ):
    if str(vote[0])[i] == "A":
        A += 1
    else:
        B += 1
if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("Tie")
