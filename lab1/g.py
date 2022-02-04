def to_dec(s:int, x=-1):
    if s==0:
        return 0
    x+=1
    return(s%10)*(1<<x)+to_dec(s//10,x)
s=int(input())
print(to_dec(s))

