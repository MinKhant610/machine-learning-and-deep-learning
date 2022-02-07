#unpacking 

a,b,c = (10,100,20)
print (a,b,c)

(a,b,c) = [2,3,4]
print (c,b,a)

(a,b,c) = 'xyz'
print (b,c,a)

dset = [1,2,3]
print (dset)

eset = {'a','b','c,','d'}
print (eset)

#extended unpacking
a, *b = [1,2,3,4,5]
print ('this is unpacking of a',a,'\nthis is unpacking of b',b)

c , *d = (1,2,3,4,5)
print (c ,d )

e , *f = ('minkhant')
print (e,f)

x = [1,2]
y = [3,4]
z = [*x,*y]
print (z)

h , *i ,(j,*k,n) = ['machinelearning','enginner']
print (h)
print (i)
print (j)
print (k)
print (n)
