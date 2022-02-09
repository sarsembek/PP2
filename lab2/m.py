a_list=[]
while True:
    a_str=input()
    if  a_str=='0':
        break
    d,m,y=a_str.split()
    x=[y,m,d]
    a_list.append(x)
a_list=sorted(a_list)
for x in range(len(a_list)):
    print(*a_list[x][::-1])
