n,f=map(int,input().split())
k=0
for i in range(2, n//2+1):
    if(n%i==0):
        k+=1
if n<=500 and k==0 and f%2==0:
    print("Good job!")
else:
    print("Try next time!")
