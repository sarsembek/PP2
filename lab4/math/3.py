import math
n=int(input())
l=int(input())
t=math.pi/n
b=(1/4)*n*l**2*(math.cos(t)/math.sin(t))
print(int(b))