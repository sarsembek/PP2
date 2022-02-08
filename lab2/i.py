n=int(input())
i=0
shelf=[]
took=[]
while i<n:
    s=input()
    l=str.split(s)
    x=int(l[0])
    try:
        y=l[1]
    except:
        pass
    if x==1:
        shelf.append(y)
    else:
        took.append(shelf[0])
        shelf.pop(0)
    i+=1
for x in range(0,len(took)):
    print(took[x],end=' ')