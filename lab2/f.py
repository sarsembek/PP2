n=int(input())
names={}
i=0
y=[]
while i<n:
    l=str.split(input())
    try:
        names.update({l[0]:names.get(l[0])+int(l[1])})
    except TypeError:
        names.update({l[0]:int(l[1])})
    l.clear()
    i+=1
keys=list(names)
keys.sort()
max_v=0
for x in range(0,len(keys)):
    if(max_v<names.get(keys[x])):
        max_v=names.get(keys[x])
for y in range(0,len(keys)):
    if max_v==names.get(keys[y]):
        print(keys[y]+' is lucky!')
    else:
        print(keys[y]+' has to receive '+str(max_v-names.get(keys[y]))+' tenge')