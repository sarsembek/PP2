n=int(input())
l=list()
for i in range(0,n):
    x=int(input())
    l.append(x)
for i in range(0,n):
    if(l[i]<=10):
        print("Go to work!")
    elif(l[i]>10 and l[i]<=25):
        print("You are weak")
    elif(l[i]>25 and l[i]<=45):
        print("Okay, fine")
    else:
        print('Burn! Burn! Burn Young!')        