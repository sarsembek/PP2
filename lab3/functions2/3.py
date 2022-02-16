from movies import movie
newlist=movie()
def genre(name_genre):
    for x in range(len(newlist)):
        if newlist[x]['category']==name_genre:
            print(newlist[x]['name'])
s=input()
genre(s)