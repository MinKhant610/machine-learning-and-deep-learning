#print len callable
#str.upper list.append
#def lambda : expression

from decimal import Decimal
print (callable(Decimal))

a = Decimal('10.10')
print (type(a))
print (callable(a))

class Myclass:
    def __init__(self,x=0):
        print ('from class')
        self.counter = x

    def __call__(self,x=1):
        print ('updating value ......')
        self.counter +=x
    def myfun(self,z =20):
        print ('This is my fun')
        self.counter = z


obj = Myclass()
print (Myclass.__call__(obj,10))
print (obj.counter)
print (callable(obj))

inobj = Myclass()
print (Myclass.__init__(inobj,10))
print (callable(inobj))

myfunobj = Myclass()
print (callable(myfunobj))
