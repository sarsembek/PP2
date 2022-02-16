from movies import movie
newlist=movie()
def average_category(genre):
    mean=0
    cnt=0
    for x in range(len(newlist)):
        if newlist[x]['category']==genre:
            cnt+=1
            mean+=newlist[x]['imdb']
    return mean/cnt
s=input()
print(average_category(s))
