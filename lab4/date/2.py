import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print('Yesterday:'+str(yesterday) + ' ' +str(yesterday.strftime('%a')))
print('Today:'+str(today) + ' '+ str(today.strftime('%a')))
print('Tomorrow:'+str(tomorrow) +' ' +str(tomorrow.strftime('%a')))