def mygen():
    data = 10 
    yield data
    yield data+1
    yield data+2
    yield data+3

result = mygen ()
print (result)
for i in result :
    print (i)
print ('_______end ______\n')

#another generator program
def gen():
    data1 = 1
    while data1 <=10:
        square = data1 * data1
        yield square
        data1 += 1
res = gen ()
for x in res:
    print (x)
