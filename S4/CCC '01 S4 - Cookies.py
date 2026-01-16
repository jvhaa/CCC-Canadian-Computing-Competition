n = int(input())
data = []
for _ in range(n): data.append(list(map(int,input().split())))
out = 0
for i in range(n):
 for j in range(i+1,n):
  x1,x2,y1,y2 = data[i][0],data[j][0],data[i][1],data[j][1]
  if ((x1-x2)**2+(y1-y2)**2)**0.5>out:out=((x1-x2)**2+(y1-y2)**2)**0.5
  for k in range(j+1,n):
   x3,y3 = data[k][0],data[k][1]
   a=((x1-x2)**2+(y1-y2)**2)**0.5
   b=((x1-x3)**2+(y1-y3)**2)**0.5
   c=((x2-x3)**2+(y2-y3)**2)**0.5
   # check if acute
   if a**2+b**2+c**2>max(a,b,c)**2*2:
    #circumradius formula
    #note that this isn't the best solution when the triangle is obtuse
    r=2*(a*b*c)/(((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))**0.5)
    if r>out:out=r
   else:
    r=max(a,b,c)
    if r>out:out=r
print("%.2f"%out)
