import re
n=int(input())
def check(s):
    ok=True
    if re.search('[0-9]',s)is None:
        ok=False
    if re.search('[A-Z]',s)is None:
        ok=False
    if re.search('[a-z]',s)is None:
        ok=False
    return ok
i=0
l=set()
while i<n:
    s=input()
    if check(s)==True:
        l.add(s)
    i+=1
l2=list(l)
l2.sort()
print(len(l2))
for x in l2:
    print(x)