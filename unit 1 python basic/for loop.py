x = [(1,2),(3,4),(4,5),(6,8)]

for i in x :
    print (i)
    #this is packing 

for i,j in x:
    print(i,j)
    #this is unpacking

a = 'minkhant'

for b in a :
    print (a,end=' ')

row = int (input('Please enter your row number :'))
for c in range (row):
    for z in range(c):
        print ('*',end = ' ')
    print ('')

row1 = int(input('Please enter your row :'))
for d in range (1,row1):
    for f in range(d):
        print(d,end=' ')
    print('')
