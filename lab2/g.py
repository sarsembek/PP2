n=int(input())
demons={}
for i in range(0,n):
    x,y=map(str,input().split())
    try:
        demons.update({y:int(demons.get(y))+1})
    except TypeError:
        demons.update({y:1})
keys=list(demons)
m=int(input())
attempts={}
for j in range(0,m):
    x,y,z=map(str,input().split())
    try:
        attempts.update({y:int(attempts.get(y))+int(z)})
    except TypeError:
        attempts.update({y:int(z)})
l=[]
keys2=list(attempts)
alive=0
for c in range(0,len(keys)):
    try:
        l.append(demons.get(keys[c])-attempts.get(keys[c]))
    except TypeError:
        l.append(demons.get(keys[c]))
for d in range(0,len(l)):
    if(l[d]>0):
        alive+=l[d]
print('Demons left: '+str(alive))


