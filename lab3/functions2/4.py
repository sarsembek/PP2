from movies import movie
newlist=movie()
def average():
    mean=0
    for x in range(len(newlist)):
        mean+=newlist[x]['imdb']
    return mean/len(newlist)
print(average())