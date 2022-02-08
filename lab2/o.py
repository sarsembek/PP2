import re
con={'ONE':1,'TWO':2,'THR':3,'FOU':4,'FIV':5,
     'SIX':6,'SEV':7,'EIG':8,'NIN':9,'ZER':0}
keys=list(con)
s=input()
l=s.split('+')
l1=re.findall(r'.{3}',l[0])
l2=re.findall(r'.{3}',l[1])
def calculate(con,l1,l2):
    first=''
    second=''
    for x in l1:
        first+=str(con.get(x))
    for x in l2:
        second+=str(con.get(x))
    return str(int(first)+int(second))
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
st=calculate(con, l1, l2)
new=list(st)
for x in new:
    print(get_key(con, int(x)),end='')

