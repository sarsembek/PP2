from movies import movie
newlist=movie()
target=0
def find_index(nameof):
    for x in range(len(newlist)):
        if nameof==newlist[x]['name']:
            target=x
            return target
def worth(target):
    for x in range(len(newlist)):
        if newlist[target]['imdb']>5.5:
            return True
        else:
            return False
s=input()
print(worth(find_index(s)))