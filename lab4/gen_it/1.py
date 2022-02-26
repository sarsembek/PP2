def square(n):
    for i in range(0,n+1):
        yield i*i
n=int(input())
a=square(n)
for x in a:
    print(x,end=' ')