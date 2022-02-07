def bshop(name,quantity,unit,tlist=None):
    if not tlist:
        tlist = []
    tlist.append(f'{name} {quantity} {unit}')
    return tlist

store1 = bshop ('java',1,'book')
bshop ('python',2,'book',store1)
store2 = bshop ('c++',3,'book')
bshop ('java',3,'book',store1)
bshop ('php',4,'book',store2)
print (store1)
print (store2)

