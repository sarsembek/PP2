import re
s=input()
s1=re.sub("[?|!|,]","",s)
l=str.split(s1)
x=set(l)
print(len(x))
l1=list(x)
l1.sort()
for i in l1:
    print(i)



