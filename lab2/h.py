def distance(x,y,i,j):
    return abs(math.sqrt((x-i)**2+(y-j)**2))
import math
x,y=map(int,input().split())
size=int(input())
points=[]
f=0
dist=[]
while f<size:
    i,j=map(int,input().split())
    points.append((str(i)+' '+str(j),distance(x,y,i,j)))
    f+=1
points.sort(key=lambda i:i[1])
for i in points:
    print(i[0])
    

