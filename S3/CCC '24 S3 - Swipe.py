n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

lo=0
ans1=[]
ans2=[]
for i in range(n):
    # spread a[i]
    if lo==n or b[lo]!=a[i]: continue
    if lo<i: ans1.append((i,lo))
    while lo<n and b[lo]==a[i]: lo+=1
    if lo>i+1: ans2.append((i,lo-1))

if lo<n: print('NO')
else:
    print('YES')
    ans=ans1+ans2[::-1]
    print(len(ans))
    for i,j in ans:
        if i<j: print(f'R {i} {j}')
        if j<i: print(f'L {j} {i}')
