n=int(input())
if n%2==0:
    for x in range(0,n):
        for y in range(0,n):
            if(x>=y):
                print('#',end='')
            else:
                print('.',end='')
        print('')
else:
    for x in range(0,n):
        for y in range(0,n):
            if(x+y>=n-1):
                print('#',end='')
            else:
                print('.',end='')
        print('')
