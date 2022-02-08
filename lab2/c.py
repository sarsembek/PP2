n=int(input())
l={}
for x in range(0,n):
    for y in range(0,n):
        l[x,y]=0
for x in range(0,n):
    l[x,0]=x
    for y in range(0,n):
        l[0,y]=y
        l[y,y]=y*y
for x in range(0,n):
    for y in range(0,n):
        print(l[x,y],end=' ')
    print(' ')