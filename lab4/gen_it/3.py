def gen(n):
    for x in range(0,n+1):
        if x%3==0 and x%4==0:
            yield x
n=int(input())
a=gen(n)
for i in a:
    print(i,end=' ')