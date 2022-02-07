def bshop(name,quantity,unit,tlist=[]):
    tlist.append(f'{name} {quantity} {unit}')
    return tlist

store1 = bshop('java',1,'book',)
bshop('python',2,'book',store1)
store2 = bshop ('C++',3,'book')
print (store1)
print (store2)

