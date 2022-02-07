def myfun(x,y):
    return x+y

myfun.__subject__ = 'bio'
myfun.__mark__ =90
print (dir(myfun))
print (myfun.__subject__)
print (myfun.__mark__)
