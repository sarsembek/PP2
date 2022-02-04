s=input()
n=input()
if s.find(n)!=s.rfind(n):
    print(str(s.find(n))+' '+str(s.rfind(n)))
else:
    print(s.find(n))    