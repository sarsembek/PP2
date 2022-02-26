from datetime import datetime
time1=input()
time2=input()
d1=datetime.strptime(time1,"%Y %m %d %H:%M:%S")
d2=datetime.strptime(time2,"%Y %m %d %H:%M:%S")
def dif(d1,d2):
    timedelta=d1-d2
    return timedelta.days*24*3600+timedelta.seconds
print(dif(d1,d2))