n=int(input())
l=list()
l2=list()
for i in range(0,n):
    s=input()
    l.append(s)
for i in range(0,n):
    if(l[i].rfind('@gmail.com')!=-1):
        l2.append(l[i])
for i in range(0,len(l2)):
    x=l2[i].find('@gmail.com')
    print(l2[i][0:x])
