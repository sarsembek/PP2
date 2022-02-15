def solve(heads,legs):
    x=int((legs-2*heads)/2)
    y=int(heads-x)
    return str(x)+' '+str(y)
