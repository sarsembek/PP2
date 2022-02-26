import json
print('Interface Status')
for x in range(0,80):
    print('=',end='')
print('\r')
print('DN',end='')
for x in range(0,49):
    print(' ',end='')
print('Description           ',end='')
print('Speed    MTU')
for x in range(0,50):
    print('-',end='')
print(' -------------------- ',end='')
print(' ------  ------')
with open('sample-data.json','r') as f:
    data=json.load(f)
for x in range(0,len(data['imdata'])):
    print(data['imdata'][x]['l1PhysIf']['attributes']['dn'],end='')
    if len(data['imdata'][x]['l1PhysIf']['attributes']['dn'])==42:
        for y in range(0,30):
            print(' ',end='')
    else:
        for y in range(0,31):
            print(' ',end='')
    print(data['imdata'][x]['l1PhysIf']['attributes']['speed'],end='   ')
    print(data['imdata'][x]['l1PhysIf']['attributes']['mtu'])
