import math
l=[]
while True:
    n=int(input())
    if n==0:
        break
    l.append(n)
size=len(l)
if size%2==0:
    for x in range(int(size/2)):
        print(l[x]+l[len(l)-1-x],end=' ')
else:
    for x in range(int(math.floor(size/2))):
        print(l[x]+l[len(l)-1-x],end=' ')
    print(l[int(math.floor(size/2))])