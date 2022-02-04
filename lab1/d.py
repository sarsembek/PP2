x=int(input())
c=str(input())
if c=='k':
    n=int(input())
if c=='b':
    res=x*1024
    print(res)
elif c=='k':
    res=x/1024
    res=float(res)
    print(f"{res:.{n}f}")

