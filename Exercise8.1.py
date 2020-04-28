def chop(c):
    del c[0]
    del c[-1]
    return None

def middle(m):
    return m[1:-1]

list = [1,2,3,4,5]

newlist = middle(list)
print(newlist)

chop(list)
print(list)
