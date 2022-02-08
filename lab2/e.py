try:
    s=input()
    l=str.split(s)
    n=int(l[0])
    x=int(l[1])
except IndexError:
    x=int(input())
l=[]
for i in range(0,n):
    l.append(x+2*i)
res=l[0]
for x in range(1,n):
    res^=l[x]
print(res)

