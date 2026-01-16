import sys,math
#sys.stdin=open("data.txt")
input=sys.stdin.readline
#sys.stdout=open("wronganswers.txt","w")

m=int(input())
g=[[1000000]*(m+1) for _ in range(m+1)]
d={}    # unconnected edges goes here
for p in range(m):
    t=list(map(int,input().split()))
    e=t[0]
    c=t[1:e+1]+[t[1]]
    for j in range(e):
        u=min(10000*c[j]+c[j+1],10000*c[j+1]+c[j])
        if u in d:
            q,r=d[u]
            g[p][q]=min(g[p][q],r)
            g[q][p]=min(g[q][p],r)
            del d[u]
        else:
            d[u]=(p,t[e+1+j])
for u,r in d.items():
    g[m][r[0]]=min(g[m][r[0]],r[1])
    g[r[0]][m]=min(g[r[0]][m],r[1])

# decompose graph into edgelist
el1=[]
for j in range(m):
    for i in range(j):
        if g[i][j]!=1000000:
            el1.append((g[i][j],i,j))
el2=list(el1)
for i in range(m):
    if g[i][m]!=1000000:
        el2.append((g[i][m],i,m))

# do kruskal's
ans1=0
connects=0
up=[-1]*m       # disjoint set can be inefficient
el1.sort()
for c,u,v in el1:
    while up[u]!=-1:
        u=up[u]
    while up[v]!=-1:
        v=up[v]
    if u!=v:
        up[u]=v
        connects+=1
        ans1+=c
if connects!=m-1: ans1=1000000

# do a second kruskal's
ans2=0
up=[-1]*(m+1)           # disjoint set can be inefficient
el2.sort()
for c,u,v in el2:
    while up[u]!=-1:
        u=up[u]
    while up[v]!=-1:
        v=up[v]
    if u!=v:
        up[u]=v
        ans2+=c

print(min(ans1,ans2))
