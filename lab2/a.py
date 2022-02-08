s=input()
l=str.split(s)
lint=[int(x) for x in l]
n=len(l)
def jump(n,lint):
    max_index=0
    i=0
    while i<n and i<=max_index:
        max_index=max(max_index,i+lint[i])
        i+=1
    if(max_index>=n-1):
        print(1)
    else:
        print(0)
jump(n,lint)

