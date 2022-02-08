from datetime import datetime
a_list=[]
while True:
    a_str=input()
    if  a_str=='0':
        break
    a_list.append(a_str)
a_list.sort(key=lambda date: datetime.strptime(date,'%d %m %Y'))
for x in range(len(a_list)):
    print(a_list[x])
