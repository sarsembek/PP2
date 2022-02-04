s=input()
l=list()
l=str.split(s)
s1=str()
for i in range(0,len(l)):
    if(len(l[i])>=3):
        s1=s1+' '+l[i]
print(s1)
