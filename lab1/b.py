s,x,=str(input()),0
l=list(s)
for i in range(len(l)):
    x+=ord(l[i])
if x<300:
    print("Oh, no!")
else:
    print("It is tasty!")


