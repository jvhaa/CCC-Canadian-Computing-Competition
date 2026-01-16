import sys
data = []

f = sys.stdin.readlines(1)[0].strip().split(" ")
s = sys.stdin.readlines(1)[0].strip().split(" ")
t = sys.stdin.readlines(1)[0].strip().split(" ")
ff = sys.stdin.readlines(1)[0].strip().split(" ")



row1 = (int(f[0]) + int(f[1]) + int(f[2]) + int(f[3])) 
row2 = (int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]))
row3 = (int(t[0]) + int(t[1]) + int(t[2]) + int(t[3]))
row4 = (int(ff[0]) + int(ff[1]) + int(ff[2]) + int(ff[3])) 
col1 = (int(f[0]) + int(s[0]) + int(t[0]) + int(ff[0]))
col2 = (int(f[1]) + int(s[1]) + int(t[1]) + int(ff[1]))
col3 = (int(f[2]) + int(s[2]) + int(t[2]) + int(ff[2]))
col4 = (int(f[3]) + int(s[3]) + int(t[3]) + int(ff[3])) 



if row1 == row2 == row3 == row4 == col1 == col2 == col3 == col4:
    print("magic")
else:
    print("not magic")
