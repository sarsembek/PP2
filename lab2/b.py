n=int(input())
x=input().split()
s=map(int,x)
l=list(s)
l.sort()
m=l[n-1]*l[n-2]
print(m)