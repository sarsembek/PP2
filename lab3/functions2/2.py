from movies import movie
newlist=movie()
def above():
    for x in range(len(newlist)):
        if newlist[x]['imdb']>5.5:
            print(newlist[x]['name'])
above()