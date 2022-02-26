def squares(a,b):
    for x in range(a,b+1):
        yield x*x
x,y=map(int,input().split())
a=squares(x, y)
for x in a:
    print(x,end=' ')
