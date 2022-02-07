def myfun(a,b,*c,d):
    print (a)
    print (b)
    print (c)
    print (d)

mylist = [1,2,3,4,5]

myfun (*mylist,d=6)

print ('_______________')
print ('  ')

def fun(*c,x,d):
    print (c)
    print (d)
    print (x)

fun (1,2,3,x=4,d = 'hello')

print ('_______________')
print ('  ')

def test (a,b,*,c):
    print (a,b,c)
test (1,2,c=10)

print ('_______________')
print ('  ')

def x (**key):
    print (key)
x (a=10,b=20,c=30)

